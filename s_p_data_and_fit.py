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


plt.plot(angles, sfit, 'r--', linewidth = 2, color = 'mediumseagreen')
plt.plot(anglep, pfit, 'b--', linewidth = 2, color = 'darkorange')
plt.errorbar(data_angles, s_data, yerr = s_error, label = 's-polarised', fmt = 'o', markersize = 3, color = 'mediumseagreen')
plt.errorbar(data_angles, p_data, yerr = p_error, label = 'p-polarised', fmt = 'o', markersize = 3, color = 'darkorange')
plt.legend()
plt.axhline(y=max(pfit), color = 'grey', linestyle = '--')
plt.axhline(y=min(pfit), color = 'grey', linestyle = '--')
plt.axhline(y=max(sfit), color = 'grey', linestyle = '--')
plt.arrow(2.5, 0, 0, max(sfit), fc="k", ec="k", head_width=0.1, head_length=5, length_includes_head=True)
plt.arrow(1, 0, 0, max(pfit), fc="k", ec="k", head_width=0.1, head_length=5, length_includes_head=True)
plt.arrow(5, 0, 0, min(pfit), fc="k", ec="k", head_width=0.1, head_length=5, length_includes_head=True)
plt.annotate('$I_{s, max}$', xy=(1,1), xytext=(2.6, max(sfit)-12), size = 14)
plt.annotate('$I_{pz, max}$', xy=(1,1), xytext=(1.1, max(pfit)-12), size = 14)
plt.annotate('$I_{px}$', xy=(1,1), xytext=(5.1, min(pfit)-12), size = 14)
plt.xlabel("Cantilever orientation $\\theta$ ($\degree$)", fontsize=14)
plt.ylabel("Cantilever deflection (nm)", fontsize=14)
#plt.ylim(ymin = 0)
plt.xlim(xmin = 0)
plt.xticks([0, math.pi/2, math.pi, 3*math.pi/2, 2*math.pi], ['0', '90', '180', '270', '360'], size=14)
plt.yticks(size=14)
plt.savefig('s_p_data_fit_clean_cantilever.pdf', format='pdf')
plt.show()