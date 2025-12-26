import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        link = HTMLNode(tag='<a>', value='tis is a link', props={"href":"https://linkidu.com"})

        props = link.props_to_html()

        self.assertEqual(props, ' href="https://linkidu.com"')

    def test_props_to_html_edge(self):
        link = HTMLNode(tag='<a>', value='tis is a link', props={"href":"https://linkidu.com", "target":"_blank"})

        props = link.props_to_html()

        self.assertEqual(props, ' href="https://linkidu.com" target="_blank"')

    def test_repr(self):
        link = HTMLNode(tag='<a>', value='tis is a link', props={"href":"https://linkidu.com"})
        
        self.assertEqual(repr(link), "HTMLNode(<a>, tis is a link, None, {'href': 'https://linkidu.com'})")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "tis is a link", props={"href":"https://linkidu.com", "target":"_blank"})
        self.assertEqual(node.to_html(), '<a href="https://linkidu.com" target="_blank">tis is a link</a>')

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "bold!")
        self.assertEqual(node.to_html(), "<b>bold!</b>")
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    
    def test_to_html_with_multiple_grandgrandchildren(self):
        grandgrandchild_node = LeafNode("b", "grandgrandchild")
        grandgrandchild_node2 = LeafNode("a", "grandgrand link", props={"href":"https://linkidu.com", "target":"_blank"})
        grandchild_node = ParentNode("p", [grandgrandchild_node, grandgrandchild_node2])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><p><b>grandgrandchild</b><a href="https://linkidu.com" target="_blank">grandgrand link</a></p></span></div>'
        )
    
    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
    



