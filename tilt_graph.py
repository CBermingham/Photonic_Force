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
        kwargs = dict(color='red', alpha=0.2)
    patch = patches.Rectangle((xmin, ymin), xmax-xmin, ymax-ymin, **kwargs)
    ax.add_patch(patch)
    return patch

time = []
pos = []
sumsig = []
laser = []

f = open('tilt_forwards_mvt.txt', 'rU')
lines=f.readlines()[1:]
f.close()
for l in lines:
	b = l.split()
	time.append(float(b[0]))
	pos.append(float(b[1]))

f = open('tilt_forwards_sum.txt', 'rU')
lines=f.readlines()[1:]
f.close()
for l in lines:
	b = l.split()
	sumsig.append(float(b[5]))
	laser.append(float(b[3]))

pos = [i * 597 for i in pos]
#backwards replace 597 with 460

on_off = []
index = []
for i in range(1, len(laser)):
	if laser[i] < 1 and laser [i-1]>4:
		on_off.append(time[i])
		index.append(i)
	if laser[i] > 4 and laser [i-1]<1:
		on_off.append(time[i])
		index.append(i)

time = time[index[0]:]
sumsig = sumsig[index[0]:]
pos = pos[index[0]:]

time = [i-on_off[0] for i in time]
on_off = [i-on_off[0] for i in on_off]
index = [i-index[0] for i in index]

pos_off = pos[index[0]:index[1]] + pos[index[2]:index[3]]+ pos[index[4]:index[5]]+ pos[index[6]:index[7]] + pos[index[8]:index[9]]
pos = [i- np.mean(pos_off) for i in pos]

print np.mean(pos[index[1]:index[2]] + pos[index[3]:index[4]]+ pos[index[5]:index[6]]+ pos[index[7]:index[8]] + pos[index[9]:index[10]])
print np.std(pos[index[1]:index[2]] + pos[index[3]:index[4]]+ pos[index[5]:index[6]]+ pos[index[7]:index[8]] + pos[index[9]:index[10]])
print np.mean(sumsig[index[1]:index[2]] + sumsig[index[3]:index[4]]+ sumsig[index[5]:index[6]]+ sumsig[index[7]:index[8]] + sumsig[index[9]:index[10]])
print np.std(sumsig[index[1]:index[2]] + sumsig[index[3]:index[4]]+ sumsig[index[5]:index[6]]+ sumsig[index[7]:index[8]] + sumsig[index[9]:index[10]])

plt.subplot(2, 1, 1)
ax1 = plt.gca()
plt.plot(time[:index[-2]], pos[:index[-2]], color = 'indigo')
plt.ylabel("Displacement (nm)", fontsize = 14)
plt.xlim(xmin = 0, xmax = 5)
plt.xticks(size = 14)
plt.yticks(size = 14)
make_highlight_region(ax=ax1, limits = (time[0], on_off[0]),  axis='x')
make_highlight_region(ax=ax1, limits = (on_off[1], on_off[2]),  axis='x')
make_highlight_region(ax=ax1, limits = (on_off[3], on_off[4]),  axis='x')
make_highlight_region(ax=ax1, limits = (on_off[5], on_off[6]),  axis='x')
make_highlight_region(ax=ax1, limits = (on_off[7], on_off[8]),  axis='x')
make_highlight_region(ax=ax1, limits = (on_off[9], on_off[10]),  axis='x')

plt.subplot(2,1,2)
ax2 = plt.gca()
plt.plot(time[:index[-2]], sumsig[:index[-2]], color = 'seagreen')
plt.ylabel("SUM (V)", fontsize = 14)
plt.xlabel("Time (s)", fontsize = 14)
plt.xlim(xmin = 0, xmax = 5)
plt.xticks(size = 14)
plt.yticks(size = 14)
make_highlight_region(ax=ax2, limits = (time[0], on_off[0]),  axis='x')
make_highlight_region(ax=ax2, limits = (on_off[1], on_off[2]),  axis='x')
make_highlight_region(ax=ax2, limits = (on_off[3], on_off[4]),  axis='x')
make_highlight_region(ax=ax2, limits = (on_off[5], on_off[6]),  axis='x')
make_highlight_region(ax=ax2, limits = (on_off[7], on_off[8]),  axis='x')
make_highlight_region(ax=ax2, limits = (on_off[9], on_off[10]),  axis='x')

# plt.subplot(3,1,3)
# plt.plot(time, laser, color = 'r')
# plt.ylabel("Laser drive voltage / V")
# plt.xlabel("Time / s")
# plt.xlim(xmin = 0, xmax = 6)

#plt.savefig("tilt_backwards.pdf")
plt.show()


