import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def straight_line(x, m, c):
	val = m * x + c
	return val

x = range(10, 70, 10)
print x

y = [6.3, 14.1, 22.2, 28.9, 36, 43.1]
yerror = [0.6, 0.7, 0.6, 1.1, 0.7, 0.6]

popt, pcov = curve_fit(straight_line, x, y)
fit = [popt[0] * i + popt[1] for i in x]

print popt[0]

fig = plt.figure()
plt.errorbar(x, y, yerr = yerror, fmt='o')
plt.plot(x, fit)
plt.xlabel('Driving laser power at source / mW')
plt.ylabel('Cantilever deflection / nm')
plt.xlim(xmax = 70)

plt.show()