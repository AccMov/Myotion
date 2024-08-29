import collections

errBuffer = collections.deque(maxlen=1000)
infoBuffer = collections.deque(maxlen=1000)


class logger:
    def __init__(self):
        self.dummy = None

    @staticmethod
    def error(str):
        errBuffer.append(str)
        print("Myotion -- ERROR: {}".format(str))

    @staticmethod
    def info(str):
        infoBuffer.append(str)
        print("Myotion -- INFO: {}".format(str))

    @staticmethod
    def errstr():
        return errBuffer[0]

    @staticmethod
    def infostr():
        return infoBuffer[0]
