import threading

from .emg import *
from .report import *
from .freq_analysis import *
from .person import *
from .timeSeriesTable import *
from thefuzz import fuzz

'''
Workspace maintained a set of people with data
'''
class workspace:
    # data profile of each participant
    class profile:
        def __init__(self, emg, kin):
            self.emg = emg
            self.report = None
            self.kinematic = kin

        def isEMGReady(self):
            return self.emg.isProcessDone()
        
        def isReportReady(self):
            return self.report != None

        def getDataStatus(self):
            return self.emg.isEMGReady(), self.isReportReady()
    
    class reportEMGConfig:
        def __init__(self):
            self.csv = True
            self.c3d = False
            self.mat = False

        def outputMVC(self, st):
            self.mvc = st
        def outputCSV(self, st):
            self.csv = st
        def outputC3D(self, st):
            self.c3d = st
        def outputMAT(self, st):
            self.mat = st

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

        # report - EMG config
        self.reportemgconfig = self.reportEMGConfig()

    def clear(self):
        self.participants.clear()
        self.profileList.clear()
        self.kinematicList.clear()
        self.saved_emgconfig.clear()

    # check if person exist
    def hasParticipant(self, person):
        return person in self.participants

    def getParticipants(self):
        return self.participants

    def getparticipantStringList(self):
        return [p.name for p in self.participants]
    
    def findParticipant(self, name):
        for s in self.participants:
            if name == s.name:
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
        return self.profileList[person.name]
    
    def __delitem__(self, key):
        return
    def __missing__(self, key):
        return

    def addParticipant(self, person, emg, kin):
        if self.hasParticipant(person):
            return -1
        
        self.participants.append(person) 
        self.profileList[person.name] = self.profile(emg, kin)
        return 0

    def profileStatusList(self):
        return [self.profileList[id].getDataStatus() for p, id in self.participants]
    
    def saveEMGConfigure(self, person, cfgname):
        if not self.hasParticipant(person):
            return -1
        self.saved_emgconfig[cfgname] = self.profileList[person.name].emg.getProcessConfig().copy()
        return 0

    def getEMGConfigures(self):
        return self.saved_emgconfig
    
    def hasEMGConfigFile(self, name):
        return False

    def genReport(self, person):
        if not self.hasParticipant(person):
            return
        profile = self.profileList[person.name]

        root = xmlElement('report')
        # person data
        root.addSubTree(person.toXML())
        # emg data
        # MVC is saved in splited file
        root.addSubTree(profile.emg.toXML())
        profile.report = root

        profile.emg.setProcessDone()

    def saveReport(self, person, path):
        if not self.hasParticipant(person):
            return
        profile = self.profileList[person.name]
        if profile.report is None:
            return
        
        # save "rpt" report
        report_name = path + '/' + person.name + '.rpt'
        writer = xmlWriter(report_name, profile.report)
        writer.write()

        # save csv
        if self.reportemgconfig.csv:
            # utf-16 for excel compactability issue
            csv_name = path + '/' + person.name + '.csv'
            emgdf = profile.emg.emgTST.toPandasFrame()
            emgdf.to_csv(csv_name, sep=',', encoding='utf-8')

            mvccsv_name = path + '/' + person.name + '(MVC)' + '.csv'
            emgmvcdf = profile.emg.emgMVCTST.toPandasFrame()
            emgmvcdf.to_csv(mvccsv_name, sep=',', encoding='utf-8')
    
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
    # return:  (matched_files_with_same_possibility, possibility)
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
