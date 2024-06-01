block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = []
    split_markdown = markdown.splitlines()
    block_text = ""
    for line in split_markdown:
        if line == "" and block_text != "":
            blocks.append(block_text)
            block_text = ""
            continue
        if block_text != "":
            block_text = f"{block_text}\n{line.strip()}"
        else:
            block_text = line.strip()
    if block_text != "":
        blocks.append(block_text)
    return blocks


def block_to_block_type(block):
    # Heading
    heading = True
    first_element = block.split()[0]
    if len(first_element) <= 6:
        for letter in first_element:
            if letter != "#":
                heading = False
                break
    else:
        heading = False
    if heading:
        return block_type_heading
    # Code
    code_split = block.split("```")
    if len(code_split) > 1 and len(code_split) % 2 != 0:
        return block_type_code
    # Quote
    lines = block.split("\n")
    quote = True
    for line in lines:
        if line[0] != ">":
            quote = False
            break
    if quote:
        return block_type_quote
    # Unordered list
    unordered = True
    for line in lines:
        if not (line[:2] == "* " or line[:2] == "- "):
            unordered = False
            break
    if unordered:
        return block_type_unordered_list
    # Ordered list
    ordered = True
    i = 1
    for line in lines:
        if line[:3] != f"{i}. ":
            ordered = False
            break
        i += 1
    if ordered:
        return block_type_ordered_list
    # Paragraph if no matches
    return block_type_paragraph
