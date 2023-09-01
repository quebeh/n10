from n10 import N10
from threading import Thread
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from math import cos, sin, radians

n10 = N10('COM7') # Change to your N10 port
fig, ax = plt.subplots()
x, y = [0]*360, [0]*360
sc = ax.scatter(x, y)

def update(data):
    ax.clear()
    for i in data:
        print(i[0], i[1])
        x[round(i[0])-1] = cos(radians(i[0])) * i[1]
        y[round(i[0])-1] = sin(radians(i[0])) * -i[1]
    ax.scatter(x, y)
    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    width, height = bbox.width*fig.dpi, bbox.height*fig.dpi
    r = width/height
    dmax = max(max(x), max(y))*1.1
    dmin = min(min(x), min(y))*1.1
    ax.add_artist(Circle((0, 0), dmax*0.01 , fc='red'))
    ax.set_xlim(dmin*r, dmax*r)
    ax.set_ylim(dmin, dmax)
    plt.pause(0.0001)
    fig.canvas.draw()

plt.show(block=False)

n10.scan(update)

n10.shutdown()
