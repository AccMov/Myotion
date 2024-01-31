from .emg import *
from .freq_analysis import *
from .person import *
from .timeSeriesTable import *



class workItem:
    def __init__(self):
        self.emg =


'''
Maintain a list of people

persons: set of people 
'''
class workspace:
    def __init__(self):
        self.peopleList = {}
        self.emg_configure = emg_configure() 

    def addPerson(self, person):
        # check person exist
        self.worklist[person] = workItem()

    def addEMGFile(self, person, f):
        return

    def addEMGTrailFile(self, person, channel, f):
        return

    def generateReport(self):
        return
