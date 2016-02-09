import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
from scipy.optimize import curve_fit
import math


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

#plot histogram
plt.subplot(2,1,1)
plt.bar(bins_1, y_1)
plt.ylabel("Probability density")

#plot potential
plt.subplot(2,1,2)
plt.plot(bins_1, V)
plt.xlabel("Displacement / nm")
plt.ylabel("Potantial Energy / $k_BT$ J")
plt.ylim(ymin = 0, ymax = 10)
#plt.savefig('190915.pdf')
plt.show()
