import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("image alt text", TextType.IMAGE, "url/of/image.jpg")
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "url/of/image.jpg")        
        self.assertEqual(html_node.props["alt"], "image alt text")        


if __name__ == "__main__":
    unittest.main()