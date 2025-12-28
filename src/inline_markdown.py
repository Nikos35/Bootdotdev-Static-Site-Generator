from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        sections = old_node.text.split(delimiter)
    
        if len(sections) % 2 == 0:
            raise Exception('Invalid markdown syntax')
        
        for i in range(0, len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(sections[i], text_type))

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        if old_node.text == "":
            continue
        matches = extract_markdown_images(old_node.text)
        if len(matches) == 0:
            new_nodes.append(old_node)

        string_index = 0
        for match in matches:
            sections = old_node.text[string_index:].split(f"![{match[0]}]({match[1]})", 1)
            # print(f"sections: {sections}, '[{match[0]}]({match[1]})'")
            if len(sections[0]) > 0:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
            
            string_index += len(sections[0]) + len(f"![{match[0]}]({match[1]})")
        # print(string_index < len(old_node.text))
    
        if string_index < len(old_node.text):
            new_nodes.append(TextNode(old_node.text[string_index:], TextType.TEXT)) 
                   
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        if old_node.text == "":
            continue
        matches = extract_markdown_links(old_node.text)
        if len(matches) == 0:
            new_nodes.append(old_node)

        string_index = 0
        for match in matches:
            sections = old_node.text[string_index:].split(f"[{match[0]}]({match[1]})", 1)
            print(f"sections: {sections}, '[{match[0]}]({match[1]})'")
            
            if len(sections[0]) > 0:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
                
            new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
            string_index += len(sections[0]) + len(f"[{match[0]}]({match[1]})")
        
        print(string_index < len(old_node.text))
        if string_index < len(old_node.text):
            new_nodes.append(TextNode(old_node.text[string_index:], TextType.TEXT)) 
                   
    return new_nodes

        
    


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches