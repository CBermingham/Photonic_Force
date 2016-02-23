import matplotlib.pyplot as plt
import numpy as np
import math

def lorentzian(f, k, gamma):
	PSD=1.38064852E-23*290/(gamma*math.pi**2*((k/(2*math.pi*gamma))**2+f**2))
	return PSD

def S0(k, gamma):
	S0 = 1.38064852E-23*290/(gamma*math.pi**2*((k/(2*math.pi*gamma))**2))
	return S0

def Shighf(f, k, gamma):
	PSD=1.38064852E-23*290/(gamma*math.pi**2*f**2)
	return PSD

# displacement = []
# f = open('/Volumes/LMF_Microscope/1-Data/2015/7_July/27_files/190915', 'rU')
# lines=f.readlines()
# f.close()
# for l in lines:
# 	b = l.split()
# 	displacement.append(float(b[9]))

# mean = np.mean(displacement)
# displacement = [i-mean for i in displacement]

# sample_rate = float(64000)
# N = len(displacement)
# freq_res = float(sample_rate/N)

# fft = np.fft.fft(displacement)
# power_spectrum = [abs(i)**2 for i in fft]

# power_spectrum = power_spectrum[len(power_spectrum)/2:]

# power_spectrum = [i*2/(N**2*freq_res) for i in power_spectrum]

# f = []
# for i in range(0, N/2):
# 	f.append(sample_rate/N*i)

# plt.plot(f[0: 100000], power_spectrum[0: 100000])

k = 3E-5
gamma = 2E-9

f = range(1, 32000)

S = [lorentzian(i, k, gamma) for i in f]
S0 = [S0(k, gamma) for i in f]
Shighf = [Shighf(i, k, gamma) for i in f]

corner_freq = k/(2*math.pi*gamma)
print "corner frequency:", corner_freq

plt.plot(f, S, color = 'indigo')
plt.plot(f, S0, linestyle = "--", color = 'darkturquoise')
plt.plot(f[2000:], Shighf[2000:], linestyle = "--", color = 'mediumorchid')
plt.axvline(corner_freq, linestyle = "--", color = 'mediumslateblue')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power Spectral Density (m$^2$/ Hz)")
plt.xscale('log')
plt.yscale('log')
plt.show()