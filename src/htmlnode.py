class HTMLNode:

    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: list = None,
        props: dict = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        class_props = {
            "tag": self.tag,
            "value": self.value,
            "children": self.children,
            "props": self.props,
        }
        return str(class_props)

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        props_string = ""
        for prop, value in self.props.items():
            props_string += f' {prop}="{value}"'
        return props_string


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeadNode object has no attribute value")
        if not self.tag:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}<{self.tag}\>"
