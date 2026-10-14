"""Basic checks for the static site and its build output."""

import unittest
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.title_open = False
        self.title_text = ""

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        if tag == "title":
            self.title_open = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.title_open = False

    def handle_data(self, data):
        if self.title_open:
            self.title_text += data


class SiteTests(unittest.TestCase):
    def test_source_page_has_document_structure_and_pipeline(self):
        page = (ROOT / "index.html").read_text(encoding="utf-8")
        parser = PageParser()
        parser.feed(page)
        self.assertIn("html", parser.tags)
        self.assertIn("head", parser.tags)
        self.assertIn("body", parser.tags)
        self.assertTrue(parser.title_text.strip())
        self.assertIn("GitHub Actions", page)
        self.assertIn("GitHub Pages", page)
        self.assertTrue(page.lower().lstrip().startswith("<!doctype html>"))

    def test_build_creates_publishable_index(self):
        result = subprocess.run(
            [sys.executable, "build.py"], cwd=ROOT, capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        output = ROOT / "dist" / "index.html"
        self.assertTrue(output.is_file())
        self.assertEqual(output.read_bytes(), (ROOT / "index.html").read_bytes())


if __name__ == "__main__":
    unittest.main()
