import numpy as np
import os

import matplotlib.pyplot as plt
import mpld3
from mpld3 import plugins

fig = plt.figure(1)

for filename in os.listdir('Data'):
    
    f = open('Data/StochasticGWLimits/' + filename, 'r')
    
    lines = f.read().split('\n')
    l = lines.__len__() - 1
    freq = np.zeros(l)
    lim = np.zeros(l)
    
    for i in range(0, l):
        freq[i] = float(lines[i].split(',')[0])
        lim[i] = float(lines[i].split(',')[1])        
    
    f.close()
    
    if filename[:-4]=='EarthMode':
        
        plt.plot(freq,lim, color='k',label=filename)
        plt.text(freq[-1],lim[0]*10,filename[:-4])
    else:   
        
        plt.loglog(freq,lim,color='k',label=filename)

        if len(lim)<10:
            plt.text(freq[0],lim[0]*10,filename[:-4])
        else:
            if lim[0]<lim[-1]:
                plt.text(freq[0],lim[-1],filename[:-4])
            else:
                plt.text(freq[-1]/100,lim[-1]*100,filename[:-4])

plt.grid()
plt.xlabel("Frequency (Hz)")
plt.ylabel("$\Omega_{GW}$")



html = mpld3.fig_to_html(fig)

f = open('script.html', 'w+')
f.write(str(html))
f.close()

plt.show()
