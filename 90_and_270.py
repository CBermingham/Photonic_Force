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

def even(Q, C,D):
	m1 = (-1j* np.cos(d) - np.sin(d) * np.cos(2*Q))/(np.sin(d) * np.sin(2*Q));
	m = (Ts/Tp)*m1
	tau = C*(1 - abs(m)**2)/(1 + abs(m)**2)
	return np.cosh(P)+ tau*np.sinh(P)**2/np.cosh(P)+D

def fit_data_even(filename):
	angle = []
	data = []
	error = []

	with open(filename, 'rb') as f:
		reader = csv.reader(f, None)
		for row in reader:
			angle.append(float(row[0]))
			data.append(float(row[1]))
			error.append(float(row[2]))

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
	return angle, data, x, fit, popt, error

def even_plot(angle, data, x, fit, error, fig_name, max_y):
	angle= [i*180/np.pi for i in angle]
	x = [i*180/np.pi for i in x]
	p1 = plt.errorbar(angle, data, yerr=error, fmt='o', color ='teal', markersize=3)
	p2, = plt.plot(x, fit, color ='teal')
	plt.xlabel('Quarter waveplate orientation $\phi$ ($\degree$)', labelpad=8)
	plt.ylabel('Force (pN)')
	if '270' in fig_name:
		leg1 = plt.legend([p1, p2], ["experiment", "fit"], loc=3, framealpha=0)
		leg1.get_frame().set_edgecolor('white')
		plt.gca().add_artist(leg1)
		plt.ylim(ymin = 0)
	else:
		leg2 = plt.legend([p1, p2], ["experiment", "fit"], loc=2, framealpha=0)
		leg2.get_frame().set_edgecolor('white')
		plt.gca().add_artist(leg2)
	fig = plt.gcf()
	fig.set_size_inches(8, 5)
	plt.xticks(np.arange(-100, 110, 20))
	plt.ylim(ymax = max_y)
	plt.savefig(fig_name)
	plt.clf()

def combined_plot(angle, data1, data2, x, fit1, fit2, error1, error2, fig_name, max_y):
	angle= [i*180/np.pi for i in angle]
	x = [i*180/np.pi for i in x]
	p1 = plt.errorbar(angle, data1, yerr=error1, fmt='o', color ='deepskyblue', markersize=3)
	p2, = plt.plot(x, fit1, color ='deepskyblue')
	p3 = plt.errorbar(angle, data2, yerr=error2, fmt='o', color ='indigo', markersize=3)
	p4, = plt.plot(x, fit2, color ='indigo')
	plt.xlabel('Quarter waveplate orientation $\phi$ ($\degree$)', labelpad=8)
	plt.ylabel('Force (pN)')
	leg1 = plt.legend([p3, p4, p1, p2], ["90$\degree$ experiment", "90$\degree$ fit", "270$\degree$ experiment", "270$\degree$ fit"], loc=5, framealpha=0)
	leg1.get_frame().set_edgecolor('white')
	plt.gca().add_artist(leg1)
	fig = plt.gcf()
	fig.set_size_inches(8, 5)
	plt.xticks(np.arange(-100, 110, 20))
	plt.ylim(ymax = max_y)
	plt.savefig(fig_name)
	plt.clf()

angle901even, data901even, x901even, fit901even, popt901even, error901 = fit_data_even('901.csv')
angle902even, data902even, x902even, fit902even, popt902even, error902 = fit_data_even('902.csv')
angle903even, data903even, x903even, fit903even, popt903even, error903 = fit_data_even('903.csv')

even_plot(angle901even, data901even, x901even, fit901even, error901, '901even.pdf', 0)
even_plot(angle902even, data902even, x902even, fit902even, error902, '902even.pdf', 0)
even_plot(angle903even, data903even, x903even, fit903even, error903, '903even.pdf', 0)

angle2701even, data2701even, x2701even, fit2701even, popt2701even, error2701 = fit_data_even('2701.csv')
angle2702even, data2702even, x2702even, fit2702even, popt2702even, error2702 = fit_data_even('2702.csv')
angle2703even, data2703even, x2703even, fit2703even, popt2703even, error2703 = fit_data_even('2703.csv')

even_plot(angle2701even, data2701even, x2701even, fit2701even, error2701, '2701even.pdf', 2)
even_plot(angle2702even, data2702even, x2702even, fit2702even, error2702, '2702even.pdf', 2)
even_plot(angle2703even, data2703even, x2703even, fit2703even, error2703, '2703even.pdf', 2)

combined_plot(angle2702even, data903even, data2702even, x2702even, fit903even, fit2702even, error903, error2702, '903_and_2702even.pdf', 2)









