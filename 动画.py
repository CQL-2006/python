import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
t = np.linspace(0,2*np.pi,200)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t)- 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

fig,ax = plt.subplots(figsize = (6,6))
ax.set_xlim(-20,20)
ax.set_ylim(-20,20)
ax.set_title("Heart to LXZ")
ax.axis('equal')
ax.axis('off')

line, = ax.plot([],[],color = "red",linewidth = 2.5)

def update(frame):
    #frame是自动传入数字从0到200
    #x[:frame]:只取前frame个点，随着它变大线变长
    line.set_data(x[:frame],y[:frame])
    return line,

ani = FuncAnimation(fig,update,frames = len(t),interval = 30,blit=True)

plt.show()