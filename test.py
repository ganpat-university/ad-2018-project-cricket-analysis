from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig =plt.figure()
ax1 = fig.add_subplot(111,projection='polar')
def animate(i):
    pullData = open("module2.txt",'r').read()
    dataArray = pullData.split('\n')
    xar=[]
    yar=[]
    zar=[]
    for eachline in dataArray:
        if len(eachline)>1:
            x,y,z=eachline.split(',')
            xar.append(float(x))
            yar.append(float(y))
            zar.append(float(z))
    ax1.plot(xar,yar,zar)
    
ani= animation.FuncAnimation(fig,animate,interval=1000)
plt.show()