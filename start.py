from tkinter import *
import tkinter.font as font

gui = Tk(className='Python Examples - Button')
gui.geometry("500x200")

# define font
myFont = font.Font(weight="bold")

# create button
button = Button(gui, text='Play', bg='#0052cc', fg='#ffffff')
# apply font to the button label
button['font'] = myFont
# add button to gui window
button.pack()

gui.mainloop() 