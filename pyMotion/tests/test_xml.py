import xml.etree.ElementTree as ET

'''
<fruit>
    <apple />
    <grape />
    <orange ppp="1">aaa</orange>
    <color>
       <read />
       <black />
    </color>
</fruit>
'''

def addNode(t, val,  attrib={}):
    return ET.SubElement(t, val, attrib)

def addSection(name):
    return ET.Element(name)

def addSubTree(element):
    sub = addSection("color")
    addNode(sub, 'read')
    addNode(sub, 'black')
    return element.append(sub)

def createXML(path):
    tree = ET.ElementTree()
    element = addSection("fruit")
    addNode(element, 'apple')
    addNode(element, 'grape')
    node = addNode(element, 'orange', { 'ppp':'1' })
    node.text = 'aaa bbb'
    addSubTree(element)
    tree._setroot(element)
    tree.write(path) 


createXML('test.xml')
