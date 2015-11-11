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

# I1 = [math.exp(-i/decay_length(45, 1.518, 660E-9)) for i in x]
# I2 = [math.exp(-i/decay_length(45, 1.518, 642E-9)) for i in x]
# I3 = [math.exp(-i/decay_length(45, 1.518, 561E-9)) for i in x]
# I4 = [math.exp(-i/decay_length(45, 1.518, 488E-9)) for i in x]

# print decay_length(45, 1.518, 660E-9)
# print decay_length(45, 1.518, 561E-9)
# print decay_length(45, 1.518, 488E-9)

# x=[i*1E9 for i in x]

# plt.plot(x, I1, color='r', label='$\lambda$=660nm ($\delta$= 135nm)')
# #plt.plot(x, I2, color = 'r')
# plt.plot(x, I3, color = 'g', label='$\lambda$=561nm ($\delta$=114 nm)')
# plt.plot(x, I4, color = 'b', label='$\lambda$=488nm ($\delta$=100 nm)')
# plt.xlabel('Height above surface / nm')
# plt.ylabel('$I/I_0$')
# plt.title('Evanescent field intensity for n(glass) = 1.518 and incident angle = 45 degrees')
# plt.legend()

# plt.show()


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


# x=range(0, 9000)
# x=[i/100.0 for i in x]
# Is = []
# Ip = []
# for i in x:
# 	Is.append(ts_squared(n, i))
# 	Ip.append(tp_squared(n, i))

# print crit_angle(n)

# plt.plot(x, Is, label = '|ts|^2')
# plt.plot(x, Ip, label = '|tp|^2')
# plt.axvline(crit_angle(n), 0, 1)
# plt.legend()
# plt.xlabel('Angle of incidence / degrees')
# plt.ylabel('$|t^{s/p}|^2$')

# plt.show()



n=1.518
wavelength = 660E-9
angle_i = 45
height = 0

y = []
y2 = []
y3 = []
y4 = []
x=range(0, 360)
for i in x:
	y.append(s_intensity(n, angle_i, 1, height, wavelength, i*math.pi/180.0))
	y2.append(px_intensity(n, angle_i, 1, height, wavelength, i*math.pi/180.0))
	y3.append(pz_intensity(n, angle_i, 1, height, wavelength, i*math.pi/180.0))
	y4.append(p_intensity(n, angle_i, 1, height, wavelength, i*math.pi/180.0))

plt.plot(x, y, label = 's polarised incident light')
plt.plot(x, y4, label = 'p polarised incident light')
plt.legend()
plt.xlabel('Cantilever orientation angle')
plt.ylabel('Cantilever response / arbitrary units')
plt.ylim(ymax = 2.5)
plt.text(190, 1.75, "E_pz")
plt.text(100, 0.7, "E_s")
plt.text(190, 0.8, "E_px")
plt.annotate('', (180, min(y4)), (180, max(y4)), arrowprops={'arrowstyle':'<->'})
plt.annotate('', (90, 0), (90, max(y)), arrowprops={'arrowstyle':'<->'})
plt.annotate('', (180, 0), (180, min(y4)), arrowprops={'arrowstyle':'<->'})
plt.show()




