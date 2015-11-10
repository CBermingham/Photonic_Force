import numpy as np

time = []
y=[]

f = open('134449y', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	time.append(float(b[0]))
	y.append(float(b[9]))

mean=np.mean(y)
ysq = [(i-mean)**2 for i in y]
meansq = np.mean(ysq)
k = 1.38064852E-23*291/meansq
print k

