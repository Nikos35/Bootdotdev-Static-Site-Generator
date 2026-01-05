import unittest

from generate_page import extract_title


class TestGeneratePage(unittest.TestCase):

    def test_extract_title(self):
        markdown = "# Title  \nWow so cool"

        title = extract_title(markdown)

        self.assertEqual(title, "Title")

    def test_extract_title_no_h1_header(self):
        markdown = "## Not title\nFile without a h1 header"

        with self.assertRaises(ValueError) as context:
            extract_title(markdown)
        
        self.assertEqual("Failed to extract title: no h1 title header found", str(context.exception))

    def test_extract_title_multiple_titles(self):
        markdown = "# Title1\nsum text\n# Title2"

        with self.assertRaises(ValueError) as context:
            extract_title(markdown)

        self.assertEqual("Failed to extract title: markdown file contains more than 1 h1 title header. Only 1 is allowed", str(context.exception))



if __name__ == "__main__":
    unittest.main()