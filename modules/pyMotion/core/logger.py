import collections
import sys
from contextlib import redirect_stdout
errBuffer = collections.deque(maxlen=1000)
infoBuffer = collections.deque(maxlen=1000)

class logger:
    pipe = sys.stdout

    def __init__(self):
        self.dummy = None

    @staticmethod
    def error(str):
        errBuffer.append(str)
        logger.pipe.write("Myotion -- ERROR: {}\n".format(str))
        logger.pipe.flush()

    @staticmethod
    def info(str):
        infoBuffer.append(str)
        logger.pipe.write("Myotion -- INFO: {}\n".format(str))
        logger.pipe.flush()

    @staticmethod
    def flush():
        logger.pipe.flush()

    @staticmethod
    def errstr():
        return errBuffer[0]

    @staticmethod
    def infostr():
        return infoBuffer[0]
