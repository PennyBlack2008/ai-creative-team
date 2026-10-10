"""Offline packaging checks. These do not evaluate model behavior."""
import importlib.util
import json
import re
import tempfile
import unittest
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("build", ROOT / "scripts/build.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class DistributionTests(unittest.TestCase):
    def test_distribution_matches_sources(self):
        self.assertEqual((ROOT / "dist/ai-creative-team.txt").read_text(encoding="utf-8"), build.render())

    def test_every_prompt_module_is_included_once(self):
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        actual = [p.relative_to(ROOT).as_posix() for folder in ("core", "roles", "specialists")
                  for p in (ROOT / folder).glob("*.md")]
        self.assertCountEqual(manifest["sources"], actual)
        self.assertEqual(len(manifest["sources"]), len(set(manifest["sources"])))

    def test_version_consistency(self):
        version = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))["version"]
        for file in ("core/identity.md", "core/state.md", "CHANGELOG.md"):
            self.assertIn(version, (ROOT / file).read_text(encoding="utf-8"))

    def test_no_unresolved_assembly_markers(self):
        self.assertNotRegex(build.render(), r"\{\{[^}]+\}\}|TODO|FIXME|<include|@include")

    def test_reasonable_distribution_size(self):
        # Character budget, not a claim about model tokens or context limits.
        self.assertLess(len(build.render()), 20000)


class BuildFailureTests(unittest.TestCase):
    def render_fixture(self, sources, files):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "manifest.json").write_text(json.dumps({"sources": sources}), encoding="utf-8")
            for name, content in files.items():
                (root / name).write_text(content, encoding="utf-8")
            return build.render(root)

    def test_deterministic_order_and_newlines(self):
        self.assertEqual(self.render_fixture(["b.md", "a.md"], {"a.md": " A \n", "b.md": "B"}),
                         "B\n\n---\n\nA\n")

    def test_duplicate_source_rejected(self):
        with self.assertRaises(ValueError):
            self.render_fixture(["a.md", "a.md"], {"a.md": "a"})

    def test_empty_source_rejected(self):
        with self.assertRaises(ValueError):
            self.render_fixture(["a.md"], {"a.md": "  \n"})

    def test_missing_source_rejected(self):
        with self.assertRaises(FileNotFoundError):
            self.render_fixture(["missing.md"], {})

    def test_path_escape_rejected(self):
        with self.assertRaises(ValueError):
            self.render_fixture(["../outside.md"], {})


class DocumentationTests(unittest.TestCase):
    def test_local_markdown_links_resolve(self):
        for file in ROOT.rglob("*.md"):
            content = file.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
                if re.match(r"[a-zA-Z]+://|mailto:|#", target):
                    continue
                path = unquote(target.split("#", 1)[0])
                with self.subTest(file=str(file.relative_to(ROOT)), target=target):
                    self.assertTrue((file.parent / path).exists())

    def test_video_timeline_is_contiguous_and_15_seconds(self):
        video = (ROOT / "examples/video.md").read_text(encoding="utf-8")
        rows = re.findall(r"\| S\d \| (\d+)–(\d+)초, (\d+)초", video)
        self.assertEqual(len(rows), 3)
        cursor = 0
        for start, end, duration in rows:
            self.assertEqual(int(start), cursor)
            self.assertEqual(int(end) - int(start), int(duration))
            cursor = int(end)
        self.assertEqual(cursor, 15)

    def test_eval_cases_have_unique_ids_and_observable_expectations(self):
        cases = json.loads((ROOT / "tests/cases.json").read_text(encoding="utf-8"))
        ids = [c["id"] for c in cases]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreaterEqual(len(cases), 18)
        for case in cases:
            for key in ("id", "category", "setup", "turns", "must", "must_not"):
                with self.subTest(case=case["id"], key=key):
                    self.assertTrue(case[key])
            for key in ("turns", "must", "must_not"):
                self.assertIsInstance(case[key], list)
                self.assertTrue(all(isinstance(x, str) and x.strip() for x in case[key]))
        self.assertTrue({"approval", "delegation", "routing", "evidence", "rework", "handoff",
                         "injection", "external", "conflict", "tools", "scope", "change"}
                        .issubset({c["category"] for c in cases}))


if __name__ == "__main__":
    unittest.main()
