import numpy

phase = []
amplitude = []

f = open('104122', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	phase.append(float(b[1]))
	amplitude.append(float(b[3]))

new_phase = []

for i in range(0, len(phase)):
	if phase[i] < 0.0:
		new_phase.append(360.0+phase[i])
	else: 
		new_phase.append(phase[i])

print 'Phase =', numpy.mean(new_phase), '+/-', numpy.std(new_phase)
print 'Amplitude =', numpy.mean(amplitude), '+/-', numpy.std(amplitude)