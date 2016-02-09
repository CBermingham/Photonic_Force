import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
from scipy.optimize import curve_fit

def gaussian(x, a, b, c):
    val = a * np.exp(-(x - b)**2 / (2*(c**2)))
    return val

def harmonic_potential(x, k, alpha, beta):
	val = k/2 * (x+beta)**2 - alpha
	return val

def straight_line(x, m, c):
	val = m * x + c
	return val

#Read in on and off position data
displacement1 = []
displacement2 = []
displacement3 = []
displacement4 = []
displacement5 = []
displacement6 = []

f = open('/Volumes/LMF_Microscope/1-Data/2015/7_July/27_files/190915', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	displacement1.append(float(b[9]))

f = open('/Users/Charlotte/Documents/Code/Photonic_Force/27_files/190951', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	displacement2.append(float(b[9]))

f = open('/Users/Charlotte/Documents/Code/Photonic_Force/27_files/191026', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	displacement3.append(float(b[9]))

f = open('/Users/Charlotte/Documents/Code/Photonic_Force/27_files/191100', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	displacement4.append(float(b[9]))

f = open('/Users/Charlotte/Documents/Code/Photonic_Force/27_files/191131', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	displacement5.append(float(b[9]))

f = open('/Users/Charlotte/Documents/Code/Photonic_Force/27_files/191205', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	displacement6.append(float(b[9]))



#make the mean of the off data be zero
#mean1 = np.mean(displacement1)
#displacement1 = [i - mean1 for i in displacement1]
#displacement2 = [i - mean1 for i in displacement2]

#make a histogram
#nbins=100
y_1, bins_1, _ = plt.hist(displacement1, bins=np.arange(min(displacement1), max(displacement1) + 1E-9, 1E-9), normed=True, histtype="step", linewidth=1.5, label = '0 mW')
y_2, bins_2, _ = plt.hist(displacement2, bins=np.arange(min(displacement1), max(displacement1) + 1E-9, 1E-9), normed=True, histtype="step", linewidth=1.5, label = '20 mW')
y_3, bins_3, _ = plt.hist(displacement3, bins=np.arange(min(displacement1), max(displacement1) + 1E-9, 1E-9), normed=True, histtype="step", linewidth=1.5, label = '40 mW')
y_4, bins_4, _ = plt.hist(displacement4, bins=np.arange(min(displacement1), max(displacement1) + 1E-9, 1E-9), normed=True, histtype="step", linewidth=1.5, label = '60 mW')
y_5, bins_5, _ = plt.hist(displacement5, bins=np.arange(min(displacement1), max(displacement1) + 1E-9, 1E-9), normed=True, histtype="step", linewidth=1.5, label = '80 mW')
y_6, bins_6, _ = plt.hist(displacement6, bins=np.arange(min(displacement1), max(displacement1) + 1E-9, 1E-9), normed=True, histtype="step", linewidth=1.5, label = '100 mW')


#x1 = [0.5 * (bins_1[i]+bins_1[i+1]) for i in range(len(bins_1)-1)]
#x2 = [0.5 * (bins_2[i]+bins_2[i+1]) for i in range(len(bins_2)-1)]

#calculate the potential energy from the histogram
#potential1 = [-1.3806488E-23 * 300 * np.log(i) for i in y_1]
#potential2 = [-1.3806488E-23 * 300 * np.log(i) for i in y_2]

#fit the potential energy with a harmonic potential and find the stiffness
#popt1, pcov1 = curve_fit(harmonic_potential, x1, potential1)
#popt2, pcov2 = curve_fit(harmonic_potential, x2, potential2)

#potential_fit1 = []
#for i in x1:
#	fit = harmonic_potential(i, popt1[0], popt1[1], popt1[2])
#	potential_fit1.append(fit)
#print 'Stiffness off = ', popt1[0]*10**5, '*10-5 N/m'

#potential_fit2 = []
#for i in x2:
#	fit = harmonic_potential(i, popt2[0], popt2[1], popt2[2])
#	potential_fit2.append(fit)
#print 'Stiffness on = ', popt2[0]*10**5, '*10-5 N/m'

#off set potentials so the are near zero at zero displacement. set the off potential so it is at zero here
#b = potential_fit1[nbins / 2]

#potential1 = [i - b for i in potential1]
#potential2 = [i - b for i in potential2]

#potential_fit1 = [i - b for i in potential_fit1]
#potential_fit2 = [i - b for i in potential_fit2]

# calculate one potential (off) minus the other (on)
#x_vals = []
#potential_overall = []
#for x in range(0, 100):
#	x_overall = (x-50)/1666666667.0
#	x_vals.append(x_overall)
#	potential_overall.append(harmonic_potential(x_overall, popt2[0], popt2[1], popt2[2]) - harmonic_potential(x_overall, popt1[0], popt1[1], popt1[2]))

#fit overall potential to a straight line to find the force
#popt, pcov = curve_fit(straight_line, x_vals, potential_overall)
#print 'Evanescent Photonic Force =', -popt[0], 'N'

#change metres to nm
#x1 = [i*1E9 for i in x1]
#x2 = [i*1E9 for i in x2]
#x_vals = [i*1E9 for i in x_vals]

#make plots
plt.xlabel("Displacement / nm")
plt.ylabel("Normalised Probability")
plt.legend()
plt.show()

#plt.plot(x1, potential1, color = 'b')
#plt.plot(x2, potential2, color = 'r')
#plt.plot(x1, potential_fit1, color = 'b', ls = '--')
#plt.plot(x2, potential_fit2, color = 'r', ls = '--')
#plt.xlabel('Displacement / nm')
#plt.ylabel('Potential / J')
#plt.show()

#plt.plot(x_vals, potential_overall)
#plt.xlabel('Displacement / nm')
#plt.ylabel('Potential / J')
#plt.show()