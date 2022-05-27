from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkinter import messagebox
import tkinter.font as font
from PIL import Image
from PIL import ImageTk
from img_conversion import img_dct

class compression:
    def __init__(self):
        self.path = ''
        self.rows = 0
        self.cols = 0
        self.f = 0
        self.d = 0

choice = compression()

def readImage():
    global choice
    img = Image.open(choice.path)
    choice.rows, choice.cols = img.size


def openFile():
    filetypes = (('images', '*.bmp'),)
    filepath = filedialog.askopenfilename(
        title='Open a file',
        initialdir='/home/Discrete_Cosine_Trasform',
        filetypes=filetypes)
    global choice
    choice.path = filepath

def updateF(val):
    global choice
    choice.f = val

def updateD(val):
    global choice
    choice.d = val

def visualize_compressed(path_result):
    display = Tk()
    display.title("Compressed")
    display.geometry('%dx%d+%d+%d' % (choice.rows, choice.cols, 900, 100))
    canvas = Canvas(display)
    img1 = ImageTk.PhotoImage(Image.open(path_result), master=canvas)
    first_image = Label(display, image=img1)
    first_image.place(x=0, y=0)
    display.mainloop()

def visualize_original():
    global choice
    # comprimo 
    path_result = 'compressed.bmp'
    img_dct(int(choice.f), int(choice.d), choice.path, path_result)
    display = Tk()
    display.title("Original")
    display.geometry('%dx%d+%d+%d' % (choice.rows, choice.cols, 800, 100))
    canvas = Canvas(display)
    img1 = ImageTk.PhotoImage(Image.open(choice.path), master=canvas)
    first_image = Label(display, image=img1)
    first_image.place(x=0, y=0)
    visualize_compressed(path_result)
    display.mainloop()


def nextWindow():
    global choice
    if choice.path == '':
        messagebox.showerror('Error', 'Error: Select a Valid File!')
    else:
        readImage()
        second_window = Tk()
        second_window.title('Parameters')
        second_window.geometry('%dx%d+%d+%d' % (430, 400, 100, 400))

        size_label = Label(second_window, text='Image size: (' + str(choice.rows) + 'x' + str(choice.cols) +')' , font=('arial', 25))
        size_label.place(x=10, y=20)


        first_label = Label(second_window, text='F (squares width):', font=('arial', 25))
        first_label.place(x=10, y=120)

        slide_bar1 = Scale(second_window, from_=1, to=min(choice.rows, choice.cols), orient=HORIZONTAL, font=('arial', 25), command=updateF)
        slide_bar1.place(x=300, y=100)

        second_label = Label(second_window, text='d (cut-off):', font=('arial', 25))
        second_label.place(x=10, y=220)

        slide_bar2 = Scale(second_window, from_=0, to=2 * min(choice.rows, choice.cols) - 2, orient=HORIZONTAL, font=('arial', 25), command=updateD)
        slide_bar2.place(x=300, y=200)

        go_next = Button(second_window, text='Compress', command=visualize_original, font=('arial', 25), width=20)
        go_next.place(x=10, y=300)

        second_window.mainloop()

def starting_window():
    window = Tk()
    window.title('File Selection')
    window.geometry('%dx%d+%d+%d' % (630, 200, 100, 100))


    button = Button(text='Open', command=openFile, font=('arial', 25))
    button.place(x=500, y=40)

    
    go_next = Button(window, text='Compress', command=nextWindow, font=('arial', 25), width=30)
    go_next.place(x=10, y=140)

    label = Label(window, text='Select an Image to Compress', font=('arial', 25))
    label.place(x=10, y=50)


    window.mainloop()


def main():
    starting_window()

if __name__ == '__main__':
    main()

