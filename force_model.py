import matplotlib.pyplot as plt
import math


phi_deg = range(-180, 180)
phi_rad = [i*math.pi/180 for i in phi_deg]
p = [2+5.0*math.cos(i)**2 for i in phi_rad]
s=[0.5+2.0 * math.sin(i)**2 for i in phi_rad]
ratio=[s[i]/p[i] for i in range(len(s))]


y_max=max(p)
plt.plot(phi_deg, p, label="p")
plt.plot(phi_deg, s, label = "s")
plt.ylim(ymin=0, ymax=y_max)
plt.axvline(x=90, ymin=min(p)/y_max, ymax=y_max)
plt.axvline(x=-90, ymin=0, ymax=min(p)/y_max)
plt.axvline(x=0, ymin=min(s)/y_max, ymax=max(s)/y_max)
plt.plot(phi_deg, ratio, label = "s/p")
plt.text(10, 1.5, "E_s")
plt.text(-80, 1, "E_pz")
plt.text(100, 4.5, "E_px")
plt.legend()
plt.show()