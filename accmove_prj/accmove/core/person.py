class person:
    def __init__(self):
        self.data = {
            "id": "",
            "name": "",
            "age": "",
            "gender": "",
        }
    
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.data[key] = value
    def __delitem__(self, key):
        return
    def __missing__(self, key):
        return
    
    def print(self):
        print("Person:")
        for x in self.data:
            print("\t", x, ":", self.data[x])
