import tkinter
from tkinter import filedialog
from tkinter import *
import numpy as np

import cv2


class Application(Frame):

    img=0






    def erosion(self):

        global img
        global E1
        global E2



        iteration = (E1.get())
        dim= int(E2.get())

        it=int(iteration)



        kernel = np.ones((dim, dim), np.uint8)

        img = cv2.erode(img, kernel, iterations=it)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    def dilation(self):
            global img
            global E1
            global E2

            iteration = (E1.get())
            dim = int(E2.get())

            it = int(iteration)

            kernel = np.ones((dim, dim), np.uint8)
            img = cv2.dilate(img, kernel, iterations=it)
            cv2.imshow('image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()



    def open(self):

            global img
            global E1
            global E2

            dim = int(E2.get())

            kernel = np.ones((dim, dim), np.uint8)


            img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
            cv2.imshow('image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()



    def close(self):

            global img
            global E1
            global E2

            dim = int(E2.get())

            kernel = np.ones((dim, dim), np.uint8)


            img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
            cv2.imshow('image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


    def open_close(self):

            global img
            global E1
            global E2

            dim = int(E2.get())

            kernel = np.ones((dim, dim), np.uint8)


            img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
            img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
            cv2.imshow('image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


    def close_open(self):

            global img
            global E1
            global E2

            dim = int(E2.get())

            kernel = np.ones((dim, dim), np.uint8)


            img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
            img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
            cv2.imshow('image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def Skeletonization(self):

            global img
            global img
            global E1
            global E2

            it = int(E1.get())




            cv2.imshow('image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def open_file(self):



        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                     filetypes=(("jpeg files", "*.jpg"),("PNG files", "*.png"), ("all files", "*.*")))

        global img
        img = cv2.imread(root.filename, 0)






    def initUI(self):



        self.master.title("Morphological Operations")

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        operation=Menu(menubar)

        submenu = Menu(fileMenu)


        submenu2 = Menu(operation)


        fileMenu.add_command(label="Open", underline=0, command=self.open_file)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", underline=0, command=self.quit())
        menubar.add_cascade(label="File", underline=0, menu=fileMenu)
        menubar.add_cascade(label="Operation", underline=0, menu=operation)
        operation.add_command(label='Erosion', underline=0, command=self.erosion)
        operation.add_separator()
        operation.add_command(label='Dilation', underline=0, command=self.dilation)
        operation.add_separator()
        operation.add_command(label='Open', underline=0, command=self.open)
        operation.add_separator()
        operation.add_command(label='Close', underline=0, command=self.close)
        operation.add_separator()
        operation.add_command(label='Open-Close', underline=0, command=self.open_close)
        operation.add_separator()
        operation.add_command(label='Close-Open', underline=0, command=self.close_open)
        operation.add_separator()
        operation.add_command(label='Skeletonization', underline=0, command=self.Skeletonization)

        label1 = Label(root, text="Number of Iterations")
        global E1
        global E2
        E1 = Entry(root, bd=5)

        label2 = Label(root, text="Kernel Size (N)")
        E2 = Entry(root, bd=5)







        #submit = Button(root, text="Submit", command=getDate)

        label1.pack()
        E1.pack()
        label2.pack()
        E2.pack()



        #submit.pack(side=BOTTOM)







    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi



    def form(self):
        labelText = StringVar()
        labelText.set("Enter directory of log files")
        labelDir = Label(root, textvariable=labelText, height=4)
        labelDir.pack(side="left")

        directory = StringVar(None)
        dirname = Entry(root, textvariable=directory, width=10)
        dirname.pack(side="left")





        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.show_entry_fields("sasaa")
        self.hi_there.pack({"side": "left"})


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.initUI()

root = Tk()



app = Application(master=root)


app.mainloop()
root.destroy()