import os

from markdown_to_html_node import markdown_to_html_node


def extract_title(markdown):
    title = ""
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            title = line[2:]
            break
    if title == "":
        raise ValueError("No h1 header found. All pages require h1.")
    return title


def generate_page(from_path, template_path, dest_path):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown file at from_path and store contents in a variable
    from_file = open(from_path, "r")
    from_contents = from_file.read()
    from_file.close()

    # Read the template file at template_path and store contents in a variable
    template_file = open(template_path, "r")
    template_contents = template_file.read()
    template_file.close()

    # Convert the markdown file to HTML
    content_node = markdown_to_html_node(from_contents)
    content_html = content_node.to_html()

    # Grab title of the page
    title = extract_title(from_contents)

    # Replace Title and Content placeholders in template
    template_contents = template_contents.replace("{{ Title }}", title)
    template_contents = template_contents.replace("{{ Content }}", content_html)

    # Write new HTML file at dest_path
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    new_file = open(dest_path, "w")
    new_file.write(template_contents)
    new_file.close()

    return None
