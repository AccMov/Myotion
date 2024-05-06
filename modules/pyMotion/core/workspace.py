from .emg import *
from .report import *
from .freq_analysis import *
from .person import *
from .timeSeriesTable import *
import threading
from thefuzz import fuzz

'''
Workspace maintained a set of people with data
'''
class workspace:
    # data profile of each participant
    class profile:
        def __init__(self, emg):
            self.emg = emg
            self.report = None

        def isEMGReady(self):
            return self.emg.isProcessDone()
        
        def isReportReady(self):
            return self.report != None

        def getDataStatus(self):
            return self.emg.isEMGReady(), self.isReportReady()

    def __init__(self, name = ''):
        self.name = name
        # list of participants in workspace
        self.participants = []
        self.filtered_participants = []
        
        # data of participants, hash:profile
        self.profileList = {}

        # list of saved emg config
        self.saved_emgconfig = {}

        # fuzzy match for channels and mvc file name
        self.fuzzforChanAndMVC = {}

    def clear(self):
        self.participants.clear()
        self.profileList.clear()
        self.saved_emgconfig.clear()

    # check if person exist
    def hasParticipant(self, person):
        return person in self.participants

    def getParticipants(self):
        return self.participants

    def getparticipantStringList(self):
        return [p.name for p in self.participants]
    
    def findParticipant(self, key):
        for s in self.participants:
            if key == s.key():
                return s
        return None
    
    def getFilteredParticipants(self, regex):
        to_be_ret = []
        if len(regex) == 0:
            return self.participants
        
        for p in self.participants:
            if re.search(regex, p.name) is not None:
                to_be_ret.append(p)

        return to_be_ret

    # use person as key to access profile
    def __getitem__(self, person):
        if not self.hasParticipant(person):
            return self.__missing__(person)
        # return profile
        return self.profileList[person.key()]
    
    def __delitem__(self, key):
        return
    def __missing__(self, key):
        return

    def addParticipant(self, person, emg):
        if self.hasParticipant(person):
            return -1
        
        self.participants.append(person) 
        self.profileList[person.key()] = self.profile(emg)

        return 0

    def profileStatusList(self):
        return [self.profileList[id].getDataStatus() for p, id in self.participants]
    
    def saveEMGConfigure(self, person, cfgname):
        if not self.hasParticipant(person):
            return -1
        self.saved_emgconfig[cfgname] = self.profileList[person.key()].emg.getProcessConfig().copy()
        return 0

    def getEMGConfigures(self):
        return self.saved_emgconfig
    
    def hasEMGConfigFile(self, name):
        return False

    def genReport(self, person):
        if not self.hasParticipant(person):
            return
        profile = self.profileList[person.key()]

        root = xmlElement('report')
        root.addSubTree(person.toXML())
        root.addSubTree(profile.emg.toXML())
        profile.report = root

    def saveReport(self, person, path):
        if not self.hasParticipant(person):
            return
        profile = self.profileList[person.key()]
        if profile.report is None:
            return

        writer = xmlWriter(path + '/' + person.name + '.xml', profile.report)
        writer.write()
    
    def saveWorkSpace(self):
        return
    
    def loadWorkSpace(self):
        return
    
    def mvcFuzzAddDicts(self, dicts):
        for key, val in dicts.items():
            if key in self.fuzzforChanAndMVC:
                self.fuzzforChanAndMVC[key].append(val)
            else:
                self.fuzzforChanAndMVC[key] = [val]

    # returned max possibile file
    # lower_bound: remove item which possiblity is lower than low_bound
    # return:  (matched_file_list, possibility)
    def mvcFuzzCheckFiles(self, chan, files, lower_bound=0):
        if chan not in self.fuzzforChanAndMVC:
            # if not in fuzz map, try to look for chan in file name
            candidate_token = [chan]
        else:
            candidate_token = self.fuzzforChanAndMVC[chan]
        
        matched = None
        max_p = 0
        for f in files:
            for c in candidate_token:
                p = fuzz.partial_ratio(f, c)
                if p >= lower_bound:
                    if p > max_p:
                        max_p = p
                        matched = [f]
                    elif p == max_p:
                        matched.append(f)

        return matched, max_p
