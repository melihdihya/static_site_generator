import re
from src.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def split_nodes(old_nodes, markdown_text_type):
    new_nodes = []
    if markdown_text_type == TextType.IMAGE:
        extracting_function = extract_markdown_images
        string_start = "!"
    else:
        extracting_function = extract_markdown_links
        string_start = ""

    for node in old_nodes:
        parts = extracting_function(node.text)
        if not parts:
            new_nodes.append(node)
            continue
        updated_text = node.text
        for part in parts:
            sections = updated_text.split(f"{string_start}[{part[0]}]({part[1]})", 1)
            if sections[0]:
                text_node = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(text_node)
            link_node = TextNode(part[0], markdown_text_type, part[1])
            new_nodes.append(link_node)
            updated_text = sections[1]

        if updated_text:
            remaining_text_node = TextNode(updated_text, TextType.TEXT)
            new_nodes.append(remaining_text_node)

    return new_nodes
