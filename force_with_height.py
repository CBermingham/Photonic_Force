import csv
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.optimize import curve_fit

def func(x, A, d):
	return np.log(A)-x/d

distance = []
force_s = []
force_p = []
error_s = []
error_p = []

with open('force_with_height.csv', 'rb') as f:
	reader = csv.reader(f, None)
	for row in reader:
		distance.append(float(row[0]))
		force_p.append(float(row[1]))
		error_p.append(float(row[2]))
		force_s.append(float(row[3]))
		error_s.append(float(row[4]))

distance2 = []
force_p2 = []
error_p2 = []

with open('force_with_height_spin.csv', 'rb') as f:
	reader = csv.reader(f, None)
	for row in reader:
		distance2.append(float(row[0]))
		force_p2.append(float(row[1]))
		error_p2.append(float(row[2]))

distance3 = []
intensity_s = []
error_int_s = []
distance4 = []
intensity_p = []
error_int_p = []

with open('intensity_with_height.csv', 'rb') as f:
	reader = csv.reader(f, None)
	for row in reader:
		distance3.append(float(row[0]))
		intensity_s.append(float(row[1]))
		error_int_s.append(float(row[2]))
		distance4.append(float(row[3]))
		intensity_p.append(float(row[4]))
		error_int_p.append(float(row[5]))

distance5 = []
intensity_5s = []
error_int_5s = []

with open('intensity_with_height_0.csv', 'rb') as f:
	reader = csv.reader(f, None)
	for row in reader:
		distance5.append(float(row[0]))
		intensity_5s.append(float(row[1]))
		error_int_5s.append(float(row[2]))

distance6 = []
intensity_6p = []
error_int_6p = []

with open('intensity_with_height_0_p.csv', 'rb') as f:
	reader = csv.reader(f, None)
	for row in reader:
		distance6.append(float(row[0]))
		intensity_6p.append(float(row[1]))
		error_int_6p.append(float(row[2]))

ylog_p = [np.log(i) for i in force_p]
error_p = [error_p[i]/ylog_p[i] for i in range(0, len(error_p))]
popt_p, pcov_p = curve_fit(func, distance, ylog_p)

ylog_s = [np.log(i) for i in force_s]
error_s = [error_s[i]/ylog_s[i] for i in range(0, len(error_s))]
popt_s, pcov_s = curve_fit(func, distance, ylog_s)

ylog_p2 = [np.log(i) for i in force_p2]
error_p2 = [error_p2[i]/ylog_p2[i] for i in range(0, len(error_p2))]
popt_p2, pcov_p2 = curve_fit(func, distance2, ylog_p2)

ylog_s_int = [np.log(i) for i in intensity_s]
error_int_s = [error_int_s[i]/ylog_s_int[i] for i in range(0, len(error_int_s))]
popt_s_int, pcov_s_int = curve_fit(func, distance3, ylog_s_int)

ylog_p_int = [np.log(i) for i in intensity_p]
error_int_p = [error_int_p[i]/ylog_p_int[i] for i in range(0, len(error_int_p))]
popt_p_int, pcov_p_int = curve_fit(func, distance4, ylog_p_int)

ylog_5s_int = [np.log(i) for i in intensity_5s]
error_int_5s = [error_int_5s[i]/ylog_5s_int[i] for i in range(0, len(error_int_5s))]
popt_5s_int, pcov_5s_int = curve_fit(func, distance5, ylog_5s_int)

ylog_6p_int = [np.log(i) for i in intensity_6p]
error_int_6p = [error_int_6p[i]/ylog_6p_int[i] for i in range(0, len(error_int_6p))]
popt_6p_int, pcov_6p_int = curve_fit(func, distance6, ylog_6p_int)

x=range(1000)
x=[i*max(distance)/1000 for i in x]
fit_p = [func(i, popt_p[0], popt_p[1]) for i in x]
fit_s = [func(i, popt_s[0], popt_s[1]) for i in x]

x2=range(1000)
x2=[i*max(distance2)/1000 for i in x2]
fit_p2 = [func(i, popt_p2[0], popt_p2[1]) for i in x2]

x3=range(1000)
x3=[i*max(distance3)/1000 for i in x3]
fit_s_int = [func(i, popt_s_int[0], popt_s_int[1]) for i in x3]

x4=range(1000)
x4=[i*max(distance4)/1000 for i in x4]
fit_p_int = [func(i, popt_p_int[0], popt_p_int[1]) for i in x4]

x5=range(1000)
x5=[i*max(distance5)/1000 for i in x5]
fit_5s_int = [func(i, popt_5s_int[0], popt_5s_int[1]) for i in x5]

x6=range(1000)
x6=[i*max(distance6)/1000 for i in x6]
fit_6p_int = [func(i, popt_6p_int[0], popt_6p_int[1]) for i in x6]

print 'Force p recent', popt_p
print 'Force s recent', popt_s
print 'Force p spin', popt_p2
print 'Intensity 90 s', popt_s_int
print 'Intensity 90 p', popt_p_int
print 'Intensity 0 s', popt_5s_int
print 'Intensity 0 p', popt_6p_int

# plt.errorbar(distance, ylog_p, yerr=error_p, fmt='o', label = 'p recent', color = 'b', markersize=3)
# plt.plot(x, fit_p, color = 'b')
# plt.errorbar(distance, ylog_s, yerr=error_s, fmt='o', label = 's recent', color = 'r', markersize=3)
# plt.plot(x, fit_s, color = 'r')
# plt.errorbar(distance2, ylog_p2, yerr=error_p2, fmt='o', label = 'p from spin experiment', color = 'g', markersize=3)
# plt.plot(x2, fit_p2, color = 'g')
plt.errorbar(distance3, ylog_s_int, yerr=error_int_s, fmt='o', label = 'intensity s 90', color = 'c', markersize=3)
plt.plot(x3, fit_s_int, color = 'g')
plt.errorbar(distance4, ylog_p_int, yerr=error_int_p, fmt='o', label = 'intensity p 90', color = 'm', markersize=3)
plt.plot(x4, fit_p_int, color = 'm')
# plt.errorbar(distance5, ylog_5s_int, yerr=error_int_5s, fmt='o', label = 'intensity s 0', color = 'r', markersize=3)
# plt.plot(x5, fit_5s_int, color = 'r')
# plt.errorbar(distance6, ylog_6p_int, yerr=error_int_6p, fmt='o', label = 'intensity p 0', color = 'b', markersize=3)
# plt.plot(x6, fit_6p_int, color = 'b')
plt.ylabel('ln(Displacement)/ln(Intensity)')
plt.xlabel('Distance above sample / nm')
leg = plt.legend()
leg.get_frame().set_edgecolor('white')
plt.savefig('intensity_with_height.pdf')
plt.show()