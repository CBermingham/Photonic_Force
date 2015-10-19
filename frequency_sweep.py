import matplotlib.pyplot as plt
import numpy as np
import csv
import os

time = []
amp = []
phase = []
voltage = []

path = '160342'
dirs = os.listdir(path)

for filename in dirs:
	f = open(path + '/' + filename, 'rU')
	lines=f.readlines()
	f.close()
	for l in lines:
		b = l.split()
		amp.append(float(b[3]))

start = int(round(64000 * 4.4685))
step = int(round(((1 / 0.03) / 300) * 64000))
#step = int(round(0.1 * 64000))

start_freq = 9.6
end_freq = 3609
freq_step = (end_freq - start_freq) / 299
#freq_step = 100

frequency = []
signal = []

for i in range (0, 300):
	frequency.append(start_freq + i * freq_step)
	signal.append(np.mean(amp[start - step + (step * i):start + (step*i)]))

rows = zip(frequency, signal)
writer = csv.writer(open("160342.csv", "wb"))
writer.writerow(["Frequency / Hz", "Signal"])
for row in rows:
	writer.writerow(row)

plt.plot(frequency, signal)
plt.xlabel("Frequency / Hz")
plt.ylabel("Signal strength / V")
#plt.yscale('log')
#plt.xscale('log')
plt.show()