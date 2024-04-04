from .timeSeriesTable import *
from .c3d import *
from .mat import *
from .xml import *
from enum import Enum
from .logger import *

class kinematic:
    def __init__(self, file=''):
        self.kmtFile = file

        # label : array
        self.data = None    

        if len(file):
            self.setFile(file)

    # VICON only
    def isrealmarker(self, label):
        """check if a marker is a real marker by replacing the last character with 'L' 'O' 'A' 'P'

        Args:
            rawlabels (list of str): all labels in the c3d file
            label (str): current label being investigated

        Returns:
            bool: True if the marker is a real marker
        """

        if (
            label.endswith("L")
            or label.endswith("O")
            or label.endswith("A")
            or label.endswith("P")
        ):
            return not (
                label[:-1] + "L" in self.labels
                and label[:-1] + "O" in self.labels
                and label[:-1] + "A" in self.labels
                and label[:-1] + "P" in self.labels
            )
        return True

    def clear(self):
        return

    def setFile(self, f):
        self.kmtFile = f

        if not self.isC3D(f):
            logger.error("unsupported file format")

        # remove old data
        self.clear()

        # load file
        try:
            c3d = c3dFile(f)
            self.data = c3d.Points
        except:
            raise Exception(logger.errstr)
        
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.data[key] = value
    def __delitem__(self, key):
        return
    def __missing__(self, key):
        return
    
