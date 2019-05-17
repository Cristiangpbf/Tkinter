from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text= 'Hombre', variable=var1).grid(row=0)

var2 = IntVar()
Checkbutton(master, text='Mujer', variable=var2,).grid(row=7)


mainloop()