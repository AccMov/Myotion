from .xml import *
import time
class person:
    def __init__(self,
                 name, 
                 dob,
                 gender,
                 height='',
                 weight='',
                 first_name='', 
                 middle_name='', 
                 last_name='',
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
        self.timestamp = str(time.localtime())
    
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
    
    def key(self):
        return hash(self.name + self.timestamp)

    def toXML(self):
        e = xmlElement('Person')
        for key in self.data.keys():
            e.addNode(key, str(self.data[key]))
        return e     

    #def fromXML(self, xml):
