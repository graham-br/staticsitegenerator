class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, __other_text_node):
        if (self.text == __other_text_node.text
            and self.text_type == __other_text_node.text_type
            and self.url == __other_text_node.url):
              return True
            
        return False
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"