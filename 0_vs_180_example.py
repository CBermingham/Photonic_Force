import csv
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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

time0p = []
pos0p = []
on_off0p = []

time90p = []
pos90p = []
on_off90p = []

time180p = []
pos180p = []
on_off180p = []

with open('p_data.csv', 'rb') as f:
	reader = csv.reader(f, None)
	for row in reader:
		time0p.append(float(row[0]))
		pos0p.append(float(row[1]))
		time180p.append(float(row[2]))
		pos180p.append(float(row[3]))
		time90p.append(float(row[4]))
		pos90p.append(float(row[5]))

with open('p_data_on_off.csv', 'rb') as f:
	reader = csv.reader(f, None)
	for row in reader:
		on_off0p.append(int(row[0]))
		on_off180p.append(int(row[1]))
		on_off90p.append(int(row[2]))

plt.subplot(1,1,1)
ax1 = plt.gca()
plt.plot(time0p, pos0p, label='cantilever oriented 0$\degree$')
plt.plot(time180p, pos180p, label='cantilever oriented 180$\degree$')
#make_highlight_region(ax=ax1, limits = (time0p[on_off0p[0]], time0p[on_off0p[1]]),  axis='x')
make_highlight_region(ax=ax1, limits = (time0p[on_off0p[2]], time0p[on_off0p[3]]),  axis='x')
make_highlight_region(ax=ax1, limits = (time0p[on_off0p[4]], time0p[on_off0p[5]]),  axis='x')
make_highlight_region(ax=ax1, limits = (time0p[on_off0p[6]], time0p[on_off0p[7]]),  axis='x')
make_highlight_region(ax=ax1, limits = (time0p[on_off0p[8]], time0p[on_off0p[9]]),  axis='x')
make_highlight_region(ax=ax1, limits = (time0p[on_off0p[10]], 5),  axis='x')
plt.xlim(xmin = 0, xmax = 5)
plt.xlabel('Time / s')
plt.legend(bbox_to_anchor=(1.05, 1.13))
plt.ylabel('Displacement / nm')

# fig = plt.gcf()
# plt.subplot(2,1,2)
# ax2 = plt.gca()
# plt.plot(time180p, pos180p)
# make_highlight_region(ax=ax2, limits = (time180p[on_off180p[1]], time180p[on_off180p[2]]),  axis='x')
# make_highlight_region(ax=ax2, limits = (time180p[on_off180p[3]], time180p[on_off180p[4]]),  axis='x')
# make_highlight_region(ax=ax2, limits = (time180p[on_off180p[5]], time180p[on_off180p[6]]),  axis='x')
# make_highlight_region(ax=ax2, limits = (time180p[on_off180p[7]], time180p[on_off180p[8]]),  axis='x')
# make_highlight_region(ax=ax2, limits = (time180p[on_off180p[9]], time180p[-1]),  axis='x')
# plt.xlabel('Time / s')
# plt.ylabel('180 degrees \n Displacement / nm')
# plt.xlim(xmin = 0, xmax = 5)












plt.show()