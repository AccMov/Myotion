from thefuzz import fuzz
from heapq import heappop, heappush, nlargest
from collections import OrderedDict


class record:
    def __init__(self, val, n, possiblity):
        self.v = val
        self.n = n
        self.p = possiblity

    # max heap, reverse
    def __lt__(self, other):
        if self.n == other.n:
            return self.p < other.p
        else:
            return self.n < other.n


class heapMDict:
    def __init__(self):
        # key : index
        self.dict = {}
        # max heap with records
        self.heaplist = []

    # max heap
    def __bubbleup(self, i):
        while i > 0:
            if self.heaplist[i] > self.heaplist[(i - 1) / 2]:
                self.heaplist[i], self.heaplist[(i - 1) / 2] = (
                    self.heaplist[(i - 1) / 2],
                    self.heaplist[i],
                )
                self.dict[self.heaplist[i].v]["index"] = (i - 1) / 2
                self.dict[self.heaplist[(i - 1) / 2].v]["index"] = i
                i = (i - 1) / 2
            else:
                break

    # max heap
    def __bubbledown(self, i):
        while i < len(self.heaplist):
            if self.heaplist[i] < self.heaplist[2 * i + 1]:
                self.heaplist[i], self.heaplist[2 * i + 1] = (
                    self.heaplist[2 * i + 1],
                    self.heaplist[i],
                )
                self.dict[self.heaplist[i].v]["index"] = 2 * i + 1
                self.dict[self.heaplist[2 * i + 1].v]["index"] = i
                i = 2 * i + 1
            else:
                break

    def __contains__(self, key):
        return key in self.dict

    def pop(self, key):
        if key in self.dict:
            index = self.dict[key]

            # swap with last
            end = len(self.heaplist)
            self.heaplist[index], self.heaplist[end - 1] = (
                self.heaplist[end - 1],
                self.heaplist[index],
            )

            # pop
            del self.heaplist[end - 1]
            self.__bubbledown(index)

    def push(self, key, p):
        if key in self.dict:
            index = self.dict[key]
            # update counter
            rc = self.heaplist[index]
            self.heaplist[index] = record(rc.v, rc.n + 1, rc.p)
            # sort
            self.__bubbleup(index)
        else:
            self.dict[key] = len(self.heaplist)
            self.heaplist.append(record(key, 1, p))
            self.__bubbleup(len(self.heaplist) - 1)

    def size(self):
        return len(self.heaplist)

    def keys(self):
        return self.dict.keys()

    def getN(self, key):
        return self.heaplist[self.dict[key]].n

    def getP(self, key):
        return self.heaplist[self.dict[key]].p

    def getMax(self, filter=set()):
        if self.size() == 0:
            return []

        candidate_heap = []
        if len(filter) == 0:
            candidate_heap = self.heaplist
        else:
            for item in self.heaplist:
                if item.v in filter:
                    candidate_heap.append(item)

        if len(candidate_heap) == 0:
            return []

        result_token = [candidate_heap[0]]
        for m in range(1, len(result_token)):
            if not m < result_token[0]:
                result_token.append(m)
            else:
                break
        return result_token


# key : [ (val, number_of_selects, fuzzPossibility), ... ]
class fuzzMatch:
    def __init__(self):
        # key : heapMDict(record1, record2, ...)
        self.fuzzDict = {}
        # store all existed values
        self.previousValues = set()

    def addPair(self, key, val):
        self.previousValues.add(val)

        if key in self.fuzzDict:
            p = self.fuzzDict[key].getP(val)
            self.fuzzDict[key].push(val, p)
        else:
            self.fuzzDict[key] = heapMDict()
            self.fuzzDict[key].push(val, fuzz.partial_ratio(key, val))

    def addPairs(self, pairs):
        for key, val in pairs.items():
            self.addPair(key, val)

    def __matchRawString(self, key, candidates, lower_bound):
        result_token = []
        max_p = lower_bound
        for v in candidates:
            p = fuzz.partial_ratio(key, v)
            if p > max_p:
                max_p = p
                result_token.clear()
                result_token = [[v, p]]
            elif p == max_p:
                result_token.append([v, p])
        return result_token

    # # look for match in key and targeted_values
    # lower_bound is the lowest possbility between [0,100] indicating a match
    def match(self, key, targeted_values, lower_bound=0):
        # get intersection of previousValue and candidates as we
        # priortize user selection
        candidate_set = set(targeted_values) & self.previousValues

        # no candidate, use raw string match
        if len(candidate_set) == 0:
            return self.__matchRawString(key, targeted_values, lower_bound)

        # check preivous record and find the possible match
        if key not in self.fuzzDict:
            # if not in dict, use raw string match
            return self.__matchRawString(key, targeted_values, lower_bound)
        else:
            previous_uses = set(self.fuzzDict[key].keys())
            candidate_set = candidate_set & previous_uses

            if len(candidate_set) == 0:
                # if prev selection not found, use raw string match
                return self.__matchRawString(key, targeted_values, lower_bound)

            # user selected these before, so we are loosing the restriction on bound
            # pick the most selected item
            result_token = []
            token = self.fuzzDict[key].getMax(candidate_set)
            for t in token:
                result_token.append([t.v, t.p])

        return result_token
