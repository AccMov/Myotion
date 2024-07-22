from thefuzz import fuzz

class fuzzMatch:
    def __init__(self):
        self.fuzzDict = {}

    def addPair(self, key, val):
        if key in self.fuzzDict:
            self.fuzzDict[key].append(val)
        else:
            self.fuzzDict[key] = [val]

    def addPairs(self, pairs):
        for key, val in pairs.items():
            self.addPair(key, val)

    # find the most possible match between key and [value0, value1, ....]
    # lower_bound is the lowest possbility between [0,100] indicating a match
    def match(self, key, values, lower_bound=0):
        if key not in self.fuzzDict:
            # if not in dict, try to look for plain text of "key" in values
            candidate_token = [key]
        else:
            candidate_token = self.fuzzDict[key]
        
        matched = None
        max_p = 0
        for v in values:
            for c in candidate_token:
                p = fuzz.partial_ratio(v, c)
                if p >= lower_bound:
                    if p > max_p:
                        max_p = p
                        matched = [v]
                    elif p == max_p:
                        matched.append(v)

        return matched, max_p