from mpl_toolkits.mplot3d import axes3d
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
#from PIL import ImageTk,Image
import numpy as np
import tkinter as a
import os



class Application(a.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.create_analysis()
        self.create_analysis1()
        self.create_analysis2()
        self.create_analysis3()

        root.geometry("450x450")

    def create_widgets(self):
        self.hi_there = a.Button(self,height=2, width=10,padx="20")
        self.hi_there["text"] = "Fetch Data"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

    def create_analysis(self):
        self.hi_there = a.Button(self,height=2, width=60,padx="20",pady="20")
        self.hi_there["text"] = "Density"
        self.hi_there["command"] = self.say_hii
        self.hi_there.pack(side="top")

    def create_analysis1(self):
        self.hi_there = a.Button(self,height=2, width=60,padx="20",pady="20")
        self.hi_there["text"] = "Bar graph"
        self.hi_there["command"] = self.say_hiii
        self.hi_there.pack(side="top")

    def create_analysis2(self):
        self.hi_there = a.Button(self,height=2, width=60,padx="20",pady="20")
        self.hi_there["text"] = "circular"
        self.hi_there["command"] = self.say_hiiii
        self.hi_there.pack(side="top")

    def create_analysis3(self):
        self.hi_there = a.Button(self,height=2, width=60,padx="20",pady="20")
        self.hi_there["text"] = "Speed"
        self.hi_there["command"] = self.say_speed
        self.hi_there.pack(side="top")

        self.quit = a.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        #self.a.Button(row=7, column=1)

        self.quit.pack(side="bottom")

    def say_hi(self):
        os.startfile('module1.py')
    

    def say_hii(self):
        os.startfile('OnDrive.png')
       # plt.show()

    def say_hiii(self):
        os.startfile('BarGraph.png')
    
    def say_hiiii(self):
        os.startfile('PolarGraph.png')
    
    def say_speed(self):
            os.startfile('speed.png')
'''
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
'''
root = a.Tk()
#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
app = Application(master=root)
#app=FullScreenApp(master=root)
app.mainloop()