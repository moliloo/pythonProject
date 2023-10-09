from tkinter import *
from tkinter.ttk import Label


def call():
    msg = Label(w, text='Você clicou aqui')
    msg.place(x=60, y=100)


w = Tk()
w.geometry('200x110')
b = Button(text='Clique aqui', command=call)
b.place(x=30, y=20, width=120, height=25)
w.mainloop()
