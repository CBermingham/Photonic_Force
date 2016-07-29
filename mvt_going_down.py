import matplotlib.pyplot as plt
import csv

time = []
y = []
sumsig = []
z = []
y_filtered = []

# f = open("/Users/Charlotte/Documents/Code/Photonic_Force/21data/150721_114438.txt", 'rU')
# lines=f.readlines()
# f.close()
# for l in lines:
# 	b = l.split()
# 	y.append(float(b[1]))
# 	sumsig.append(float(b[7]))
# 	z.append(float(b[8]))
# 	y_filtered.append(float(b[9]))

f = open("/Users/Charlotte/Documents/Code/Photonic_Force/21data/150721_134241.txt", 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	y.append(float(b[1]))
	sumsig.append(float(b[7]))
	z.append(float(b[8]))
	y_filtered.append(float(b[9]))

f = open("/Users/Charlotte/Documents/Code/Photonic_Force/21data/150721_134247.txt", 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	y.append(float(b[1]))
	sumsig.append(float(b[7]))
	z.append(float(b[8]))
	y_filtered.append(float(b[9]))

# f = open("/Users/Charlotte/Documents/Code/Photonic_Force/21data/150721_135024.txt", 'rU')
# lines=f.readlines()
# f.close()
# for l in lines:
# 	b = l.split()
# 	y.append(float(b[1]))
# 	sumsig.append(float(b[7]))
# 	z.append(float(b[8]))
# 	y_filtered.append(float(b[9]))

# f = open("/Users/Charlotte/Documents/Code/Photonic_Force/21data/150721_135030.txt", 'rU')
# lines=f.readlines()
# f.close()
# for l in lines:
# 	b = l.split()
# 	y.append(float(b[1]))
# 	sumsig.append(float(b[7]))
# 	z.append(float(b[8]))
# 	y_filtered.append(float(b[9]))

# f = open("/Users/Charlotte/Documents/Code/Photonic_Force/21data/150721_135036.txt", 'rU')
# lines=f.readlines()
# f.close()
# for l in lines:
# 	b = l.split()
# 	y.append(float(b[1]))
# 	sumsig.append(float(b[7]))
# 	z.append(float(b[8]))
# 	y_filtered.append(float(b[9]))

# f = open("/Users/Charlotte/Documents/Code/Photonic_Force/21data/150721_135042.txt", 'rU')
# lines=f.readlines()
# f.close()
# for l in lines:
# 	b = l.split()
# 	y.append(float(b[1]))
# 	sumsig.append(float(b[7]))
# 	z.append(float(b[8]))
# 	y_filtered.append(float(b[9]))

# f = open("/Users/Charlotte/Documents/Code/Photonic_Force/21data/150721_135048.txt", 'rU')
# lines=f.readlines()
# f.close()
# for l in lines:
# 	b = l.split()
# 	y.append(float(b[1]))
# 	sumsig.append(float(b[7]))
# 	z.append(float(b[8]))
# 	y_filtered.append(float(b[9]))

y = [(y[i]*0.703/sumsig[i])*1E9 for i in range(0, len(y))]
y_filtered = [(y_filtered[i]*0.703/sumsig[i])*1E9 for i in range(0, len(y_filtered))]

z = [i+360 for i in z]

data = zip(z, y_filtered)

writer = csv.writer(open("134241.csv", "wb"))
for row in data:
    writer.writerow(row)

plt.scatter(z, y_filtered)
# plt.savefig("135011")
plt.show()