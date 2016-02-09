import matplotlib.pyplot as plt
import math

angles = []
anglep = []
pfit = []
sfit = []


f = open('pfit_data_clean_cantilever.txt', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	anglep.append(float(b[0]))
	pfit.append(float(b[1]))

f = open('sfit_data_clean_cantilever.txt', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	angles.append(float(b[0]))
	sfit.append(float(b[1]))

data_angles = [0, math.pi, 3*math.pi/2, math.pi/2]
# s_data = [565, 492, 86, 27]
# p_data = [632, 695, 164, 67]
# s_error = [0.298, 0.328, 1.42, 0.571]
# p_error = [0.254, 0.611, 1.48, 0.539]

#clean cantilever data (below)
p_data = [258, 241, 11.5, 19.6]
s_data = [9.1, 5.61, 32.6, 66]
s_error = [0.298, 0.328, 1.42, 0.571]
p_error = [0.254, 0.611, 1.48, 0.539]

#glue cantilever2 data
# s_data = [-449, -17.6, 106, 69.1]
# p_data = [197, 4.25, 368, 29.6]
# s_error = [0.341, 0.263, 0.382, 0.602]
# p_error = [0.97, 0.358, 0.232, 0.355]


plt.plot(angles, sfit, 'r--', linewidth = 2)
plt.plot(anglep, pfit, 'b--', linewidth = 2)
plt.errorbar(data_angles, s_data, yerr = s_error, color = 'r', label = 's data', fmt = 'o', markersize = 5)
plt.errorbar(data_angles, p_data, yerr = p_error, color = 'b', label = 'p data', fmt = 'o', markersize = 5)
plt.legend()
plt.xlabel("Cantilever orientation $\\theta$ ($\degree$)", fontsize=14)
plt.ylabel("Cantilever displacement (nm)", fontsize=14)
#plt.ylim(ymin = 0)
plt.xlim(xmin = 0)
plt.xticks([0, math.pi/2, math.pi, 3*math.pi/2, 2*math.pi], ['0', '90', '180', '270', '360'], size=14)
plt.yticks(size=14)
plt.savefig('s_p_data_fit_clean_cantilever.pdf', format='pdf')
plt.show()