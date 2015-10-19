import matplotlib.pyplot as plt
import csv
import matplotlib.gridspec as gridspec
import math
import numpy as np

frequency0 = []
amp0 = []
phase0 = []
frequency1 = []
amp1 = []
phase1 = []
phasediff = []
rough_frequency = []
amp_error = []
amp1_error = []

with open('combined_data.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, None)
	next(reader, None)
	for row in reader:
		rough_frequency.append(float(row[0]))
		frequency0.append(float(row[1]))
		amp0.append(float(row[2]))
		amp_error.append(float(row[3]))
		phase0.append(float(row[4]))
		frequency1.append(float(row[6]))
		amp1.append(float(row[7]))
		amp1_error.append(float(row[8]))
		phase1.append(float(row[9]))
		phasediff.append(float(row[11]))

phase0 = [i * math.pi / 180 for i in phase0]
phase1 = [i * math.pi / 180 for i in phase1]
phasediff = [i * math.pi/ 180 for i in phasediff]

fig = plt.figure(figsize=(11, 6))
gs1 = gridspec.GridSpec(3, 1)
gs1.update(wspace=0.1, hspace=0.1) 
ax4 = plt.subplot(gs1[0, 0])

ax4.errorbar(frequency0, amp0, yerr = amp_error,  color = 'navy', linestyle = 'None')
ax4.errorbar(frequency1, amp1, yerr = amp1_error, color = 'lightcoral', linestyle = 'None')
ax4.scatter(frequency0, amp0, label = 'Cantilever oriented 0 degrees', color = 'navy', s=5)
ax4.scatter(frequency1, amp1, label = 'Cantilever oriented 180 degrees', color = 'lightcoral', s = 5)
plt.ylabel('Amplitude / nm')
plt.hlines(90, 0, 10000, linestyles = 'dashed')
ax4.yaxis.set_ticks_position('left')
ax4.xaxis.set_ticks_position('bottom')
plt.axvline(x=110000, color = 'k', linestyle = 'dashed')
plt.axvline(x=7500, color = 'k', linestyle = 'dashed')
plt.xscale('log')
plt.yscale('log')
plt.ylim(ymin = 0, ymax = 60)
ax4.legend(frameon=False, bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, borderaxespad=0.)
ax4.get_yaxis().set_label_coords(-0.06,0.5)

ax5 = plt.subplot(gs1[1, 0], sharex=ax4)
ax5.scatter(frequency0, phase0, label = 'Oriented 0 degrees', color = 'navy', s=5)
ax5.scatter(frequency1, phase1, label = 'Oriented 180 degrees', color = 'lightcoral', s=5)
plt.ylabel('Phase')
plt.axvline(x=110000, color = 'k', linestyle = 'dashed')
plt.axvline(x=7500, color = 'k', linestyle = 'dashed')
plt.ylim(ymin = -3.5, ymax = 3.5)
plt.axhline(y=np.pi/2, color = 'c', linestyle = 'dashed')
plt.axhline(y=-np.pi/2, color = 'c', linestyle = 'dashed')
ax5.yaxis.set_ticks_position('left')
ax5.xaxis.set_ticks_position('bottom')
plt.yticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
ax5.get_yaxis().set_label_coords(-0.06,0.5)

ax6 = plt.subplot(gs1[2, 0], sharex=ax4)
ax6.scatter(rough_frequency, phasediff, color = 'm', s=5)
plt.xlabel('Frequency / Hz')
plt.ylabel('Phase difference')
ax6.yaxis.set_ticks_position('left')
ax6.xaxis.set_ticks_position('bottom')
plt.axvline(x=110000, color = 'k', linestyle = 'dashed')
plt.axvline(x=7500, color = 'k', linestyle = 'dashed')
plt.ylim(ymin = np.pi/2, ymax = 3.5)
plt.xlim(xmin = 0, xmax = 200000)
plt.yticks([np.pi/2, 3*np.pi/4, np.pi],[r'$+\pi/2$', r'$+3\pi/4$', r'$+\pi$'])
ax6.get_yaxis().set_label_coords(-0.06,0.5)

plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax5.get_xticklabels(), visible=False)

frequency0 = [i/1000.0 for i in frequency0]
frequency1 = [i/1000.0 for i in frequency1]
rough_frequency = [i/1000.0 for i in rough_frequency]

plt.show()


fig = plt.figure(figsize=(11, 6))
gs2 = gridspec.GridSpec(3, 1)
ax1 = plt.subplot(gs2[0, 0])

#x1.errorbar(frequency0[31:], amp0[31:], yerr = amp_error[31:],  label = 'Cantilever oriented 0 degrees', color = 'b')
#x1.errorbar(frequency1[31:], amp1[31:], yerr = amp1_error[31:], label = 'Cantilever oriented 180 degrees', color = 'g')
#lt.ylabel('Amplitude / nm')
#lt.hlines(90, 0, 10000, linestyles = 'dashed')
#x1.yaxis.set_ticks_position('left')
#x1.xaxis.set_ticks_position('bottom')
#lt.axvline(x=110.000, color = 'k', linestyle = 'dashed')
#lt.ylim(ymin = 0, ymax = 10)
#x1.legend(frameon=False, bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, borderaxespad=0.)
#x1.get_yaxis().set_label_coords(-0.06,0.5)

#x2 = plt.subplot(gs2[1, 0], sharex=ax1)
#x2.scatter(frequency0[31:33], phase0[31:33], label = 'Oriented 0 degrees', color = 'b')
#x2.scatter(frequency0[33:], phase0[33:], label = 'Oriented 0 degrees', color = 'b')
#x2.scatter(frequency1[31:43], phase1[31:43], label = 'Oriented 180 degrees', color = 'g')
#x2.scatter(frequency1[43:], phase1[43:], label = 'Oriented 180 degrees', color = 'g')
#lt.ylabel('Phase')
#lt.ylim(ymin = -3.5, ymax = 3.5)
#lt.axhline(y=np.pi/2, color = 'c', linestyle = 'dashed')
#lt.axhline(y=-np.pi/2, color = 'c', linestyle = 'dashed')
#lt.axvline(x=110.000, color = 'k', linestyle = 'dashed')
#x2.yaxis.set_ticks_position('left')
#x2.xaxis.set_ticks_position('bottom')
#lt.yticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
#x2.get_yaxis().set_label_coords(-0.06,0.5)

#ax3 = plt.subplot(gs2[2, 0], sharex=ax1)
#ax3.scatter(rough_frequency[31:], phasediff[31:], color = 'm')
#plt.xlabel('Frequency / kHz')
#plt.ylabel('Phase difference')
#plt.ylim(ymin = np.pi/2, ymax = 3.5)
#plt.axvline(x=110.000, color = 'k', linestyle = 'dashed')
#plt.yticks([np.pi/2, 3*np.pi/4, np.pi],[r'$+\pi/2$', r'$+3\pi/4$', r'$+\pi$'])
#ax3.get_yaxis().set_label_coords(-0.06,0.5)
#ax4.yaxis.set_ticks_position('left')
#ax4.xaxis.set_ticks_position('bottom')

plt.xlim(0, xmax = 180.000)

plt.setp(ax1.get_xticklabels(), visible=False)
plt.setp(ax2.get_xticklabels(), visible=False)
plt.subplots_adjust(hspace=0.05)



plt.setp(ax1.get_xticklabels(), visible=False)
plt.setp(ax2.get_xticklabels(), visible=False)
plt.subplots_adjust(hspace=0.05)

plt.tight_layout
plt.show()

