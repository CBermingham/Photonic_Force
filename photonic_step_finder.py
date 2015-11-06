import csv
import matplotlib.pyplot as plt
import numpy as np
import os

#Function that reads all the files in the directory 'path'
#If the filename contains 'y' it reads the position data
#If the filename contains 'laser' if reads the laser on/off voltage
#The data from each y file is added into one long list and the same for laser
def data_reader(path, calibration):
	ydata = []
	laser = []
	directory = sorted(os.listdir(path))
	for filename in directory:
	    if 'y' in filename:
	        with open(path + '/' + filename) as f:
	            for line in f:
	            	b = line.split()
	                ydata.append(float(b[9]))
	    if 'laser' in filename:
	        with open(path + '/' + filename) as f:
	            for line in f:
	                b = line.split()
	                laser.append(float(b[1]))
	ydata = [i*calibration*1E9/1311.0 for i in ydata]
	return ydata, laser

#Function to find the step size
def find_step(ydata, laser):
	#Find the positions in the laser data where the laser was switched on and off,
	#this is where the voltage switched from 100 to 0 (or whatever the voltage is recorded as)
	#At each on/off point, recoded the index. The indexes are the same for the y and laser data
	on_off = []
	for i in range(0, len(laser)-1):
	    if (laser[i]>50 and laser[i+1] <50) or (laser[i]<50 and laser[i+1]>50):
	        on_off.append(i)

	#Use the indexes to find the mean of the first 'on'step after a full 'off' step
	#and do the mean of the on step - the mean of the off step before
	step = []
	if laser[0]>50:
		for i in range(0, len(on_off[:-2]), 2):
			step.append(np.mean(ydata[on_off[i+1]:on_off[i+2]])-np.mean(ydata[on_off[i]:on_off[i+1]]))

	if laser[0]<50:
		for i in range(0, len(on_off[:-3]), 2):
			step.append(np.mean(ydata[on_off[i+2]:on_off[i+3]])-np.mean(ydata[on_off[i+1]:on_off[i+2]]))

	#Find the average of all steps and the standard deviation
	#Print this result
	print "Average step: ", np.mean(step), "nm +/- ", np.std(step)

# ydata1, laser1 = data_reader('/Volumes/LMF_Microscope/1-Data/2015/11_November/05saveddata/150946', 3216)
# find_step(ydata1, laser1)
# ydata2, laser2 = data_reader('/Volumes/LMF_Microscope/1-Data/2015/11_November/05saveddata/151031', 3216)
# find_step(ydata2, laser2)
# ydata3, laser3 = data_reader('/Volumes/LMF_Microscope/1-Data/2015/11_November/05saveddata/151143', 2167)
# find_step(ydata3, laser3)
# ydata4, laser4 = data_reader('/Volumes/LMF_Microscope/1-Data/2015/11_November/05saveddata/151221', 2167)
# find_step(ydata4, laser4)
# ydata5, laser5 = data_reader('/Volumes/LMF_Microscope/1-Data/2015/11_November/05saveddata/151318', 1634)
# find_step(ydata5, laser5)
# ydata6, laser6 = data_reader('/Volumes/LMF_Microscope/1-Data/2015/11_November/05saveddata/151359', 1634)
# find_step(ydata6, laser6)
# ydata7, laser7 = data_reader('/Volumes/LMF_Microscope/1-Data/2015/11_November/05saveddata/151512', 1312)
# find_step(ydata7, laser7)
ydata8, laser8 = data_reader('/Volumes/LMF_Microscope/1-Data/2015/11_November/05saveddata/151556', 1312)
find_step(ydata8, laser8)









