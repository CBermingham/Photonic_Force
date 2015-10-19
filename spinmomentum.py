import matplotlib.pyplot as plt
import numpy as np

angle = [-45, 0, 45]
forwards = [4.41, 0.6745, 3.99]
forwardserr = [0.284, 0.243, 0.264]
backwards = [-2.82, 0.00633, -3.387]
backwardserr = [0.294, 0.523, 0.429]

spinforwards = (forwards[0] - forwards[2])/2.0
spinbackwards = (backwards[0] - backwards[2])/2.0
thermandradpos = forwards[0] - spinforwards
thermandradneg = backwards[2] + spinbackwards


x = [i * 0.1 for i in range(-500, 500)]
y = []
for i in x[0:500]:
	yval = forwards[0]/2 * -np.cos(i / 14.3) + forwards[0]/2
	y.append(yval)

for i in x[500:1000]:
	yval = forwards[2]/2 * -np.cos(i / 14.3) + forwards[2]/2
	y.append(yval)


y2 = []
for i in x[0:500]:
	y2val = backwards[0]/2 * -np.cos(i / 14.3) + backwards[0]/2
	y2.append(y2val)

for i in x[500:1000]:
	y2val = backwards[2]/2 * -np.cos(i / 14.3) + backwards[2]/2
	y2.append(y2val)



fig1 = plt.figure(figsize=(10, 10))
plt.errorbar(angle, forwards, yerr=forwardserr, fmt='o')
plt.errorbar(angle, backwards, yerr=backwardserr, fmt='o')
plt.xlabel('Quarter wave plate angle / degrees')
plt.ylabel('Cantilever displacement / nm')
plt.xlim(xmin = -50, xmax = 50)
plt.hlines(0, -50, 50, linestyles = 'dashed')
plt.hlines(thermandradpos, -50, 50, linestyles = 'dashed')
plt.hlines(thermandradneg, -50, 50, linestyles = 'dashed')
plt.arrow(-20,0,0,thermandradpos, length_includes_head=True, head_width=1, head_length=0.2, fc='k', ec='k')
plt.arrow(-15,0,0,thermandradneg, length_includes_head=True, head_width=1, head_length=0.2, fc='k', ec='k')
plt.annotate('Radiation pressure + Photothermal effect', xy=(-19, 3.3))
plt.annotate('Radiation pressure + Photothermal effect', xy=(-14, -2.3))
plt.arrow(-44,thermandradpos,0,forwards[0]-thermandradpos, length_includes_head=True, head_width=1, head_length=0.1, fc='k', ec='k')
plt.annotate('Spin', xy=(-43, 4.3))
plt.arrow(44,thermandradpos,0,forwards[2]-thermandradpos, length_includes_head=True, head_width=1, head_length=0.1, fc='k', ec='k')
plt.annotate('Spin', xy=(38, 3.98))

plt.plot(x, y, linestyle ='--')
plt.plot(x, y2, linestyle ='--')


plt.show()