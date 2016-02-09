import matplotlib.pyplot as plt
import math

s_45=[0, -1.54994789358, 0, 1.54994789358]
p_45=[1.75926416197, 0, -1.75926416197, 0]

s_minus45=[-1.58726836208, 0, 1.58726836208, 0]
p_minus45=[0, 1.72139022895, 0, -1.72139022895]

circ_max = (1.54994789358+1.58726836208)/2.0

theta=range(0, 361)
theta = [i*math.pi/180.0 for i in theta]
s_45 = [1.54994789358*math.cos(i) for i in theta]
p_45 = [1.75926416197*math.sin(i) for i in theta]

s_minus45 = [1.58726836208*math.cos(i) for i in theta]
p_minus45 = [1.72139022895*math.sin(i) for i in theta]

circ_s = [circ_max*math.cos(i) for i in theta]
circ_p = [circ_max*math.sin(i) for i in theta]

plt.plot(s_45, p_45, color = 'indigo', label = '$+45\degree$')
plt.plot(s_minus45, p_minus45, color = 'deeppink', label = '$-45\degree$')
plt.plot(circ_s, circ_p, color = 'k', linestyle = '--', label = 'circle')
plt.gca().set_aspect('equal')
plt.xlim(xmin=-2, xmax = 2)
plt.ylim(ymin=-2, ymax = 2)
leg = plt.legend(framealpha=0, fontsize = 12)
leg.get_frame().set_edgecolor('white')
plt.xlabel('s polarisation intensity (mW)')
plt.ylabel('p polarisation intensity (mW)')
plt.arrow(0, 1.75926416197, 0.01, 0.0, head_width = 0.05, head_length = 0.08, length_includes_head=True, color = 'indigo')
plt.arrow(0, -1.75926416197, -0.01, 0.0, head_width = 0.05, head_length = 0.08, length_includes_head=True, color = 'indigo')
plt.arrow(1.58726836208, 0, 0.0, 0.01, head_width = 0.05, head_length = 0.08, length_includes_head=True, color = 'deeppink')
plt.arrow(-1.58726836208, 0, 0.0, -0.01, head_width = 0.05, head_length = 0.08, length_includes_head=True, color = 'deeppink')
plt.savefig('circ_check.pdf')
plt.show()