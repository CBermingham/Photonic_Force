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

# Read time, position and voltage data from Labview files
time, y = read_data_y('141015_270deg', 0, 9)
voltage, = read_data_v('141015_270deg', 1)
voltage = [i/20.0 for i in voltage]

# Find the max of each square wave (2kHz) and time index
v_max = []
time_index = []
for i in range(0, len(voltage)-31, 32):
	v_max.append(max(voltage[i:i+32]))
	time_index.append(i)

step_voltage = []
step_time_index = []

for i in range(len(v_max)-1):
	if v_max[i]>v_max[i+1]+0.09:
		step_voltage.append(v_max[i])
		step_time_index.append(time_index[i])
	if v_max[i]<v_max[i+1]-0.09:
		step_voltage.append(v_max[i])
		step_time_index.append(time_index[i])

step_time_index.append(len(time)-1)
step_voltage.append(v_max[-1])

y_ave = []

y_ave.append(np.mean(y[:step_time_index[0]]))

for i in range(len(step_time_index[:-1])):
	y_ave.append(np.mean(y[step_time_index[i]:step_time_index[i+1]]))

time2 = [time[i] for i in step_time_index]

y_ave = [i * 1E9 for i in y_ave]

rows = zip(step_voltage, y_ave)

# name = raw_input("Enter filename: ")
# writer = csv.writer(open(name, "wb"))
# for row in rows:
#     writer.writerow(row)

#plt.plot(step_voltage)
#plt.plot(time, voltage)
plt.scatter(step_voltage, y_ave)
plt.xticks([1.19, 1.53, 2, 3.14],[r'$\lambda$', r'$3\lambda/4$', r'$\lambda/2$', r'$\lambda/4$'])
plt.ylim(ymin = -200, ymax = 200)
plt.title('270 degrees')
plt.xlabel('Retardation produced by quarter wave plate')
plt.ylabel('Cantilever displacement / nm')
plt.show()






