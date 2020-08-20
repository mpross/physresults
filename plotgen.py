import numpy as np
import os

from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.embed import file_html

plot = figure()

for filename in os.listdir('Data'):

    f = open('Data/' + filename, 'r')
    
    lines = f.read().split('\n')
    l = lines.__len__() - 1
    freq = np.zeros(l)
    lim = np.zeros(l)
    
    for i in range(0, l):
        try:
            freq[i] = float(lines[i].split(' ')[0])
            lim[i] = float(lines[i].split(' ')[1])
    
        except:
            print('Read error')
    f.close()
    
    plot.line(freq,lim)


html = file_html(plot, CDN, "my plot")

f = open('script.html', 'w+')
f.write(str(html))
f.close()