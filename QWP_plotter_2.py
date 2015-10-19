import matplotlib.pyplot as plt
import numpy as np
import os
import csv

# Function that reads a data flie and extracts data in columns
def read_data_y(path, *columns):
	out = [list() for _ in columns]
	directory = os.listdir(path)
	for filename in directory:
		if 'y' in filename:
		 	with open(path + '/' + filename) as f:
				for line in f:
					b = line.split()
					for i,j in enumerate(columns):
						out[i].append(float(b[j]))
	return out

def read_data_v(path, *columns):
	out = [list() for _ in columns]
	directory = os.listdir(path)
	for filename in directory:
		if 'v' in filename:
		 	with open(path + '/' + filename) as f:
				for line in f:
					b = line.split()
					for i,j in enumerate(columns):
						out[i].append(float(b[j]))
	return out


#time_step = float(raw_input("Time step / ms: "))
time_step = 500
v_start = 1
v_end = 3.5
v_step = 0.1
steps = int((v_end - v_start)/v_step)


calc_voltage = [v_start+i*v_step for i in range(0, int((v_end-v_start) / v_step))]

# Read time, position and voltage data from Labview files
time, y_pos = read_data_y('141015_0deg', 0, 9)
voltage, = read_data_v('141015_0deg', 1)
voltage = [i/20.0 for i in voltage]

# Find the max of each square wave (2kHz) and time index

start = []

step = 32
max_v = [max(voltage[i:i+step]) for i in range(0, len(voltage)-31, step)]
values = [i*32 for i in range(len(max_v))]
diff = [x-y for x,y in zip(max_v[:-1], max_v[1:])]
for n, d in enumerate(diff):
    if d > 0.3 :	
        start.append(int((n+1)*32))

print start

ave = []

for i in range(0, len(start)-1):
	y_ave = []
	y_error = []
	for j in range(start[i], start[i+1], int(64000 * time_step / 1000)):
		y_ave.append(np.mean(y_pos[j:j+32000]))
		y_error.append(np.std(y_pos[j:j+32000]))
	ave.append(y_ave)

print len(calc_voltage)
print len(ave[1])
print len(ave[2])
print len(ave[3])

for a in ave:
	plt.plot(a)
plt.show()

# step_time_index.append(len(time)-1)
# step_voltage.append(v_max[-1])

# y_ave = []

# y_ave.append(np.mean(y[:step_time_index[0]]))

# for i in range(len(step_time_index[:-1])):
# 	y_ave.append(np.mean(y[step_time_index[i]:step_time_index[i+1]]))

# time2 = [time[i] for i in step_time_index]

# rows = zip(step_voltage, y_ave)

# name = raw_input("Enter filename: ")
# writer = csv.writer(open(name, "wb"))
# for row in rows:
#     writer.writerow(row)


# #plt.plot(time, voltage)
# plt.scatter(step_voltage, y_ave)
# plt.ylim(ymin = -200E-9, ymax = 200E-9)
