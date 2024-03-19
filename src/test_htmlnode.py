import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "link for more info", None, {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.boot.dev\" target=\"_blank\"")
        
    def test_repr(self):
        child_node = HTMLNode("a", "link for more info", None, {"href": "https://www.boot.dev", "target": "_blank"})
        node = HTMLNode("p", "text of the site here", child_node, {"class": "bold important-text color2"})
        self.assertEqual("HTMLNode(p, text of the site here, HTMLNode(a, link for more info, None, {'href': 'https://www.boot.dev', 'target': '_blank'}), {'class': 'bold important-text color2'})", repr(node))

    def test_no_tag_to_html(self):
        leaf_node = LeafNode(None, "Hello")
        self.assertEqual(leaf_node.to_html(), "Hello")

    def test_leaf_node_to_html(self):
        leaf_node = LeafNode("a", "link to somewhere", {"href": "https://www.boot.dev"})
        self.assertEqual(leaf_node.to_html(), '<a href="https://www.boot.dev">link to somewhere</a>')

    def test_leaf_no_value(self):
        leaf_node = LeafNode("p", None)
        with self.assertRaises(ValueError) as cm:
            leaf_node.to_html()
        self.assertEqual(
            "value required for LeafNode",
            str(cm.exception)
        )

if __name__ == "__main__":
    unittest.main()