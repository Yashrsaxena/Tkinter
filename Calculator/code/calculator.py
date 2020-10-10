import tkinter
from tkinter import *
from tkinter import messagebox
val = ""
operand = 0
operator = ""

def btn0_isClicked():
    global val
    val = val + "0"
    data.set(val)

def btn1_isClicked():
    global val
    val = val + "1"
    data.set(val)

def btn2_isClicked():
    global val
    val = val + "2"
    data.set(val)

def btn3_isClicked():
    global val
    val = val + "3"
    data.set(val)

def btn4_isClicked():
    global val
    val = val + "4"
    data.set(val)

def btn5_isClicked():
    global val
    val = val + "5"
    data.set(val)

def btn6_isClicked():
    global val
    val = val + "6"
    data.set(val)

def btn7_isClicked():
    global val
    val = val + "7"
    data.set(val)

def btn8_isClicked():
    global val
    val = val + "8"
    data.set(val)

def btn9_isClicked():
    global val
    val = val + "9"
    data.set(val)

def btnplus_isClicked():
    global operand
    global operator
    global val
    operand = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btnminus_isClicked() :
    global operand
    global operator
    global val
    operand = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btnmultiply_isClicked():
    global operand
    global operator
    global val
    operand = int(val)
    operator = "×"
    val = val + "×"
    data.set(val)

def btndivide_isClicked():
    global operand
    global operator
    global val
    operand = int(val)
    operator = "÷"
    val = val + "÷"
    data.set(val)

def btnclear_isClicked():
    global val
    global operand
    global operator
    operand = 0
    operator = ""
    val = ""
    data.set(val)

def result():
    global operand
    global operator
    global val
    temp = val
    if operator == "+":
        x = int(temp.split("+")[1])
        C = operand + x
        val = str(C)
        data.set(C)
    elif operator == "-":
        x = int(temp.split("-")[1])
        C = operand - x
        val = str(C)
        data.set(C)
    elif operator == "×":
        x = int(temp.split("×")[1])
        C = operand * x
        val = str(C)
        data.set(C)
    elif operator == "÷":
        x = int(temp.split("÷")[1])
        if x == 0:
            print("Divisibility from zero is not allowed")
            messagebox.showerror("Error", "Divisibility from zero is not allowed")
            operand = 0
            operator = ""
            val = ""
            data.set(val)
        else:
            C = int(operand / x)
            val = str(C)
            data.set(C)




root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator")

data  = StringVar()
lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("Verdana", 22),
    textvariable = data,
    background = "#ffffff",
    fg = "#000000"
)
lbl.pack(expand = True, fill = "both")

btnrow1 = Frame(root,bg="#000000")
btnrow1.pack(expand = True, fill = "both",)

btnrow2 = Frame(root,bg="#ffffff")
btnrow2.pack(expand = True, fill = "both",)

btnrow3 = Frame(root,bg="#000000")
btnrow3.pack(expand = True, fill = "both",)

btnrow4 = Frame(root,bg="#ffffff")
btnrow4.pack(expand = True, fill = "both",)

btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn1_isClicked,
)
btn1.pack(side = LEFT, expand = True, fill = "both")

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn2_isClicked
)
btn2.pack(side = LEFT, expand = True, fill = "both")

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn3_isClicked
)
btn3.pack(side = LEFT, expand = True, fill = "both")

btnplus = Button(
    btnrow1,
    text = "+",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btnplus_isClicked
)
btnplus.pack(side = LEFT, expand = True, fill = "both")




btn4 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn4_isClicked
)
btn4.pack(side = LEFT, expand = True, fill = "both")

btn5 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn5_isClicked
)
btn5.pack(side = LEFT, expand = True, fill = "both")

btn6 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn6_isClicked
)
btn6.pack(side = LEFT, expand = True, fill = "both")

btnminus = Button(
    btnrow2,
    text = "-",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btnminus_isClicked
)
btnminus.pack(side = LEFT, expand = True, fill = "both")




btn7 = Button(
    btnrow3,
    text = "7",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn7_isClicked
)
btn7.pack(side = LEFT, expand = True, fill = "both")

btn8 = Button(
    btnrow3,
    text = "8",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn8_isClicked
)
btn8.pack(side = LEFT, expand = True, fill = "both")

btn9 = Button(
    btnrow3,
    text = "9",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn9_isClicked
)
btn9.pack(side = LEFT, expand = True, fill = "both")

btnmultiply = Button(
    btnrow3,
    text = "×",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btnmultiply_isClicked
)
btnmultiply.pack(side = LEFT, expand = True, fill = "both")




btnclear = Button(
    btnrow4,
    text = "C",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btnclear_isClicked
)
btnclear.pack(side = LEFT, expand = True, fill = "both")

btn0 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn0_isClicked
)
btn0.pack(side = LEFT, expand = True, fill = "both")

btnequal = Button(
    btnrow4,
    text = "=",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = result
)
btnequal.pack(side = LEFT, expand = True, fill = "both")

btndivide = Button(
    btnrow4,
    text = "÷",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btndivide_isClicked
)
btndivide.pack(side = LEFT, expand = True, fill = "both")

root.mainloop()
