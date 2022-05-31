from tkinter import *

def somar ():
    if lb1["text"]<10:
        lb1["text"]+=1
def subtrair ():
    if lb1["text"]>-10:
        lb1["text"] -=1

root = Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.bind("-",lambda event: subtrair())
root.bind("+",lambda event: somar())

bt1 = Button(root, text= "-", command=subtrair)
bt2 = Button(root, text= "+", command=somar)
lb1 = Label(root, text=0)
bt1.grid(row=0, column=0, sticky=NSEW)
bt2.grid(row=0, column=2, sticky=NSEW)
lb1.grid(row=0, column=1, sticky=NSEW)

root.mainloop()
