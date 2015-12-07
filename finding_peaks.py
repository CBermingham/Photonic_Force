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

angle_neg = angle[7:]
pdata_neg = pdata[7:]
sdata_neg = sdata[7:]

angle_plus = angle[:7]
pdata_plus = pdata[:7]
sdata_plus = sdata[:7]

poptp1, pcovp1 = curve_fit(func_p, angle_plus, pdata_plus)
popts1, pcovs1 = curve_fit(func_s, angle_plus, sdata_plus)

print '45, s', popts1[0]+popts1[0]*math.cos(2*45*math.pi/180)**2
print '45, p', poptp1[0]*math.sin(2*45*math.pi/180)**2

poptp2, pcovp2 = curve_fit(func_p, angle_neg, pdata_neg)
popts2, pcovs2 = curve_fit(func_s, angle_neg, sdata_neg)

print '-45, s', popts2[0]+popts2[0]*math.cos(2*45*math.pi/180)**2
print '-45, p', poptp2[0]*math.sin(2*45*math.pi/180)**2

plt.scatter(angle_plus, sdata_plus, color = 'r')
plt.scatter(angle_plus, pdata_plus, color = 'b')
plt.show()