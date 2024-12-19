import unittest
from src.htmlnode import HTMLNode, LeafNode


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

    def test_to_html(self):
        leaf_node = LeafNode("a", "Link to my website", {"href": "melihdihya.art"})
        html = leaf_node.to_html()
        expected = '<a href="melihdihya.art">Link to my website<a\>'
        self.assertEqual(html, expected)

    def test_missing_value(self):
        leaf_node = LeafNode("a", None, {"href": "melihdihya.art"})
        with self.assertRaises(ValueError):
            leaf_node.to_html()

    def test_return_value_only(self):
        leaf_node = LeafNode(None, "Link to my website", None)
        html = leaf_node.to_html()
        self.assertEqual(html, "Link to my website")


if __name__ == "__main__":
    unittest.main()
