from .timeSeriesTable import *

class emg:
    def __init__(self):
        self.trials = []
        self.channels = []
        self.data = {
            "emg": dict(),
            "mvcraw": dict(),
            "mvc": timeSeriesTable(),
        }
    
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        if key is "trials":
            self.data[key] = value
    def __delitem__(self, key):
        return
    def __missing__(self, key):
        return
    
    def addFile(self, file, trial=""):
        # load from file
        return 0
    
    def loadMVCFile(self, file, channel):
        return
    
    def writeFile(self, file):
        #write to file
        return 0

    def print(self):
        print("EMG:")
        