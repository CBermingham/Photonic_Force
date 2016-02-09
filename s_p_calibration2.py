import csv
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit
import numpy as np

def func_s(x, A):
	return A+A*np.cos(2*x*np.pi/180.0)**2

def func_p(x, A):
	return A*np.sin(2*x*np.pi/180.0)**2

angle = []
pdata = []
sdata = []

with open('s_p_calibration.csv', 'rb') as f:
	reader = csv.reader(f, None)
	for row in reader:
		angle.append(float(row[0]))
		pdata.append(float(row[1]))
		sdata.append(float(row[2]))

angle = np.asarray(angle)
pdata = np.asarray(pdata)
sdata = np.asarray(sdata)

poptp, pcovp = curve_fit(func_p, angle, pdata)
popts, pcovs = curve_fit(func_s, angle, sdata)

x =range(1000)
x =[i/6.25-80 for i in x]
y1 = [popts[0]+popts[0]*math.cos(2*i*math.pi/180)**2 for i in x]
y2 = [poptp[0]*math.sin(2*i*math.pi/180)**2 for i in x]

print math.sqrt(popts*2/0.94**2)
print math.sqrt(poptp*2/0.88**2)

plt.errorbar(angle, pdata, yerr=0.1, color = 'c', fmt='o', label = 'p-polarisation')
plt.errorbar(angle, sdata, yerr=0.1, color = 'm', fmt='o', label='s-polarisation')
plt.plot(x, y2, color = 'c', label = 'p-pol fit')
plt.plot(x, y1, color = 'm', label = 's-pol fit')
plt.xlim(xmin=-80, xmax = 80)
plt.ylim(ymin=0, ymax=3.5)
plt.xlabel('QWP angle ($\degree$)')
plt.ylabel('Power (mW)')
plt.legend()
plt.savefig('s_p_calibration2.pdf')
plt.show()