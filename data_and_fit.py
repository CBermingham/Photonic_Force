import cmath
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit
import numpy as np

d = np.pi / 4.0
a = 54.6*np.pi/180.0
n1 = 1.5
lamda = 660E-9
k = 2*np.pi/lamda
kz = k*n1*np.sin(a)
kappa = np.sqrt(kz**2 - k**2)
P = np.arcsin(kappa/k)
Ts = 2*n1*np.cos(a)/(n1*np.cos(a) + 1j*np.sinh(P))
Tp = 2* n1*np.cos(a)/(np.cos(a) + 1j*n1*np.sinh(P))

def sigma(Q, A):
	m1 = (-1j* np.cos(d) - np.sin(d) * np.cos(2*Q))/(np.sin(d) * np.sin(2*Q));
	m = (Ts/Tp)*m1
	sigma= A*((2*m.imag)/(1 + abs(m)**2))
	return sigma*np.sinh(P)/np.cosh(P)

def chi(Q, B):
	m1 = (-1j* np.cos(d) - np.sin(d) * np.cos(2*Q))/(np.sin(d) * np.sin(2*Q));
	m = (Ts/Tp)*m1
	chi=B*(2*m.real/(1 + abs(m)**2))
	return -chi*np.sinh(P)/np.cosh(P)

def odd(Q, A, B):
	return sigma(Q, A)+chi(Q, B)

def even(Q, C,D):
	m1 = (-1j* np.cos(d) - np.sin(d) * np.cos(2*Q))/(np.sin(d) * np.sin(2*Q));
	m = (Ts/Tp)*m1
	tau = C*(1 - abs(m)**2)/(1 + abs(m)**2)
	return np.cosh(P)+ tau*np.sinh(P)**2/np.cosh(P)+D

def total_fit(Q, A, B, C, D):
	m1 = (-1j* np.cos(d) - np.sin(d) * np.cos(2*Q))/(np.sin(d) * np.sin(2*Q));
	m = (Ts/Tp)*m1
	tau = C*(1 - abs(m)**2)/(1 + abs(m)**2)
	odd = A*((2*m.imag)/(1 + abs(m)**2)) + B*(2*m.real/(1 + abs(m)**2))
	even = np.cosh(P)+ tau*np.sinh(P)**2/np.cosh(P)+D
	return odd+even

def fit_data(filename):
	angle = []
	data = []
	with open(filename, 'rb') as f:
		reader = csv.reader(f, None)
		for row in reader:
			angle.append(float(row[0]))
			data.append(float(row[1]))

	angle2 = angle[:9]
	for i in angle[10:]:
		angle2.append(i)

	data2 = data[:9]
	for i in data[10:]:
		data2.append(i)

	angle2 = np.asarray(angle2)
	data2 = np.asarray(data2)

	popt, pcov = curve_fit(odd, angle2, data2)

	x =range(-90, 0)
	for i in range(1, 90):
		x.append(i)

	x = [i*np.pi/180.0 for i in x]
	fit = [odd(i, popt[0], popt[1]) for i in x]
	fit_sigma = [sigma(i, popt[0]) for i in x]
	fit_chi = [chi(i, popt[1]) for i in x]

	return angle, data, x, fit, popt, fit_sigma, fit_chi

def fit_data_even(filename):
	angle = []
	data = []

	with open(filename, 'rb') as f:
		reader = csv.reader(f, None)
		for row in reader:
			angle.append(float(row[0]))
			data.append(float(row[1]))

	angle2 = angle[:9]
	for i in angle[10:]:
		angle2.append(i)

	data2 = data[:9]
	for i in data[10:]:
		data2.append(i)

	angle2 = np.asarray(angle2)
	data2 = np.asarray(data2)

	popt, pcov = curve_fit(even, angle2, data2)

	x =range(-90, 0)
	for i in range(1, 90):
		x.append(i)

	x = [i*np.pi/180.0 for i in x]
	fit = [even(i, popt[0], popt[1]) for i in x]
	return angle, data, x, fit, popt

def fit_data_total(filename):
	angle = []
	data = []

	with open(filename, 'rb') as f:
		reader = csv.reader(f, None)
		for row in reader:
			angle.append(float(row[0]))
			data.append(float(row[1]))

	angle2 = angle[:9]
	for i in angle[10:]:
		angle2.append(i)

	data2 = data[:9]
	for i in data[10:]:
		data2.append(i)

	angle2 = np.asarray(angle2)
	data2 = np.asarray(data2)

	popt, pcov = curve_fit(total_fit, angle2, data2)

	x =range(-90, 0)
	for i in range(1, 90):
		x.append(i)

	x = [i*np.pi/180.0 for i in x]
	fit = [total_fit(i, popt[0], popt[1], popt[2], popt[3]) for i in x]
	return angle, data, x, fit, popt

angle01odd, data01odd, x01odd, fit01odd, popt01odd, fit_sigma01odd, fit_chi01odd = fit_data('data01odd.csv')
angle02odd, data02odd, x02odd, fit02odd, popt02odd, fit_sigma02odd, fit_chi02odd = fit_data('data02odd.csv')
angle03odd, data03odd, x03odd, fit03odd, popt03odd, fit_sigma03odd, fit_chi03odd = fit_data('data03odd.csv')
angle1801odd, data1801odd, x1801odd, fit1801odd, popt1801odd, fit_sigma1801odd, fit_chi1801odd = fit_data('data1801odd.csv')
angle1802odd, data1802odd, x1802odd, fit1802odd, popt1802odd, fit_sigma1802odd, fit_chi1802odd = fit_data('data1802odd.csv')
angle1803odd, data1803odd, x1803odd, fit1803odd, popt1803odd, fit_sigma1803odd, fit_chi1803odd = fit_data('data1803odd.csv')

angle1801even, data1801even, x1801even, fit1801even, popt1801even = fit_data_even('data1801even.csv')
angle01even, data01even, x01even, fit01even, popt01even = fit_data_even('data01even.csv')
angle1802even, data1802even, x1802even, fit1802even, popt1802even = fit_data_even('data1802even.csv')
angle02even, data02even, x02even, fit02even, popt02even = fit_data_even('data02even.csv')
angle1803even, data1803even, x1803even, fit1803even, popt1803even = fit_data_even('data1803even.csv')
angle03even, data03even, x03even, fit03even, popt03even = fit_data_even('data03even.csv')

angle01, data01, x01, fit01, popt01 = fit_data_total('data01.csv')
angle02, data02, x02, fit02, popt02 = fit_data_total('data02.csv')
angle03, data03, x03, fit03, popt03 = fit_data_total('data03.csv')
angle1801, data1801, x1801, fit1801, popt1801 = fit_data_total('data1801.csv')
angle1802, data1802, x1802, fit1802, popt1802 = fit_data_total('data1802.csv')
angle1803, data1803, x1803, fit1803, popt1803 = fit_data_total('data1803.csv')

angle01odd = [i*180/np.pi for i in angle01odd]
x01odd = [i*180/np.pi for i in x01odd]

p1 = plt.scatter(angle01odd, data01odd, color ='r', label = "experiment")
p2 = plt.plot(x01odd, fit01odd, color ='r', label ="fit")
p3 = plt.plot(x01odd, fit_sigma01odd, 'r--', label = '$\sigma$ contribution')
p4 = plt.plot(x01odd, fit_chi01odd, 'r:', label = '$\chi$ contribution')
plt.xlabel('Quarter waveplate orientation $\phi$ ($\degree$)')
plt.legend([p2, p1], ["line 2", "line 1"])
# plt.scatter(angle02odd, data02odd, color = 'g')
# plt.plot(x02odd, fit02odd, color = 'g')
# plt.scatter(angle03odd, data03odd, color = 'b')
# plt.plot(x03odd, fit03odd, color = 'b')

# plt.scatter(angle1801odd, data1801odd, color = 'g')
# plt.plot(x1801odd, fit1801odd, label = '1801odd', color = 'g')
# plt.scatter(angle1802odd, data1802odd, color = 'g')
# plt.plot(x1802odd, fit1802odd, label = '1802odd', color = 'g')
# plt.scatter(angle1803odd, data1803odd, color = 'g')
# plt.plot(x1803odd, fit1803odd, label = '1803odd', color = 'g')

# plt.scatter(angle01even, data01even, color = 'b')
# plt.plot(x01even, fit01even, label = '01even', color = 'b')
# plt.scatter(angle02even, data02even, color = 'b')
# plt.plot(x02even, fit02even, label = '01even', color = 'b')
# plt.scatter(angle03even, data03even, color = 'b')
# plt.plot(x03even, fit03even, label = '01even', color = 'b')

# plt.scatter(angle1801even, data1801even, color = 'b')
# plt.plot(x1801even, fit1801even, label = '01even', color = 'b')
# plt.scatter(angle1802even, data1802even, color = 'b')
# plt.plot(x1802even, fit1802even, label = '01even', color = 'b')
# plt.scatter(angle1803even, data1803even, color = 'b')
# plt.plot(x1803even, fit1803even, label = '01even', color = 'b')

# plt.scatter(angle01, data01, color = 'r')
# plt.plot(x01, fit01, label = '01', color = 'r')
# plt.scatter(angle02, data02, color = 'r')
# plt.plot(x02, fit02, label = '02', color = 'r')
# plt.scatter(angle03, data03, color = 'r')
# plt.plot(x03, fit03, label = '03', color = 'r')

# plt.scatter(angle1801, data1801, color = 'r')
# plt.plot(x1801, fit1801, label = '01', color = 'r')
# plt.scatter(angle1802, data1802, color = 'r')
# plt.plot(x1802, fit1802, label = '02', color = 'r')
# plt.scatter(angle1803, data1803, color = 'r')
# plt.plot(x1803, fit1803, label = '03', color = 'r')

plt.show()


