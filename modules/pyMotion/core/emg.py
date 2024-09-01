from .timeSeriesTable import *
from .c3d import *
from .mat import *
from .xml import *
from enum import Enum
from .logger import *
import re
from enum import IntEnum


class emgConfigEnum(IntEnum):
    FILTER = 0
    FULL_W_RECT = 1
    DC_OFFSET = 2
    ACTIVATION = 3
    NORMALIZATION = 4
    SUMMARY = 5
    MAX = 6


class emgConfigInfo:
    classical_steps = [
        emgConfigEnum.DC_OFFSET,
        emgConfigEnum.FILTER,
        emgConfigEnum.FULL_W_RECT,
        emgConfigEnum.FILTER,
        emgConfigEnum.NORMALIZATION,
        emgConfigEnum.SUMMARY,
    ]
    nameMap = {
        emgConfigEnum.DC_OFFSET: "remove_dc_offset",
        emgConfigEnum.FULL_W_RECT: "full_wave_rectification",
        emgConfigEnum.FILTER: "filter",
        emgConfigEnum.NORMALIZATION: "normalization",
        emgConfigEnum.ACTIVATION: "activation",
        emgConfigEnum.SUMMARY: "summary",
    }


class emgDCOffset:
    id = emgConfigEnum.DC_OFFSET

    def __init__(self):
        self.enable = False

    def toXML(self):
        e = xmlElement("emgDCOffset")
        e.addNode("enable", xmlString(self.enable))
        return e

    @staticmethod
    def fromXML(xml):
        root = xml.find("emgDCOffset")
        if root == None:
            return None

        obj = emgDCOffset
        e = root.find("enable")
        if e and e.text:
            obj.enable = xmlStringParse(e.text, bool)
        else:
            obj.enable = False
        return obj


class emgRectification:
    id = emgConfigEnum.FULL_W_RECT

    def __init__(self):
        self.enable = False

    def toXML(self):
        e = xmlElement("emgRectification")
        e.addNode("enable", xmlString(self.enable))
        return e

    @staticmethod
    def fromXML(xml):
        root = xml.find("emgRectification")
        if root == None:
            return None

        obj = emgRectification
        e = root.find("enable")
        if e and e.text:
            obj.enable = xmlStringParse(e.text, bool)
        else:
            obj.enable = False
        return obj


class emgNormalization:
    id = emgConfigEnum.NORMALIZATION

    def __init__(self):
        self.enable = False

    def toXML(self):
        e = xmlElement("emgNormalization")
        e.addNode("enable", xmlString(self.enable))
        return e

    @staticmethod
    def fromXML(xml):
        root = xml.find("emgNormalization")
        if root == None:
            return None

        obj = emgNormalization
        e = root.find("enable")
        if e and e.text:
            obj.enable = xmlStringParse(e.text, bool)
        else:
            obj.enable = False
        return obj


class emgSummary:
    id = emgConfigEnum.SUMMARY

    def __init__(self):
        self.max = 0
        self.min = 0
        self.med = 0
        self.rms = 0
        self.ptp = 0
        self.zeros = 0

    def toXML(self):
        e = xmlElement("emgSummary")
        # we don't save temp calculation to config file
        return e


class emgFilterEnum(IntEnum):
    LOW_PASS = 0
    BAND_PASS = 1
    MAX = 2


class emgFilter:
    id = emgConfigEnum.FILTER

    def __init__(self):
        self.enable = False
        self.type = emgFilterEnum.LOW_PASS
        self.cutoff_l = 0
        self.cutoff_h = 0
        self.order = int(2)

        self.nameMap = {
            emgFilterEnum.LOW_PASS: "low pass filter",
            emgFilterEnum.BAND_PASS: "band pass filter",
            emgFilterEnum.MAX: "N/A",
        }

    def setType(self, t: int):
        if t >= emgFilter.MAX or t < 0:
            logger.error("invalid filter type!")
            return -1

        self.type = t

    def setCutOff_L(self, freq: float):
        self.cutoff_l = freq

    def setCutOff_H(self, freq: float):
        self.cutoff_h = freq

    def setOrder(self, index: int):
        self.order = index

    def toXML(self):
        e = xmlElement("emgFilter")
        e.addNode("type", xmlString(int(self.type)))
        e.addNode("order", xmlString(self.order))
        e.addNode("cutoff_l", xmlString(self.cutoff_l))
        e.addNode("cutoff_h", xmlString(self.cutoff_h))
        return e

    @staticmethod
    def fromXML(xml):
        root = xml.find("emgFilter")
        if root == None:
            return None

        obj = emgFilter
        e = root.find("type")
        if e and e.text:
            obj.type = xmlStringParse(e.text, int)
        else:
            obj.type = emgFilterEnum.LOW_PASS
        e = root.find("order")
        if e and e.text:
            obj.order = xmlStringParse(e.text, int)
        else:
            obj.order = 2
        e = root.find("cutoff_l")
        if e and e.text:
            obj.cutoff_l = xmlStringParse(e.text, float)
        else:
            obj.cutoff_l = 0
        e = root.find("cutoff_h")
        if e and e.text:
            obj.cutoff_h = xmlStringParse(e.text, float)
        else:
            obj.cutoff_h = 0
        return obj


class emgActivation:
    id = emgConfigEnum.ACTIVATION

    def __init__(self):
        self.threhold = 0
        self.n_above = 5
        self.n_below = 5

    def setThreHold(self, t: float):
        self.threhold = t

    def set_L(self, l):
        self.n_below = l

    def set_H(self, h):
        self.n_above = h

    def toXML(self):
        e = xmlElement("emgActivation")
        e.addNode("threhold", xmlString(self.threhold))
        e.addNode("n_above", xmlString(self.n_above))
        e.addNode("n_below", xmlString(self.n_below))
        return e

    @staticmethod
    def fromXML(xml):
        root = xml.find("emgActivation")
        if root == None:
            return None

        obj = emgActivation
        e = root.find("threhold")
        if e and e.text:
            obj.threhold = xmlStringParse(e.text, float)
        else:
            obj.type = 0
        e = root.find("n_above")
        if e and e.text:
            obj.n_above = xmlStringParse(e.text, int)
        else:
            obj.n_above = 5
        e = root.find("n_below")
        if e and e.text:
            obj.n_below = xmlStringParse(e.text, int)
        else:
            obj.n_below = 5
        return obj


class emgConfigure:
    def __init__(self):
        # default config for each step
        self.stepConfig = []
        for s in emgConfigInfo.classical_steps:
            self.stepConfig.append(self.initConfig(s))

    # use step id as key to access config file
    def __getitem__(self, id):
        return self.stepConfig[id]

    def copy(self):
        t = emgConfigure()
        t.stepConfig = self.stepConfig.copy()
        return t

    """
    # add new step
    def addStep(self, idx, pos):
        if idx >= emgConfigure.MAX or idx < 0:
            logger.error("invalid emg steps!")
            return -1

        self.step.insert(pos, idx)

    # remove step
    def removeStep(self, pos):
        self.step.remove(pos)
    """

    def getTypeInfo(self, idx):
        type_id = self.stepConfig[idx].id
        return type_id, emgConfigInfo.nameMap[type_id]

    def getStepStringList(self):
        return [emgConfigInfo.nameMap[s.id] for s in self.stepConfig]

    def size(self):
        return len(self.stepConfig)

    # create a config for one step
    def initConfig(self, type):
        if type == emgConfigEnum.FILTER:
            return emgFilter()
        elif type == emgConfigEnum.ACTIVATION:
            return emgActivation()
        elif type == emgConfigEnum.DC_OFFSET:
            return emgDCOffset()
        elif type == emgConfigEnum.FULL_W_RECT:
            return emgRectification()
        elif type == emgConfigEnum.NORMALIZATION:
            return emgNormalization()
        elif type == emgConfigEnum.SUMMARY:
            return emgSummary()
        else:
            return None

    """
    <emgConfigure>
        <remove_dc_offset/>
        <filter> 
           <type> </type>
           ...
        </filter>
    </emgConfigure>
    """

    def toXML(self):
        # top tree
        e = xmlElement("emgConfigure")
        for s in self.stepConfig:
            e.addSubTree(s.toXML())
        return e

    @staticmethod
    def fromXML(xml):
        root = xml.find("emgConfigure")
        if root == None:
            return None

        obj = emgConfigure()
        for el in root:
            cfg = emgFilter.fromXML(el)
            if cfg:
                obj.stepConfig.append(cfg)
                continue
            cfg = emgActivation.fromXML(el)
            if cfg:
                obj.stepConfig.append(cfg)
                continue
            cfg = emgDCOffset.fromXML(el)
            if cfg:
                obj.stepConfig.append(cfg)
                continue
            cfg = emgRectification.fromXML(el)
            if cfg:
                obj.stepConfig.append(cfg)
                continue
            cfg = emgNormalization.fromXML(el)
            if cfg:
                obj.stepConfig.append(cfg)
                continue
        return obj


class emg:
    def __init__(self, file=""):
        self.emgFile = file  # file path
        self.emgTST = None  # emg data
        self.emgMVCTST = None  # emg MVC data
        self.processCFG = None  # emg data process configure
        self.Channels = []  # channels of emg
        self.controlSignals = set()  # sync up channel
        self.mvcFilesMap = {}  # channels:mvc_file_path
        self.chanMap = {}  # old chan name: new chan name
        self.isprocessdone = False

        # filter of channel name, regex
        self.channel_filter = "(emg|EMG)+"

        if file != None and len(file):
            self.setEMGFile(file)

    # async load of emg file, use for loading file in worker thread
    # required emgfile, mvcfile and mvcfilemap to be pre-configured
    def async_load(self):
        if self.emgFile == None:
            return -1
        else:
            self.setEMGFile(self.emgFile)

        for chan, mvcfile in self.mvcFilesMap.items():
            self.setMVCFile(chan, mvcfile)

        # rename channel using map
        for old, new in self.chanMap.items():
            self.renameChannel(old, new)
        return 0

    # applying tst to emg, used when
    # loading emg from a report
    def load_from_report(self, tst):
        self.emgTST = tst.copy()
        self.isprocessdone = True
        self.Channels = tst.labels.copy()

    # use channel as key to access TST
    def __getitem__(self, chan):
        return self.emgTST[chan]

    def getLinspace(self):
        return self.emgTST.getLinspace()

    def isC3D(self, f):
        return f.endswith(".c3d")

    def isMAT(self, f):
        return f.endswith(".mat")

    # check if MVC TST has all channels in place
    def isMVCComplete(self):
        for c in self.Channels:
            if c not in self.controlSignals and not self.emgMVCTST.hasChannel(c):
                return False
        return True

    # remove old data
    def clear(self):
        self.emgTST = None
        self.emgMVCTST = None
        self.Channels.clear()

    # return channels
    def getChannels(self):
        return self.Channels

    def getfs(self):
        return self.emgTST.fs

    def getTST(self):
        return self.emgTST

    # search channels
    def searchChannels(self, filter):
        return self.emgTST.searchChannel(filter)

    # filter for channel name, use regex
    def applyChannelFiler(self, filter):
        self.channel_filter = filter
        self.emgTST.filterChannel(self.channel_filter)
        self.emgMVCTST.filterChannel(self.channel_filter)

    # remove a channel from emg
    def removeChannel(self, channel):
        if channel in self.Channels:
            del self.emgTST[channel]
            del self.emgMVCTST[channel]
            self.Channels.remove(channel)

    # remove a list of channels
    def removeChannels(self, channels):
        for c in channels:
            self.removeChannel(c)

    # rename channel from old to new, keep data the same
    def renameChannel(self, old, new):
        if old in self.Channels:
            self.emgTST.renameChannel(old, new)
            self.emgMVCTST.renameChannel(old, new)
            # rename channel name
            self.Channels[self.Channels.index(old)] = new
            self.chanMap[old] = new

    # set the name of the sync up channel of emg
    def setControlSignal(self, chan):
        if chan not in self.Channels:
            return -1

        self.controlSignals.add(chan)

    def removeControlSignal(self, chan):
        if chan not in self.Channels:
            return -1

        self.controlSignals.remove(chan)

    # set EMG file path
    def setEMGFile(self, f):
        self.emgFile = f

        # remove old data
        self.clear()

        # load file
        try:
            if self.isC3D(f):
                c3d = c3dFile(f)
                self.Channels = c3d.analog.labels

                # load TST
                self.emgTST = c3d.analog.convertToTST()

            elif self.isMAT(f):
                mat = matFile(f)
                self.Channels = mat.labels
                # load TST
                self.emgTST = mat.convertToTST()
            else:
                logger.error("unsupported file format")
        except:
            raise Exception(logger.errstr)

        # sanities
        assert self.Channels != None, "channels not extracted"
        assert self.emgTST != None, "emg cannot be convert to TimeSeriesTable"

        # update MVC TST
        self.emgMVCTST = timeSeriesTable(self.emgTST.fs, self.emgTST.labels)

    # set MVC file path
    def setMVCFile(self, channel, f):
        if len(self.Channels) == 0:
            logger.error("channels is empty!")
            raise Exception(logger.errstr)

        if channel not in self.Channels:
            logger.error("channel {} does not exists!".format(channel))
            raise Exception(logger.errstr)

        MVCTST = None
        # open file and load TST
        try:
            if self.isC3D(f):
                c3d = c3dFile(f)
                MVCChannels = c3d.analog.labels
                MVCTST = c3d.analog.convertToTST()

            elif self.isMAT(f):
                mat = matFile(f)
                MVCChannels = mat.labels
                MVCTST = mat.convertToTST()
            else:
                logger.error("unsupported file format")
                raise Exception(logger.errstr)
        except:
            logger.error("cannot open mvc file")
            raise Exception(logger.errstr)

        # check if targetted channel exists in f
        if channel not in MVCChannels:
            logger.error("Targetted channel not found in file")
            raise Exception(logger.errstr)

        self.emgMVCTST[channel] = MVCTST[channel]
        self.mvcFilesMap[channel] = f

    def toXML(self):
        root = xmlElement("emg")
        root.addNode("path", self.emgFile)
        t = xmlElement("mvcPath")
        for chan, f in self.mvcFilesMap.items():
            t.addNode("chan", [xmlString(chan), xmlString(f)])
        root.addSubTree(t)
        root.addNode("controlSignals", self.controlSignals)
        # channel name migh have spaces or invalid chars,
        # so addDict is not applicable here
        t = xmlElement("chanMap")
        for old, new in self.chanMap.items():
            t.addNode("chan", [xmlString(old), xmlString(new)])
        root.addSubTree(t)
        return root

    @staticmethod
    def fromXML(xml):
        root = xml.find("emg")
        if root == None:
            return None
        emg_obj = emg()
        e = root.find("path")
        if e == None:
            return None
        emg_obj.emgFile = xmlStringParse(e.text)
        e = root.find("mvcPath")
        if e != None:
            for el in e:
                l = xmlStringParseList(el.text)
                emg_obj.mvcFilesMap[l[0]] = l[1]
        e = root.find("controlSignals")
        if e != None and e.text != None:
            emg_obj.controlSignals = xmlStringParseList(e.text)
        e = root.find("chanMap")
        if e != None:
            for el in e:
                l = xmlStringParseList(el.text)
                emg_obj.chanMap[l[0]] = l[1]
        return emg_obj

    def isProcessDone(self):
        return self.isprocessdone

    def setProcessDone(self):
        self.isprocessdone = True

    def startProcess(self):
        self.processCFG = emgConfigure()

    # return EMG configure file
    def getProcessConfig(self):
        return self.processCFG

    # assign EMG configure file
    def setProcessConfig(self, cfg):
        self.processCFG = cfg

    def __tryConfigStepImpl(self, tst, chan, step):
        if chan not in self.Channels:
            logger.error("Targetted channel not exist")
            raise Exception(logger.errstr)

        if step >= self.processCFG.size():
            logger.error("Selected step out of bound")
            raise Exception(logger.errstr)

        # apply functions
        type, tname = self.processCFG.getTypeInfo(step)
        cfg = self.processCFG[step]
        output = tst[chan]
        try:
            if type == emgConfigEnum.FILTER:
                if cfg.enable:
                    if cfg.type == emgFilterEnum.LOW_PASS:
                        output = tst.lowpass(chan, cfg.cutoff_l, cfg.order)
                    elif cfg.type == emgFilterEnum.BAND_PASS:
                        output = tst.bandpass(
                            chan, cfg.cutoff_l, cfg.cutoff_h, cfg.order
                        )
                    else:
                        output = None
            elif type == emgConfigEnum.FULL_W_RECT:
                if cfg.enable:
                    output = tst.rectification(chan)
            elif type == emgConfigEnum.DC_OFFSET:
                if cfg.enable:
                    output = tst.removeDC(chan)
            elif type == emgConfigEnum.ACTIVATION:
                output = tst.threholdDetection(
                    chan, cfg.threhold, cfg.n_above, cfg.n_below
                )
            elif type == emgConfigEnum.NORMALIZATION:
                if cfg.enable:
                    # get max from MVCTST
                    max_v = self.emgMVCTST.max(chan)
                    output = tst.normalization(chan, max_v)
            elif type == emgConfigEnum.SUMMARY:
                # output remain the same
                cfg.max = tst.max(chan)
                cfg.min = tst.min(chan)
                cfg.med = tst.median(chan)
                cfg.rms = tst.rms(chan)
                cfg.ptp = tst.ptp(chan)
                cfg.zeros = tst.countZeros(chan)
        except:
            output = [0] * tst.size()
            logger.error(
                "cannot apply configuration on chan: {}, step: {}".format(chan, tname)
            )
        return output

    def tryConfigStep(self, chan, step):
        return self.__tryConfigStepImpl(self.emgTST, chan, step)

    def tryConfigStepTo(self, chan, step):
        tst = self.emgTST.copy()
        for i in range(0, step + 1):
            tst[chan] = self.__tryConfigStepImpl(tst, chan, i)
        return tst[chan]

    # process EMG and MVC using configure file
    def processWithConfigure(self):
        for chan in self.Channels:
            if chan in self.controlSignals:
                continue

            for step in range(0, self.processCFG.size()):
                self.emgTST[chan] = self.__tryConfigStepImpl(self.emgTST, chan, step)
                self.emgMVCTST[chan] = self.__tryConfigStepImpl(
                    self.emgMVCTST, chan, step
                )
