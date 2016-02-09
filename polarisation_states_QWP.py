import matplotlib.pyplot as plt

def import_data(filename):
	x = []
	y = []

	f = open(filename, 'rU')
	lines=f.readlines()
	f.close()
	for l in lines:
		b = l.split()
		x.append(float(b[0]))
		y.append(float(b[1]))
	return x, y

x45, y45 = import_data('45_example_data.txt')
x30, y30 = import_data('30_example_data.txt')
x15, y15 = import_data('15_example_data.txt')
x0, y0 = import_data('0_example_data.txt')
x_15, y_15 = import_data('minus_15_example_data.txt')
x_30, y_30 = import_data('minus_30_example_data.txt')
x_45, y_45 = import_data('minus_45_example_data.txt')


f = plt.figure()
f.subplots_adjust(wspace=0)

plt.subplot(1, 7, 1)
frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticks([])
frame1.axes.get_yaxis().set_ticks([])
plt.plot(x_45, y_45, color = 'slateblue')
plt.arrow(x_45[int(len(x_45)/2)], y_45[int(len(x_45)/2)], 0.1, 0.0, head_width = 0.15, head_length = 0.2, length_includes_head=True, color = 'slateblue')
plt.gca().set_aspect('equal')
plt.xlim(xmin=-1, xmax=1)
plt.ylim(ymin=-1, ymax=1)
plt.xlabel('-45$\degree$')

plt.subplot(1, 7, 2)
frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticks([])
frame1.axes.get_yaxis().set_ticks([])
plt.plot(x_30, y_30, color = 'slateblue')
plt.arrow(x_30[int(len(x_30)/2)], y_30[int(len(x_30)/2)], 0.1, 0.0, head_width = 0.15, head_length = 0.2, length_includes_head=True, color = 'slateblue')
plt.gca().set_aspect('equal')
plt.xlim(xmin=-1, xmax=1)
plt.ylim(ymin=-1, ymax=1)
plt.xlabel('-30$\degree$')

plt.subplot(1, 7, 3)
frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticks([])
frame1.axes.get_yaxis().set_ticks([])
plt.plot(x_15, y_15, color = 'slateblue')
plt.arrow(x_15[int(len(x_15)/2)], y_15[int(len(x_15)/2)], 0.1, 0.0, head_width = 0.15, head_length = 0.2, length_includes_head=True, color = 'slateblue')
plt.gca().set_aspect('equal')
plt.xlim(xmin=-1, xmax=1)
plt.ylim(ymin=-1, ymax=1)
plt.xlabel('-15$\degree$')

plt.subplot(1, 7, 4)
frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticks([])
frame1.axes.get_yaxis().set_ticks([])
plt.plot(x0, y0, color = 'slateblue')
plt.gca().set_aspect('equal')
plt.xlim(xmin=-1, xmax=1)
plt.ylim(ymin=-1, ymax=1)
plt.xlabel('0$\degree$ \n QWP angle $\phi$ ($\degree$)')

plt.subplot(1, 7, 5)
frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticks([])
frame1.axes.get_yaxis().set_ticks([])
plt.plot(x15, y15, color = 'slateblue')
plt.arrow(x15[0], y15[0], -0.1, 0.0, head_width = 0.15, head_length = 0.2, length_includes_head=True, color = 'slateblue')
plt.gca().set_aspect('equal')
plt.xlim(xmin=-1, xmax=1)
plt.ylim(ymin=-1, ymax=1)
plt.xlabel('15$\degree$')

plt.subplot(1, 7, 6)
frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticks([])
frame1.axes.get_yaxis().set_ticks([])
plt.plot(x30, y30, color = 'slateblue')
plt.arrow(x30[0], y30[0], -0.1, 0.0, head_width = 0.15, head_length = 0.2, length_includes_head=True, color = 'slateblue')
plt.gca().set_aspect('equal')
plt.xlim(xmin=-1, xmax=1)
plt.ylim(ymin=-1, ymax=1)
plt.xlabel('30$\degree$')

plt.subplot(1, 7, 7)
frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticks([])
frame1.axes.get_yaxis().set_ticks([])
plt.plot(x45, y45, color = 'slateblue')
plt.arrow(x45[0], y45[0], -0.1, 0.0, head_width = 0.15, head_length = 0.2, length_includes_head=True, color = 'slateblue')
plt.gca().set_aspect('equal')
plt.xlim(xmin=-1, xmax=1)
plt.ylim(ymin=-1, ymax=1)
plt.xlabel('45$\degree$')

plt.savefig('polarisation_states_QWP.pdf')

plt.show()

