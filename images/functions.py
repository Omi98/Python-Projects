from tkinter import *
from PIL import ImageTk, Image


global myLabel
global next_Button
global prev_Button
global image_list


def create_window():
    myWindow = Tk()
    myWindow.title("Image Viewer")
    #myWindow.geometry("500x500")
    myWindow.configure(background="#f5ebe0")
    return myWindow


def loadImages(myWindow):
    global myLabel
    global next_Button
    global prev_Button
    global image_list

    # open images
    img1 = Image.open("images\moon-branches.jpg")
    img2 = Image.open("images\moon-clouds.jpg")
    img3 = Image.open("images\moon-flowers.jpg")
    img4 = Image.open("images\moon-reflection.jpg")
    img5 = Image.open("images\moon-sea.jpg")

    # create copy + thumbnails
    thumbnail_img1 = img1.copy()
    thumbnail_img1.thumbnail((500, 400))

    thumbnail_img2 = img2.copy()
    thumbnail_img2.thumbnail((500, 400))

    thumbnail_img3 = img3.copy()
    thumbnail_img3.thumbnail((500, 400))

    thumbnail_img4 = img4.copy()
    thumbnail_img4.thumbnail((500, 400))

    thumbnail_img5 = img5.copy()
    thumbnail_img5.thumbnail((500, 400))

    # deal as photoimage
    image1 = ImageTk.PhotoImage(thumbnail_img1)
    image2 = ImageTk.PhotoImage(thumbnail_img2)
    image3 = ImageTk.PhotoImage(thumbnail_img3)
    image4 = ImageTk.PhotoImage(thumbnail_img4)
    image5 = ImageTk.PhotoImage(thumbnail_img5)

    image_list = [image1, image2, image3, image4, image5]

    # create label to show status of images
    status = Label(myWindow, text="Image 1 of " + str(len(image_list)), border=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    # create a label, set it to 1st image
    myLabel = Label(myWindow, image=image1)
    myLabel.grid(row=0, column=0, columnspan=3)


def prevButton(myWindow):
    prev_Button = Button(myWindow, text="<<", state=DISABLED)
    prev_Button.grid(row=1, column=0, pady=10)


def exitButton(myWindow):
    exit_Button = Button(myWindow, text="Exit Viewer", command=myWindow.quit)
    exit_Button.grid(row=1, column=1, pady=10)
    #myButton.place(x=270, y=150)


def nextButton(myWindow):
    # current image index is 1 (will be called as 1 - 1 = 0)
    next_Button = Button(myWindow, text=">>", command=lambda:next(myWindow, 1))
    next_Button.grid(row=1, column=2, pady=10)


def next(myWindow, image_num):
    global myLabel
    global next_Button
    global prev_Button
    global image_list

    # forget what's already being played by label in grid
    myLabel.grid_forget()
    # display new image - define label again
    myLabel = Label(myWindow, image=image_list[image_num])
    # using - 1 because list starts at 0, so whatever image number is
    # passed, we need to display the image with list indexing
    # so, image_num = 1 -> 1 - 1 = 0, so 0th index img will be displayed

    # define << button - to remove disabled state
    prev_Button = Button(myWindow, text="<<", command=lambda:back(myWindow, image_num-1))

    # if image_number is out of index
    # make next button disabled
    if image_num >= 4:
        next_Button = Button(myWindow, text=">>", state=DISABLED)
    else:
        # update next button - define again
        next_Button = Button(myWindow, text=">>", command=lambda:next(myWindow, image_num+1))
    
    myLabel.grid(row=0, column=0, columnspan=3)  # show updated image 
    next_Button.grid(row=1, column=2)  # show >> button
    prev_Button.grid(row=1, column=0)  # show << button

    # update status
    status = Label(myWindow, text="Image " + str(image_num+1) + " of " + str(len(image_list)), border=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(myWindow, image_num):
    global myLabel
    global next_Button
    global prev_Button
    global image_list

    myLabel.grid_forget()  # forget the current image
    myLabel = Label(myWindow, image=image_list[image_num])  # display new image

    next_Button = Button(myWindow, text=">>", command=lambda:next(myWindow, image_num+1))

    if image_num <= 0:
        prev_Button = Button(myWindow, text="<<", state=DISABLED)
    else:
        prev_Button = Button(myWindow, text="<<", command=lambda:back(myWindow, image_num-1))

    myLabel.grid(row=0, column=0, columnspan=3)
    next_Button.grid(row=1, column=2)
    prev_Button.grid(row=1, column=0)

    # update status
    status = Label(myWindow, text="Image " + str(image_num-(-1)) + " of " + str(len(image_list)), border=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def main():
    ...

if __name__ == "__main__":
    main()