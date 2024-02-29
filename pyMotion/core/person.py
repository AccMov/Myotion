import xml.etree.ElementTree as ET

class person:
    def __init__(self, ):
        self.data = {
            "name": "",
            "first_name": "",
            "middle_name": "",
            "last_name": "",
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
    
    def toXML(self, xml):
        sub = ET.SubElement(xml, "Person")
        for key in self.data.keys():
            t = ET.SubElement(sub, key)
            t.text = self.data[key]

    def fromXML(self, xml):
