import os

from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")


    markdown = ""
    with open(from_path) as f:
        markdown = f.read()
    
    template = ""
    with open(template_path) as f:
        template = f.read()

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    html = template.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", content)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, mode="w") as f:
        f.write(html)
    
def extract_title(markdown):
    lines = markdown.split("\n")

    title_line = ""
    for line in lines:
        if line.startswith("# "):
            if title_line == "":
                title_line = line
            else:
                raise ValueError("Failed to extract title: markdown file contains more than 1 h1 title header. Only 1 is allowed")
    
    if title_line == "":
        raise ValueError("Failed to extract title: no h1 title header found")

    return title_line.strip("# ")