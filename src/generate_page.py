import os

from pathlib import Path

from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)



def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")


    markdown = ""
    with open(from_path) as f:
        markdown = f.read()
    
    template = ""
    with open(template_path) as f:
        template = f.read()

    title = extract_title(markdown)
    html_content = markdown_to_html_node(markdown).to_html()
    

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    
    dest_dir_path = os.path.dirname(dest_path)
    
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, mode="w") as f:
        f.write(template)
    

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