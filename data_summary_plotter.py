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

plt.subplot(3,3,1)
ax1 = plt.gca()
ax1.set_title('p polarised (shaded) / off')
plt.plot(time0p, pos0p)
#make_highlight_region(ax=ax1, limits = (time0p[on_off0p[0]], time0p[on_off0p[1]]),  axis='x')
make_highlight_region(ax=ax1, limits = (time0p[on_off0p[2]], time0p[on_off0p[3]]),  axis='x')
make_highlight_region(ax=ax1, limits = (time0p[on_off0p[4]], time0p[on_off0p[5]]),  axis='x')
make_highlight_region(ax=ax1, limits = (time0p[on_off0p[6]], time0p[on_off0p[7]]),  axis='x')
make_highlight_region(ax=ax1, limits = (time0p[on_off0p[8]], time0p[on_off0p[9]]),  axis='x')
make_highlight_region(ax=ax1, limits = (time0p[on_off0p[10]], time0p[-1]),  axis='x')
plt.xlim(xmin = 0, xmax = 5)
plt.ylabel('0 degrees \n Displacement / nm')

fig = plt.gcf()
plt.subplot(3,3,4)
ax2 = plt.gca()
plt.plot(time180p, pos180p)
make_highlight_region(ax=ax2, limits = (time180p[on_off180p[1]], time180p[on_off180p[2]]),  axis='x')
make_highlight_region(ax=ax2, limits = (time180p[on_off180p[3]], time180p[on_off180p[4]]),  axis='x')
make_highlight_region(ax=ax2, limits = (time180p[on_off180p[5]], time180p[on_off180p[6]]),  axis='x')
make_highlight_region(ax=ax2, limits = (time180p[on_off180p[7]], time180p[on_off180p[8]]),  axis='x')
make_highlight_region(ax=ax2, limits = (time180p[on_off180p[9]], time180p[-1]),  axis='x')
plt.ylabel('180 degrees \n Displacement / nm')
plt.xlim(xmin = 0, xmax = 5)

plt.subplot(3,3,7)
ax3 = plt.gca()
plt.plot(time90p, pos90p)
#make_highlight_region(ax=ax3, limits = (time90p[on_off90p[0]], time90p[on_off90p[1]]),  axis='x')
make_highlight_region(ax=ax3, limits = (time90p[on_off90p[2]], time90p[on_off90p[3]]),  axis='x')
make_highlight_region(ax=ax3, limits = (time90p[on_off90p[4]], time90p[on_off90p[5]]),  axis='x')
make_highlight_region(ax=ax3, limits = (time90p[on_off90p[6]], time90p[on_off90p[7]]),  axis='x')
make_highlight_region(ax=ax3, limits = (time90p[on_off90p[8]], time90p[on_off90p[9]]),  axis='x')
make_highlight_region(ax=ax3, limits = (time90p[on_off90p[10]], time90p[-1]),  axis='x')
plt.xlabel('Time / s')
plt.xlim(xmin = 0, xmax = 5)
plt.ylabel('270 degrees \n Displacement / nm')


time0s = []
pos0s = []
on_off0s = []

time90s = []
pos90s = []
on_off90s = []

time180s = []
pos180s = []
on_off180s = []

with open('s_data.csv', 'rb') as f:
	reader = csv.reader(f, None)
	for row in reader:
		time0s.append(float(row[0]))
		pos0s.append(float(row[1]))
		time180s.append(float(row[2]))
		pos180s.append(float(row[3]))
		time90s.append(float(row[4]))
		pos90s.append(float(row[5]))


with open('s_data_on_off.csv', 'rb') as f:
	reader = csv.reader(f, None)
	for row in reader:
		on_off0s.append(int(row[0]))
		on_off180s.append(int(row[1]))
		on_off90s.append(int(row[2]))

plt.subplot(3,3,2)
ax4 = plt.gca()
ax4.set_title('s polarised (shaded) / off')
plt.plot(time0s, pos0s)
make_highlight_region(ax=ax4, limits = (time0s[on_off0s[1]], time0s[on_off0s[2]]),  axis='x')
make_highlight_region(ax=ax4, limits = (time0s[on_off0s[3]], time0s[on_off0s[4]]),  axis='x')
make_highlight_region(ax=ax4, limits = (time0s[on_off0s[5]], time0s[on_off0s[6]]),  axis='x')
make_highlight_region(ax=ax4, limits = (time0s[on_off0s[7]], time0s[on_off0s[8]]),  axis='x')
make_highlight_region(ax=ax4, limits = (time0s[on_off0s[9]], time0s[on_off0s[10]]),  axis='x')
plt.xlim(xmin = 0, xmax = 5)


plt.subplot(3,3,5)
ax5 = plt.gca()
plt.plot(time180s, pos180s)
make_highlight_region(ax=ax5, limits = (time180s[on_off180s[0]], time180s[on_off180s[1]]),  axis='x')
make_highlight_region(ax=ax5, limits = (time180s[on_off180s[2]], time180s[on_off180s[3]]),  axis='x')
make_highlight_region(ax=ax5, limits = (time180s[on_off180s[4]], time180s[on_off180s[5]]),  axis='x')
make_highlight_region(ax=ax5, limits = (time180s[on_off180s[6]], time180s[on_off180s[7]]),  axis='x')
make_highlight_region(ax=ax5, limits = (time180s[on_off180s[8]], time180s[on_off180s[9]]),  axis='x')
plt.xlim(xmin = 0, xmax = 5)




plt.subplot(3,3,8)
ax6 = plt.gca()
plt.plot(time90s, pos90s)
make_highlight_region(ax=ax6, limits = (time90s[on_off90s[1]], time90s[on_off90s[2]]),  axis='x')
make_highlight_region(ax=ax6, limits = (time90s[on_off90s[3]], time90s[on_off90s[4]]),  axis='x')
make_highlight_region(ax=ax6, limits = (time90s[on_off90s[5]], time90s[on_off90s[6]]),  axis='x')
make_highlight_region(ax=ax6, limits = (time90s[on_off90s[7]], time90s[on_off90s[8]]),  axis='x')
make_highlight_region(ax=ax6, limits = (time90s[on_off90s[9]], time90s[on_off90s[10]]),  axis='x')
plt.xlabel('Time / s')
plt.xlim(xmin = 0, xmax = 5)

time0circ = []
pos0circ = []
on_off0circ = []

time90circ = []
pos90circ = []
on_off90circ = []

time180circ = []
pos180circ = []
on_off180circ = []

with open('circ_data.csv', 'rb') as f:
	reader = csv.reader(f, None)
	for row in reader:
		time0circ.append(float(row[0]))
		pos0circ.append(float(row[1]))
		time180circ.append(float(row[2]))
		pos180circ.append(float(row[3]))
		time90circ.append(float(row[4]))
		pos90circ.append(float(row[5]))


with open('circ_data_on_off.csv', 'rb') as f:
	reader = csv.reader(f, None)
	for row in reader:
		on_off0circ.append(int(row[0]))
		on_off180circ.append(int(row[1]))
		on_off90circ.append(int(row[2]))

plt.subplot(3,3,3)
ax7 = plt.gca()
ax7.set_title('Left / right circularly polarised')
plt.plot(time0circ, pos0circ)
make_highlight_region(ax=ax7, limits = (time0circ[on_off0circ[1]], time0circ[on_off0circ[2]]),  axis='x')
make_highlight_region(ax=ax7, limits = (time0circ[on_off0circ[3]], time0circ[on_off0circ[4]]),  axis='x')
make_highlight_region(ax=ax7, limits = (time0circ[on_off0circ[5]], time0circ[on_off0circ[6]]),  axis='x')
make_highlight_region(ax=ax7, limits = (time0circ[on_off0circ[7]], time0circ[on_off0circ[8]]),  axis='x')
make_highlight_region(ax=ax7, limits = (time0circ[on_off0circ[9]], time0circ[on_off0circ[10]]),  axis='x')
plt.xlim(xmin = 0, xmax = 5)

plt.subplot(3,3,6)
ax8 = plt.gca()
plt.plot(time180circ, pos180circ)
#make_highlight_region(ax=ax8, limits = (time180circ[on_off180circ[0]], time180circ[on_off180circ[1]]),  axis='x')
make_highlight_region(ax=ax8, limits = (time180circ[on_off180circ[1]], time180circ[on_off180circ[2]]),  axis='x')
make_highlight_region(ax=ax8, limits = (time180circ[on_off180circ[3]], time180circ[on_off180circ[4]]),  axis='x')
make_highlight_region(ax=ax8, limits = (time180circ[on_off180circ[5]], time180circ[on_off180circ[6]]),  axis='x')
make_highlight_region(ax=ax8, limits = (time180circ[on_off180circ[7]], time180circ[on_off180circ[8]]),  axis='x')
make_highlight_region(ax=ax8, limits = (time180circ[on_off180circ[9]], time180circ[on_off180circ[10]]),  axis='x')
plt.xlim(xmin = 0, xmax = 5)



plt.subplot(3,3,9)
ax9 = plt.gca()
plt.plot(time90circ, pos90circ)
make_highlight_region(ax=ax9, limits = (time90circ[on_off90circ[0]], time90circ[on_off90circ[1]]),  axis='x')
make_highlight_region(ax=ax9, limits = (time90circ[on_off90circ[2]], time90circ[on_off90circ[3]]),  axis='x')
make_highlight_region(ax=ax9, limits = (time90circ[on_off90circ[4]], time90circ[on_off90circ[5]]),  axis='x')
make_highlight_region(ax=ax9, limits = (time90circ[on_off90circ[6]], time90circ[on_off90circ[7]]),  axis='x')
make_highlight_region(ax=ax9, limits = (time90circ[on_off90circ[8]], time90circ[on_off90circ[9]]),  axis='x')
#make_highlight_region(ax=ax9, limits = (time90circ[on_off90circ[10]], time90circ[on_off90circ[11]]),  axis='x')
plt.xlabel('Time / s')
plt.xlim(xmin = 0, xmax = 5)

plt.subplots_adjust(hspace=0.4)
fig.set_size_inches(10,10)


plt.show()