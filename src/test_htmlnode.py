import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "link for more info", None, {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.boot.dev\" target=\"_blank\"")
        
    def test_repr(self):
        child_node = HTMLNode("a", "link for more info", None, {"href": "https://www.boot.dev", "target": "_blank"})
        node = HTMLNode("p", "text of the site here", child_node, {"class": "bold important-text color2"})
        self.assertEqual("HTMLNode(p, text of the site here, HTMLNode(a, link for more info, None, {'href': 'https://www.boot.dev', 'target': '_blank'}), {'class': 'bold important-text color2'})", repr(node))

if __name__ == "__main__":
    unittest.main()