import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import csv

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

def read_data_y(path):
    t = []
    p = []
    time = []
    pos = []
    filenames = []
    s = []
    l = []
    sum_sig = []
    laser = []
    directory = os.listdir(path)
    for filename in directory:
        if 'pos' in filename:
            with open(path + '/' + filename) as f:
                t = []
                p = []
                next(f)
                for line in f:
                    b = line.split()
                    t.append(float(b[0]))
                    p.append(float(b[1]))
            time.append(t)
            pos.append(p)
            filenames.append(filename)
        if 'sum' in filename:
            with open(path + '/' + filename) as f:
                s = []
                l = []
                next(f)
                for line in f:
                    b = line.split()
                    s.append(float(b[5]))
                    l.append(float(b[3]))
            sum_sig.append(s)
            laser.append(l)
            filenames.append(filename)
    return time, pos, filenames, sum_sig, laser

def plot_graph(index):
    on_off = []
    for i in range(0, len(laser[index])-1):
        if (laser[index][i]>4 and laser[index][i+1] <1) or (laser[index][i]<1 and laser[index][i+1]>4):
            on_off.append(i)

    newtime = []
    newpos = []

    for i in range(0, len(on_off)-1):
        newpos = newpos + pos[index][on_off[i]+50:on_off[i+1]]
    for i in range(0, len(newpos)):
        newtime.append(i/640.0)
    newpos = [i-np.mean(newpos) for i in newpos]

    plt.subplot(3,1,index)
    ax1 = plt.gca()
    ax1.set_title('0 degrees')
    make_highlight_region(ax=ax1, limits = (newtime[0], newtime[270]),  axis='x')
    make_highlight_region(ax=ax1, limits = (newtime[540], newtime[810]),  axis='x')
    make_highlight_region(ax=ax1, limits = (newtime[1080], newtime[1350]),  axis='x')
    make_highlight_region(ax=ax1, limits = (newtime[1620], newtime[1890]),  axis='x')
    make_highlight_region(ax=ax1, limits = (newtime[2160], newtime[2430]),  axis='x')
    make_highlight_region(ax=ax1, limits = (newtime[2700], newtime[-1]),  axis='x')
    plt.xlabel('Time / s')
    plt.show()


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

f = open('0_pos_circ.txt', 'rU')
lines=f.readlines()[1:]
f.close()
for l in lines:
    b = l.split()
    time0.append(float(b[0]))
    pos0.append(float(b[1]))

f = open('0_sum_circ.txt', 'rU')
lines=f.readlines()[1:]
f.close()
for l in lines:
    b = l.split()
    sumsig0.append(float(b[5]))
    laser0.append(float(b[3]))

f = open('180_pos_circ.txt', 'rU')
lines=f.readlines()[1:]
f.close()
for l in lines:
    b = l.split()
    time180.append(float(b[0]))
    pos180.append(float(b[1]))

f = open('180_sum_circ.txt', 'rU')
lines=f.readlines()[1:]
f.close()
for l in lines:
    b = l.split()
    sumsig180.append(float(b[5]))
    laser180.append(float(b[3]))

f = open('90_pos_circ.txt', 'rU')
lines=f.readlines()[1:]
f.close()
for l in lines:
    b = l.split()
    time90.append(float(b[0]))
    pos90.append(float(b[1]))

f = open('90_sum_circ.txt', 'rU')
lines=f.readlines()[1:]
f.close()
for l in lines:
    b = l.split()
    sumsig90.append(float(b[5]))
    laser90.append(float(b[3]))

print time90[-1]

on_off0 = []

for i in range(0, len(laser0)-1):
    if (laser0[i]>4 and laser0[i+1] <1) or (laser0[i]<1 and laser0[i+1]>4):
        on_off0.append(i)
print on_off0[0]

zero_pos0 = np.mean(pos0[on_off0[0]:on_off0[1]])
pos0 = [i-zero_pos0 for i in pos0]

pos0 = pos0[on_off0[1]:]
time0 = time0[on_off0[1]:]
time0 = [i-time0[1] for i in time0]
on_off0 = [i-on_off0[1] for i in on_off0]


on_off180 = []

for i in range(0, len(laser180)-1):
    if (laser180[i]>4 and laser180[i+1] <1) or (laser180[i]<1 and laser180[i+1]>4):
        on_off180.append(i)

zero_pos180 = np.mean(pos180[on_off180[0]:on_off180[1]])
pos180 = [i-zero_pos180 for i in pos180]

pos180 = pos180[on_off180[1]:]
time180 = time180[on_off180[1]:]
time180 = [i-time180[1] for i in time180]
on_off180 = [i-on_off180[1] for i in on_off180]

on_off90 = []

for i in range(0, len(laser90)-1):
    if (laser90[i]>4 and laser90[i+1] <1) or (laser90[i]<1 and laser90[i+1]>4):
        on_off90.append(i)

zero_pos90 = np.mean(pos90[on_off90[1]:on_off90[2]])
pos90 = [i-zero_pos90 for i in pos90]

pos90 = pos90[on_off90[0]:]
time90 = time90[on_off90[0]:]
time90 = [i-time90[0] for i in time90]
on_off90 = [i-on_off90[0] for i in on_off90]

rows = zip(time0, pos0, time180, pos180, time90, pos90)

name = raw_input("Enter filename: ")
writer = csv.writer(open(name, "wb"))
for row in rows:
    writer.writerow(row)

rows = zip(on_off0, on_off180, on_off90)

name = raw_input("Enter filename: ")
writer = csv.writer(open(name, "wb"))
for row in rows:
    writer.writerow(row)

