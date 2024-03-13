from .emg import *
from .freq_analysis import *
from .person import *
from .workspace import *
from .kinematic import *
from .advance_analysis import *
from .xml import *

class report:
    def __init__(self, person, emg):
        root = xmlElement('report')
        root.addSubTree(person.toXML())
        root.addSubTree(emg.toXML())

    def loadFile(self, file):
        # load from file
        return 0
    
    def writeXML(self, file):
        xmlWriter(file, self.root).write()