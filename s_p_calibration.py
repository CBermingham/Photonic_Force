import csv
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit
import numpy as np

def func(x, A, B, C):
#	return np.log(A)-x/d
	return A+B*np.cos(C*x*np.pi/180.0)

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

poptp, pcovp = curve_fit(func, angle, pdata)
popts, pcovs = curve_fit(func, angle, sdata)

x=range(1000)
x=[i/6.25-80 for i in x]
y1 = [popts[0]+popts[1]*math.cos(popts[2]*i*math.pi/180) for i in x]
y2 = [poptp[0]+poptp[1]*math.cos(poptp[2]*i*math.pi/180) for i in x]

print popts
print poptp

plt.errorbar(angle, pdata, yerr=0.1, color = 'b', fmt='o', label = 'p-polarisation')
plt.errorbar(angle, sdata, yerr=0.1, color = 'r', fmt='o', label='s-polarisation')
plt.plot(x, y1, color = 'r', label = 's-pol fit')
plt.plot(x, y2, color = 'b', label = 'p-pol fit')
plt.xlim(xmin=-80, xmax = 80)
plt.ylim(ymin=0, ymax=3.5)
plt.xlabel('QWP angle (degrees)')
plt.ylabel('Power / mW')
plt.legend()
plt.savefig('s_p_calibration.pdf')
plt.show()