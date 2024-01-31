from.timeSeriesTable import *

class advance_analysis:
    def __init__(self):
        self.data = {
            "ms_weighting": timeSeriesTable(),
            "ms_timing": timeSeriesTable(),
        }
    
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.data[key] = value
    def __delitem__(self, key):
        return
    def __missing__(self, key):
        return
    