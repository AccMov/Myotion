from accmove.core import *
import matplotlib.pyplot as plt

#a = c3dFile('Sample_data\Sample_data\c3d_emg\ERRPT.c3d')
a = matFile('Sample_data\Sample_data\mat_emg\zhangjun\Trials\\2023-02-03-14-53_SBDDQB.mat')

# get TST
b = a.convertToTST()

# print labels and data
for label in b.labels:
    print("{} : {}".format(label, b[label]))

# print frequency
print("frequency: {}".format(b.fs)) 

label_A = b.labels[0]

# data processing
print("{}'s max: {}".format(label_A, b.max(label_A)))
print("{}'s min: {}".format(label_A, b.min(label_A)))
print("{}'s mean: {}".format(label_A, b.mean(label_A)))
print("{}'s median: {}".format(label_A, b.median(label_A)))
print("{}'s standard deviation: {}".format(label_A, b.std(label_A)))
print("{}'s variance: {}".format(label_A, b.var(label_A)))
print("{}'s rms: {}".format(label_A, b.rms(label_A)))
print("{}'s ptp: {}".format(label_A, b.ptp(label_A)))


fig, axs = plt.subplots(3)
display_len = 5000
# plot first channel
axs[0].plot(b[label_A][0:display_len])

# filter low pass
low_result = b.lowpass(label_A, 10)
axs[1].plot(low_result[0:display_len])

# filter band pass
band_result = b.bandpass(label_A, 10, 100)
axs[2].plot(band_result[0:display_len])

fig2, axs_2 = plt.subplots(3)
axs_2[0].plot(b[label_A][0:display_len])
# removed dc
removed = b.removeDC(label_A)
axs_2[1].plot(removed[0:display_len])

plt.show()

