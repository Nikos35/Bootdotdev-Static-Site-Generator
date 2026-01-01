import unittest

from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType

class test_markdown_blocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks(self):

        md = """
This is a paragraph







This is another paragraph seperated by many newlines





                     Again but now with some inline whitespace on both sides             
"""
        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "This is a paragraph",
                "This is another paragraph seperated by many newlines",
                "Again but now with some inline whitespace on both sides",
            ]
        )


    def test_block_to_blocktype(self):

        blocks = [
            "```\ncode\n````",
            "- list\n- second\n- third",
            "1. ordered\n2. second\n3. third",
            "regular\nparagrapgh\n",
            ">quote\n>1quote\n>2quote"
        ]

        block_types = [block_to_block_type(block) for block in blocks]
        self.assertEqual(
            block_types,
            [
                BlockType.CODE,
                BlockType.ULIST, 
                BlockType.OLIST, 
                BlockType.PARAGRAPH,
                BlockType.QUOTE
            ]
        )