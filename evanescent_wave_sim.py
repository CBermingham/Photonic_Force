import matplotlib.pyplot as plt 
import math
import cmath

x=range(800)
x=[i*1E-9 for i in x]


def decay_length(theta_i, n_i, lambda0):
	return lambda0/(4*math.pi*math.sqrt(n_i**2*(math.sin(theta_i*math.pi/180.0))**2-1))

def ts_squared(n_i, theta_i):
	theta_i = theta_i*math.pi/180.0
	cos_theta_t=cmath.sqrt(1-n_i**2*(math.sin(theta_i)**2))
	ts=abs(2*n_i*math.cos(theta_i)/(n_i*math.cos(theta_i)+cos_theta_t))
	return ts**2

def tp_squared(n_i, theta_i):
	theta_i = theta_i*math.pi/180.0
	cos_theta_t=cmath.sqrt(1-n_i**2*(math.sin(theta_i)**2))
	tp=abs(2*n_i*math.cos(theta_i)/(n_i*cos_theta_t+math.cos(theta_i)))
	return tp**2

def crit_angle(n_i):
	c = math.asin(1/n_i)
	return c*180.0/math.pi

def ts_tp_ratio(n_i, theta_i, E_s, E_p):
	theta_i = theta_i*math.pi/180.0
	return E_s**2*ts_squared(n_i, theta_i)/(E_p**2*tp_squared(n_i, theta_i)*(2*n_i**2*math.sin(theta_i)**2-1))

def s_intensity(n_i, theta_i, E_s, z, lambda0, phi):
	gamma=1.0/(2.0*decay_length(theta_i, n_i, lambda0))
	theta_i = theta_i*math.pi/180.0
	return E_s**2*ts_squared(n_i, theta_i)*math.exp(-2*gamma*z)*(math.sin(phi)**2)

def px_intensity(n_i, theta_i, E_p, z, lambda0, phi):
	gamma=1.0/(2.0*decay_length(theta_i, n_i, lambda0))
	theta_i = theta_i*math.pi/180.0
	return E_p**2*tp_squared(n_i, theta_i)*n_i**2*math.sin(theta_i)**2

def pz_intensity(n_i, theta_i, E_p, z, lambda0, phi):
	gamma=1.0/(2.0*decay_length(theta_i, n_i, lambda0))
	theta_i = theta_i*math.pi/180.0
	return E_p**2*tp_squared(n_i, theta_i)*(n_i**2*math.sin(theta_i)**2-1)*math.cos(phi)**2

def p_intensity(n_i, theta_i, E_p, z, lambda0, phi):
	px = px_intensity(n_i, theta_i, E_p, z, lambda0, phi)
	pz = pz_intensity(n_i, theta_i, E_p, z, lambda0, phi)
	return px+pz

I1 = [math.exp(-i/decay_length(42, 1.52, 660E-9)) for i in x]
I5 = [math.exp(-i/decay_length(44, 1.52, 660E-9)) for i in x]
I6 = [math.exp(-i/decay_length(50, 1.52, 660E-9)) for i in x]
I2 = [math.exp(-i/decay_length(42, 1.52, 642E-9)) for i in x]
I3 = [math.exp(-i/decay_length(42, 1.52, 561E-9)) for i in x]
I4 = [math.exp(-i/decay_length(42, 1.52, 488E-9)) for i in x]

print decay_length(42, 1.52, 660E-9)
print decay_length(44, 1.52, 488E-9)
print decay_length(50, 1.52, 488E-9)
print decay_length(42, 1.52, 561E-9)
print decay_length(42, 1.52, 488E-9)
print crit_angle(1.52)

x=[i*1E9 for i in x]

plt.plot(x, I1, color='r', label='$\lambda$=660nm, $\\theta_i$=42$\degree$ ($\delta$=283 nm)')
plt.plot(x, I5, color='r', linestyle = 'dashed', label='$\lambda$=660nm, $\\theta_i$=44$\degree$ ($\delta$=115 nm)')
plt.plot(x, I6, color='r', linestyle = 'dotted', label='$\lambda$=660nm, $\\theta_i$=50$\degree$ ($\delta$=65 nm)')
#plt.plot(x, I2, color = 'r')
plt.plot(x, I3, color = 'g', label='$\lambda$=561nm, $\\theta_i$=42$\degree$ ($\delta$=241 nm)')
plt.plot(x, I4, color = 'b', label='$\lambda$=488nm, $\\theta_i$=42$\degree$ ($\delta$=209 nm)')
plt.xlabel('Height above surface / nm', size = 14)
plt.ylabel('$I/I_0$', size = 14)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
#plt.title('Evanescent field intensity for n(glass) = 1.518 and incident angle = 45 degrees')
plt.legend(fontsize = 14)
plt.savefig('example_decay_lengths.pdf')
plt.show()


# x=range(int(round(crit_angle(n))), 9000)
# x=[int(round(crit_angle(1.518)))+i/100.0-int(round(crit_angle(1.518)))/100.0 for i in x]
# Is = []
# Ip = []
# Iratio = []
# sp_ratio = []
# for i in x:
# 	Is.append(ts_squared(n, i))
# 	Ip.append(tp_squared(n, i))
# 	Iratio.append(ts_squared(n, i)/tp_squared(n, i))
# 	sp_ratio.append(ts_tp_ratio(n, i, 1, 1))


# # plt.plot(x, Is, label = '|ts|^2')
# # plt.plot(x, Ip, label = '|tp|^2')
# # plt.plot(x, Iratio, label = '|ts|^2/|tp|^2')
# plt.axvline(crit_angle(n), 0, 1)
# plt.axhline(1, 0, crit_angle(n)/90)
# plt.plot(x, sp_ratio)
# # plt.legend()
# plt.xlabel('Angle of incidence / degrees')
# plt.ylabel('$|E_{t}^s|^2/|E_{t}^p|^2$')
# plt.xlim(xmin=0, xmax=90)
# plt.ylim(ymin = 0, ymax=1.5)

# plt.show()

# n=1.518
# wavelength = 660E-9
# angle_i = 45
# height = 0

# x=range(0, 9000)
# x=[i/100.0 for i in x]
# Is = []
# Ip = []
# for i in x:
# 	Is.append(ts_squared(n, i))
# 	Ip.append(tp_squared(n, i))

# print crit_angle(n)

# plt.plot(x, Is, label = 's-polarised', color = 'm', linewidth = 2)
# plt.plot(x, Ip, label = 'p-polarised', color = 'c', linewidth = 2)
# plt.axvline(crit_angle(n), 0, 1, color = 'k', linewidth = 1, linestyle = '--')
# plt.legend()
# plt.xlabel('Angle of incidence / degrees', fontsize = 14)
# plt.ylabel('$I_t(x=0)$ / $I_i(x=0)$', fontsize = 14)
# plt.xticks(size = 14)
# plt.yticks(size = 14)
# plt.savefig('Intensity_ratio_at_interface.pdf')

# plt.show()





# y = []
# y2 = []
# y3 = []
# y4 = []
# x=range(0, 360)
# for i in x:
# 	y.append(s_intensity(n, angle_i, 1, height, wavelength, i*math.pi/180.0))
# 	y2.append(px_intensity(n, angle_i, 1, height, wavelength, i*math.pi/180.0))
# 	y3.append(pz_intensity(n, angle_i, 1, height, wavelength, i*math.pi/180.0))
# 	y4.append(p_intensity(n, angle_i, 1, height, wavelength, i*math.pi/180.0))

# plt.plot(x, y, label = 's polarised incident light')
# plt.plot(x, y4, label = 'p polarised incident light')
# plt.legend()
# plt.xlabel('Cantilever orientation angle')
# plt.ylabel('Cantilever response / arbitrary units')
# plt.ylim(ymax = 2.5)
# plt.text(190, 1.75, "E_pz")
# plt.text(100, 0.7, "E_s")
# plt.text(190, 0.8, "E_px")
# plt.annotate('', (180, min(y4)), (180, max(y4)), arrowprops={'arrowstyle':'<->'})
# plt.annotate('', (90, 0), (90, max(y)), arrowprops={'arrowstyle':'<->'})
# plt.annotate('', (180, 0), (180, min(y4)), arrowprops={'arrowstyle':'<->'})
# plt.show()




