from .xml import *
import time


class person:
    def __init__(
        self,
        name,
        dob="",
        gender="",
        height="",
        weight="",
        first_name="",
        middle_name="",
        last_name="",
    ):
        self.data = {
            "name": name,
            "first_name": first_name,
            "middle_name": middle_name,
            "last_name": last_name,
            "dob": dob,
            "gender": gender,
            "height": str(height),
            "weight": str(weight),
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

    def toXML(self):
        e = xmlElement("person")
        for key in self.data.keys():
            e.addNode(key, str(self.data[key]))
        return e

    @staticmethod
    def fromXML(xml):
        root = xml.find("person")
        if root == None:
            return None

        e = root.find("name")
        if e is None or e.text is None:
            return None

        p = person(xmlStringParse(e.text, str))

        data = {
            "first_name": "",
            "middle_name": "",
            "last_name": "",
            "dob": "",
            "gender": "",
            "height": "",
            "weight": "",
        }
        for key in data.keys():
            e = root.find(key)
            if e != None:
                p[key] = e.text

        return p
