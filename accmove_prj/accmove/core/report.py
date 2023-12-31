from .emg import *
from .freq_analysis import *
from .person import *
from .workspace import *
from .kinematic import *
from .advance_analysis import *

class report:
    def __init__(self):
        self.data = {
            "person":person(),
            "kinematic":kinematic(),
            "emg":emg(),
            "freq_analysis":freq_analysis(),
            "advance_analysis":advance_analysis(),
        }

    @classmethod
    def fromFile(self, file):
        return
        
    @classmethod
    def fromWorkSpace(self, workspace):
        return
        
    def loadFile(self, file):
        # load from file
        return 0
    
    def writeFile(self, file):
        #write to file
        return 0

    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.data[key] = value
    def __delitem__(self, key):
        return
    def __missing__(self, key):
        return

    def print(self):
        print("Report:")
        for x in self.data:
            print("\t", x, ":")
            self.data[x].print()


    
