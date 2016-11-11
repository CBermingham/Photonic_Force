import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit
import numpy as np
import math
import cmath
from numpy.lib.scimath import sqrt as csqrt

def linear_function(x, m, c):
	return m * x + c

def incident_angle(delta, wavelength, n):
	root = math.sqrt(((wavelength/(4*math.pi*delta))**2+1)/n**2)
	return np.arcsin(root)*180/math.pi

def ts_squared(theta_i, A):
	n=1.52
	theta_i = theta_i*math.pi/180.0
	cos_theta_t=np.sqrt(1-n**2*(np.sin(theta_i)**2)+0j)
	ts=abs(2*n*np.cos(theta_i)/(n*np.cos(theta_i)+cos_theta_t))
	return A*ts**2

def fit_data(filename, cutoff):
	z1 = []
	sum1 = []
	f = open(filename, 'rU')
	reader = csv.reader(f, None)
	for row in reader:
		z1.append(float(row[0]))
		sum1.append(float(row[1]))
	f.close()

	z1 = np.array(z1)
	sum1 = np.array(sum1)

	sum1 = [-i for i in sum1]

	#popt, pcov = curve_fit(linear_function, z1[1:cutoff], sum1[1:cutoff])
	popt, pcov = curve_fit(linear_function, z1, sum1)
	popt[0] = -popt[0]
	popt[1] = -popt[1]
	fit = [linear_function(i, popt[0], popt[1]) for i in z1]

	sum1 = [-i for i in sum1]

	I0 = np.exp(popt[1])
	delta = -1/popt[0]
	angle = incident_angle(delta*1E-9, 561E-9, 1.52)
	perr = np.sqrt(np.diag(pcov))
	errorI0 = perr[1]*I0

	print "I0 =", I0, "V, delta = ", delta, "nm, incident angle = ", angle

	return z1, sum1, fit, I0, delta, angle, errorI0


z1, sum1, fit1, I01, delta1, angle1, errorI01 = fit_data("/Users/Charlotte/Documents/PhD/Data/160323_140400.csv", 6)
z2, sum2, fit2, I02, delta2, angle2, errorI02 = fit_data("/Users/Charlotte/Documents/PhD/Data/160323_142408.csv", 15)
z3, sum3, fit3, I03, delta3, angle3, errorI03 = fit_data("/Users/Charlotte/Documents/PhD/Data/160323_143955.csv", 10)
z4, sum4, fit4, I04, delta4, angle4, errorI04 = fit_data("/Users/Charlotte/Documents/PhD/Data/160323_144616.csv", 8)
z5, sum5, fit5, I05, delta5, angle5, errorI05 = fit_data("/Users/Charlotte/Documents/PhD/Data/160323_145522.csv", 14)
z6, sum6, fit6, I06, delta6, angle6, errorI06 = fit_data("/Users/Charlotte/Documents/PhD/Data/160323_145942.csv", 7)
z7, sum7, fit7, I07, delta7, angle7, errorI07 = fit_data("/Users/Charlotte/Documents/PhD/Data/160323_143215.csv", 10)

# z1, sum1, fit1, I01, delta1, angle1, errorI01 = fit_data("/Users/Charlotte/Documents/PhD/Data/160324_133504.csv", 6)
# z2, sum2, fit2, I02, delta2, angle2, errorI02 = fit_data("/Users/Charlotte/Documents/PhD/Data/160324_130523.csv", 15)
# z3, sum3, fit3, I03, delta3, angle3, errorI03 = fit_data("/Users/Charlotte/Documents/PhD/Data/160324_132006.csv", 10)
# z4, sum4, fit4, I04, delta4, angle4, errorI04 = fit_data("/Users/Charlotte/Documents/PhD/Data/160324_132514.csv", 8)
# z5, sum5, fit5, I05, delta5, angle5, errorI05 = fit_data("/Users/Charlotte/Documents/PhD/Data/160324_132021.csv", 14)
# z6, sum6, fit6, I06, delta6, angle6, errorI06 = fit_data("/Users/Charlotte/Documents/PhD/Data/160324_133504.csv", 7)
# z7, sum7, fit7, I07, delta7, angle7, errorI07 = fit_data("/Users/Charlotte/Documents/PhD/Data/160324_133958.csv", 10)


angles = np.array([angle1, angle2, angle3, angle4, angle5, angle6, angle7])
print angles
I0 = np.array([I01, I02, I03, I04, I05, I06, I07])
print I0
errors = np.array([errorI01, errorI02, errorI03, errorI04, errorI05, errorI06, errorI07])


popt1, pcov1 = curve_fit(linear_function, angles, I0)
xvalues = [angles[0]+(angles[-2]-angles[0])/10*i for i in range(0, 11)]
fitnew = [linear_function(i, popt1[0], popt1[1]) for i in xvalues]

# plt.scatter(z1, sum1, color = 'r', s = 3, label = "%.1f$\degree$" % angle1)
# plt.plot(z1, fit1, color = 'r')
plt.scatter(z2, sum2, color = 'r', s = 5)
# plt.plot(z2, fit2, color = 'r')
plt.scatter(z7, sum7, color = 'darkorange', s = 5)
# plt.plot(z7, fit7, color = 'darkorange')
plt.scatter(z3, sum3, color = 'gold', s = 5)
# plt.plot(z3, fit3, color = 'gold')
plt.scatter(z4, sum4, color = 'g', s = 5)
# plt.plot(z4, fit4, color = 'g')
plt.scatter(z5, sum5, color = 'b', s = 5)
# plt.plot(z5, fit5, color  = 'b')
plt.scatter(z6, sum6, color = 'purple', s = 5)
# plt.plot(z6, fit6, color = 'purple')
# plt.legend()
# plt.xlabel("Distance above surface / nm", fontsize = 14)
# plt.ylabel("ln(Intensity)", fontsize = 14)
# plt.xlim(xmin = 0)
# plt.xticks(size = 14)
# plt.yticks(size = 14)
# plt.savefig('multiple_scattering_with_fit_to_all.pdf')
# # plt.savefig("Multiple_scattering.pdf")
# plt.show()

plt.plot(z2, sum2, color = 'r', label = "%.1f$\degree$" % angle2)
plt.plot(z2, fit2, color = 'r', linestyle = '--')
plt.plot(z7, sum7, color = 'darkorange', label = "%.1f$\degree$" % angle7)
plt.plot(z7, fit7, color = 'darkorange', linestyle = '--')
plt.plot(z3, sum3, color = 'gold', label = "%.1f$\degree$" % angle3)
plt.plot(z3, fit3, color = 'gold', linestyle = '--')
plt.plot(z4, sum4, color = 'g', label = "%.1f$\degree$" % angle4)
plt.plot(z4, fit4, color = 'g', linestyle = '--')
plt.plot(z5, sum5, color = 'b', label = "%.1f$\degree$" % angle5)
plt.plot(z5, fit5, color  = 'b', linestyle = '--')
plt.plot(z6, sum6, color = 'purple', label = "%.1f$\degree$" % angle6)
plt.plot(z6, fit6, color = 'purple', linestyle = '--')
plt.legend()
plt.xlabel("Distance above surface / nm", fontsize = 14)
plt.ylabel("ln(Intensity)", fontsize = 14)
plt.xlim(xmin = 0)
plt.xticks(size = 14)
plt.yticks(size = 14)
# plt.savefig('multiple_scattering_with_fit_to_all.pdf')
#plt.savefig("Multiple_scattering_ITO.pdf")
plt.show()

# plt.errorbar(angles[1:], I0[1:], yerr = errors[1:],  color = 'm', fmt='o')
# plt.plot(xvalues, fitnew, color = 'm', linestyle = '--')
# plt.ylabel("I(z=0)", fontsize = 14)
# plt.xlabel("Angle of incidence ($\degree$)", fontsize = 14)
# plt.xticks(size = 14)
# plt.yticks(size = 14)
# plt.savefig("angle_and_I0.pdf")

plt.figure(tight_layout = True)
norm_I_2 = [np.exp(sum2[k])/(I02*np.exp(-z2[k]/delta2)) for k in range(0, len(sum2))]
plt.plot(z2, norm_I_2, color = 'r', label = "%.1f$\degree$" % angle2, zorder = 0)
norm_I_7 = [np.exp(sum7[k])/(I07*np.exp(-z7[k]/delta7)) for k in range(0, len(sum7))]
plt.plot(z7, norm_I_7, color = 'darkorange', label = "%.1f$\degree$" % angle7, zorder = 1)
norm_I_3 = [np.exp(sum3[k])/(I03*np.exp(-z3[k]/delta3)) for k in range(0, len(sum3))]
plt.plot(z3, norm_I_3, color = 'gold', label = "%.1f$\degree$" % angle3, zorder = 2)
norm_I_4 = [np.exp(sum4[k])/(I04*np.exp(-z4[k]/delta4)) for k in range(0, len(sum4))]
plt.plot(z4, norm_I_4, color = 'g', label = "%.1f$\degree$" % angle4, zorder = 3)
norm_I_5 = [np.exp(sum5[k])/(I05*np.exp(-z5[k]/delta5)) for k in range(0, len(sum5))]
plt.plot(z5, norm_I_5, color = 'b', label = "%.1f$\degree$" % angle5, zorder = 4)
norm_I_6 = [np.exp(sum6[k])/(I06*np.exp(-z6[k]/delta6)) for k in range(0, len(sum6))]
plt.plot(z6, norm_I_6, color = 'indigo', label = "%.1f$\degree$" % angle6, zorder = 5)


plt.xlabel("z (nm)", size = 24)
plt.ylabel("Normlised intensity", size = 24)
plt.xlim(xmin = 0)
plt.xticks(size = 24)
plt.yticks(size = 24)
plt.savefig("normalised_intensity.pdf")

plt.show()

