import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def getData():
    ax.plot(19)

fig = plt.figure(figsize=(16, 9))
ax = plt.subplot(111)

ani = FuncAnimation(fig, getData, interval=1000)
plt.show()