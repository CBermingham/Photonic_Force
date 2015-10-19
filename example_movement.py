import matplotlib.pyplot as plt

time = []
displacement = []
time2 = []
displacement2 = []

f = open('174744_filtered', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	time.append(float(b[0]))
	displacement.append(float(b[9]))

f = open('102723', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	time2.append(float(b[0]))
	displacement2.append(float(b[9]))

signal = []
signal2 = []

f = open('174744_phase', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	signal.append(float(b[3])/10)

f = open('102723_phase', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	signal2.append(float(b[3])/10)

displacement = [i * 1E9 for i in displacement]
signal = [i * 4 for i in signal]

displacement2 = [i * 1E9 for i in displacement2]
signal2 = [i * 6 for i in signal2]

fig = plt.figure()
ax1 = plt.subplot(211)
ax1.plot(time, displacement, label = 'Displacement', color = 'c')
ax1.set_xlabel('Time / s')

ax1.set_ylabel('Displacement / nm')
#frame1 = plt.gca()
#frame1.axes.get_yaxis().set_ticks([])

ax2 = ax1.twinx()
ax2.plot(time, signal, color = 'k', label = 'Laser drive voltage')
ax2.set_ylabel('Laser power / mW')

ax1.set_xlim(xmax = 6)



ax3 = plt.subplot(212)
ax3.plot(time2, displacement2, label = 'Displacement', color = 'm')
ax3.set_xlabel('Time / s')
ax3.set_ylabel('Displacement / nm')


ax4 = ax3.twinx()
ax4.plot(time2, signal2, color = 'k', label = 'Laser drive voltage')
ax4.set_ylabel('Laser power / mW')

ax3.set_xlim(xmax = 6)
plt.show()