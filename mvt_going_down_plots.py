import csv
import matplotlib.pyplot as plt

z1 = []
y1 = []
z2 = []
y2 = []
z3 = []
y3 = []

f = open("132106.csv", 'rU')
reader = csv.reader(f, None)
for row in reader:
    z1.append(float(row[0]))
    y1.append(float(row[1]))
f.close()

f = open("134241.csv", 'rU')
reader = csv.reader(f, None)
for row in reader:
    z2.append(float(row[0]))
    y2.append(float(row[1]))
f.close()

f = open("135011.csv", 'rU')
reader = csv.reader(f, None)
for row in reader:
    z3.append(float(row[0]))
    y3.append(float(row[1]))
f.close()

#plt.scatter(z1, y1, s = 3, marker = 'o', color = 'b')
# plt.scatter(z2, y2, s = 3, marker = 'o', color = 'g')
plt.scatter(z3, y3, s = 3, marker = 'o', color = 'r')
plt.xlabel("z position (nm)")
plt.ylabel("y position (nm)")


plt.savefig("0_degrees_beam out")
plt.show()