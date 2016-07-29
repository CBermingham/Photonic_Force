import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.optimize import curve_fit

def linear_function(x, m, c):
	return m * x + c

z = []
z_error = []
sumsig = []
sumsig_error = []
ln_sum = []
ln_sum_error = []
ln_d = []
ln_d_error = []
d = []
d_error = []

f = open("160401p2data.csv", 'rU')
reader = csv.reader(f, None)
for row in reader:
	z.append(float(row[0]))
	z_error.append(float(row[1]))
	sumsig.append(float(row[2]))
	sumsig_error.append(float(row[3]))
	ln_sum.append(float(row[4]))
	ln_sum_error.append(float(row[5]))
	ln_d.append(float(row[6]))
	ln_d_error.append(float(row[7]))
	d.append(float(row[8]))
	d_error.append(float(row[9]))
f.close()

z3 = []
z_error3 = []
sumsig3 = []
sumsig_error3 = []
ln_sum3 = []
ln_sum_error3 = []
ln_d3 = []
ln_d_error3 = []
d3 = []
d_error3 = []

f = open("160401p3data.csv", 'rU')
reader = csv.reader(f, None)
for row in reader:
	z3.append(float(row[0]))
	z_error3.append(float(row[1]))
	sumsig3.append(float(row[2]))
	sumsig_error3.append(float(row[3]))
	ln_sum3.append(float(row[4]))
	ln_sum_error3.append(float(row[5]))
	ln_d3.append(float(row[6]))
	ln_d_error3.append(float(row[7]))
	d3.append(float(row[8]))
	d_error3.append(float(row[9]))
f.close()

z = np.array(z)
ln_d = np.array(ln_d)

popt, pcov = curve_fit(linear_function, z, ln_d)
fit = [linear_function(i, popt[0], popt[1]) for i in z]
z_values = [z[0]+((z[-1]-z[0])/1000)*i for i in range(0, 1000)]
print z
print z_values[0]
print z_values[-1]
fitexp = [-np.exp(linear_function(i, popt[0], popt[1])) for i in z_values]

norm_F = [d[i]/-np.exp(linear_function(z[i], popt[0], popt[1])) for i in range(0, len(z))]

plt.errorbar(z, d, yerr = d_error, fmt='o', markersize = 3, color = 'darkorchid')
#plt.errorbar(z3, d3, yerr = d_error3, fmt='o', markersize = 3, color = 'darkorchid')
plt.xlabel("Height above surface (nm)", fontsize = 14)
plt.ylabel("Cantilever deflection (nm)", fontsize = 14)
plt.plot(z_values, fitexp, color = 'darkorchid')
plt.savefig('direction_mvt.pdf')
plt.show()


# plt.plot(z, norm_F)


# plt.errorbar(z, ln_d, yerr = ln_d_error, fmt='o', markersize = 3, color = 'darkturquoise', zorder = 1)
# plt.plot(z, fit, color = 'darkturquoise', zorder = 0)
# #plt.errorbar(z3, ln_d3, yerr = ln_d_error3, fmt='o', markersize = 3, color = 'darkorchid')
# plt.xlabel("Height above surface (nm)", fontsize = 14)
# plt.ylabel("ln(deflection magnitude)", fontsize = 14)
# plt.savefig('ln_magnitude_mvt.pdf')



# norm_F = [np.exp(sumsig3[k])/(popt[0]*np.exp(-z[k]/popt[1])) for k in range(0, len(sumsig3))]
# plt.plot(z, norm_F)
# plt.show()


# plt.show()

#fig, ax1 = plt.subplots()
# lns1 = ax1.errorbar(z, ln_sum, yerr = ln_sum_error, fmt='o', markersize = 3, color = 'r', label = "ln(SUM signal)")
# ax1.set_xlabel('Height above surface (nm)', fontsize = 14)
# ax1.set_ylabel('ln(Cantilever deflection)', fontsize = 14)
# plt.xticks(size = 14)
# plt.yticks(size = 14)

# ax2 = ax1.twinx()
# lns2 = ax2.errorbar(z, ln_d, yerr = ln_d_error, fmt='o', markersize = 3, color = 'b', label = "ln(Cantilever deflection)")
# ax2.set_ylabel('ln(SUM signal)', size = 14)
# plt.yticks(size = 14)

# lines, labels = ax1.get_legend_handles_labels()
# lines2, labels2 = ax2.get_legend_handles_labels()
# ax2.legend(lines + lines2, labels + labels2, loc=0)
















