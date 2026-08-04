"""Regression tests for the canonical repository validation gate."""

from __future__ import annotations

import importlib.util
import subprocess
import tempfile
import unittest
from importlib.machinery import SourceFileLoader
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
LOADER = SourceFileLoader("repository_validate", str(ROOT / "scripts" / "validate"))
SPEC = importlib.util.spec_from_loader(LOADER.name, LOADER)
assert SPEC is not None
VALIDATE = importlib.util.module_from_spec(SPEC)
LOADER.exec_module(VALIDATE)


def write_skill(root: Path, name: str, description: str) -> None:
    skill_dir = root / name
    (skill_dir / "agents").mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: {description}\n---\n",
        encoding="utf-8",
    )
    (skill_dir / "agents" / "openai.yaml").write_text(
        "interface:\n"
        '  display_name: "Test Skill"\n'
        '  short_description: "Validate repository skill metadata"\n'
        f'  default_prompt: "Use ${name} to test validation."\n',
        encoding="utf-8",
    )


class SkillMetadataTests(unittest.TestCase):
    def validate_skill(self, name: str, description: str) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_skill(root, name, description)
            errors: list[str] = []
            with mock.patch.object(VALIDATE, "ROOT", root):
                VALIDATE.validate_skills(errors)
            return errors

    def test_accepts_platform_metadata_boundaries(self) -> None:
        errors = self.validate_skill("a" * 64, "d" * 1024)
        self.assertEqual(errors, [])

    def test_rejects_metadata_beyond_platform_boundaries(self) -> None:
        errors = self.validate_skill("a" * 65, "d" * 1025)
        self.assertTrue(any("skill name must not exceed 64" in error for error in errors))
        self.assertTrue(
            any("description must not exceed 1024" in error for error in errors)
        )


class MarkdownDiscoveryTests(unittest.TestCase):
    def test_discovers_only_present_nonignored_markdown(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(
                ["git", "init", "--quiet"],
                cwd=root,
                check=True,
                capture_output=True,
            )
            (root / ".gitignore").write_text(
                ".skill-validation/\n.venv/\n",
                encoding="utf-8",
            )
            (root / "tracked.md").write_text("# Tracked\n", encoding="utf-8")
            (root / "deleted.md").write_text("# Deleted\n", encoding="utf-8")
            (root / "docs").mkdir()
            (root / "docs" / "untracked.md").write_text(
                "# Untracked source\n",
                encoding="utf-8",
            )
            for ignored in (".skill-validation", ".venv"):
                (root / ignored).mkdir()
                (root / ignored / "ignored.md").write_text(
                    "[broken](missing.md)\n",
                    encoding="utf-8",
                )
            subprocess.run(
                ["git", "add", ".gitignore", "tracked.md", "deleted.md"],
                cwd=root,
                check=True,
                capture_output=True,
            )
            (root / "deleted.md").unlink()

            errors: list[str] = []
            discovered = VALIDATE.discover_markdown_files(root, errors)
            relative = {path.relative_to(root).as_posix() for path in discovered}

            self.assertEqual(errors, [])
            self.assertEqual(relative, {"docs/untracked.md", "tracked.md"})


if __name__ == "__main__":
    unittest.main()
