from enum import Enum

from htmlnode import LeafNode, ParentNode

from textnode import text_node_to_html_node, TextNode, TextType

from inline_markdown import text_to_textnodes


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"



def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    clean_blocks = []
    for raw_block in raw_blocks:

        raw_block = raw_block.strip()

        if raw_block != "":
            clean_blocks.append(raw_block)
    return clean_blocks




def block_to_block_type(block):
    
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING

    lines = block.split("\n")

    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE

    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST

    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
        
    return BlockType.PARAGRAPH
    


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_blocks = []
    for block in blocks:
        html_blocks.append(block_to_parent_htmlnode(block))

    return ParentNode("div", html_blocks)

def block_to_parent_htmlnode(block):
    block_type = block_to_block_type(block)
    
    children = text_to_html_children(block, block_type)
    
    if block_type == BlockType.PARAGRAPH:    
        return ParentNode("p", children)
    
    if block_type == BlockType.CODE:
        if not block.startswith("```") or not block.endswith("```"):
            raise ValueError("invalidd code block")
        return ParentNode("pre", children)
        
    if block_type == BlockType.QUOTE: 
        return ParentNode("blockquote", children)
    
    if block_type == BlockType.ULIST:
        return ParentNode("ul", children)
    
    if block_type == BlockType.OLIST:
        return ParentNode("ol", children)
    
    if block_type == BlockType.HEADING:
        if len(block) < 3:
            raise ValueError("Invalid Heading block: Not enough characters")
        if block.count("\n") > 0:
            raise ValueError("Invalid heading block: heading cannot have new lines")
        if block[0] != "#":
            raise ValueError(f"Invalid heading block: expected to start with '#', not '{block[0]}'")
        heading_level = 0
        for char in block:
            if char == "#":
                heading_level += 1
                if heading_level > 6:
                    raise ValueError("Invalid heading block: heading level too high")
                continue
            if char == " ":
                break
            if char not in ("#"," "):
                raise ValueError("Invalid heading block: ")

        if heading_level < 1 or heading_level > 6:
            raise ValueError("Invalid heading block: not allowed heading level")
        return ParentNode(f"h{heading_level}", children)


def text_to_html_children(text, block_type):
    text_nodes = []
    
    if block_type == BlockType.CODE:
        text_nodes = [TextNode(text[4:-3], TextType.CODE)]

    if block_type == BlockType.HEADING:
        text = text.strip("# ")
        text_nodes = text_to_textnodes(text)

    if block_type == BlockType.PARAGRAPH:
        text_nodes = text_to_textnodes(text.replace("\n", " "))
    
    if block_type == BlockType.QUOTE: 
        for line in text.split("\n"):
            if not line.startswith("> "):
                raise ValueError("Invalid quote block: invalid markdown syntax")
        text_nodes = text_to_textnodes(text[2:].replace("\n> ", " "))

    if block_type == BlockType.ULIST:
        lines = text.split("\n")
        children = []
        for line in lines:
            text_nodes = text_to_textnodes(line[2:])
            children.append(ParentNode("li", [text_node_to_html_node(text_node) for text_node in text_nodes]))
        return children
    
    if block_type == BlockType.OLIST:
        lines = text.split("\n")
        children = []
        for line in lines:
            text_nodes = text_to_textnodes(line[3:])
            children.append(ParentNode("li", [text_node_to_html_node(text_node) for text_node in text_nodes]))
        return children
    

    return [text_node_to_html_node(text_node) for text_node in text_nodes]

