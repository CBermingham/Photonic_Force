import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit
import numpy as np
import math

def linear_function(x, m, c):
	return m * x + c

def incident_angle(delta, wavelength, n):
	root = math.sqrt(((wavelength/(4*math.pi*delta))+1)/n**2)
	return np.arcsin(root)*180/math.pi

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

	popt, pcov = curve_fit(linear_function, z1[1:cutoff], sum1[1:cutoff])
	popt[0] = -popt[0]
	popt[1] = -popt[1]
	fit = [linear_function(i, popt[0], popt[1]) for i in z1[1:]]

	sum1 = [-i for i in sum1]

	I0 = np.exp(popt[1])
	delta = -1/popt[0]
	angle = incident_angle(delta*1E-9, 561E-9, 1.52)

	print "I0 =", I0, "V, delta = ", delta, "nm, incident angle = ", angle

	return z1, sum1, fit, I0, delta, angle


z1, sum1, fit1, I01, delta1, angle1 = fit_data("/Users/Charlotte/Documents/PhD/Data/160323_140400.csv", 6)
z2, sum2, fit2, I02, delta2, angle2 = fit_data("/Users/Charlotte/Documents/PhD/Data/160323_142408.csv", 15)
z3, sum3, fit3, I03, delta3, angle3 = fit_data("/Users/Charlotte/Documents/PhD/Data/160323_143955.csv", 10)
z4, sum4, fit4, I04, delta4, angle4 = fit_data("/Users/Charlotte/Documents/PhD/Data/160323_144616.csv", 8)
z5, sum5, fit5, I05, delta5, angle5 = fit_data("/Users/Charlotte/Documents/PhD/Data/160323_145522.csv", 14)
z6, sum6, fit6, I06, delta6, angle6 = fit_data("/Users/Charlotte/Documents/PhD/Data/160323_145942.csv", 7)
z7, sum7, fit7, I03, delta7, angle7 = fit_data("/Users/Charlotte/Documents/PhD/Data/160323_143215.csv", 10)

#plt.scatter(z1, sum1, color = 'r', s = 3, label = "%.1f$\degree$" % angle1)
#plt.plot(z1, fit1, color = 'r')
plt.scatter(z2[1:], sum2[1:], color = 'r', s = 3, label = "%.1f$\degree$" % angle2)
plt.plot(z2[1:], fit2, color = 'r')
plt.scatter(z7[1:], sum7[1:], color = 'darkorange', s = 3, label = "%.1f$\degree$" % angle7)
plt.plot(z7[1:], fit7, color = 'darkorange')
plt.scatter(z3[1:], sum3[1:], color = 'gold', s = 3, label = "%.1f$\degree$" % angle3)
plt.plot(z3[1:], fit3, color = 'gold')
plt.scatter(z4[1:], sum4[1:], color = 'g', s = 3, label = "%.1f$\degree$" % angle4)
plt.plot(z4[1:], fit4, color = 'g')
plt.scatter(z5[1:], sum5[1:], color = 'b', s = 3, label = "%.1f$\degree$" % angle5)
plt.plot(z5[1:], fit5, color  = 'b')
plt.scatter(z6[1:], sum6[1:], color = 'purple', s = 3, label = "%.1f$\degree$" % angle6)
plt.plot(z6[1:], fit6, color = 'purple')
plt.legend()
plt.xlabel("Distance above surface / nm", fontsize = 14)
plt.ylabel("ln(Intensity)", fontsize = 14)
plt.xlim(xmin = 0)
plt.xticks(size = 14)
plt.yticks(size = 14)
plt.savefig("Multiple_scattering.pdf")


plt.show()

