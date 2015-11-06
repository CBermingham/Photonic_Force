import matplotlib.pyplot as plt
import math

x_deg = range(-90, 90)
x_rad = [i*math.pi/180 for i in x_deg]
p = [math.sin(2*i)/math.sqrt(2) for i in x_rad]
s = [math.sqrt(0.5*(math.cos(2*i))**2) for i in x_rad]

plt.plot(x_deg, p)
plt.plot(x_deg, s)
plt.show()