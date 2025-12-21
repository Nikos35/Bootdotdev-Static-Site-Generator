import unittest

from htmlnode import HTMLNode


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

