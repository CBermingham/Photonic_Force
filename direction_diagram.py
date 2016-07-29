import matplotlib.pyplot as plt

#Values = [-106, -368]
#Values = [-449, 197]
#Values = [-81.9, -320, -84.2]
#Values = [-32.4, 23.2, -28.2]
#Values = [-249, 108, -58.9]
#Values = [-497, 91.1, -227]
#Values = [-520, 69, -279]
#Values = [8.15, 432, 271]
#Values = [-7.71, -300, -152]
#Values = [-324, 232, -282]
Values = [100, 100, 100]

plt.arrow(0, 1, Values[0], 0, fc="r", ec="r", head_width=0.7, head_length=20, length_includes_head=True)
plt.arrow(0, 2, Values[1], 0, fc="g", ec="g", head_width=0.7, head_length=20, length_includes_head=True)
plt.arrow(0, 3, Values[2], 0, fc="b", ec="b", head_width=0.7, head_length=20, length_includes_head=True)
plt.xlim(xmin = -550, xmax = 550)
plt.ylim(ymin = -6, ymax = 10)
frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticks([])
frame1.axes.get_yaxis().set_ticks([])

plt.savefig('arrow_plots/arrows.pdf')
plt.show()