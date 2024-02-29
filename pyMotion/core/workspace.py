from .emg import *
from .report import *
from .freq_analysis import *
from .person import *
from .timeSeriesTable import *

'''
Workspace maintained a set of people with data
'''
class workspace:
    def __init__(self, name=''):
        self.name = name

        # list of people in workspace, name:people
        self.peopleList = {}
        # list of workplace item
        self.emgList = {}
        self.reportList = {}
        # list of emgConfigure
        self.emg_configs = {}

    def ifPersonExist(self, name):
        if name in self.peopleList.keys:
            return True
        return False
    
    def addPerson(self, person):
        if self.ifPersonExist(person.name):
            return -1
        self.peopleList[person.name] = person
        self.emgList[person.name] = None
        self.reportList[person.name] = None
        return 0

    def setEMGFile(self, name, f):
        if not self.ifPersonExist(name):
            return -1
        return self.emgList[name].setEMGFile(f)

    def addMVCFile(self, name, channel, f):
        if not self.ifPersonExist(name):
            return -1
        return self.emgList[name].setMVCFile(channel, f)

    def generateReport(self, person):
        return
