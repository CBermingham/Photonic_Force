import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def make_highlight_region(ax, limits, axis, **kwargs):
    """
    Make a semi-transparent patch to highlight a region on a given axis.
    ax is the Axes object you want to plot it on.
    limits is a list of [min, max] for the variable
    axis is the axis that represents the variable in question, e.g. 'x'
    kwargs passes keyword arguments to patches.Rectagle
    """
    xmin, xmax = 0, 0
    ymin, ymax = 0, 0
    if axis == 'x':
        xmin, xmax = limits
        ymin, ymax = ax.get_ylim()
    else:
        ymin, ymax = limits
        xmin, xmax = ax.get_xlim()
    if not kwargs:
        kwargs = dict(color='grey', alpha=0.2)
    patch = patches.Rectangle((xmin, ymin), xmax-xmin, ymax-ymin, **kwargs)
    ax.add_patch(patch)
    return patch

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


on_off0 = []

for i in range(0, len(laser0)-1):
	if (laser0[i]>4 and laser0[i+1] <1) or (laser0[i]<1 and laser0[i+1]>4):
		on_off0.append(i)


newtime0 = []
newpos0 = []

for i in range(0, len(on_off0)-1):
	newpos0 = newpos0 + pos0[on_off0[i]+50:on_off0[i+1]]
for i in range(0, len(newpos0)):
	newtime0.append(i/640.0)
newpos0 = [i-np.mean(newpos0) for i in newpos0]

plt.subplot(3,1,1)
ax1 = plt.gca()
ax1.set_title('0 degrees')
plt.plot(newtime0, newpos0)
make_highlight_region(ax=ax1, limits = (newtime0[0], newtime0[270]),  axis='x')
make_highlight_region(ax=ax1, limits = (newtime0[540], newtime0[810]),  axis='x')
make_highlight_region(ax=ax1, limits = (newtime0[1080], newtime0[1350]),  axis='x')
make_highlight_region(ax=ax1, limits = (newtime0[1620], newtime0[1890]),  axis='x')
make_highlight_region(ax=ax1, limits = (newtime0[2160], newtime0[2430]),  axis='x')
make_highlight_region(ax=ax1, limits = (newtime0[2700], newtime0[-1]),  axis='x')
plt.xlabel('Time / s')


on_off180 = []

for i in range(0, len(laser180)-1):
	if (laser180[i]>4 and laser180[i+1] <1) or (laser180[i]<1 and laser180[i+1]>4):
		on_off180.append(i)


newtime180 = []
newpos180 = []

for i in range(0, len(on_off180)-1):
	newpos180 = newpos180 + pos180[on_off180[i]+50:on_off180[i+1]]
for i in range(0, len(newpos180)):
	newtime180.append(i/640.0)
newpos180 = [i-np.mean(newpos180) for i in newpos180]

fig = plt.gcf()
plt.subplot(3,1,2)
ax2 = plt.gca()
ax2.set_title('180 degrees')
plt.plot(newtime180, newpos180)
make_highlight_region(ax=ax2, limits = (newtime180[0], newtime180[270]),  axis='x')
make_highlight_region(ax=ax2, limits = (newtime180[540], newtime180[810]),  axis='x')
make_highlight_region(ax=ax2, limits = (newtime180[1080], newtime180[1350]),  axis='x')
make_highlight_region(ax=ax2, limits = (newtime180[1620], newtime180[1890]),  axis='x')
make_highlight_region(ax=ax2, limits = (newtime180[2160], newtime180[2430]),  axis='x')
make_highlight_region(ax=ax2, limits = (newtime180[2700], newtime180[-1]),  axis='x')
plt.xlabel('Time / s')
plt.ylabel('Displacement / nm')

on_off90 = []

for i in range(0, len(laser90)-1):
	if (laser90[i]>4 and laser90[i+1] <1) or (laser90[i]<1 and laser90[i+1]>4):
		on_off90.append(i)


newtime90 = []
newpos90 = []

for i in range(1, len(on_off90)-2):
	newpos90 = newpos90 + pos90[on_off90[i]+50:on_off90[i+1]]
for i in range(0, len(newpos90)):
	newtime90.append(i/640.0)
newpos90 = [i-np.mean(newpos90) for i in newpos90]

plt.subplot(3,1,3)
ax3 = plt.gca()
ax3.set_title('270 degrees')
plt.plot(newtime90, newpos90)
make_highlight_region(ax=ax3, limits = (newtime90[0], newtime90[270]),  axis='x')
make_highlight_region(ax=ax3, limits = (newtime90[540], newtime90[810]),  axis='x')
make_highlight_region(ax=ax3, limits = (newtime90[1080], newtime90[1350]),  axis='x')
make_highlight_region(ax=ax3, limits = (newtime90[1620], newtime90[1890]),  axis='x')
#make_highlight_region(ax=ax3, limits = (newtime90[2160], newtime90[2430]),  axis='x')
#make_highlight_region(ax=ax3, limits = (newtime90[2700], newtime90[-1]),  axis='x')
plt.xlabel('Time / s')


plt.subplots_adjust(hspace=0.4)
fig.set_size_inches(5,10)




plt.show()



#f, (ax1, ax2, ax3) = plt.subplots(3 , sharex = True)
#ax1.plot(time0, pos0, 'mediumblue')
# Make the y-axis label and tick labels match the line color.
#for tl in ax1.get_yticklabels():
#    tl.set_color('mediumblue')

#ax12 = ax1.twinx()
#ax12.plot(time0, laser0, 'crimson')

#ax2.plot(time180, pos180, 'mediumblue')
# Make the y-axis label and tick labels match the line color.
#ax2.set_ylabel('Displacement / nm', color='mediumblue')
#for tl in ax2.get_yticklabels():
#    tl.set_color('mediumblue')

#ax22 = ax2.twinx()
#ax22.plot(time180, laser180, 'crimson')

#ax3.plot(time90, pos90, 'mediumblue')
#ax3.set_xlabel('Time / s')
# Make the y-axis label and tick labels match the line color.
#for tl in ax3.get_yticklabels():
#    tl.set_color('mediumblue')

#ax32 = ax3.twinx()
#ax32.plot(time90, laser90, 'crimson')

#plt.xlim(xmin = 0, xmax = 6)

#plt.show()