from tkinter import *
from PIL import ImageTk, Image


# global vars
global first_number
global second_number 
global math 
first_number = None
second_number = None
math = None


# create window
def createWindow():
    myWindow = Tk()
    myWindow.title("My Calculator")
    myWindow.geometry("400x600") 
    return myWindow
    #window.configure(bg="black")


# create entry field
def entryField(window):
    myEntry = Entry(window, width=45, borderwidth=5)
    myEntry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    return myEntry


def create_buttons(window, e):
    # all buttons 0-9 and +,x,-,÷
    btn0 = Button(window, text="0", padx=20, pady=10, command=lambda: btn_click(0, e))
    btn1 = Button(window, text="1", padx=20, pady=10, command=lambda: btn_click(1, e))
    btn2 = Button(window, text="2", padx=20, pady=10, command=lambda: btn_click(2, e))
    btn3 = Button(window, text="3", padx=20, pady=10, command=lambda: btn_click(3, e))
    btn4 = Button(window, text="4", padx=20, pady=10, command=lambda: btn_click(4, e))
    btn5 = Button(window, text="5", padx=20, pady=10, command=lambda: btn_click(5, e))
    btn6 = Button(window, text="6", padx=20, pady=10, command=lambda: btn_click(6, e))
    btn7 = Button(window, text="7", padx=20, pady=10, command=lambda: btn_click(7, e))
    btn8 = Button(window, text="8", padx=20, pady=10, command=lambda: btn_click(8, e))
    btn9 = Button(window, text="9", padx=20, pady=10, command=lambda: btn_click(9, e))

    btnClear = Button(window, text="Clear", padx=10, pady=10, command=lambda: btn_clear(e))
    btnEqual = Button(window, text="=", padx=20, pady=10, command=lambda: btn_equal(e))
    btnAdd = Button(window, text="+", padx=20, pady=10, command=lambda: btn_add(e))
    btnSub = Button(window, text="-", padx=20, pady=10, command=lambda: btn_sub(e))
    btnMul = Button(window, text=chr(215), padx=20, pady=10, command=lambda: btn_mul(e))
    btnDiv = Button(window, text=chr(247), padx=20, pady=10, command=lambda: btn_div(e))

    # first row
    btn7.grid(row=1, column=0, padx=5, pady=5)
    btn8.grid(row=1, column=1, padx=5, pady=5)
    btn9.grid(row=1, column=2, padx=5, pady=5)
    btnDiv.grid(row=1, column=3, padx=5, pady=5)

    # second row
    btn4.grid(row=2, column=0, padx=5, pady=5)
    btn5.grid(row=2, column=1, padx=5, pady=5)
    btn6.grid(row=2, column=2, padx=5, pady=5)
    btnMul.grid(row=2, column=3, padx=5, pady=5)

    # third row
    btn1.grid(row=3, column=0, padx=5, pady=5)
    btn2.grid(row=3, column=1, padx=5, pady=5)
    btn3.grid(row=3, column=2, padx=5, pady=5)
    btnSub.grid(row=3, column=3, padx=5, pady=5)

    # fourth row
    btn0.grid(row=4, column=0, padx=5, pady=5)
    btnClear.grid(row=4, column=1, padx=5, pady=5)
    btnEqual.grid(row=4, column=2, padx=5, pady=5)
    btnAdd.grid(row=4, column=3)


def btn_click(number, e):  # dealing with entry field
    current = e.get()  # get what's already typed and store in var
    e.delete(0, END)  # delete(END) what's already typed in - 0 index
    e.insert(0, str(current) + str(number))  
    # insert what's stored + clicked - 0 index


# clear button
def btn_clear(e):
    # delete what's already stored
    e.delete(0, END)


def btn_add(e):
    global first_number  # accessing global var
    global math
    math = "add"
    first_number = int(e.get())  # get and store first number
    e.delete(0, END)  # delete what's entered


def btn_sub(e):
    global first_number
    global math 
    math = "subtract"
    first_number = int(e.get())
    e.delete(0, END)


def btn_mul(e):
    global first_number
    global math 
    math = "multiply"
    first_number = int(e.get())
    e.delete(0, END)


def btn_div(e):
    global first_number
    global math 
    math = "divide"
    first_number = int(e.get())
    e.delete(0, END)


def btn_equal(e):
    global first_number, second_number  # accessing global vars
    second_number = int(e.get())
    e.delete(0, END)

    match math:
        case "add":
            e.insert(0, first_number + second_number)
        case "subtract":
            e.insert(0, first_number - second_number) 
        case "multiply":
            e.insert(0, first_number * second_number)
        case "divide":
            e.insert(0, first_number // second_number)


def main():
    ...


if __name__ == "__main__":
    main()