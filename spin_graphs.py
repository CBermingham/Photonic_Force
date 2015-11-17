import csv
import matplotlib.pyplot as plt
import numpy as np

angle = []
odd180 = []
even180 = []
error180 = []
odd0 = []
even0 = []
error0 = []

with open('spin_data.csv', 'rb') as f:
	reader = csv.reader(f, None)
	for row in reader:
		angle.append(float(row[0]))
		odd180.append(float(row[1]))
		even180.append(float(row[2]))
		error180.append(float(row[3]))
		odd0.append(float(row[4]))
		even0.append(float(row[4]))
		error0.append(float(row[4]))

plt.errorbar(angle, odd180, error180, fmt='o')
plt.xlabel('QWP angle (degrees)')
plt.ylabel('Force (pN)')
plt.show()