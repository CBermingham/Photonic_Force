import matplotlib.pyplot as plt
import csv

frequency0 = []
amp0 = []
phase0 = []
frequency1 = []
amp1 = []
phase1 = []

with open('amp_phase.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, None)
	next(reader, None)
	for row in reader:
		frequency0.append(float(row[0]))
		amp0.append(float(row[5]))
		phase0.append(float(row[6]))
		frequency1.append(float(row[11]))
		amp1.append(float(row[16]))
		phase1.append(float(row[17]))

csvfile.close()

fig = plt.figure(figsize=(11, 8))

ax1 = plt.subplot(211)
ax1.plot(frequency0, amp0, label = 'Cantilever oriented 0 degrees')
ax1.plot(frequency1, amp1, label = 'Cantilever oriented 180 degrees')
ax1.legend()
plt.ylabel('Amplitude of oscillation / nm')
plt.hlines(90, 0, 10000, linestyles = 'dashed')
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')
plt.xscale('log')


ax2 = plt.subplot(212, sharex=ax1)
ax2.plot(frequency0, phase0, label = 'Oriented 0 degrees')
ax2.plot(frequency1, phase1, label = 'Oriented 180 degrees')
plt.xlabel('Frequency / Hz')
plt.ylabel('Phase / Degrees')

plt.ylim(ymin = -200, ymax = 200)
plt.axhline(y=90, color = 'k', linestyle = 'dashed')
plt.axhline(y=-90, color = 'k', linestyle = 'dashed')
ax2.yaxis.set_ticks_position('left')
ax2.xaxis.set_ticks_position('bottom')

plt.setp(ax1.get_xticklabels(), visible=False)
plt.subplots_adjust(hspace=0.05)

plt.show()


