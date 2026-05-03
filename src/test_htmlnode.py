import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_allNone(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_tagOnly(self):
        node = HTMLNode(tag = "a")
        self.assertIsNotNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_valueOnly(self):
        node = HTMLNode(value = "This is some test text that is in the value field")
        self.assertIsNone(node.tag)
        self.assertIsNotNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_propsToHTML(self):
        node = HTMLNode(props = {"href":"https://www.google.com", "target":"_blank"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

if __name__ == "__main__":
    unittest.main()