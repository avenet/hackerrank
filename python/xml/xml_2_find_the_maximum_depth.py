import xml.etree.ElementTree as etree

maxdepth = 0


def depth(elem, level):
    global maxdepth

    element_children = elem.getchildren()

    if not len(element_children):
        maxdepth = max(maxdepth, level + 1)
        return

    for element_child in element_children:
        depth(element_child, level + 1)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
