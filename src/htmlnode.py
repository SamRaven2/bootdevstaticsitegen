class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError()
    def props_to_html(self):
        if self.props == None or len(self.props) == 0:
            return ""
        result = ""
        for i in self.props:
            result += f" {i}=\"{self.props[i]}\""
        return result
    def __repr__(self):
        return f"HTMLNode Object || Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}"