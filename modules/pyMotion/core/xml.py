import xml.etree.ElementTree as ET
import os
import numpy as np

# helper function to convert e to a XML value
# this add pair of "" on strings
def xmlString(e):
    if isinstance(e, list) or isinstance(e, set) or isinstance(e, np.ndarray):
        return " ".join(xmlString(p) for p in e)
    elif isinstance(e, float):
        return xmlString(str(format(e, ".6f")))
    elif isinstance(e, int) or isinstance(e, bool):
        return xmlString(str(e))
    elif isinstance(e, str):
        if e.startswith('"') and e.endswith('"'):
            return e
        else:
            return '"' + e + '"'
    else:
        assert 0, "xmlString type:" + type(e) + " not supported"


# this remove pair of "" on strings
def xmlStringParse(s, t=str):
    if t is int:
        return int(xmlStringParse(s, str))
    elif t is float:
        return float(xmlStringParse(s, str))
    elif t is str:
        return s[1:-1] # remove double quotes


def xmlStringParseList(s):
    return [a for a in [a.strip() for a in s.split("\"")] if a]


"""
a = xmlElement('a')
a.addNode('b', '1', {'c': '2'})
d = xmlElement('d')
d.addNode('e', '3')
a.addSubTree(d)
a.addNode('f', [1,2,3,4])
a.addDict('animals', {'cat':1, 'dog':2})
output:
<a>
    <b c=2> 1 </b>
    <d>
        <e> 3 </e>
    </d>
    <f> 1 2 3 4 </f>
    <animals>
        <cat> 1 </cat>
        <dog> 2 </dog>
    </animals>
</a>
"""


class xmlElement(ET.Element):
    def __init__(self, name, attrib={}):
        super().__init__(name, attrib)

    # expect ET.Element
    def addSubTree(self, e):
        self.append(e)

    # add a dict as a subtree
    # please note that "key" string has to be a valid xml token
    # (i.e. cannot have space)
    def addDict(self, name, e, attrib={}):
        root = xmlElement(name, attrib)
        for a, b in e.items():
            root.addNode(xmlString(a), xmlString(b))
        self.addSubTree(root)

    # add a dict as a special subtree with format:
    # i.e  <name>
    #      <map name="old"> new </map>
    #      ...
    #      </name>
    # this is for mapping while the name could be
    # an invalid xml token
    def addMap(self, name, map):
        root = xmlElement(name)
        for old, new in map.items():
            root.addNode("map", xmlString(new), {"name": xmlString(old)})
        self.addSubTree(root) 

    # return ET.subElement
    # tag: Node tag,
    # val: text of the tag,
    # attrib: attribute of the tag
    # i.e  <color required=true> yellow </color>
    #      color -> tag
    #      yellow -> val
    #      required=true -> attrib
    def addNode(self, tag, val, attrib={}):
        n = ET.SubElement(self, tag, attrib)
        n.text = xmlString(val)


class xmlWriter:
    def __init__(self, path, xmlElement=""):
        self.path = os.path.normpath(path)

        self.tree = ET.ElementTree()
        if xmlElement != None:
            self.root = xmlElement
        else:
            self.root = None

    def setRoot(self, xmlElement):
        self.root = xmlElement.element

    def write(self):
        self.tree._setroot(self.root)
        # pretty print
        ET.indent(self.tree)
        self.tree.write(self.path, encoding="utf-8", xml_declaration=True)


class xmlReader:
    def __init__(self, path):
        self.path = path
        self.tree = ET.parse(path)
        self.root = self.tree.getroot()

    def get(self):
        e = xmlElement(self.root.tag, self.root.attrib)
        for el in self.root.iter():
            e.addSubTree(el)
        return e
