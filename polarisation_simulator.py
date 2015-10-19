import math
import matplotlib.pyplot as plt
import numpy

#theta = float(raw_input('Angle of polarised light wrt fast axis of quarter waveplate in radians: '))
#E0 = float(raw_input('Magnitude of polarised light: '))
#phase_diff = float(raw_input('Phase shift produced by waveplate: '))
#wavelength = float(raw_input('Wavelength of polarised light in nm: '))
theta = 45.0 * math.pi/ 180.0
E0 = 1.0
phase_diff = math.pi * (1.0 / 2.0)
wavelengthnm = 660.0
wavelength = wavelengthnm

z = 0
omega = (2.0 * math.pi) / wavelength
k = (2.0 * math.pi) / wavelength
period = wavelength / 3E8

time = []
for i in range(0, 330):
	time.append(i*2)

Ex = []
Ey = []
E = []
for i in time:
	x = E0 * math.cos(theta) * math.cos(k * z - omega * i)
	y = E0 * math.sin(theta) * math.cos(k * z - omega * i - phase_diff)
	Ex.append(x)
	Ey.append(y)
	E.append(math.sqrt(x**2 + y**2))

print abs(Ex[0])-abs(Ey[82])

angles = []
ellipcicity = []
for i in range(-50, 50):
	angle = i * math.pi / 180
	angles.append(i)
	Ex0 = E0 * math.cos(angle) * math.cos(k * z - omega * time[0])
	Ey247 = E0 * math.sin(angle) * math.cos(k * z - omega * time[82] - phase_diff)
	ellipcicity.append(abs(Ex0) - abs(Ey247))

fig1 = plt.figure(figsize=(10, 10))
plt.scatter(angles, ellipcicity)

fig2 = plt.figure(figsize=(10, 10))
plt.scatter(Ex, Ey)
plt.xlim(xmin = -1, xmax = 1)
plt.ylim(ymin = -1, ymax = 1)
plt.show()