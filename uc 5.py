from tkinter import *

janela = Tk()

janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)

# widgets
bt1 = Button(janela, text="bt 1", font="arial 36")
bt2 = Button(janela, text="bt 2", font="arial 36")
bt3 = Button(janela, text="bt 3", font="arial 36")
bt4 = Button(janela, text="bt 4", font="arial 36")
bt5 = Button(janela, text="bt 5", font="arial 36")
bt6 = Button(janela, text="bt 6", font="arial 36")

bt1.grid(row=0, column=0,sticky=NSEW)
bt2.grid(row=1, column=1,sticky=NSEW)
bt3.grid(row=0, column=2,sticky=NSEW)
bt4.grid(row=1, column=0,sticky=NSEW)
bt5.grid(row=0, column=1,sticky=NSEW)
bt6.grid(row=1, column=2,sticky=NSEW)

janela.mainloop()