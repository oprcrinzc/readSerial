import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# s = serial.Serial("/dev/ttyUSB0")
# print(s.name)
gcm = []
s = serial.Serial('/dev/ttyUSB0', 9600)
def getData(i):
    global gcm
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    cm = int(str(s.readline()).split('\\')[0].split("b'")[1])
    # print(cm)
    if len(gcm) >= 40: 
        gcm = []
        ax.cla()
    gcm.append(cm)
    ax.plot(gcm)

fig = plt.figure(figsize=(16, 9), facecolor='#DEDEDE')
ax = plt.subplot()
plt.xlim(0, 100)
plt.ylim(0, 100)
ax.set_facecolor('#DEDEDE')
ani = FuncAnimation(fig, getData, interval=0)
plt.show()