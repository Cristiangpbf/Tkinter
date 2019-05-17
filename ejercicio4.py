from tkinter import *
root = Tk()
v = IntVar()
Label(root, text="""Choose a progaming language:""", justify = LEFT, padx = 20).pack()
Radiobutton(root, text='Python', padx = 20, variable=v, value=1).pack(anchor=W)

mainloop()