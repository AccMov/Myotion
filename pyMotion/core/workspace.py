from .emg import *
from .report import *
from .freq_analysis import *
from .person import *
from .timeSeriesTable import *

'''
Workspace maintained a set of people with data
'''
class workspace:
    def __init__(self, name = ''):
        self.name = name
        # list of people in workspace, name:people
        self.peopleList = {}
        # list of workplace item
        self.emgList = {}
        self.reportList = {}
        self.emgstatus = {}
        self.reportstatus = {}
        # list of emgConfigure
        self.emg_configs = {}

    def getPeopleList(self):
        return self.peopleList
    def getEMGStatus(self):
        return self.emgstatus
    def getReportStatus(self):
        return self.reportstatus

    def hasPerson(self, name):
        if name in self.peopleList.keys:
            return True
        return False
    
    def addPerson(self, person):
        if self.hasPerson(person.name):
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
    
    def addConfigFile(self, name):
        return
    
    def hasConfigFile(self, name):
        return False

    def genReport(self, person):
        return
