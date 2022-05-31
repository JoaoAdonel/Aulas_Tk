from tkinter import *
def soma():
    print()
    if en1.get().isnumeric() and en2.get().isnumeric():
        lb1{"text"}=float(en1.get()) + float(en2.get())
    else:
        lb1{"text"}="valor invalido"

janela=tk()

fn= "arial 36"


lb1=label(janelatext=resultado, text="arial36")
entry1=entry(janela, font="arial 36")
entry2=entry(janela, font="arial 36")
btn1 = button(janela, text=soma, font=fn, comand=soma)

label1.pack()
entry1.pack()
btn1.pack()

janela.mainloop()
