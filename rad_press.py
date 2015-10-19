import matplotlib.pyplot as plt

time = []
displacement = []

f = open('193417', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	time.append(float(b[0]))
	displacement.append(float(b[9]))

signal = []

f = open('193417_signal', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	signal.append(float(b[3])/10)

displacement = [i * 1E9 for i in displacement]
signal = [i * 4 for i in signal]


fig = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(time, displacement, label = 'Displacement', color = 'blueviolet')
ax1.set_xlabel('Time / s')

ax1.set_ylabel('Displacement / arbitrary units')
frame1 = plt.gca()
frame1.axes.get_yaxis().set_ticks([])

ax2 = ax1.twinx()
ax2.plot(time, signal, color = 'k', label = 'Laser drive voltage')
ax2.set_ylabel('Laser power / mW')

ax1.set_xlim(xmax = 6)



plt.show()