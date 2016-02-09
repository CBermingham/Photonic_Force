import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
from scipy.optimize import curve_fit
import math

def harmonic_potential(x, spring_const):
	val = spring_const/2.0 * np.power(x, 2)
	return val

#Read in position data
displacement1 = []
f = open('/Volumes/LMF_Microscope/1-Data/2015/7_July/27_files/190915', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	displacement1.append(float(b[9]))

#Centre data around zero
mean_d1 = np.mean(displacement1)
displacement1 = [i-mean_d1 for i in displacement1]

mean=np.mean(displacement1)
ysq = [(i-mean)**2 for i in displacement1]
meansq = np.mean(ysq)
k = 1.38064852E-23*290/meansq
print "k from equipartition theorem =", k, "N/m"

#Find histogram bins and values
y_1, bins_1= np.histogram(displacement1, bins=np.arange(min(displacement1), max(displacement1) + 1E-9, 1E-9), normed=True)

#Set max value to be just more than 1 (so min value is just more than zero, just more
	#so the log doesn't produce an error)
y_1 = [i/max(y_1)+0.000000000001 for i in y_1]

#Find the potential 
V=[-math.log(i) for i in y_1]



#Put displacement data in nm and take off last bin edge
bins_1=[i*1E9 for i in bins_1]
bins_1 = bins_1[:-1]

popt1, pcov1 = curve_fit(harmonic_potential, bins_1, V)
print "k from potential fit =", popt1[0]*1.38064852E-5*290, "N/m"

addition = [i*0.02 for i in bins_1]

new_pot = [V[i]+addition[i] for i in range(0, len(V))]

k_sp=0.05
stiff_pot = [k_sp/2.0*i**2 for i in bins_1]
print "k for stiff cantilever", '%E' % (k_sp*1.38064852E-5*290), "N/m"

new_stiff_pot=[stiff_pot[i]+addition[i] for i in range(0, len(stiff_pot))]

#plot potential
plt.subplot(2,1,1)
plt.plot(bins_1, V)
plt.plot(bins_1, addition)
plt.plot(bins_1, new_pot)

plt.xlabel("Displacement / nm")
plt.ylabel("Potantial Energy / $k_BT$ J")
plt.ylim(ymin = -5, ymax = 10)

plt.subplot(2,1,2)
plt.plot(bins_1, stiff_pot)
plt.plot(bins_1, addition)
plt.plot(bins_1, new_stiff_pot)
plt.xlabel("Displacement / nm")
plt.ylabel("Potantial Energy / $k_BT$ J")
plt.ylim(ymin = -5, ymax = 10)

plt.savefig('190915_adding_potentials.pdf')
plt.show()
