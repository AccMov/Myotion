import sys
sys.path.insert(0, '../')

from core.mat import * 

import matplotlib.pyplot as plt

a = matFile('Sample_data/Sample_data/mat_emg/zhangjun/Trials/2023-02-03-14-53_SBDDQB.mat')
#a = matFile('Sample_data\Sample_data\mat_emg\lijianhua\Trials\\2023-02-03-17-16_qing.mat')

#get metadata
print("meta data:", a.metadata)

#get frame 0
frame0 = a.channels[0]

#get metadata from frame 0
print("metadata from frame 0:", frame0.metadata)

print("type:", frame0.type)
print("name:", frame0.name)
print("time_units:", frame0.time_units)
print("begin_time:", frame0.begin_time)
print("frequency:", frame0.frequency)
print("count:", frame0.count)
print("units:", frame0.units)

#get data from from 0
print("data from frame 0:", frame0.data)

plt.plot(frame0.data)
plt.show()

