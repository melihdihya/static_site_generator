import unittest
from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        str_repr = node.__repr__()
        self.assertIsInstance(str_repr, str)

    def test_eq_method(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node_2 = TextNode("This is a text node", TextType.BOLD)
        is_equal = node.__eq__(node_2)
        self.assertIs(True, is_equal)

    def test_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIs(node.url, None)

    def test_different_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node_2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node_2)


if __name__ == "__main__":
    unittest.main()
