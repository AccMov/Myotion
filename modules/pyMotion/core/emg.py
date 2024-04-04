from .timeSeriesTable import *
from .c3d import *
from .mat import *
from .xml import *
from enum import Enum
from .logger import *
import re

class emgDCOffset():
    def __init__(self):
        self.enable = False
    
    def toXML(self, e):
        e.addNode('enable', self.enable)
        return e

class emgRectification():
    def __init__(self):
        self.enable = False

    def toXML(self, e):
        e.addNode('enable', self.enable)
        return e

class emgNormalization():
    def __init__(self):
        self.enable = False
    
    def toXML(self, e):
        e.addNode('enable', self.enable)
        return e

class emgSummary():
    def __init__(self):
        self.max = 0
        self.min = 0
        self.med = 0
        self.rms = 0
        self.ptp = 0
        self.zeros = 0

    def toXML(self, e):
        # we don't save temp calculation to config file
        return e

class emgFilterEnum(Enum):
    LOW_PASS = 0
    BAND_PASS = 1
    MAX = 2
class emgFilter():
    def __init__(self):
        self.enable = False
        self.type = emgFilterEnum.LOW_PASS
        self.cutoff_l = 0
        self.cutoff_h = 0

        self.nameMap = {
            emgFilterEnum.LOW_PASS: 'low pass filter',
            emgFilterEnum.BAND_PASS: 'band pass filter',
            emgFilterEnum.MAX: 'N/A',
        }

    def setType(self, t):
        if t >= emgFilter.MAX or t < 0:
            logger.error("invalid filter type!")
            return -1

        self.type = t
    
    def setCutOff_L(self, freq):
        self.cutoff_l = freq

    def setCutOff_H(self, freq):
        self.cutoff_h = freq

    # add nodes to xml tree
    def toXML(self, e):
        e.addNode('type', self.nameMap[self.type])
        e.addNode('cutoff_l', str(self.cutoff_l))
        e.addNode('cutoff_h', str(self.cutoff_h))
        return e

    def fromXML(self, xml_element):
        return

class emgActivation:
    def __init__(self):
        self.threhold = 0
        self.n_above = 5
        self.n_below = 5

    def setThreHold(self, t):
        self.threhold = t

    def setCutOff_L(self, freq):
        self.cutoff_l = freq

    def setCutOff_H(self, freq):
        self.cutoff_h = freq

    def toXML(self, e):
        e.addNode('threhold', str(self.threhold))
        e.addNode('n_above', str(self.n_above))
        e.addNode('n_below', str(self.n_below))
        return e

    def fromXML(self, xml_element):
        return
    
class emgConfigureEnum(Enum):
    # name of steps
    FILTER = 0
    FULL_W_RECT = 1
    DC_OFFSET = 2
    ACTIVATION = 3
    NORMALIZATION = 4
    SUMMARY = 5
    MAX = 6
class emgConfigure():
    def __init__(self):
        # pre-loaded steps
        self.classical_steps = [
            emgConfigureEnum.DC_OFFSET,
            emgConfigureEnum.FULL_W_RECT,
            emgConfigureEnum.FILTER,
            emgConfigureEnum.FILTER,
            emgConfigureEnum.NORMALIZATION,
            emgConfigureEnum.SUMMARY,
        ]

        self.nameMap = {
            emgConfigureEnum.DC_OFFSET: 'remove_dc_offset',
            emgConfigureEnum.FULL_W_RECT: 'full_wave_rectification',
            emgConfigureEnum.FILTER: 'filter',
            emgConfigureEnum.NORMALIZATION: 'normalization',
            emgConfigureEnum.ACTIVATION: 'activation',
            emgConfigureEnum.SUMMARY: 'summary',
        }

        # set default
        self.step = self.classical_steps

        # default config for each step
        self.stepConfig = []
        for s in self.step:
            self.stepConfig.append(self.initConfig(s))

    # use step id as key to access config file
    def __getitem__(self, id):
        return self.stepConfig[id]

    # add new step
    def addStep(self, idx, pos):
        if idx >= emgConfigure.MAX or idx < 0:
            logger.error("invalid emg steps!")
            return -1

        self.step.insert(pos, idx)

    # remove step
    def removeStep(self, pos):        
        self.step.remove(pos)
    
    def getTypeInfo(self, idx):
        type_id = self.step[idx]
        return type_id, self.nameMap[type_id]

    def getStepStringList(self):
        return [self.nameMap[s] for s in self.step]
    
    def size(self):
        return len(self.step)
    
    # create a config for one step
    def initConfig(self, type):
        if type == emgConfigureEnum.FILTER:
            return emgFilter()
        elif type == emgConfigureEnum.ACTIVATION:
            return emgActivation()
        elif type == emgConfigureEnum.DC_OFFSET:
            return emgDCOffset()
        elif type == emgConfigureEnum.FULL_W_RECT:
            return emgRectification()
        elif type == emgConfigureEnum.NORMALIZATION:
            return emgNormalization()
        elif type == emgConfigureEnum.SUMMARY:
            return emgSummary()
        else:
            return None
    '''
    <emgConfigure>
        <remove_dc_offset/>
        <filter> 
           <type> </type>
           ...
        </filter>
    </emgConfigure>
    '''
    def toXML(self):
        # top tree
        e = xmlElement('emgConfigure')
        for i in range(0, len(self.step)):
            # subtree for each step
            subElement = xmlElement(self.nameMap[self.step[i]])
            config = self.stepConfig[i]
            if config is not None:
                config.toXML(subElement)
        return e

    def fromXML(self, xml_element):
        return

class emg:
    def __init__(self, file=''):
        self.emgFile = file                #file path
        self.emgTST = None                 #emg data
        self.emgMVCTST = None              #emg MVC data
        self.processCFG = None             #emg data process configure
        self.Channels = []
        # key:val pair
        # key = channels, val = mvc file path
        self.mvcFilesMap = {}
        self.isprocessdone = False

        # filter of channel name, regex
        self.channel_filter = '(emg|EMG)+'

        if len(file):
            self.setEMGFile(file)

    # use channel as key to access TST
    def __getitem__(self, chan):
        return self.emgTST[chan]
    
    def getLinspace(self):
        return self.emgTST.getLinspace()

    def isC3D(self, f):
        return f.endswith('.c3d')
    
    def isMAT(self, f):
        return f.endswith('.mat')
    
    # check if MVC TST has all channels in place
    def isMVCComplete(self):
        for c in self.Channels:
            if not self.emgMVCTST.hasChannel(c):
                return False
        return True
    
    # remove old data
    def clear(self):
        self.emgTST = None
        self.emgMVCTST = None
        self.Channels.clear()
        self.mvcFilesMap.clear()
        
    # return channels
    def getChannels(self):
        return self.Channels
    
    def getfs(self):
        return self.emgTST.fs

    # search channels
    def searchChannels(self, filter):
        return self.emgTST.searchChannel(filter)

    # filter for channel name, use regex
    def applyChannelFiler(self, filter):
        self.channel_filter = filter
        self.emgTST.filterChannel(self.channel_filter)
        self.emgMVCTST.filterChannel(self.channel_filter)

    def removeChannel(self, channel):
        del self.emgTST[channel]
        del self.emgMVCTST[channel]

    def removeChannels(self, channels):
        for c in channels:
            self.removeChannel(c)

    def renameChannel(self, old, new):
        self.emgTST.renameChannel(old, new)
        self.emgMVCTST.renameChannel(old, new)

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

                #load TST
                self.emgTST = c3d.analog.convertToTST()

            elif self.isMAT(f):
                mat = matFile(f)
                self.Channels = mat.labels
                #load TST
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
        self.emgTST.setname('EMG')
        self.emgMVCTST.setname('MVC')
        # top tree
        root = xmlElement('emg')
        root.addSubTree(self.emgTST.toXML())
        root.addSubTree(self.emgMVCTST.toXML())
        root.addSubTree(self.processCFG.toXML())
        return root
    
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
            if type == emgConfigureEnum.FILTER:
                if cfg.enable:
                    if cfg.type == emgFilterEnum.LOW_PASS:
                        output = tst.lowpass(chan, cfg.cutoff_l)
                    elif cfg.type == emgFilterEnum.BAND_PASS:
                        output = tst.bandpass(chan, cfg.cutoff_l, cfg.cutoff_h)
                    else:
                        output = None
            elif type == emgConfigureEnum.FULL_W_RECT:
                if cfg.enable:
                    output = tst.rectification(chan)
            elif type == emgConfigureEnum.DC_OFFSET:
                if cfg.enable:
                    output = tst.removeDC(chan)
            elif type == emgConfigureEnum.ACTIVATION:
                output = tst.threholdDetection(chan, cfg.threhold, cfg.n_above, cfg.n_below)
            elif type == emgConfigureEnum.NORMALIZATION:
                if cfg.enable:
                    # get max from MVCTST
                    max_v = self.emgMVCTST.max(chan)
                    output = tst.normalization(chan, max_v)
            elif type == emgConfigureEnum.SUMMARY:
                # output remain the same
                cfg.max = tst.max(chan)
                cfg.min = tst.min(chan)
                cfg.med = tst.median(chan)
                cfg.rms = tst.rms(chan)
                cfg.ptp = tst.ptp(chan)
                cfg.zeros = tst.countZeros(chan)
        except:
            output = [0] * tst.size()
            logger.error("cannot apply configuration")
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
            for step in range(0, self.processCFG.size()):
                self.emgTST[chan] = self.__tryConfigStepImpl(self.emgTST, chan, step)
                self.emgMVCTST[chan] = self.__tryConfigStepImpl(self.emgMVCTST, chan, step)


        
