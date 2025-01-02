from src.textnode import TextNode, TextType, text_node_to_html_node


def test_eq():
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    assert node == node2


def test_repr():
    node = TextNode("This is a text node", TextType.BOLD)
    str_repr = node.__repr__()
    assert isinstance(str_repr, str)


def test_eq_method():
    node = TextNode("This is a text node", TextType.BOLD)
    node_2 = TextNode("This is a text node", TextType.BOLD)
    is_equal = node.__eq__(node_2)
    assert is_equal


def test_no_url():
    node = TextNode("This is a text node", TextType.BOLD)
    assert not node.url


def test_different_text_type():
    node = TextNode("This is a text node", TextType.BOLD)
    node_2 = TextNode("This is a text node", TextType.ITALIC)
    assert node != node_2


def test_text():
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    assert not html_node.tag
    assert html_node.value == "This is a text node"


def test_image():
    node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
    html_node = text_node_to_html_node(node)
    assert html_node.tag == "img"
    assert not html_node.value
    assert html_node.props == {"src": "https://www.boot.dev", "alt": "This is an image"}


def test_bold():
    node = TextNode("This is bold", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    assert html_node.tag == "b"
    assert html_node.value == "This is bold"
