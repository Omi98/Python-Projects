from tkinter import * 
from functions import *
from PIL import ImageTk, Image


def main():
    w = createWindow()  # create window
    w.iconbitmap("D:\TkinterProjects\calculator\images\bitmap-cal.ico")
    e = entryField(w)  # create entry field
    create_buttons(w, e)  # create buttons

    w.mainloop()  # display window


if __name__ == "__main__":
    main()