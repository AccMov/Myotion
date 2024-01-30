import xml.etree.ElementTree as ET

class person:
    def __init__(self, ):
        self.data = {
            "first name": "",
            "middle name": "",
            "last name": "",
            "dob": "",
            "gender": "",
            "height":"",
            "weight":"",
        }
    
    def __getattr__(self, key):
        if key in self.data.keys():
            return self.data[key]

    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.data[key] = value
    def __delitem__(self, key):
        return
    def __missing__(self, key):
        return
    
    def print(self):
        print("Person:")
        for x in self.data:
            print("\t", x, ":", self.data[x])

    def toXML(self, xml):
        sub = ET.SubElement(xml, "Person")
        for key in self.data.keys():
            t = ET.SubElement(sub, key)
            t.text = self.data[key]

    def fromXML(self, xml):
