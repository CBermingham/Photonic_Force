import matplotlib.pyplot as plt
import math
import cmath

x_deg = range(-90, 90)
x_rad = [i*math.pi/180 for i in x_deg]

m1 = (-cmath.j* math.cos(delta) - math.sin(delta)*math.cos(2*phi))/(math.sin(delta)*math.sin(2))


plt.show()