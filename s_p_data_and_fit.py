import matplotlib.pyplot as plt
import math

angles = []
anglep = []
pfit = []
sfit = []


f = open('pfit_data_glue_cantilever2.txt', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	anglep.append(float(b[0]))
	pfit.append(float(b[1]))

f = open('sfit_data_glue_cantilever2.txt', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	angles.append(float(b[0]))
	sfit.append(float(b[1]))

data_angles = [0, math.pi, 3*math.pi/2, math.pi/2]
#s_data = [565, 492, 86, 27]
#p_data = [632, 695, 164, 67]
# s_error = [0.298, 0.328, 1.42, 0.571]
# p_error = [0.254, 0.611, 1.48, 0.539]

#clean cantilever data (below)
# p_data = [258, 241, 11.5, 19.6]
# s_data = [9.1, 5.61, 32.6, 66]
# s_error = [0.298, 0.328, 1.42, 0.571]
# p_error = [0.254, 0.611, 1.48, 0.539]

#glue cantilever2 data
s_data = [247, 168, 17.2, 56.7]
p_data = [379.5, 337, 14.6, 95.2]
s_error = [4, 11, 3.8, 6.2]
p_error = [2.4, 10, 5, 11]


plt.plot(angles, sfit, 'r--')
plt.plot(anglep, pfit, 'b--')
plt.errorbar(data_angles, s_data, yerr = s_error, color = 'r', label = 's data', fmt = 'o', markersize = 3)
plt.errorbar(data_angles, p_data, yerr = p_error, color = 'b', label = 'p data', fmt = 'o', markersize = 3)
plt.legend()
plt.xlabel("Cantilever orientation / degrees")
plt.ylabel("Cantilever displacement / nm")
plt.ylim(ymin = 0)
plt.xlim(xmin = 0)
plt.xticks([0, math.pi/2, math.pi, 3*math.pi/2, 2*math.pi], ['0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$'])
plt.savefig('s_p_data_fit_glue_cantilever2.pdf', format='pdf')
plt.show()