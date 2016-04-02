import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit
import numpy as np
import math

def polynomial(x, a, b, c, d, e, f, g, h):
	return a + b*x + c*x**2 + d*x**3 + e*x**4 + f*x**5 + g*x**6 + h*x**7

def polynomial3(x, a, b, c, d, e, f, g, h):
	return a + b*x + c*x**2 + d*x**3 + e*x**4 + f*x**5 + g*x**6 + h*x**7

def reciprocal(x, a):
	return x/a

def undefined_poly(x, a, b, c):
	return a + b*x**c

voltage = []
s = []
s_error = []
p = []
p_error = []
retardance_precise = []

f = open('LCVRprecise.csv', 'rU')
reader = csv.reader(f, None)
for row in reader:
	voltage.append(float(row[0]))
	s.append(float(row[1]))
	s_error.append(float(row[2]))
	p.append(float(row[3]))
	p_error.append(float(row[4]))
	retardance_precise.append(float(row[5]))
f.close()

voltage=np.array(voltage)
s = np.array(s)
retardance_precise = np.array(retardance_precise)

popts, pcovs = curve_fit(polynomial, voltage, s)
fits = [polynomial(i, popts[0], popts[1], popts[2], popts[3], popts[4], popts[5], popts[6], popts[7]) for i in voltage]
poptp, pcovp = curve_fit(polynomial, voltage, p)
fitp = [polynomial(i, poptp[0], poptp[1], poptp[2], poptp[3], poptp[4], poptp[5], poptp[6], poptp[7]) for i in voltage]

poptrprec, pcovrprec = curve_fit(polynomial, voltage, retardance_precise)
fitrprec = [polynomial(i, poptrprec[0], poptrprec[1], poptrprec[2], poptrprec[3], poptrprec[4], poptrprec[5], poptrprec[6], poptrprec[7]) for i in voltage]
print poptrprec

voltage_rough = []
s_rough = []
s_error_rough = []
p_rough = []
p_error_rough = []
retardance = []

f = open('LCVRrough.csv', 'rU')
reader = csv.reader(f, None)
for row in reader:
	voltage_rough.append(float(row[0]))
	s_rough.append(float(row[1]))
	s_error_rough.append(float(row[2]))
	p_rough.append(float(row[3]))
	p_error_rough.append(float(row[4]))
	retardance.append(float(row[5]))
f.close()

voltage_rough=np.array(voltage_rough)
s_rough = np.array(s_rough)

fit_voltages = [voltage_rough[8]+((voltage_rough[-2]-voltage_rough[8])*i/1000) for i in range (0, 1000)]

popts_rough, pcovs_rough = curve_fit(polynomial, voltage_rough[8:-2], s_rough[8:-2])
fits_rough = [polynomial(i, popts_rough[0], popts_rough[1], popts_rough[2], popts_rough[3], popts_rough[4], popts_rough[5], popts_rough[6], popts_rough[7]) for i in fit_voltages]
poptp_rough, pcovp_rough = curve_fit(polynomial, voltage_rough[8:-2], p_rough[8:-2])
fitp_rough = [polynomial(i, poptp_rough[0], poptp_rough[1], poptp_rough[2], poptp_rough[3], poptp_rough[4], poptp_rough[5], poptp_rough[6], poptp_rough[7]) for i in fit_voltages]

# one_over_r = [1/i for i in retardance]
# poptr, pcovr = curve_fit(reciprocal, voltage_rough[8:], one_over_r[8:])
# fitr = [1/reciprocal(i, poptr[0]) for i in voltage_rough[8:]]
#poptr, pcovr = curve_fit(polynomial, voltage_rough[8:], retardance[8:])
#fitr = [polynomial(i, poptr[0], poptr[1], poptr[2], poptr[3], poptr[4], poptr[5], poptr[6], poptr[7]) for i in voltage_rough[8:]]
poptr, pcovr = curve_fit(undefined_poly, voltage_rough[8:], retardance[8:], [1,1,-0.5])
fitr = [undefined_poly(i, poptr[0], poptr[1], poptr[2]) for i in voltage_rough[8:]]
print poptr

voltage_specs = []
retardance_specs = []

f = open('LCVR_manufacturer_retardance.csv', 'rU')
reader = csv.reader(f, None)
for row in reader:
	voltage_specs.append(float(row[0]))
	retardance_specs.append(float(row[1]))
f.close()

retardance_specs = [i*2*math.pi for i in retardance_specs]
retardance_specs = np.array(retardance_specs)
voltage_specs = np.array(voltage_specs)

poptrspecs, pcovrspecs = curve_fit(undefined_poly, voltage_specs[9:], retardance_specs[9:], [1, 1, -0.5])
fitrspecs = [undefined_poly(i, poptrspecs[0], poptrspecs[1], poptrspecs[2]) for i in voltage_specs[9:]]
print poptrspecs

# plt.figure(figsize=(8,4), tight_layout = True)
# plt.errorbar(voltage, s, yerr = s_error, fmt='o', markersize = 3, color = 'turquoise', zorder = 3, label = 's polarisation')
# plt.errorbar(voltage, p, yerr = p_error, fmt='o', markersize = 3, color = 'slateblue', zorder = 4, label = 'p polarisation')
# plt.plot(voltage, fits, color = 'turquoise', zorder = 1)
# plt.plot(voltage, fitp, color = 'slateblue', zorder = 2)
# plt.xlabel("LCVR voltage (V)", fontsize = 14, labelpad=3)
# plt.ylabel("Intensity (mW)", fontsize = 14, labelpad=3)
# plt.xticks(size = 14)
# plt.yticks(size = 14)
# leg = plt.legend(loc = 7, prop={'size':14})
# leg.get_frame().set_edgecolor('white')
# plt.savefig('LCVRprecise.pdf')

# plt.figure(figsize=(8,4), tight_layout = True)
# plt.errorbar(voltage_rough, s_rough, yerr = s_error_rough, fmt='o', markersize = 3, color = 'turquoise', zorder = 3, label = 's polarisation')
# plt.errorbar(voltage_rough, p_rough, yerr = p_error_rough, fmt='o', markersize = 3, color = 'slateblue', zorder = 4, label = 'p polarisation')
# plt.plot(fit_voltages[:-50], fits_rough[:-50], color = 'turquoise', zorder = 1)
# plt.plot(fit_voltages[:-50], fitp_rough[:-50], color = 'slateblue', zorder = 2)
# plt.xlabel("LCVR voltage (V)", fontsize = 14, labelpad=3)
# plt.ylabel("Intensity (mW)", fontsize = 14, labelpad=3)
# plt.xticks(np.arange(0, 4, 1), size = 14)
# plt.yticks(np.arange(0, 25, 5), size = 14)
# leg = plt.legend(loc = 1, prop={'size':14}, fancybox=True, framealpha=0.5)
# leg.get_frame().set_edgecolor('white')
# plt.ylim(ymin=0, ymax = 18)
# plt.savefig('LCVRrough.pdf')

plt.figure(figsize=(8,3), tight_layout = True)
plt.axhline(y=6.283185307, xmin=0, xmax=1.5/3.5, linestyle = '--', color = 'darkgrey', zorder = 1)
plt.axhline(y=7.853891634, xmin=0, xmax=1.2/3.5, linestyle = '--', color = 'darkgrey', zorder = 2)
plt.axhline(y=4.71238898, xmin=0, xmax=1.9/3.5, linestyle = '--', color = 'darkgrey', zorder = 3)
plt.axhline(y=3.141592654, xmin=0, xmax=2.3/3.5, linestyle = '--', color = 'darkgrey', zorder = 4)
plt.scatter(voltage_rough, retardance, label = 'Measured retardance at 660 nm', color = 'dodgerblue', s = 4, zorder = 5)
plt.scatter(voltage_specs[:116] , retardance_specs[:116], label = 'Nominal retardance at 635 nm', color = 'orchid', s = 4, zorder = 6)
#plt.plot(voltage_rough[8:], fitr)
#plt.plot(voltage_specs[9:], fitrspecs)
plt.plot(voltage, fitrprec)
plt.scatter(voltage, retardance_precise)
plt.xlabel("LCVR voltage (V)", fontsize = 14, labelpad=3)
plt.ylabel("Retardance (radians)", fontsize = 14, labelpad=3)
plt.yticks([0, math.pi/2, math.pi, 3*math.pi/2, 2*math.pi, 5*math.pi/2, 3*math.pi], ['$0$', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$', '$5\pi/2$', '$3\pi$'] ,size = 14)
plt.xticks(size = 14)
plt.xlim(xmin = 0, xmax = 3.5)
leg = plt.legend()
leg.get_frame().set_edgecolor('white')
# plt.savefig('LCVRretardance.pdf')

plt.show()
