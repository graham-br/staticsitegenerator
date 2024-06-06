import unittest

from markdown_to_html_node import markdown_to_html_node

from htmlnode import (
    LeafNode,
    ParentNode,
)


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_heading_to_html(self):
        md = """
# Heading 1

###### Heading 6
"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(), "<div><h1>Heading 1</h1><h6>Heading 6</h6></div>"
        )

    def test_code_to_html(self):
        md = """
```
my_list = [1, 2, 3]
print(my_list)
```
"""

        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><pre><code>\nmy_list = [1, 2, 3]\nprint(my_list)\n</code></pre></div>",
        )

    def test_quote_to_html(self):
        md = "> Quote of the day ~ Someone"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><blockquote>Quote of the day ~ Someone</blockquote></div>",
        )

    def test_ul_to_html(self):
        md = """
- one
- two
- three
"""

        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(), "<div><ul><li>one</li><li>two</li><li>three</li></ul></div>"
        )

    def test_ol_to_html(self):
        md = """
1. one
2. two
3. three
"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(), "<div><ol><li>one</li><li>two</li><li>three</li></ol></div>"
        )

    def test_paragraph_to_html(self):
        md = "This is a paragraph"
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><p>This is a paragraph</p></div>")

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )


if __name__ == "__main__":
    unittest.main()
