
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None or self.props == {}:
            return ""

        props_html = ""
        
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"



class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
        
    
    def to_html(self):
        if self.value is None:
            raise ValueError
        
        if self.tag is None:
            return self.value
         

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag,children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("no tag on parent html node")
        if self.children is None or len(self.children) == 0:
            raise ValueError("parent html node doesn't have any children")

        html_string = f"<{self.tag}>"

        for child in self.children:
            html_string += child.to_html()

        html_string += f"</{self.tag}>"

        return html_string

