from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
)

from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes

from htmlnode import (
    ParentNode,
    LeafNode,
)


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_heading:
            nodes.append(block_to_heading(block))
            continue
        if block_type == block_type_code:
            nodes.append(block_to_code(block))
            continue
        if block_type == block_type_quote:
            nodes.append(block_to_quote(block))
            continue
        if block_type == block_type_unordered_list:
            nodes.append(block_to_unordered_list(block))
        if block_type == block_type_ordered_list:
            nodes.append(block_to_ordered_list(block))
        if block_type == block_type_paragraph:
            nodes.append(block_to_paragraph(block))
            continue
    div_node = ParentNode("div", nodes)
    return div_node


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def block_to_heading(markdown_block):
    heading_sections = markdown_block.split()
    heading_number = len(heading_sections[0])
    text = markdown_block[heading_number + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{heading_number}", children)


def block_to_code(markdown_block):
    code_sections = markdown_block.split("```")
    text = code_sections[1]
    children = text_to_children(text)
    code_node = ParentNode("code", children)
    return ParentNode("pre", [code_node])


def block_to_quote(markdown_block):
    lines = markdown_block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def block_to_unordered_list(markdown_block):
    lines = markdown_block.splitlines()
    html_items = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def block_to_ordered_list(markdown_block):
    lines = markdown_block.splitlines()
    html_items = []
    for line in lines:
        text = line[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def block_to_paragraph(markdown_block):
    lines = markdown_block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)
