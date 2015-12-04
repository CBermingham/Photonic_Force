import matplotlib.pyplot as plt
import csv

angle = []
data = []
error = []

with open('example_data.csv', 'rb') as f:
	reader = csv.reader(f, None)
	for row in reader:
		angle.append(float(row[0]))
		data.append(float(row[1]))
		error.append(float(row[2]))


plt.scatter(angle, data, color='r', s=25, label = 'experiment')
plt.xlabel('Quarter waveplate orientation $\phi$ ($\degree$)')
plt.ylabel('Total froce F($\phi$)-F(0) (pN)')
plt.legend(loc=9)
plt.show()