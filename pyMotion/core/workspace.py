from .emg import *
from .report import *
from .freq_analysis import *
from .person import *
from .timeSeriesTable import *
import threading

'''
Workspace maintained a set of people with data
'''
class workspace:
    # data profile of each participant
    class profile:
        def __init__(self, emg):
            self.emg = emg
            self.proccessed = None
            self.report = None

        def isEMGReady(self):
            return self.proccessed != None

        def isReportReady(self):
            return self.report != None

        def getDataStatus(self):
            return self.isEMGReady(), self.isReportReady()

    def __init__(self, name = ''):
        self.name = name
        # total number of participants, use as id
        # be careful these are multi-thread friendly
        self.participantCount = 0
        # list of participants in workspace,  person : id
        self.participants = {}
        
        # data of participants, hash:profile
        self.profileList = {}

        # list of global emg config
        self.global_emgconfig = {}

    def clear(self):
        self.participantCount = 0
        self.participants.clear()
        self.profileList.clear()
        self.global_emgconfig.clear()

    # check if person exist
    def hasParticipant(self, person):
        return person in self.participants
    
    def getParticipantId(self, person):
        if self.hasParticipant(person):
            return self.participants[person]
        else:
            return len(self.participants)
        
    # use person as key to access profile
    def __getitem__(self, person):
        if not self.hasParticipant(person):
            return self.__missing__(person)
        id = self.getParticipantId(person)
        # return emg
        return self.profileList[id]
    
    def __delitem__(self, key):
        return
    def __missing__(self, key):
        return

    def addParticipant(self, person, emg):
        if self.hasParticipant(person):
            return -1
        
        id = self.getParticipantId(person) 
        self.participants[person] = id 
        self.profileList[id] = self.profile(emg)
        return 0

    def participantStringList(self):
        return [p.name for p, id in self.participants]
    
    def profileStatusList(self):
        return [self.profileList[id].getDataStatus() for p, id in self.participants]
    
    def saveCurrentConfigure(self, name):
        return
    
    def hasConfigFile(self, name):
        return False

    def genReport(self, person):
        return
