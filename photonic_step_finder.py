import csv
import numpy as np
import os
import Tkinter, tkFileDialog

#Function that reads all the files in the directory 'path'
#If the filename contains 'y' it reads the position data
#If the filename contains 'laser' if reads the laser on/off voltage
#The data from each y file is added into one long list and the same for laser
def find_step(path, calibration):
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

root = Tkinter.Tk()
root.withdraw()

file_path = tkFileDialog.askdirectory()
cal = float(raw_input('Calibration: '))

find_step(file_path, cal)
















