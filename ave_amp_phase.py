import numpy as np
import os
import math
import csv

def circmean(alpha,axis=None):
    mean_angle = np.arctan2(np.mean(np.sin(alpha),axis),np.mean(np.cos(alpha),axis))
    return mean_angle
    
def circvar(alpha,axis=None):
    if np.ma.isMaskedArray(alpha) and alpha.mask.shape!=():
        N = np.sum(~alpha.mask,axis)
    else:
        if axis is None:
            N = alpha.size
        else:
            N = alpha.shape[axis]
    R = np.sqrt(np.sum(np.sin(alpha),axis)**2 + np.sum(np.cos(alpha),axis)**2)/N
    V = 1-R
    return V

ave_amplitude = []
err_amplitude = []
ave_phase = []
err_phase = []

path = '180'
dirs = os.listdir(path)

for filename in dirs:
	phase = []
	amplitude = []
	f = open(path + '/' + filename, 'rU')
	lines=f.readlines()
	f.close()
	
	for l in lines:
		b = l.split()
		amplitude.append(float(b[3]))
		phase.append(float(b[1])*math.pi / 180)

	ave_amplitude.append(np.mean(amplitude))
	ave_phase.append(circmean(phase)*180 / math.pi)
	err_amplitude.append(np.std(amplitude))
#	err_phase.append(circvar(phase)*180 / math.pi)

rows = zip(ave_amplitude, ave_phase, err_amplitude)
writer = csv.writer(open("180.csv", "wb"))
writer.writerow(["Amplitude", "Phase", "Amplitude error"])
for row in rows:
	writer.writerow(row)






