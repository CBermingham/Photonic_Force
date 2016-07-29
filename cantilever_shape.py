import matplotlib.pyplot as plt
import csv 
import math

displacement1 = []
error1 = []
labels1 = []
pos1 = []
f = open('cantilever_7_0.csv', 'rU')
reader = csv.reader(f, None)
for row in reader:
    displacement1.append(float(row[0]))
    error1.append(float(row[1]))
    labels1.append(str(row[2]))
    pos1.append(float(row[3]))
f.close()

displacement2 = []
error2 = []
labels2 = []
pos2 = []
f = open('cantilever_7_180a.csv', 'rU')
reader = csv.reader(f, None)
for row in reader:
    displacement2.append(float(row[0]))
    error2.append(float(row[1]))
    labels2.append(str(row[2]))
    pos2.append(float(row[3]))
f.close()

displacement3 = []
error3 = []
labels3 = []
pos3 = []
f = open('cantilever_7_180b.csv', 'rU')
reader = csv.reader(f, None)
for row in reader:
    displacement3.append(float(row[0]))
    error3.append(float(row[1]))
    labels3.append(str(row[2]))
    pos3.append(float(row[3]))
f.close()

displacement4 = []
error4 = []
labels4 = []
pos4 = []
f = open('cantilever_7_180_best.csv', 'rU')
reader = csv.reader(f, None)
for row in reader:
    displacement4.append(float(row[0]))
    error4.append(float(row[1]))
    labels4.append(str(row[2]))
    pos4.append(float(row[3]))
f.close()

sum1 = [2.167, 2.167, 2.166, 2.35, 2.01, 1.95, 1.007, 1.13]
sum2 = [1.34, 1.25, 1.31, 1.77, 3.2, 1.92, 1.129]
sum3 = [1.31, 2.29, 2.26, 2.411, 1.74, 0.977]
sum4 = [1.31, 2.29, 1.31, 2.29, 2.26, 2.411, 1.74, 0.977]

k1 = [2.57E-5, 1.43E-5, 1.36E-5, 9.38E-6, 1.64E-5, 1.5E-5, 1.81E-5, 1.52E-5]
k2 = [2.57E-5, 1.43E-5, 1.36E-5, 9.38E-6, 1.64E-5, 1.81E-5, 1.52E-5]
k3 = [1.36E-5, 9.38E-6, 1.64E-5, 1.5E-5, 1.81E-5, 1.52E-5]
k4 = [2.57E-5, 1.43E-5, 1.36E-5, 9.38E-6, 1.64E-5, 1.5E-5, 1.81E-5, 1.52E-5]
force1 = [i*j*1E3 for i, j in zip(displacement1, k1)]
force2 = [i*j*1E3  for i, j in zip(displacement2, k2)]
force3 = [i*j*1E3  for i, j in zip(displacement3, k3)]
force4 = [i*j*1E3  for i, j in zip(displacement4, k4)]

errork1 = [1.86E-6, 1.73E-7, 1.15E-7, 1.09E-7, 2.08E-7, 1.71E-7, 4.62E-7, 1.5E-7]
errork2 = [1.86E-6, 1.73E-7, 1.15E-7, 1.09E-7, 2.08E-7, 4.62E-7, 1.5E-7]
errork3 = [1.15E-7, 1.09E-7, 2.08E-7, 1.71E-7, 4.62E-7, 1.5E-7]
errork4 = [1.86E-6, 1.73E-7, 1.15E-7, 1.09E-7, 2.08E-7, 1.71E-7, 4.62E-7, 1.5E-7]

errforce1 = [math.sqrt((a/b)**2+(c/d)**2)*abs(e) for a,b,c,d,e in zip(error1, displacement1, errork1, k1, force1)]
errforce2 = [math.sqrt((a/b)**2+(c/d)**2)*abs(e) for a,b,c,d,e in zip(error2, displacement2, errork2, k2, force2)]
errforce3 = [math.sqrt((a/b)**2+(c/d)**2)*abs(e) for a,b,c,d,e in zip(error3, displacement3, errork3, k3, force3)]
errforce4 = [math.sqrt((a/b)**2+(c/d)**2)*abs(e) for a,b,c,d,e in zip(error4, displacement4, errork4, k4, force4)]

# plt.bar([i+0.2 for i in pos1], displacement1, 0.2, color = 'c', yerr = error1, ecolor = 'k', label = "0 degrees")
# plt.bar([i+0.4 for i in pos2], displacement2, 0.2, color = 'm', yerr = error2, ecolor = 'k', label = "180 degrees")
# plt.bar([i+0.6 for i in pos3], displacement3, 0.2, color = 'm', yerr = error3, ecolor = 'k')
# plt.yticks(size = 14)
# plt.xticks(size = 14)
# plt.ylabel("Displacement (nm)", size = 14)
# plt.legend(loc = 2, fontsize = 14)
# plt.text(1, 8, 'A')
# plt.text(2, 8, 'B')
# plt.text(3, 8, 'C')
# plt.text(4, 8, 'D')
# plt.text(5, 8, 'E')
# plt.text(6, 8, 'F')
# plt.text(7, 8, 'H')
# plt.text(8, 8, 'J')
# plt.gca().xaxis.set_major_locator(plt.NullLocator())
# plt.savefig("Cantilever_combined.pdf", size = 14)
# plt.show()

# plt.bar([i+0.2 for i in pos1], displacement1, 0.3, color = 'c', yerr = error1, ecolor = 'k', label = "0 degrees")
# plt.bar([i+0.5 for i in pos4], displacement4, 0.3, color = 'm', yerr = error4, ecolor = 'k', label = "180 degrees")
# plt.yticks(size = 14)
# plt.xticks(size = 14)
# plt.ylabel("Displacement (nm)", size = 14)
# plt.legend(loc = 2, fontsize = 14)
# plt.text(1, 8, 'A')
# plt.text(2, 8, 'B')
# plt.text(3, 8, 'C')
# plt.text(4, 8, 'D')
# plt.text(5, 8, 'E')
# plt.text(6, 8, 'F')
# plt.text(7, 8, 'H')
# plt.text(8, 8, 'J')
# plt.gca().xaxis.set_major_locator(plt.NullLocator())
# plt.savefig("Cantilever_combined_simple.pdf", size = 14)
# plt.show()

# plt.bar([i+0.2 for i in pos1], force1, 0.3, color = 'c', yerr = errforce1, ecolor = 'k',  label = "0 degrees")
# plt.bar([i+0.5 for i in pos4], force4, 0.3, color = 'm', yerr = errforce4, ecolor = 'k',  label = "180 degrees")
# # plt.bar([i+0.4 for i in pos2], force2, 0.2, color = 'm', yerr = errforce2, ecolor = 'k',  label = "180 degrees")
# # plt.bar([i+0.6 for i in pos3], force3, 0.2, color = 'm', yerr = errforce3, ecolor = 'k')
# plt.yticks(size = 14)
# plt.xticks(size = 14)
# plt.ylabel("Force (pN)", size = 14)
# plt.legend(loc = 2, fontsize = 14)
# plt.text(1, 0.2, 'A')
# plt.text(2, 0.2, 'B')
# plt.text(3, 0.2, 'C')
# plt.text(4, 0.2, 'D')
# plt.text(5, 0.2, 'E')
# plt.text(6, 0.2, 'F')
# plt.text(7, 0.2, 'H')
# plt.text(8, 0.2, 'J')
# plt.gca().xaxis.set_major_locator(plt.NullLocator())
# plt.savefig("Cantilever_combined_force_simple.pdf", size = 14)
# plt.show()

labels = ["A", "B", "C", "D", "E", "F", "H", "J"]

plt.bar([i+0.2 for i in pos1], sum1, 0.3, color = 'c', label = "0 degrees")
plt.bar([i+0.5 for i in pos4], sum4, 0.3, color = 'm', label = "180 degrees")
# plt.bar([i+0.4 for i in pos2], sum2, 0.2, color = 'm', label = "180 degrees")
# plt.bar([i+0.6 for i in pos3], sum3, 0.2, color = 'm', label = "180 degrees")
plt.yticks(size = 14)
plt.ylabel("Intensity (a.u.)", size = 14)
plt.legend(loc = 1, fontsize = 14)
plt.xticks([i+0.5 for i in pos1], labels)
plt.savefig("Cantilever_combined_sum.pdf", size = 14)
plt.show()