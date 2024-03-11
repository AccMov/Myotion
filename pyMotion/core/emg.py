from .timeSeriesTable import *
from .c3d import *
from .mat import *
from .xml import *
from enum import Enum
import re

class emgFilterEnum(Enum):
    LOW_PASS = 0
    BAND_PASS = 1
    MAX = 2
class emgFilter():
    def __init__(self):
        self.type = emgFilterEnum.MAX
        self.cutoff_l = 0
        self.cutoff_h = 0

        self.nameMap = {
            self.LOW_PASS: 'low pass filter',
            self.BAND_PASS: 'band pass filter',
            self.MAX: 'N/A',
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
        self.n_above = 0
        self.n_below = 0

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

class emgConfigure():
    class emgConfigureEnum(Enum):
        # name of steps
        FILTER = 0
        FULL_W_RECT = 1
        DC_OFFSET = 2
        ACTIVATION = 3
        NORMALIZATION = 4
        SUMMARY = 5
        MAX = 6

    def __init__(self):
        # pre-loaded steps
        self.classical_steps = [
            emgConfigureEnum.DC_OFFSET,
            emgConfigureEnum.FULL_W_RECT,
            emgConfigureEnum.FILTER,
            emgConfigureEnum.NORMALIZATION,
            emgConfigureEnum.SUMMARY,
        ]

        self.nameMap = {
            self.DC_OFFSET: 'remove_dc_offset',
            self.FULL_W_RECT: 'full_wave_rectification',
            self.FILTER: 'filter',
            self.NORMALIZATION: 'normalization',
            self.ACTIVATION: 'activation',
            self.SUMMARY: 'summary',
        }

        # current running step at 0
        self.curr = 0

        # current selecting index
        self.select = 0

        # default
        self.step = self.classical_steps

        # default config for each step
        self.stepConfig = {}
        for s in self.step:
            self.stepConfig[s] = self.initConfig(s)
    
    # set the index of current highlighted step
    def setSelectedIndex(self, idx):
        if idx > len(self.step):
            logger.error("selected index out of range!")
            return -1
        
        self.select = idx
    
    # set the index of current highlighted step and current running step
    def setCurrIndex(self, idx):
        if idx > len(self.step):
            logger.error("selected index out of range!")
            return -1
        
        self.select = idx
        self.curr = idx

    # add new step
    def addStep(self, idx):
        if idx >= emgConfigure.MAX or idx < 0:
            logger.error("invalid emg steps!")
            return -1
        
        # insert new step after selection index
        self.step.insert(self.select, idx)

        # jump to next step
        self.select += 1

    # remove step
    def removeStep(self, idx):
        if idx >= emgConfigure.MAX or idx < 0:
            logger.error("invalid emg steps!")
            return -1
        
        # insert new step after selection index
        self.step.remove(self.select, idx)
        
        if self.select > 0:
            self.select -= 1

    def getSelectedIndex(self):
        return self.select
    
    def getCurrIndex(self):
        return self.curr
    
    def getSelectedType(self):
        type_id = self.step[self.select]
        return type_id
    
    def getSelectedTypeName(self):
        return self.nameMap[self.getSelectedType()]
    
    def getCurrType(self):
        type_id = self.step[self.curr]
        return type_id
    
    def getCurrTypeName(self):
        return self.nameMap[self.getCurrType()]
    
    # create a config for one step
    def initConfig(self, type):
        if type == emgConfigure.FILTER.value:
            return emgFilter()
        elif type == emgConfigure.ACTIVATION.value:
            return emgActivation()
        else:
            return None
       
    def setConfig(self, index, config):
        self.stepConfig[index] = config
    
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
        for s in self.step:
            # subtree for each step
            subElement = xmlElement(self.nameMap[s])
            config = self.stepConfig[s]
            if config is not None:
                config.toXML(subElement)
        return e

    def fromXML(self, xml_element):
        return

class emg:
    def __init__(self):
        self.emgFile = ""
        self.emgTST = timeSeriesTable()
        self.emgMVCTST = timeSeriesTable()
        self.Channels = []
        # key:val pair
        # key = channels, val = mvc file path
        self.mvcFilesMap = {}

        # filter of channel name, regex
        self.channel_filter = '(emg|EMG)+'

    def isC3D(self, f):
        return f.endswith('.c3d')
    
    def isMAT(self, f):
        return f.endswith('.mat')
    
    def isMVCValid(self):
        # check if MVC TST has all channels
        for c in self.Channels:
            if not self.emgMVCTST.hasChannel(c):
                return False
        return True
    
    def clear(self):
        # remove old data
        self.emgTST = timeSeriesTable()
        self.emgMVCTST = timeSeriesTable()
        self.Channels.clear()
        self.mvcFilesMap.clear()


    # filter for channel name, use regex
    def setChannelFiler(self, filter):
        self.channel_filter = filter

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
                self.Channels = mat.analog.labels

                #load TST
                self.emgTST = mat.convertToTST()
            else:
                logger.error("unsupported file format")
        except:
            raise

        # filter channel
        self.emgTST.filterChannel(self.channel_filter)

    # set MVC file path
    def setMVCFile(self, channel, f):
        if len(self.Channels) == 0:
            logger.error("channels is empty!")
            return -1

        if channel not in self.Channels:
            logger.error("channel {} does not exists!".format(channel))
            return -1
        
        # open file and load TST
        try:
            if self.isC3D(f):
                c3d = c3dFile(f)
                MVCChannels = c3d.analog.labels
                MVCTST = c3d.analog.convertToTST()

            elif self.isMAT(f):
                mat = matFile(f)
                MVCChannels = mat.analog.labels
                MVCTST = mat.convertToTST()

            else:
                logger.error("unsupported file format")
        except:
            raise

        # check if targetted channel exists in f
        if channel not in MVCChannels:
            logger.error("Targetted channel not found in file")
            return -1
        
        self.emgMVCTST[channel] = MVCTST[channel]
        self.mvcFilesMap[channel] = f
    
    # return channels
    def getChannels(self):
        return self.Channels

    # filter channels
    def getFilteredChannels(self):
        return

    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        if key == "trials":
            self.data[key] = value
    def __delitem__(self, key):
        return
    def __missing__(self, key):
        return

    def writeFile(self, file):
        #write to file
        return 0
        
    # process data using configure file
    def processWithConfigure(self, emgConfigure):
        return


        
