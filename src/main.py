from textnode import TextNode, TextType

def main():
    test = TextNode('sum anchor text', TextType.LINK, "https://www.test.com")
    print(test)

main()