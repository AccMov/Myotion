import numpy as np
import scipy.signal as sig
import pandas as pd
import re
from .xml import *

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


all returned vector remain same dimension
'''

class timeSeriesTable:
    '''
    expect input to be a len(labels) x N matrix
    input can be None, but fs and labels must be defined
    '''
    def __init__(self, fs, labels, input=None):
        self.data = {}

        if len(labels) == 0:
            raise ValueError("at least one label required!")
        
        if type(input) is dict:
            self.data = input
        else:
            for i in range(0, len(labels)):
                if input is None:
                    self.data[labels[i]] = np.array([])
                else:
                    self.data[labels[i]] = np.array(input[i])
        

        self.metadata = {
            "fs" : fs,
            "ts" : 1.0/fs,
            "labels":  labels,
            "n" :  len(self.data[labels[0]]),
            "time" : len(self.data[labels[0]]) / fs
        }

        self.iter = 0
    
    # accessor of object
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        # check dimension
        if self.n != 0 and len(value) != self.n:
            raise ValueError("all rows need to have same dimension!")    
        if key not in self.labels:
            self.__missing__(key)
            # update time if first row added
            if self.n == 0:
                self.time = len(value) / self.fs
        self.data[key] = value
    def __delitem__(self, key):
        if key not in self.labels:
            return
        del self.data[key]
        self.labels.remove(key)
    def __missing__(self, key):
        self.labels.append(key)
        self.data[key] = np.array([])
    def __getattr__(self, key):
        if key in self.metadata:
            return self.metadata[key]

    # iterator
    def __iter__(self):
        self.iter = 0
        return self
    def __next__(self):
        if self.iter < self.size():
            return self.data[self.labels[self.iter]]
        else:
            raise StopIteration

    def copy(self):
        return timeSeriesTable(self.fs, self.labels.copy(), self.data.copy())

    def size(self):
        return self.n
    
    def clear(self):
        for i in range(0, len(self.labels)):
            self.data[self.labels[i]] = np.array([])
        self.n = 0
        self.time = 0

    def rename(self, old, new):
        self.data[new] = self.data.pop(old)

    # check if has channel
    def hasChannel(self, chan):
        if chan in self.labels:
            return True
        else:
            return False
        
    # convert to pandas
    def toPandasFrame(self):
        return pd.DataFrame(self.data)

    # get time step in linspace format
    def getLinspace(self):
        return np.linspace(0, self.time, self.n)

    # search channels in regex
    def searchChannel(self, regex):
        to_be_ret = []
        for c in self.labels:
            if re.search(regex, c) is not None:
                to_be_ret.append(c)

        return to_be_ret

    # filter out channels not in regex
    def filterChannel(self, regex):
        to_be_del = []
        for c in self.labels:
            if re.search(regex, c) is None:
                to_be_del.append(c)

        new_labels = []
        for c in self.labels:
            if c in to_be_del:
                del self.data[c]
            else:
                new_labels.append(c)
        self.labels = new_labels

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
    def ptp(self, key):
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
    
    # return ndarray with dc removed
    def removeDC(self, key):
        return self.data[key] - self.mean(key)

    # rectification
    def rectification(self, key):
        return np.absolute(self.data[key])

    # normalization
    def normalization(self, key, val):
        if val <= 0:
            raise ValueError("normalization val has be bigger than zero")
        return self.data[key] / val
    
    # threhold detection
    # https://github.com/BMClab/BMC/blob/master/notebooks/DetectOnset.ipynb
    # slow impl
    def threholdDetection(self, key, threhold, n_above=10, n_below=10):
        if n_above < 0 or n_above >= self.n or n_below < 0 or n_below >= self.n:
            raise ValueError("sliding windows has to be a postive value and smaller then total points!")

        activated = []

        above_counter = 0
        below_counter = 0
        isactivated = False
        seg = [0, 0]

        for i in range(0, len(self.data[key])):
            p = self.data[key][i]
            if p >= threhold:          #above
                below_counter = 0      #clear below counter
                if isactivated:
                    continue

                if above_counter < n_above:
                    above_counter += 1
                if above_counter >= n_above:
                    isactivated = True
                    seg[0] = i
            else:                     #below
                above_counter = 0
                if not isactivated:
                    continue

                if below_counter < n_below:
                    below_counter += 1
                if below_counter >= n_below:
                    isactivated = False
                    seg[1] = i
                    activated.append(seg)
                    seg = [0, 0]
                    above_counter = 0
                    below_counter = 0

        if isactivated:
            activated.append([seg[0], len(self.data[key])])

        return activated

    # co-contraction 
    def cocontraction(self, key1, key2):
        return np.trapz(self.data[key1]) / np.trapz(self.data[key2]);

    def countZeros(self, key):
        return len(self.data[key]) - np.count_nonzero(self.data[key])

    def entropy(self, key):
        return

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

    '''
    <timeSeriesTable>
        <channels_num></channels_num>
        <channels_name> </channels_name>
        <fs> </fs>
        <N> </N>
        <channels>
            <A>  </A>
            ...
        </channels>
    </timeSeriesTable>
    '''
    def toXML(self):
        e = xmlElement('timeSeriesTable')
        e.addNode('channels_num', str(len(self.labels)))
        e.addNode('channels_name', ' '.join(self.labels))
        e.addNode('fs', str(self.fs))
        e.addNode('N', str(self.n))

        c = xmlElement('channels')
        e.addSubTree(c)
        for k in self.labels:
            c.addNode(k, ' '.join(format(x, '.6f') for x in self.data[k]))
        return e