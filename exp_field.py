import csv
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.optimize import curve_fit

def func(x, A, d):
	return np.log(A)-x/d

distance = []
intensity = []
error = []

with open('exp_field.csv', 'rb') as f:
	reader = csv.reader(f, None)
	for row in reader:
		distance.append(float(row[0]))
		intensity.append(float(row[1]))
		error.append(float(row[2]))

intensity2 = [i*100/384.73 for i in intensity]

ylog = [np.log(i) for i in intensity2]
popt, pcov = curve_fit(func, distance, ylog)

print popt
print pcov

x=range(1000)
x=[i*max(distance)/1000 for i in x]
fit = [popt[0]*np.exp(-i/popt[1]) for i in x]

plt.errorbar(distance, intensity2, yerr=error, fmt='o', label = 'experiment', color = 'r', markersize=3)
plt.plot(x, fit, label = 'exponential fitting', color = 'b')
plt.yscale('log')
plt.ylabel('Intensity of the field (a.u.)')
plt.xlabel('Distance from the interface $x$ (nm)')
plt.ylim(ymin = 20, ymax = 100)
plt.minorticks_on()
plt.yticks([20, 30, 50, 70, 100], ['20', '30', '50', '70', '100'])
leg = plt.legend()
leg.get_frame().set_edgecolor('white')
plt.savefig('exp_field.pdf')

plt.show()