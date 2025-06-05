from tkinter import *
import random
screen = Tk()
screen.title("bob")
screen.geometry('330x250')
screen.configure(bg="#C96868")
screen.resizable(False,False)
def press(num):
    e.insert(END, num)

def clear():
    e.delete(0,END)
def calc():
    try:
        a = e.get()
        result = eval(a)
        e.delete(0,END)
        e.insert(END,result)
    except:
        e.delete(0,END)
        e.insert(END,"ERROR")
e = Entry(font=("Arial",20),width=20,bg="#C96868",fg="white")
b1 = Button(screen, text="1", bg="#C96868", fg="white", width=10, height=2 , command=lambda : press("1"))
b2 = Button(screen, text="2", bg="#C96868", fg="white", width=10, height=2, command=lambda : press("2"))
b3 = Button(screen, text="3", bg="#C96868", fg="white", width=10, height=2, command=lambda : press("3"))
b4 = Button(screen, text="4", bg="#C96868", fg="white", width=10, height=2, command=lambda : press("4"))
b5 = Button(screen, text="5", bg="#C96868", fg="white", width=10, height=2, command=lambda : press("5"))
b6 = Button(screen, text="6", bg="#C96868", fg="white", width=10, height=2, command=lambda : press("6"))
b7 = Button(screen, text="7", bg="#C96868", fg="white", width=10, height=2, command=lambda : press("7"))
b8 = Button(screen, text="8", bg="#C96868", fg="white", width=10, height=2, command=lambda : press("8"))
b9 = Button(screen, text="9", bg="#C96868", fg="white", width=10, height=2, command=lambda : press("9"))
b0 = Button(screen, text="0", bg="#C96868", fg="white", width=10, height=2, command=lambda : press("0"))
bTeleia = Button(screen, text=".", bg="#C96868", fg="white", width=10, height=2, command=lambda : press("."))
bC = Button(screen, text="C", bg="#C96868", fg="white", width=10, height=2,command= clear)
bEqual =  Button(screen, text="=", bg="black", fg="white", width=10, height=2, command=calc)


bMult = Button(screen, text="*", bg="#C96868", fg="white", width=10, height=2, command=lambda : press("*"))
bDiv = Button(screen, text="/", bg="#C96868", fg="white", width=10, height=2, command=lambda : press("/"))
bAdd = Button(screen, text="+", bg="#C96868", fg="white", width=10, height=2, command=lambda : press("+"))
bMinus = Button(screen, text="-", bg="#C96868", fg="white", width=10, height=2, command=lambda : press("-"))
e.grid(row = 0 , column = 0 ,columnspan=4)
b7.grid(row = 1 , column = 0)
b8.grid(row = 1 , column = 1)
b9.grid(row = 1 , column = 2)
bAdd.grid(row =1 , column = 3)
b4.grid(row = 2 , column = 0)
b5.grid(row = 2 , column = 1)
b6.grid(row = 2 , column = 2)
bMinus.grid(row = 2 , column = 3)
b1.grid(row = 3 , column = 0)
b2.grid(row = 3 , column = 1)
b3.grid(row = 3 , column = 2)
bMult.grid(row = 3 , column = 3)
b0.grid(row = 4 , column = 1)
bTeleia.grid(row=4 , column=2)
bC.grid(row=4 , column=0)
bDiv.grid(row=4 , column=3)
bEqual.grid(row=5 , column=1)










screen.mainloop()