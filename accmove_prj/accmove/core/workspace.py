from .emg import *
from .freq_analysis import *
from .person import *
from .timeSeriesTable import *


'''
1. max/min/med/sd/var/rms/peak-to-peak-distance
2. filter
3. remove-dc offset
4. full-wave rectification
5. interpolation
6. Normalization
7. Regularity/Entropy:  pattern matching, check complexity of waveform
8. on/off detection:    threhold detection
9. co-contraction index:  integration ratio between two waveform
10. zero-crossing:   count zero values
'''

class workspace:
    def __init__(self):
        self.person = person()
        self.kinematic = timeSeriesTable()
        self.emg = timeSeriesTable()