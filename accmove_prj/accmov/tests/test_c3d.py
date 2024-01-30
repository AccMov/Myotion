import sys
sys.path.insert(0, '../')

from core.c3d import * 

import matplotlib.pyplot as plt

#a = c3dFile('Sample_data\Sample_data\c3d_emg\ERRPT.c3d')
a = c3dFile('Sample_data/Sample_data/c3d_emg/RPT_1.c3d')

#metadata
print("metadata", a.metadata)

# seperate meta info
print("point_fs", a.point_fs)
print("analog_fs", a.analog_fs)
print("point_number", a.point_number)
print("channel_number", a.channel_number)
print("point_labels", a.point_labels)
print("channel_labels", a.channel_labels)
print("frame_number", a.frame_number)
print("time", a.time)

#get points
p = a.points
print("total points:", p.size())
print("point fs:", p.fs)

#iteration
for key in p.labels:
    print(p.data[key])

#get analog
analog = a.analog
print("total analog data:", analog.size())
print("analog fs:", analog.fs)
print("analog label:", analog.label)

#get data from from analog
plt.plot(analog['UT.IM EMG1'])
plt.show()
