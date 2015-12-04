import matplotlib.pyplot as plt

time = []
psd = []
fit = []

f = open('psddata', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	time.append(float(b[0]))
	psd.append(float(b[1]))
	fit.append(float(b[2]))

plt.scatter(time, psd, color='c', s=1, label='experiment')
plt.plot(time, fit, color='purple', label='fit')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power spectral density (m$^2$Hz$^{-1}$)")
plt.xscale('log')
plt.yscale('log')
plt.ylim(ymax=1E-18)
plt.legend()
leg = plt.legend()
leg.get_frame().set_edgecolor('white')
plt.savefig('psd_figure.pdf')
plt.show()