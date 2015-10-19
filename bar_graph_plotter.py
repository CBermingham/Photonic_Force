import numpy as np
import matplotlib.pyplot as plt



N = 3
shortMeans100 = (18.3, 3.8, 1)
shortStd100 =   (4.8, 0.98, 0)

longMeans100 = (12.1, 1.8, 1)
longStd100 =   (2.6, 0.42, 0)

shortMeans50 = (1.03, 0.53, 1)
shortStd50 = (0.12, 0.058, 0)

longMeans50 = (1.07, 0.52, 1)
longStd50 = (0.14, 0.04, 0)

Means200 = (1, 1, 1)
Std200 = (0, 0, 0)

Meanscoated = (1, 1, 1)
Stdcoated = (0, 0, 0)

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(7, 7))
ind = np.arange(N)
width = 0.35

pos = 0.87

ax[0][0].bar(ind, shortMeans50, width, color=['r', 'g', 'b'], yerr=shortStd50, ecolor = 'k')
ax[0][0].set_xticks(ind+width/2)
ax[0][0].tick_params(axis='x', which='both', bottom='off', top='off')
ax[0][0].set_xticklabels( ('641', '562', '488') )
ax[0][0].annotate('(a)', (pos, pos), textcoords='axes fraction', size=16)


ax[0][1].bar(ind, longMeans50, width, color=['r', 'g', 'b'], yerr=longStd50, ecolor = 'k')
ax[0][1].set_xticks(ind+width/2)
ax[0][1].tick_params(axis='x', which='both', bottom='off', top='off')
ax[0][1].set_xticklabels( ('641', '562', '488') )
ax[0][1].annotate('(b)', (pos, pos), textcoords='axes fraction', size=16)


ax[1][0].bar(ind, shortMeans100, width, color=['r', 'g', 'b'], yerr=shortStd100, ecolor = 'k')
ax[1][0].set_xticks(ind+width/2)
ax[1][0].tick_params(axis='x', which='both', bottom='off', top='off')
ax[1][0].set_xticklabels( ('641', '562', '488') )
ax[1][0].annotate('(c)', (pos, pos), textcoords='axes fraction', size=16)


ax[1][1].bar(ind, longMeans100, width, color=['r', 'g', 'b'], yerr=longStd100, ecolor = 'k')
ax[1][1].set_xticks(ind+width/2)
ax[1][1].tick_params(axis='x', which='both', bottom='off', top='off')
ax[1][1].set_xticklabels( ('641', '562', '488') )
ax[1][1].annotate('(d)', (pos, pos), textcoords='axes fraction', size=16)

#ax[2][0].bar(ind, Means200, width, color=['r', 'g', 'b'], yerr=Std200, ecolor = 'k')
#ax[2][0].set_xticks(ind+width/2)
#ax[2][0].tick_params(axis='x', which='both', bottom='off', top='off')
#ax[2][0].set_xticklabels( ('641', '562', '488') )
#ax[2][0].annotate('(c)', (pos, pos), textcoords='axes fraction', size=16)


#ax[2][1].bar(ind, Meanscoated, width, color=['r', 'g', 'b'], yerr=Stdcoated, ecolor = 'k')
#ax[2][1].set_xticks(ind+width/2)
#ax[2][1].tick_params(axis='x', which='both', bottom='off', top='off')
#ax[2][1].set_xticklabels( ('641', '562', '488') )
#ax[2][1].annotate('(d)', (pos, pos), textcoords='axes fraction', size=16)


fig.text(0.5, 0.015, 'Drive laser wavelength / nm', ha='center', va='center')
fig.text(0.02, 0.5, 'Relative amplitude of cantilever oscillations', ha='center', va='center', rotation='vertical')
plt.subplots_adjust(left = 0.08, top=0.98, right=0.99, bottom=0.05)

plt.show()
