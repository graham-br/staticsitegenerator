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
