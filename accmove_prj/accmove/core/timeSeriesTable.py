import numpy as np
import scipy.signal as sig

'''
1. max/min/med/std/var/rms/peak-to-peak-distance
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

class timeSeriesTable:
    def __init__(self, fs, labels, input):
        self.data = {}

        if(len(labels) != len(input)):
            raise ValueError("labels and input must have same dimension")

        if(len(input) == 0):
            raise ValueError("input must have at least one channel")

        for i in range(0, len(labels)):
            self.data[labels[i]] = np.array(input[i])

        self.metadata = {
            "fs" : fs,
            "ts" : 1.0/fs,
            "labels":  labels,
            "n" :  len(input[0]),
            "time" : len(input[0]) / fs
        }
    
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        if key not in self.labels:
            self.__missing__(key)
        self.data[key] = value
    def __delitem__(self, key):
        return
    def __missing__(self, key):
        self.labels.append(key)
        self.data[key] = np.array()

    def __getattr__(self, key):
        if key in self.metadata:
            return self.metadata[key]

    # method of one channel
    def max(self, key):
        return self.data[key].max()
    def min(self, key):
        return self.data[key].min()
    def mean(self, key):
        return self.data[key].mean()
    def median(self, key):
        return np.median(self.data[key])
    def std(self, key):
        return np.std(self.data[key])
    def var(self, key):
        return np.var(self.data[key])
    def rms(self, key):
        return np.sqrt(np.mean(self.data[key]**2))
    def ptp(self, key):   #peak to peak
        return np.ptp(self.data[key])
    
    # digital butterWorth filter
    def __butterWorth(self, N, Wn, btype):
        return sig.butter(N, Wn, btype, False, 'sos', self.fs)

    # return ndarray with filterd data
    def lowpass(self, key, Wn):
        if Wn < 0 or Wn >= self.fs/2:
            raise ValueError("frequency must be 0 < Wn < fs/2")
        # create low pass filter
        sos = self.__butterWorth(2, Wn, 'low')
        return sig.sosfilt(sos, self.data[key])
    
    # return ndarray with filterd data
    def bandpass(self, key, Wlow, Whigh):
        if Wlow < 0 or Wlow >= self.fs/2:
            raise ValueError("frequency must be 0 < Wn < fs/2")
        if Whigh < 0 or Whigh >= self.fs/2:
            raise ValueError("frequency must be 0 < Wn < fs/2")
        # create band pass filter
        sos = self.__butterWorth(2, [Wlow, Whigh], 'bandpass')
        return sig.sosfilt(sos, self.data[key])
    
    #  return ndarray with dc removed
    def removeDC(self, key):
        return self.data[key] - self.mean(key)

    #method of all channels
    def max_all(self):
        return [self.data[p].max() for p in self.labels]
    def min_all(self):
        return [self.data[p].min() for p in self.labels]

    def loadFile(self, file):
        #load from file
        return 0
    
    def writeFile(self, file):
        #write to file
        return 0