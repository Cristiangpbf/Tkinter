from tkinter import *
master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it\n (Mahatma Gandhi)"

mag = Message(master,text = whatever_you_do)
mag.config(bg='lightgreen',font=('times', 24, 'italic'))
mag.pack()
mainloop()