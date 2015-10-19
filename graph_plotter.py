import matplotlib.pyplot as plt
import csv

frequency1 = []
frequency2 = []
frequency3 = []
frequency4 = []
signal1 = []
signal2 = []
signal3 = []
signal4 = []


with open('155323corrected.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, None)
	next(reader, None)
	for row in reader:
		frequency1.append(float(row[0]))
		signal1.append(float(row[1]))
csvfile.close()

with open('155533.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, None)
	next(reader, None)
	for row in reader:
		frequency2.append(float(row[0]))
		signal2.append(float(row[1]))
csvfile.close()

with open('122905.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, None)
	next(reader, None)
	for row in reader:
		frequency3.append(float(row[0]))
		signal3.append(float(row[1]))
csvfile.close()

with open('123004.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, None)
	next(reader, None)
	for row in reader:
		frequency4.append(float(row[0]))
		signal4.append(float(row[1]))
csvfile.close()

#	phase.append(float(b[9]))
#	amplitude.append(float(b[2]))




#psd3 = [i *0.2 for i in psd3]

#phase = [i * 1E9 for i in phase]
#time = [i - time[0] for i in time]

#time2 = []
#phase2 = []
#amp2 = []

#f = open('touch_amp_phase', 'rU')
#lines=f.readlines()
#f.close()
#for l in lines:
#	b = l.split()
#	time2.append(float(b[0]))
#	phase2.append(float(b[1]))
#	amp2.append(float(b[3]))

#amp2 = [5E-4 * i *378 for i in amp2]

#time2 = [i - time2[0] for i in time2]

#f1=plt.figure("Graph")
#plt.plot(time, amplitude, label='Amplitude')
#plt.plot(time, phase, label='Phase')
#plt.xlabel("Time / s", fontsize=18)
#plt.ylabel("Displacement from initial position / nm", fontsize=18)
#plt.legend()
#plt.show()

#fig, ax1 = plt.subplots()
#ax1.plot(time, phase, 'b')
#ax1.set_xlabel('Time / s')
#ax1.set_ylabel('Position / nm (blue)')
#plt.xlim(xmin = 4, xmax = 4.3)

#ax2 = ax1.twinx()
#ax2.plot(time2, phase2, 'r')
#ax2.set_ylabel('sine of oscillation phase (red)')
#plt.xlim(xmin = 4, xmax = 4.3)

#ax3 = ax1.twinx()
#ax2.plot(time2, amp2, 'g', label = 'Amplitude')
#ax2.set_ylabel('Amplitude')
#plt.ylim(ymin = -1, ymax = 1)


fig = plt.figure(figsize=(15, 8))
ax1 = plt.subplot(211)
plt.plot(frequency1, signal1, label = 'Drive response')
plt.plot(frequency2, signal2, label = 'Thermal background')
plt.legend(bbox_to_anchor=(0.55, 1.02, 0.45, .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
plt.annotate('(a)', (0.965, 0.83), textcoords='axes fraction', size=16)
plt.tick_params(axis='y', left = 'on', right='off')


ax2 = plt.subplot(212, sharex = ax1)
plt.plot(frequency3, signal3, label = 'Drive response')
plt.plot(frequency4, signal4, label = 'Thermal Background')
plt.annotate('(b)', (0.965, 0.83), textcoords='axes fraction', size=16)
plt.tick_params(axis='y', left = 'on', right='off')

#plt.plot(frequency1, signal1, label = 'Optical Drive')
#plt.plot(frequency2, signal2, label = 'Background')
#plt.plot(time, fit)
#plt.plot(time2, amp2)
#plt.plot(time2, phase2)
plt.xlabel("Frequency / Hz")
fig.text(0.02, 0.5, 'Signal / V', ha='center', va='center', rotation='vertical')
#plt.ylabel("Signal / V")
#plt.yscale('log')
#plt.xscale('log')

plt.xlim(xmin = 0, xmax = 30000)

plt.subplots_adjust(left = 0.05, top=0.92, right=0.98, bottom=0.08)

#plt.ylim(ymax = 3)
plt.show()