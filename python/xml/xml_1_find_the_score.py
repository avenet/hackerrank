import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    node_children = node.getchildren()
    attr_number = len(node.attrib)

    if not len(node_children):
        return attr_number

    for node_child in node_children:
        attr_number += get_attr_number(node_child)

    return attr_number


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
