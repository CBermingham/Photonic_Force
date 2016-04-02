import matplotlib.pyplot as plt
import csv
import numpy as np
import os
import csv

path = '23_saved/'

z_ave = []
sum_sig_ave = []
z_error = []
sum_error = []
directory = sorted(os.listdir(path))

for filename in directory:
	z = []
	sum_sig = []
	with open(path + '/' + filename) as f:
		for line in f:
			b = line.split()
	    	sum_sig.append(float(b[7]))
	    	z.append(float(b[8]))
		print z
	z_ave.append(np.mean(z))
	sum_sig_ave.append(np.mean(sum_sig))
	z_error.append(np.std(z, dtype=np.float64))
	sum_error.append(np.std(sum_sig))



data = zip(z_ave, z_error, sum_sig_ave, sum_error)

writer = csv.writer(open('140400zandsum.csv', "wb"))
for row in data:
    writer.writerow(row)

plt.plot(z_ave, sum_sig_ave)
plt.show()
