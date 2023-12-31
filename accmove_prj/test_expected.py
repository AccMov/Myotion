from accmove.core import *

a = person()
a["name"] = "abc"
a["age"] = 12
a["gender"] = "female"
a.print()

dat1 = timeSeriesTable()
dat1["A"] = [1,2,3,4,5]
dat1["B"] = [7,8,9,10,11]
dat1.print()

dat2 = timeSeriesTable()
dat2["A"] = [1,2,3,4,5]
dat2["B"] = [7,8,9,10,11]
dat2.print()

c = emg()
c["channel"] = ["A", "B", "C"]

adv_analysis = advance_analysis()
adv_analysis["ms_weighting"] = dat1
adv_analysis["ms_timing"] = dat2


d = report()
d["person"] = a
d["advance_analysis"] = adv_analysis
analysis = d["freq_analysis"]


# R
# read(...)
# Plot (...)

# Python
# rep = report.fromFile("xiongda.report")
# adv_analysis = rep["advance_analysis"]
# data_table1 = adv_analysis["ms_weighting"]
# print(data_table1["Muscle_1"])  ->  [1, 2, 3, 4, 5, 6]

# Python plot -> plotly