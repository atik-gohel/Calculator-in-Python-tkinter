import tkinter as tk
from tkinter import *
from tkinter import messagebox


tw = tk.Tk()
tw.title("Calculator by Atik Gohel")
tw.geometry('481x502')
tw.resizable(0, 0)
tw.configure(bg='#eee')


w = Canvas(tw, width=466, height=100, bg='#eee', bd=1)
w.place(x=5, y=10)
w.config(highlightbackground="#c2c2c2") #boader color


storeval=""

def press(num):
    global storeval
    storeval = storeval + str(num)
    equation.set(storeval)


def clear():
    global storeval
    storeval = ""
    equation.set("")
    


def btnequal():
    # Try and except statement is used for handling the errors like zero division error etc. 

    try:
        global storeval

        total = str(eval(storeval))

        equation.set(total)

        storeval = ""

    except:
        equation.set(" Error....")
        storeval = ""






equation = StringVar()

#input box
Entry(tw, textvariable=equation, width="17",font="times 30", bg="#eee", bd=0).place(x=8, y=35)
equation.set("Can I Help you?")



#Numeric Button
Button(tw, command=lambda: press(1), text="1", font=("times",28,"bold"), width=5, height=1, bg="#f8f8ff",bd=0).place(x=4,   y=352)
Button(tw, command=lambda: press(2), text="2", font=("times",28,"bold"), width=5, height=1, bg="#f8f8ff",bd=0).place(x=123, y=352)
Button(tw, command=lambda: press(3), text="3", font=("times",28,"bold"), width=5, height=1, bg="#f8f8ff",bd=0).place(x=242, y=352)
Button(tw, command=lambda: press(4), text="4", font=("times",28,"bold"), width=5, height=1, bg="#f8f8ff",bd=0).place(x=4,   y=278)
Button(tw, command=lambda: press(5), text="5", font=("times",28,"bold"), width=5, height=1, bg="#f8f8ff",bd=0).place(x=123, y=278)
Button(tw, command=lambda: press(6), text="6", font=("times",28,"bold"), width=5, height=1, bg="#f8f8ff",bd=0).place(x=242, y=278)
Button(tw, command=lambda: press(7), text="7", font=("times",28,"bold"), width=5, height=1, bg="#f8f8ff",bd=0).place(x=4,   y=204)
Button(tw, command=lambda: press(8), text="8", font=("times",28,"bold"), width=5, height=1, bg="#f8f8ff",bd=0).place(x=123, y=204)
Button(tw, command=lambda: press(9), text="9", font=("times",28,"bold"), width=5, height=1, bg="#f8f8ff",bd=0).place(x=242, y=204)
Button(tw, command=lambda: press(0), text="0", font=("times",28,"bold"), width=5, height=1, bg="#f8f8ff",bd=0).place(x=123, y=426)



#Arithmetic Operator Button
Button(tw, command=lambda: press("+"), text="+", font=("times",28,"bold"), width=5, height=1, bg="#E1E1E1",bd=0).place(x=361, y=352)
Button(tw, command=lambda: press("/"), text="/", font=("times",28,"bold"), width=5, height=1, bg="#E1E1E1",bd=0).place(x=361, y=130)
Button(tw, command=lambda: press("*"), text="x", font=("times",28,"bold"), width=5, height=1, bg="#E1E1E1",bd=0).place(x=361, y=204)
Button(tw, command=lambda: press("-"), text="-", font=("times",28,"bold"), width=5, height=1, bg="#E1E1E1",bd=0).place(x=361, y=278)
Button(tw, command=lambda: press("."), text=".", font=("times",28,"bold"), width=5, height=1, bg="#E1E1E1",bd=0).place(x=4,   y=426)
Button(tw, command=lambda: press("%"), text="%", font=("times",28,"bold"), width=5, height=1, bg="#E1E1E1",bd=0).place(x=242, y=130)



#Action Button
clear = Button(tw, text="CE", command=clear, font=("times",28,"bold"), width=11, height=1, bg="#E1E1E1",bd=0)
equal = Button(tw, text="=", command=btnequal, font=("times",29), width=11, height=1, bg="#E1E1E1",bd=0)

#Action Button Set Place
clear.place(x=4, y=130)
equal.place(x=242, y=426)







tw.mainloop()
