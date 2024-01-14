class freq_analysis:
    def __init__(self):
        self.freq = 0.0
        self.data = dict()
        # 2d table stored in dictionary
    
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.data[key] = value
    def __delitem__(self, key):
        return
    def __missing__(self, key):
        return
    