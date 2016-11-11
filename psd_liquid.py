import matplotlib.pyplot as plt

frequency = []
psd = []
fit = []

f = open('liquid_drive', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	frequency.append(float(b[0]))
	psd.append(float(b[1]))
	fit.append(float(b[2]))

psd = [i*350 for i in psd]

plt.figure(figsize=(8,4), tight_layout = True)

plt.plot(frequency, psd, color = 'darkviolet')
plt.xscale('log')
plt.yscale('log')
plt.xticks(size = 14)
plt.yticks(size = 14)
plt.ylim(ymin = 1E-22)
plt.xlabel('Frequency (Hz)', size = 14)
plt.ylabel('PSD (m$^2$ / Hz)', size = 14)


plt.savefig('liquid_drive.pdf')
plt.show()