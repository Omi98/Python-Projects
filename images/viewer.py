from tkinter import *
from PIL import ImageTk, Image
from functions import *


def main():
    w = create_window()
    loadImages(w)

    prevButton(w)  # previous button
    exitButton(w)
    nextButton(w)

    w.mainloop()


if __name__ == "__main__":
    main()