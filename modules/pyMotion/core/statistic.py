from .xml import *
from .timeSeriesTable import *
class emgStatistic:
    def __init__(self, tst):
        #time_domain
        self.min = tst.min()
        self.max = tst.max()
        self.mean = tst.mean()
        self.med = tst.median()
        self.std = tst.std()
        self.var = tst.var()
        self.ptp = tst.ptp()
        self.zc = tst.countZeros()
        self.auc = tst.trapz()
        self.rms = tst.rms()
        self.mp = tst.trapz()
        self.mav = tst.meanAbsoluate()
        self.en = None
        self.sk = tst.skew()
        self.kur = tst.kurtosis()

        #freq domain
        self.mnf = tst.meanFreq()
        self.mdf = tst.medFreq()

        bandpower = tst.BandPower()
        self.bpd = [bandpower[idx]["delta"] for idx in range(0, tst.chanSize())]
        self.bdt = [bandpower[idx]["theta"] for idx in range(0, tst.chanSize())]
        self.bpa = [bandpower[idx]["alpha"] for idx in range(0, tst.chanSize())]
        self.bpb = [bandpower[idx]["beta"] for idx in range(0, tst.chanSize())]
        self.bpg = [bandpower[idx]["gamma"] for idx in range(0, tst.chanSize())]

    def toXML(self):
        e = xmlElement('statistic')
        e.addNode('min', self.min)
        e.addNode('max', self.max)
        e.addNode('mean', self.mean)
        e.addNode('med', self.med)
        e.addNode('std', self.std)
        e.addNode('var', self.var)
        e.addNode('ptp', self.ptp)
        e.addNode('zc', self.zc)
        e.addNode('auc', self.auc)
        e.addNode('rms', self.rms)
        e.addNode('mp', self.mp)
        e.addNode('sk', self.sk)
        e.addNode('kur', self.kur)

        e.addNode('mnf', self.mnf)
        e.addNode('mdf', self.mdf)
        e.addNode('bpd', self.bpd)
        e.addNode('bdt', self.bdt)
        e.addNode('bpa', self.bpa)
        e.addNode('bpb', self.bpb)
        e.addNode('bpg', self.bpg)
        return e