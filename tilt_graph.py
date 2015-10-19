import matplotlib.pyplot as plt

time = []
pos = []
sumsig = []
laser = []

f = open('tilt_forwards_mvt.txt', 'rU')
lines=f.readlines()[1:]
f.close()
for l in lines:
	b = l.split()
	time.append(float(b[0]))
	pos.append(float(b[1]))

f = open('tilt_forwards_sum.txt', 'rU')
lines=f.readlines()[1:]
f.close()
for l in lines:
	b = l.split()
	sumsig.append(float(b[5]))
	laser.append(float(b[3]))

pos = [i * 597 for i in pos]
#backwards replace 597 with 460

plt.subplot(3, 1, 1)
plt.plot(time, pos)
plt.ylabel("Displacement / nm")
plt.xlim(xmin = 0, xmax = 6)

plt.subplot(3,1,2)
plt.plot(time, sumsig, color = 'g')

plt.ylabel("SUM / V")
plt.xlabel("Time / s")
plt.xlim(xmin = 0, xmax = 6)

plt.subplot(3,1,3)
plt.plot(time, laser, color = 'r')
plt.ylabel("Laser drive voltage / V")
plt.xlabel("Time / s")
plt.xlim(xmin = 0, xmax = 6)

plt.show()


