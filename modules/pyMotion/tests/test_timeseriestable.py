import sys
sys.path.insert(0, '../')

from core.timeSeriesTable import * 
from core.mat import * 
from core.c3d import *
from core.xml import * 
import matplotlib.pyplot as plt

# get TST / c3d-analogdata
a = c3dFile('Sample_data/Sample_data/c3d_emg/ERRPT.c3d')
b = a.analog.convertToTST()

# get TST / mat
#a = matFile('Sample_data/Sample_data/mat_emg/zhangjun/Trials/2023-02-03-14-53_SBDDQB.mat')
#b = a.convertToTST()

# print labels and data
for label in b.labels:
    print("{} : {}".format(label, b[label]))

label_A = b.labels[12]
label_B = b.labels[1]

# print frequency
print("frequency: {}".format(b.fs)) 

display_len = 5000
#display_len = -1

# preprocess

# plot original
fig2, axs_2 = plt.subplots(2)
axs_2[0].plot(b[label_A][0:display_len])
axs_2[0].set_title("original")

# removed dc
removed = b.removeDC(label_A)
#replaced
b[label_A] = removed
axs_2[1].plot(removed[0:display_len])
axs_2[1].set_title("removed DC")

fig00, axs00 = plt.subplots(4)
# plot original
axs00[0].plot(b[label_A][0:display_len])
axs00[0].set_title("original")

# filter band pass
band_result = b.bandpass(label_A, 10, 200)
axs00[1].plot(band_result[0:display_len])
axs00[1].set_title("band pass: 10-200Hz")

# fft before
fft_before_bp_freq, fft_before_bp = b.fft(label_A)
axs00[2].plot(fft_before_bp_freq, fft_before_bp)
axs00[2].set_title("fft: before band pass")

# fft after
b[label_A] = band_result
fft_after_bp_freq, fft_after_bp = b.fft(label_A)
axs00[3].plot(fft_after_bp_freq, fft_after_bp)
axs00[3].set_title("fft: after band pass")

fig01, axs01 = plt.subplots(2)
axs01[0].plot(b[label_A][0:display_len])
axs01[0].set_title("original")
# rectification
rect = b.rectification(label_A)
b[label_A] = rect
axs01[1].plot(rect[0:display_len])
axs01[1].set_title("rectified")

fig, axs = plt.subplots(4)
# plot original
axs[0].plot(b[label_A][0:display_len])
axs[0].set_title("original")

# filter low pass
low_result = b.lowpass(label_A, 10, 4)
axs[1].plot(low_result[0:display_len])
axs[1].set_title("low pass: 10Hz")

# fft before
fft_before_lp_freq, fft_before_lp = b.fft(label_A)
axs[2].plot(fft_before_lp_freq, fft_before_lp)
axs[2].set_title("fft: before low pass")

# fft after
b[label_A] = low_result
fft_after_lp_freq, fft_after_lp = b.fft(label_A)
axs[3].plot(fft_after_lp_freq, fft_after_lp)
axs[3].set_title("fft: after low pass")

fig3, axs_3 = plt.subplots(2)
# threholdDetection
activated = b.threholdDetection(label_A, 0.5*b.max(label_A), 5, 5)
axs_3[0].plot(b[label_A])
axs_3[0].set_title("original")
red_data = b[label_A]

for pair in activated:
    axs_3[1].plot(np.arange(pair[0], pair[1]), b[label_A][pair[0]:pair[1]], c='green')
axs_3[1].set_title("activated threhold:{} n_above:5 n_below:5".format(0.5*b.max(label_A)))

fig4, axs_4 = plt.subplots(2)
#cocontration
axs_4[0].plot(b[label_A])
b[label_B] = b.removeDC(label_B)
b[label_B] = b.rectification(label_B)
b[label_B] = b.lowpass(label_B, 10)
axs_4[1].plot(b[label_B])

# statistic after filtering
print("{}'s max: {}".format(label_A, b.max(label_A)))
print("{}'s min: {}".format(label_A, b.min(label_A)))
print("{}'s mean: {}".format(label_A, b.mean(label_A)))
print("{}'s median: {}".format(label_A, b.median(label_A)))
print("{}'s standard deviation: {}".format(label_A, b.std(label_A)))
print("{}'s variance: {}".format(label_A, b.var(label_A)))
print("{}'s rms: {}".format(label_A, b.rms(label_A)))
print("{}'s ptp: {}".format(label_A, b.ptp(label_A)))
print("{}'s zeros: {}".format(label_A, b.countZeros(label_A)))
print("{} and {}'s co-contration: {}".format(label_A, label_B, b.cocontraction(label_A, label_B)))

# change to xml
xmlWriter('b_test.xml',b.toXML()).write()

print("search channel with regex: {}".format(b.searchChannel('F+')))

b.filterChannel('F+')
print("filtered channel with regex:")
for label in b.labels:
    print("{} : {}".format(label, b[label]))


plt.show()
