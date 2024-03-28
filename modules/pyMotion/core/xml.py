import xml.etree.ElementTree as ET

class xmlElement():
    def __init__(self, name):
        self.element = ET.Element(name)
    
    # return ET.element
    def addSubTree(self, xmlElement):
        self.element.append(xmlElement.element)

    # return ET.subElement
    # tag: Node tag, 
    # val: text of the tag, 
    # attrib: attribute of the tag
    # i.e  <color required=true> yellow </color>
    #      color -> tag
    #      yellow -> text
    #      required=true -> attrib
    def addNode(self, tag, val, attrib={}):
        n = ET.SubElement(self.element, tag, attrib)
        n.text = val
        return n

class xmlWriter():
    def __init__(self, path, xmlElement=''):
        self.path = path

        self.tree = ET.ElementTree()
        self.root = xmlElement.element
        
    def setRoot(self, xmlElement):
        self.root = xmlElement.element

    def write(self):
        self.tree._setroot(self.root)
        # pretty print
        ET.indent(self.tree)
        self.tree.write(self.path)
