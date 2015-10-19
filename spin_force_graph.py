import matplotlib.pyplot as plt

time0 = []
pos0 = []
sumsig0 = []
laser0 = []

time90 = []
pos90 = []
sumsig90 = []
laser90 = []

time180 = []
pos180 = []
sumsig180 = []
laser180 = []

f = open('0_pos_p.txt', 'rU')
lines=f.readlines()[1:]
f.close()
for l in lines:
	b = l.split()
	time0.append(float(b[0]))
	pos0.append(float(b[1]))

f = open('0_sum_p.txt', 'rU')
lines=f.readlines()[1:]
f.close()
for l in lines:
	b = l.split()
	sumsig0.append(float(b[5]))
	laser0.append(float(b[3]))

f = open('180_pos_p.txt', 'rU')
lines=f.readlines()[1:]
f.close()
for l in lines:
	b = l.split()
	time180.append(float(b[0]))
	pos180.append(float(b[1]))

f = open('180_sum_p.txt', 'rU')
lines=f.readlines()[1:]
f.close()
for l in lines:
	b = l.split()
	sumsig180.append(float(b[5]))
	laser180.append(float(b[3]))

f = open('90_pos_p.txt', 'rU')
lines=f.readlines()[1:]
f.close()
for l in lines:
	b = l.split()
	time90.append(float(b[0]))
	pos90.append(float(b[1]))

f = open('90_sum_p.txt', 'rU')
lines=f.readlines()[1:]
f.close()
for l in lines:
	b = l.split()
	sumsig90.append(float(b[5]))
	laser90.append(float(b[3]))

# on_off = []

# for i in range(0, len(laser0)-1):
# 	if (laser0[i]>4 and laser0[i+1] <1) or (laser0[i]<1 and laser0[i+1]>4):
# 		on_off.append(i)


#time0 = [time0[]]


f, (ax1, ax2, ax3) = plt.subplots(3 , sharex = True)
ax1.plot(time0, pos0, 'mediumblue')
# Make the y-axis label and tick labels match the line color.
for tl in ax1.get_yticklabels():
    tl.set_color('mediumblue')

ax12 = ax1.twinx()
ax12.plot(time0, laser0, 'crimson')

ax2.plot(time180, pos180, 'mediumblue')
# Make the y-axis label and tick labels match the line color.
ax2.set_ylabel('Displacement / nm', color='mediumblue')
for tl in ax2.get_yticklabels():
    tl.set_color('mediumblue')

ax22 = ax2.twinx()
ax22.plot(time180, laser180, 'crimson')

ax3.plot(time90, pos90, 'mediumblue')
ax3.set_xlabel('Time / s')
# Make the y-axis label and tick labels match the line color.
for tl in ax3.get_yticklabels():
    tl.set_color('mediumblue')

ax32 = ax3.twinx()
ax32.plot(time90, laser90, 'crimson')

plt.xlim(xmin = 0, xmax = 6)

plt.show()