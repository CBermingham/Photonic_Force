import csv
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

time = []
y = []
laser = []

f = open('151015_152124.txt', 'rU')
lines=f.readlines()
f.close()
for l in lines:
    b = l.split()
    time.append(float(b[0]))
    y.append(float(b[1]))
    laser.append(float(b[4]))

y = [i*10**9 for i in y]

on_off = []

for i in range(0, len(laser)-1):
    if (laser[i]>4 and laser[i+1] <1) or (laser[i]<1 and laser[i+1]>4):
        on_off.append(i)

zero_pos = np.mean(y[on_off[1]:on_off[2]]+y[on_off[3]:on_off[4]]+y[on_off[5]:on_off[6]]+y[on_off[7]:on_off[8]]+y[on_off[9]:on_off[10]])
pos = [i-zero_pos for i in y]

on_pos = pos[on_off[2]:on_off[3]]+pos[on_off[4]:on_off[5]]+pos[on_off[6]:on_off[7]]+pos[on_off[8]:on_off[9]]+pos[on_off[10]:on_off[11]]
other_pos = np.mean(on_pos)
off_pos = pos[on_off[1]:on_off[2]]+pos[on_off[3]:on_off[4]]+pos[on_off[5]:on_off[6]]+pos[on_off[7]:on_off[8]]+pos[on_off[9]:on_off[10]]

pos = pos[on_off[1]:]
time = time[on_off[1]:]
time = [i-time[1] for i in time]
on_off = [i-on_off[1] for i in on_off]

# fig_size = plt.rcParams["figure.figsize"]
# fig_size=[3, 6]
# plt.rcParams["figure.figsize"] = fig_size
# plt.subplot(1,1,1)

# plt.hist(on_pos, bins=40, orientation='horizontal', color = 'b')
# plt.hist(off_pos, bins=40, orientation='horizontal', color = 'b')
# plt.axhline(y=0, color = 'limegreen', linewidth = 3)
# plt.axhline(y=other_pos, linewidth = 3, color = 'limegreen')
# plt.ylabel('Displacement (nm)')
# plt.xlabel('Counts')
# plt.xticks([0, 10000, 20000, 30000], ['0', '10000', '20000', '30000'])
# plt.savefig('histograms.pdf')

fig_size = plt.rcParams["figure.figsize"]
fig_size=[8, 6]
plt.rcParams["figure.figsize"] = fig_size
plt.subplot(1,1,1)
ax1 = plt.gca()
plt.plot(time, pos, label='cantilever oriented 0$\degree$')
make_highlight_region(ax=ax1, limits = (time[on_off[2]], time[on_off[3]]),  axis='x')
make_highlight_region(ax=ax1, limits = (time[on_off[4]], time[on_off[5]]),  axis='x')
make_highlight_region(ax=ax1, limits = (time[on_off[6]], time[on_off[7]]),  axis='x')
make_highlight_region(ax=ax1, limits = (time[on_off[8]], time[on_off[9]]),  axis='x')
make_highlight_region(ax=ax1, limits = (time[on_off[10]], 5),  axis='x')
plt.axhline(y=0, color = 'limegreen', linewidth = 3)
plt.axhline(y=other_pos, linewidth = 3, color = 'limegreen')
plt.xlim(xmin = 0, xmax = 5)
plt.xlabel('Time (s)')
plt.savefig('example_for_spin_paper.pdf')

plt.show()