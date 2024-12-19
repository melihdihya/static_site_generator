import unittest
from src.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_repr(self):

        html_node = HTMLNode("a", "test", None, {"test": "test"})
        str_repr = repr(html_node)
        self.assertIsInstance(str_repr, str)

    def test_props_to_html(self):
        html_node = HTMLNode("a", "test", None, {"test": "test"})
        props = html_node.props_to_html()
        self.assertIsInstance(props, str)

    def test_init(self):
        html_node = HTMLNode()
        self.assertIsInstance(html_node, HTMLNode)


if __name__ == "__main__":
    unittest.main()
