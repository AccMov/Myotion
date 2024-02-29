import xml.etree.ElementTree as ET

class xmlElement():
    def __init__(self, name):
        self.element = ET.Element(name)
    
    # return ET.element
    def addSubTree(self, element):
        self.element.append(element)

    # return ET.subElement
    # tag: Node tag, 
    # val: text of the tag, 
    # attrib: attribute of the tag
    # i.e  <color required=true> yellow </color>
    #      color -> tag
    #      yellow -> text
    #      required=true -> attrib
    def addNode(t, tag, val, attrib={}):
        n = ET.SubElement(t, val, attrib)
        n.text = val
        return n

class xmlWriter():
    def __init__(self, path, element=''):
        self.path = path

        self.tree = ET.ElementTree()
        self.root = element
        self.tree._setroot(self.root)

    def setRoot(self, element):
        self.root = element

    def write(self):
        self.tree.write(self.path)
