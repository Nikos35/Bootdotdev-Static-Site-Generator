from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"



def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    clean_blocks = []
    for i in range(0, len(raw_blocks)):

        raw_blocks[i] = raw_blocks[i].strip()

        if raw_blocks[i] != "":
            clean_blocks.append(raw_blocks[i])


    return clean_blocks

def block_to_block_type(block):
    
    if block[:2] == "# ":
        return BlockType.HEADING

    if block[:3] == "```" and block[2::-1] == "```":
        return BlockType.CODE
    
    lines = block.split("\n")


    isQuote = True
    i = 0
    while isQuote and i < len(lines) - 1:
        if lines[i][0] != ">":
            isQuote = False
        i += 1

    if isQuote:
        return BlockType.QUOTE

    isUnorderedList = True
    i = 0
    while isUnorderedList and i < len(lines) - 1:
        if lines[i][0:2] != "- ":
            isUnorderedList = False
        i += 1
    if isUnorderedList:
        return BlockType.UNORDERED_LIST 
    

    isOrderedList = True
    i = 0
    while isOrderedList and i < len(lines) - 1:
        if lines[i][0:3] != f"{i+1}. ":
            isOrderedList = False
        i += 1

    if isOrderedList:
        return BlockType.ORDERED_LIST 
    
    return BlockType.PARAGRAPH
    