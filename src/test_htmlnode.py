import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "link for more info",
            None,
            {"href": "https://www.boot.dev", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://www.boot.dev" target="_blank"'
        )

    def test_repr(self):
        child_node = HTMLNode(
            "a",
            "link for more info",
            None,
            {"href": "https://www.boot.dev", "target": "_blank"},
        )
        node = HTMLNode(
            "p",
            "text of the site here",
            child_node,
            {"class": "bold important-text color2"},
        )
        self.assertEqual(
            "HTMLNode(p, text of the site here, HTMLNode(a, link for more info, None, {'href': 'https://www.boot.dev', 'target': '_blank'}), {'class': 'bold important-text color2'})",
            repr(node),
        )

    def test_no_tag_to_html(self):
        leaf_node = LeafNode(None, "Hello")
        self.assertEqual(leaf_node.to_html(), "Hello")

    def test_leaf_node_to_html(self):
        leaf_node = LeafNode("a", "link to somewhere", {"href": "https://www.boot.dev"})
        self.assertEqual(
            leaf_node.to_html(), '<a href="https://www.boot.dev">link to somewhere</a>'
        )

    def test_leaf_no_value(self):
        leaf_node = LeafNode("p", None)
        with self.assertRaises(ValueError) as cm:
            leaf_node.to_html()
        self.assertEqual("value required for LeafNode", str(cm.exception))

    def test_to_html_parent_with_child(self):
        child_node = LeafNode("p", "text")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><p>text</p></div>")

    def test_to_html_parent_with_grandchild(self):
        grandchild_node = LeafNode("b", "bold text")
        child_node = ParentNode("p", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><p><b>bold text</b></p></div>")

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )


if __name__ == "__main__":
    unittest.main()
