import numpy as np
import os

import matplotlib.pyplot as plt, mpld3

fig = plt.figure(1)

for filename in os.listdir('Data'):
    
    f = open('Data/' + filename, 'r')
    
    lines = f.read().split('\n')
    l = lines.__len__() - 1
    freq = np.zeros(l)
    lim = np.zeros(l)
    
    for i in range(0, l):
        freq[i] = float(lines[i].split(',')[0])
        lim[i] = float(lines[i].split(',')[1])        
    
    f.close()
    
    plt.loglog(freq,lim)

plt.grid()
plt.xlabel("Frequency (Hz)")
plt.ylabel("$\Omega_{GW}$")

html = mpld3.fig_to_html(fig)

f = open('script.html', 'w+')
f.write(str(html))
f.close()

plt.show()