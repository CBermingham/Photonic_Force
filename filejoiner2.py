import Tkinter, tkFileDialog

root = Tkinter.Tk()
root.withdraw()

file_path = tkFileDialog.askopenfilename()

f = open(file_path, 'r')
lines=f.readlines()
f.close()

time=[]
y_pos=[]

for l in lines:
	p = l.split()
	time.append(float(p[0]))
	y_pos.append(float(p[1]))


endtime=time[-1]

var = raw_input("Add another file? (enter y or n) ")

while var == 'y':
	root = Tkinter.Tk()
	root.withdraw()
	file_path = tkFileDialog.askopenfilename()
	f = open(file_path, 'r')
	lines=f.readlines()
	f.close()
	del lines[0]
	for l in lines:
		p = l.split()
		time.append(float(p[0]))
		y_pos.append(endtime+float(p[1]))
	endtime=time[-1]
	var = raw_input("Add another file? (enter y or n) ")

rows = zip(time, y_pos)

import csv
name = raw_input("Enter filename: ")
writer = csv.writer(open(name, "wb"))
for row in rows:
    writer.writerow(row)

