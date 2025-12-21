import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_un_eq(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a different text node", TextType.TEXT)
        self.assertNotEqual(node, node2)


    def test_un_eq_edge(self):
        node = TextNode("This is a text node", TextType.IMAGE, "img/dpic")
        node2 = TextNode("This is a different text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    
    def test_eq_edge(self):
        node = TextNode("This is a text node", TextType.IMAGE, "img/dpic")
        node2 = TextNode("This is a text node", TextType.IMAGE, "img/dpic")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()