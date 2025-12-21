import unittest

from htmlnode import HTMLNode, LeafNode


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
