import scipy.io
import numpy as np
from .logger import *
from .timeSeriesTable import *

'''
mat data class

movement_data:   input raw data from mat file
format:
{
 "type":
 "name""
 ...
 "data":
}
'''
class matdata:
    def __init__(self, movement_data):

        self.metadata_keys = ["type", "name", "time_units", "begin_time", "frequency", "count", "units", "data"]

        self.keys = self.metadata_keys
        self.keys.append("data")

        self.dict = {}
        for key in self.keys:
            self.dict[key] = movement_data[key]

        self.metadata = {}
        for key in self.metadata_keys:
            self.metadata[key] = movement_data[key]

    def keys(self):
        return self.keys

    def __getattr__(self, key):
        if key in self.keys:
            return self.dict[key]
        elif key == "metadata":
            return self.metadata
        elif key == "keys":
            return self.keys

class matFile:
    def __init__(self, file):
        self.file = file
        self.reader = scipy.io.loadmat(file, squeeze_me=True)
        self.keylist = sorted(self.reader.keys())

        #['__globals__', '__header__', '__version__', 'TABLE']
        self.raw = self.reader[self.keylist[3]]

        # ['info', 'movements']
        info = self.raw['info'].tolist()

        self.metadata = {
            "create_version" : info['created_with_version'].tolist(),
            "export_version" : info['exported_with_version'].tolist(),
            "last_name"    : info['last_name'].tolist(),
            "first_name"    : info['first name'].tolist(),
            "gender"  : info['sex'].tolist(),
            "date"    : info['measurement_date'].tolist(),
            "record_name"    : info['record_name'].tolist(),
            "channel_number":    0,
            "labels":    [],
        }

        # ['type', 'name', 'time_begin', 'time_end', sources]
        movements = self.raw['movements'].tolist()

        # [ 'sources', 'signals' ]
        sources = movements['sources'].tolist()
        signals = sources['signals'].tolist()

        # matdata type
        movement_datas = []
        for key in signals.dtype.fields:
            signal_x = signals[key].tolist()
            movement_data = {}
            for sub_key in signal_x.dtype.fields:
                movement_data[sub_key] = np.squeeze(signal_x[sub_key]).tolist()
            movement_datas.append(matdata(movement_data))

        self.movements = {
            "type" : movements['type'].tolist(),
            "name" : movements['name'].tolist(),
            "time_begin"  : movements['time_begin'].tolist(),
            "time_end"    : movements['time_end'].tolist(),
            "source"      : sources,
            "channels"      : movement_datas,
        }

        self.metadata["labels"] = [m.name for m in self.movements["channels"]]
        self.metadata["channel_number"] = len(self.movements["channels"])

    def __getattr__(self, key):
        if key == "metadata":
            return self.metadata
        elif key in self.movements.keys():
            return self.movements[key]

    def __getitem__(self, idx):
        return self.data[idx] 
    def __setitem__(self, idx, value):
            self.data[idx] = value
    def __delitem__(self, key):
        return
    def __missing__(self, key):
        return  
    
    def convertToTST(self):
        if self.channel_number == 0:
            return timeSeriesTable()
        
        label = [c.name for c in self.channels]
        data = [c.data for c in self.channels]
        fs = self.channels[0].frequency
        return timeSeriesTable(fs, label, data)
