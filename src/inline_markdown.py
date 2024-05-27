import re
from typing import Text
from textnode import (
    TextNode,
    text_type_text,
    text_type_image,
    text_type_link,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
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
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    regex = r"!\[(.*?)\]\((.*?)\)"

    matches = re.findall(regex, text)

    return matches


def extract_markdown_links(text):
    regex = r"\[(.*?)\]\((.*?)\)"

    matches = re.findall(regex, text)

    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        image_nodes = extract_markdown_images(old_node.text)

        if len(image_nodes) == 0:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        for i in range(len(image_nodes)):
            sections = old_node.text.split(
                f"![{image_nodes[i][0]}]({image_nodes[i][1]})", 1
            )
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] == "":
                split_nodes.append(
                    TextNode(image_nodes[i][0], text_type_image, image_nodes[i][1])
                )
            else:
                split_nodes.append(TextNode(sections[0], text_type_text))
                split_nodes.append(
                    TextNode(image_nodes[i][0], text_type_image, image_nodes[i][1])
                )

            if len(sections) > 1:
                old_node = TextNode(sections[1], text_type_text)
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        link_nodes = extract_markdown_links(old_node.text)

        if len(link_nodes) == 0:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        for i in range(len(link_nodes)):
            sections = old_node.text.split(
                f"[{link_nodes[i][0]}]({link_nodes[i][1]})", 1
            )
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] == "":
                split_nodes.append(
                    TextNode(link_nodes[i][0], text_type_link, link_nodes[i][1])
                )
            else:
                split_nodes.append(TextNode(sections[0], text_type_text))
                split_nodes.append(
                    TextNode(link_nodes[i][0], text_type_link, link_nodes[i][1])
                )

            if len(sections) > 1:
                old_node = TextNode(sections[1], text_type_text)
        new_nodes.extend(split_nodes)
    return new_nodes
