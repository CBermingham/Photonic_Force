import matplotlib.pyplot as plt
import math
import csv
from scipy.optimize import curve_fit
import numpy as np
from matplotlib import gridspec


s_45=[0, -1.54994789358, 0, 1.54994789358]
p_45=[1.75926416197, 0, -1.75926416197, 0]

s_minus45=[-1.58726836208, 0, 1.58726836208, 0]
p_minus45=[0, 1.72139022895, 0, -1.72139022895]

circ_max = (1.54994789358+1.58726836208)/2.0

theta=range(0, 361)
theta = [i*math.pi/180.0 for i in theta]
s_45 = [1.54994789358*math.cos(i) for i in theta]
p_45 = [1.75926416197*math.sin(i) for i in theta]

s_minus45 = [1.58726836208*math.cos(i) for i in theta]
p_minus45 = [1.72139022895*math.sin(i) for i in theta]

circ_s = [circ_max*math.cos(i) for i in theta]
circ_p = [circ_max*math.sin(i) for i in theta]


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

x=range(1000)
x=[i/6.25-80 for i in x]
y1 = [popts[0]+popts[0]*math.cos(2*i*math.pi/180)**2 for i in x]
y2 = [poptp[0]*math.sin(2*i*math.pi/180)**2 for i in x]

print popts
print poptp


fig = plt.figure(figsize=(18, 6))
gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
ax0 = plt.subplot(gs[0])
ax0.errorbar(angle, pdata, yerr=0.1, color = 'b', fmt='o', label = 'p-polarisation')
ax0.errorbar(angle, sdata, yerr=0.1, color = 'r', fmt='o', label='s-polarisation')
ax0.plot(x, y2, color = 'b', label = 'p-pol fit')
ax0.plot(x, y1, color = 'r', label = 's-pol fit')
ax0.xlim(xmin=-80, xmax = 80)
ax0.ylim(ymin=0, ymax=3.5)
ax0.xlabel('QWP angle (degrees)')
ax0.ylabel('Power / mW')
ax0.legend()

plt.subplot(1, 2, 2)
plt.plot(s_45, p_45, color = 'r', label = '$+45\degree$')
plt.plot(s_minus45, p_minus45, color = 'b', label = '$-45\degree$')
plt.plot(circ_s, circ_p, color = 'g', linestyle = '--', label = 'circle')
plt.gca().set_aspect('equal')
plt.xlim(xmin=-2, xmax = 2)
plt.ylim(ymin=-2, ymax = 2)
leg = plt.legend(framealpha=0, fontsize = 12)
leg.get_frame().set_edgecolor('white')
plt.xlabel('s polarisation intensity / mW')
plt.ylabel('p polarisation intensity / mW')
plt.arrow(0, 1.75926416197, -0.01, 0.0, head_width = 0.05, head_length = 0.08, length_includes_head=True, color = 'r')
plt.arrow(0, -1.75926416197, 0.01, 0.0, head_width = 0.05, head_length = 0.08, length_includes_head=True, color = 'r')
plt.arrow(1.58726836208, 0, 0.0, -0.01, head_width = 0.05, head_length = 0.08, length_includes_head=True, color = 'b')
plt.arrow(-1.58726836208, 0, 0.0, 0.01, head_width = 0.05, head_length = 0.08, length_includes_head=True, color = 'b')
plt.savefig('QWP_combined.pdf')
plt.show()