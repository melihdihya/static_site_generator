from src.markdown_parser import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes,
)
from src.textnode import TextNode, TextType

code = TextNode("Testing the parser `code block` word", TextType.TEXT)
bold = TextNode("Testing the parser **bold block** word", TextType.TEXT)
italic = TextNode("Testing the parser *italic block* word", TextType.TEXT)


def test_parser_code():
    new_nodes = split_nodes_delimiter([code], "`", TextType.CODE)

    assert new_nodes[1].text == "code block"
    assert new_nodes[1].text_type == TextType.CODE


def test_parser_bold():
    new_nodes = split_nodes_delimiter([bold], "**", TextType.BOLD)

    assert new_nodes[1].text == "bold block"
    assert new_nodes[1].text_type == TextType.BOLD


def test_parser_italic():
    new_nodes = split_nodes_delimiter([italic], "*", TextType.ITALIC)

    assert new_nodes[1].text == "italic block"
    assert new_nodes[1].text_type == TextType.ITALIC


def test_extract_markdown_images():
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    output = extract_markdown_images(text)
    expected = [
        ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
        ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
    ]
    assert output == expected


def test_extract_markdown_links():
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    output = extract_markdown_links(text)
    expected = [
        ("to boot dev", "https://www.boot.dev"),
        ("to youtube", "https://www.youtube.com/@bootdotdev"),
    ]
    assert output == expected


def test_split_nodes_image():
    node = TextNode(
        "This is text with a image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev) lol",
        TextType.TEXT,
    )
    new_nodes = split_nodes([node], TextType.IMAGE)
    assert len(new_nodes) == 5
    assert new_nodes[1].text == "to boot dev"
    assert new_nodes[3].url == "https://www.youtube.com/@bootdotdev"


def test_split_nodes_link():
    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) lol",
        TextType.TEXT,
    )
    new_nodes = split_nodes([node], TextType.LINK)

    assert len(new_nodes) == 5
    assert new_nodes[2].text == " and "
    assert new_nodes[1].url == "https://www.boot.dev"


def test_split_nodes_single_markdown():
    # Single image
    node = TextNode(
        "This is an image ![to boot dev](https://www.boot.dev)",
        TextType.TEXT,
    )
    new_nodes = split_nodes([node], TextType.IMAGE)
    assert len(new_nodes) == 2
    assert new_nodes[1].text == "to boot dev"
    assert new_nodes[1].url == "https://www.boot.dev"

    # Single link
    node = TextNode(
        "This is a link [to boot dev](https://www.boot.dev)",
        TextType.TEXT,
    )
    new_nodes = split_nodes([node], TextType.LINK)
    assert len(new_nodes) == 2
    assert new_nodes[1].text == "to boot dev"
    assert new_nodes[1].url == "https://www.boot.dev"


def test_split_nodes_no_markdown():
    node = TextNode(
        "This is plain text with no markdown.",
        TextType.TEXT,
    )
    new_nodes = split_nodes([node], TextType.IMAGE)
    assert len(new_nodes) == 1
    assert new_nodes[0].text == "This is plain text with no markdown."
    assert new_nodes[0].text_type == TextType.TEXT


def test_split_nodes_sarts_with_markdown():
    # Starts with markdown
    node = TextNode(
        "![start image](https://www.start.dev) and some text.",
        TextType.TEXT,
    )
    new_nodes = split_nodes([node], TextType.IMAGE)
    assert len(new_nodes) == 2
    assert new_nodes[0].text_type == TextType.IMAGE
    assert new_nodes[0].url == "https://www.start.dev"
    assert new_nodes[1].text == " and some text."


def test_split_nodes_ends_with_markdown():
    # Ends with markdown
    node = TextNode(
        "Some text and a link [end link](https://www.end.dev)",
        TextType.TEXT,
    )
    new_nodes = split_nodes([node], TextType.LINK)
    assert len(new_nodes) == 2
    assert new_nodes[1].text_type == TextType.LINK
    assert new_nodes[1].url == "https://www.end.dev"


def test_split_nodes_empty_text():
    node = TextNode(
        "",
        TextType.TEXT,
    )
    new_nodes = split_nodes([node], TextType.LINK)
    assert len(new_nodes) == 1
    assert new_nodes[0].text == ""
    assert new_nodes[0].text_type == TextType.TEXT


def test_split_nodes_consecutive_markdown():
    node = TextNode(
        "![first image](https://www.first.dev)![second image](https://www.second.dev)",
        TextType.TEXT,
    )
    new_nodes = split_nodes([node], TextType.IMAGE)
    assert len(new_nodes) == 2
    assert new_nodes[0].text_type == TextType.IMAGE
    assert new_nodes[0].url == "https://www.first.dev"
    assert new_nodes[1].url == "https://www.second.dev"

    node = TextNode(
        "[first link](https://www.first.dev)[second link](https://www.second.dev)",
        TextType.TEXT,
    )
    new_nodes = split_nodes([node], TextType.LINK)
    assert len(new_nodes) == 2
    assert new_nodes[0].text_type == TextType.LINK
    assert new_nodes[0].url == "https://www.first.dev"
    assert new_nodes[1].url == "https://www.second.dev"
