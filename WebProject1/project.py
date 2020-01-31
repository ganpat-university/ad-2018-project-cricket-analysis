from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig =plt.figure()
ax1 = fig.add_subplot(111,projection='3d')

def animate(i):
    pullData = open("module1.txt",'r').read()
    dataArray = pullData.split('\n')
    xar=[]
    yar=[]
    zar=[]
    for eachline in dataArray:
        if len(eachline)>1:
            x,y,z=eachline.split(',')
            xar.append(int(x))
            yar.append(int(y))
            zar.append(int(z))
    ax1.plot(xar,yar,zar)
ani= animation.FuncAnimation(fig,animate,interval=1000)
plt.show()