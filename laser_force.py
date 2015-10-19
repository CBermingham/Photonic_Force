import os
import numpy as np
import csv

path = "ref2_start_off"
dirs = os.listdir(path)

ref = []
step_size = []
step_std = []
names = []

for file in dirs:
	del ref[:]
	# read in on/off voltage data
	filename = file
	datafile = path + '/' + file
	f = open(datafile, 'rU')
	lines=f.readlines()
	f.close()
	for l in lines:
		b = l.split()
		ref.append(float(b[3]))

	on_ref = []


# Find where the laser was on
	for i in range(0, len(ref)):
		if ref[i] > 49.9:
			on_ref.append(i)

# Find teh points that the laser was switched on an off
	a = []
	a.append(on_ref[0])
	for i in range(0, len(on_ref)-1):
		if on_ref[i+1] - on_ref[i] != 1:
			a.append(on_ref[i])
			a.append(on_ref[i+1])
	a.append(on_ref[-1])
	a.append(len(ref))
	on_ref = a

# read in amplitude data
	yposition = []
	amp_path = "amplitude2_start_off"
	datafile = amp_path + '/' + filename
	f = open(datafile, 'rU')
	lines=f.readlines()
	f.close()
	for l in lines:
		b = l.split()
		yposition.append(float(b[9]))

#calculate steps
	step1 = (np.mean(yposition[on_ref[0]:on_ref[1]]) - np.mean(yposition[on_ref[1]:on_ref[2]]))*1E9
	step2 = (np.mean(yposition[on_ref[2]:on_ref[3]]) - np.mean(yposition[on_ref[1]:on_ref[2]]))*1E9
	step3 = (np.mean(yposition[on_ref[2]:on_ref[3]]) - np.mean(yposition[on_ref[3]:on_ref[4]]))*1E9

#	step1 = (np.mean(yposition[on_ref[0]:on_ref[1]]) - np.mean(yposition[0:on_ref[0]]))*1E9
#	step2 = (np.mean(yposition[on_ref[0]:on_ref[1]]) - np.mean(yposition[on_ref[1]:on_ref[2]]))*1E9
#	step3 = (np.mean(yposition[on_ref[2]:on_ref[3]]) - np.mean(yposition[on_ref[3]:on_ref[4]]))*1E9

	step_size.append(np.mean([step1, step2, step3]))
	step_std.append(np.std([step1, step2, step3]))
	names.append(filename)

rows = zip(names, step_size, step_std)
writer = csv.writer(open("2_steps_starting_on.csv", "wb"))
writer.writerow(["Filename", "Mean step size / nm", "Standard deviation / nm"])
for row in rows:
	writer.writerow(row)