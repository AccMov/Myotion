from .emg import *
from .freq_analysis import *
from .person import *
from .workspace import *
from .kinematic import *
from .advance_analysis import *
from .statistic import *
from .xml import *


class report:
    def __init__(self, person, emg):
        self.root = None
        self.fpath = None

        if person is None or emg is None:
            return

        self.root = xmlElement("report")
        self.root.addSubTree(person.toXML())
        # get a copy of emgTST, filter out control signal
        filteredTST = emg.emgTST.copy()
        filteredTST.setname("EMG")
        for c in filteredTST.channels:
            if c not in emg.enabledChannels:
                filteredTST.removeChannel(c)

        # emg Time Series Data
        # MVC is saved in splited file
        self.root.addSubTree(filteredTST.toXML())
        # emg process configuration
        self.root.addSubTree(emg.processCFG.toXML())

        # emg Statistical data
        self.root.addSubTree(emgStatistic(filteredTST).toXML())

    def toXML(self):
        return self.root

    def getPath(self):
        return self.fpath

    # load report, return tst
    def async_load(self):
        if self.fpath is None:
            return
        xml = xmlReader(self.fpath).get()
        if xml == None:
            logger.error("report: file is empty")
            return -1
        root = xml.find("report")
        if root == None:
            logger.error("report: no report found")
            return -1
        self.root = xml
        # this assumes only one tst is included
        return timeSeriesTable.fromXML(root)

    def writeXML(self, file):
        self.fpath = file
        xmlWriter(file, self.root).write()
