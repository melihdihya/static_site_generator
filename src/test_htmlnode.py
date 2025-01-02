import pytest
from src.htmlnode import HTMLNode, LeafNode, ParentNode


def test_repr():
    html_node = HTMLNode("a", "test", None, {"test": "test"})
    str_repr = repr(html_node)
    assert isinstance(str_repr, str)


def test_props_to_html():
    html_node = HTMLNode("a", "test", None, {"test": "test"})
    props = html_node.props_to_html()
    assert isinstance(props, str)


def test_init():
    html_node = HTMLNode()
    assert isinstance(html_node, HTMLNode)


def test_to_html():
    leaf_node = LeafNode("a", "Link to my website", {"href": "melihdihya.art"})
    html = leaf_node.to_html()
    expected = '<a href="melihdihya.art">Link to my website</a>'
    assert html == expected


def test_missing_value():
    leaf_node = LeafNode("a", None, {"href": "melihdihya.art"})

    with pytest.raises(ValueError):
        leaf_node.to_html()


def test_return_value_only():
    leaf_node = LeafNode(None, "Link to my website", None)
    html = leaf_node.to_html()
    assert html == "Link to my website"


def test_parent_to_html():
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    html_string = node.to_html()
    assert (
        html_string == "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
    )


def test_parent_to_html_nested():
    node = ParentNode(
        "p",
        [
            ParentNode(
                "div",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
        ],
    )
    html_string = node.to_html()
    assert (
        html_string
        == "<p><div><b>Bold text</b>Normal text<i>italic text</i>Normal text</div></p>"
    )


def test_parent_to_html_no_children():
    node = ParentNode("p", [])
    with pytest.raises(ValueError):
        node.to_html()
