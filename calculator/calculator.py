from tkinter import * 
from functions import *


def main():
    w = setWindow()  # create window
    e = entryField(w)  # create entry field
    create_buttons(w, e)  # create buttons

    w.mainloop()  # display window


if __name__ == "__main__":
    main()