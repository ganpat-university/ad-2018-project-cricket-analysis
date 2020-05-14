import tkinter as tk
import requests
from tkinter import *
import os
import socket
from PIL import ImageTk
from PIL import Image


HEIGHT = 500
WIDTH = 600

root = tk.Tk()
root.title('cricket pitch player analysis')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


#canvas.create_image(0,0,image=photo)
background = tk.PhotoImage(file='cricket1.png')
label = tk.Label(root, image=background)
label.place(relwidth=1, relheight=1)

def FetchData():
    r = tk.Tk()
    r.title("Data Visualization")
    canvas = tk.Canvas(r, height=HEIGHT, width=WIDTH)
    canvas.pack()
    import socket
    import sys
    btn = Button(r, text="Bar Graph", fg="orange", command=Img1, height="2", width="40", relief=GROOVE)
    btn.place(relx=0.3, rely=0.1, relheight=0.1, relwidth=0.5)
    btn = Button(r, text="Direction of shot", fg="orange", command=Img2, height="2", width="40", relief=GROOVE)
    btn.place(relx=0.3, rely=0.3, relheight=0.1, relwidth=0.5)
    btn = Button(r, text="On Drive", fg="orange", command=Img3, height="2", width="40", relief=GROOVE)
    btn.place(relx=0.3, rely=0.5, relheight=0.1, relwidth=0.5)
    btn = Button(r, text="Leg Glance", fg="orange", command=Img4, height="2", width="40", relief=GROOVE)
    btn.place(relx=0.3, rely=0.7, relheight=0.1, relwidth=0.5)
    btn = Button(r, text="Close", fg="red", command=r.destroy, relief=GROOVE)
    btn.place(relx=0.5, rely=0.9, relheight=0.1, relwidth=0.1)


'''UDP_IP = "192.168.43.159"
UDP_PORT_NO = 50000
# target = "www.google.com"
ServerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# ServerSock.connect((target,8968))
ServerSock.bind((UDP_IP, UDP_PORT_NO))
i = 0
splitData = []

while (i < 30):
    data, addr = ServerSock.recvfrom(1024)
    newData = data.decode().split(",")
    newData[2] = newData[2][:-1]
    splitData.append(newData)
    print(data)
    i = i + 1

'''
# Function for BarGraph Graph
def Img1():
    r = Toplevel()
    r.title("BarGraph")
    canvas = Canvas(r, height=600, width=1200)
    canvas.pack()
    widget = Label(r, text='The last three shots  played by batsman', fg='red')
    widget.place(relx=0.4, rely=0.1, relheight=0.1, relwidth=0.3)
    widget.pack()
    my_image = PhotoImage(file='BarGraph.png', master=root)
    canvas.create_image(0, 0, anchor=NW, image=my_image)
    r.mainloop()


# Function for Direction Graph
def Img2():
    r = Toplevel()
    r.title("Direction Of Shot")
    canvas = Canvas(r, height=460, width=600)
    canvas.pack()
    widget = Label(r, text=' That is a fine sweep shot near the fine leg ', fg='red')
    widget.place(relx=0.4, rely=0.1, relheight=0.1, relwidth=0.3)
    widget.pack()
    my_image = PhotoImage(file='PolarGraph1.png', master=root)
    canvas.create_image(10, 10, anchor=NW, image=my_image)
    r.mainloop()


# Function for Sweep Shot Graph
def Img3():
    r = Toplevel()
    r.title("Sweep shot elevation")
    canvas = Canvas(r, height=500, width=600)
    canvas.pack()
    widget = Label(r, text='A perfect bat elevation and timing fot the shot played', fg='red')
    widget.place(relx=0.4, rely=0.1, relheight=0.1, relwidth=0.3)
    widget.pack()
    my_image = PhotoImage(file='OnDrive.png', master=root)
    canvas.create_image(10, 10, anchor=NW, image=my_image)
    r.mainloop()

def Img4():
    r = Toplevel()
    r.title("3D presentation")
    canvas = Canvas(r, height=450, width=600)
    canvas.pack()
    widget = Label(r, text='Visual Presentation of shot along with bat of player', fg='red')
    widget.place(relx=0.4, rely=0.1, relheight=0.1, relwidth=0.3)
    widget.pack()
    my_image = PhotoImage(file='leg glance.png', master=root)
    canvas.create_image(0, 0, anchor=NW, image=my_image)
    r.mainloop()


btn = tk.Button(root, text="Play a Shot", fg='red', font=40, bg='yellow', command=FetchData, relief=GROOVE)
btn.place(relx=0.35, rely=0.25, relheight=0.05, relwidth=0.3)
btn = tk.Button(root, text="Quit", fg='red', command=root.destroy, bg='skyblue', relief=GROOVE)
btn.place(relx=0.46, rely=0.85, relheight=0.08, relwidth=0.1)

root.mainloop()
