
from asyncio.windows_events import NULL
import os
import cv2
import glob
import os.path
import tkinter as tk
from tkinter import *
from tkinter import font as tkfont
from PIL import Image, ImageTk
from datetime import datetime
from tkinter import messagebox, filedialog

# from rsa import PublicKey

saved_image = 'outside_class'


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(
            family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)

        container.pack(side="top", ipadx=200, ipady=50)

        container.grid_rowconfigure(0, weight=1)

        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Camera, History, Capture, Send, Save):

            page_name = F.__name__

            frame = F(parent=container, controller=self)

            self.frames[page_name] = frame

            # put all of the pages in the same location;

            # the one on the top of the stacking order

            # will be the one that is visible.

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''

        frame = self.frames[page_name]

        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.controller = controller

        label = tk.Label(self, text="Welcome Doctor !",
                         bg="steelblue", fg="white", font=('Comic Sans MS', 20))

        label.pack(side="top", fill="x", pady=10)

        camera_button = tk.Button(self, text="Camera",

                                  command=lambda: controller.show_frame("Camera"), bg="LIGHTBLUE", font=('Comic Sans MS', 15), width=20)

        history_button = tk.Button(self, text="History",

                                   command=lambda: controller.show_frame("History"), bg="LIGHTBLUE", font=('Comic Sans MS', 15), width=20)

        camera_button.pack(side="left", pady=30, padx=30)

        history_button.pack(side="right", pady=30, padx=30)


class Camera(tk.Frame):

    def __init__(self, parent, controller):

        def show_frames():
            # Get the latest frame and convert into Image
            cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            cameraLabel.imgtk = imgtk
            cameraLabel.configure(image=imgtk)
            cameraLabel.after(20, show_frames)

        def Capture():

            image_name = datetime.now().strftime('%d-%m-%Y %H-%M-%S')
            imgName = "E:\Graduation_project" + '/' + image_name + ".jpg"
            ret, frame = cap.read()

            cv2.putText(frame, datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                        (430, 460), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 255))

            cv2.imwrite(imgName, frame)

        tk.Frame.__init__(self, parent)

        self.controller = controller

        feedlabel = Label(self, bg="steelblue", fg="white",
                          text="WEBCAM FEED", font=('Comic Sans MS', 20))
        feedlabel.pack(side="top", fill="x", pady=3)

        cameraLabel = Label(self, bg="steelblue",
                            borderwidth=3, relief="groove")
        cameraLabel.pack(side="top", pady=3)

        captureBTN = Button(self, text="CAPTURE",  command=lambda: [Capture(), controller.show_frame("Capture")],
                            bg="LIGHTBLUE", font=('Comic Sans MS', 15), width=20)
        captureBTN.pack(side="left", pady=3)

        history_button = tk.Button(self, text="History",
                                   command=lambda: controller.show_frame("History"), bg="LIGHTBLUE", font=('Comic Sans MS', 15), width=20)
        history_button.pack(side="right", pady=3)

        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame("StartPage"), bg="red", font=('Comic Sans MS', 15), width=10)
        back_button.pack(side="bottom")

        show_frames()


class History(tk.Frame):

    def __init__(self, parent, controller):

        def imageBrowse():
            openDirectory = filedialog.askopenfilename(
                initialdir="YOUR DIRECTORY PATH")

            imagePath = 'E:\Graduation_project'
            imageView = Image.open(openDirectory)
            imageResize = imageView.resize((640, 480), Image.ANTIALIAS)
            imageDisplay = ImageTk.PhotoImage(imageResize)
            imageLabel.config(image=imageDisplay)
            imageLabel.photo = imageDisplay

        tk.Frame.__init__(self, parent)

        self.controller = controller

        feedlabel = Label(self, bg="steelblue", fg="white",
                          text="History", font=('Comic Sans MS', 20))
        feedlabel.pack(side="top", fill="x", pady=3)

        imageLabel = Label(self, bg="steelblue",
                           borderwidth=3, relief="groove")
        imageLabel.pack(side="top", pady=3)

        openImageButton = Button(
            self, text="BROWSE", command=imageBrowse, bg="LIGHTBLUE", font=('Comic Sans MS', 15), width=20)
        openImageButton.pack(side="left", pady=3)

        camera_button = tk.Button(
            self, text="Camera", command=lambda: controller.show_frame("Camera"), bg="LIGHTBLUE", font=('Comic Sans MS', 15), width=20)
        camera_button.pack(side="right", pady=3)

        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame("StartPage"), bg="red", font=('Comic Sans MS', 15), width=10)
        back_button.pack(side="bottom")


class Capture(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.controller = controller

        feedlabel = Label(self, bg="steelblue", fg="white",
                          text="Image", font=('Comic Sans MS', 20))
        feedlabel.pack(side="top", fill="x", pady=3)

        imageLabel = Label(self, bg="steelblue",
                           borderwidth=3, relief="groove")
        imageLabel.pack(side="top", pady=3)

        capture_button = tk.Button(
            self, text="Capture again !", command=lambda: [controller.show_frame("Camera")], bg="LIGHTBLUE", font=('Comic Sans MS', 15), width=20)
        capture_button.pack(side="left", pady=3)

        send_button = tk.Button(
            self, text="Send", command=lambda: controller.show_frame("Send"), bg="LIGHTBLUE", font=('Comic Sans MS', 15), width=20)
        send_button.pack(side="right", pady=3)

        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame("StartPage"), bg="red", font=('Comic Sans MS', 15), width=10)
        back_button.pack(side="bottom")


class Send(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        feedlabel = Label(self, bg="steelblue", fg="white",
                          text="Send to model", font=('Comic Sans MS', 20))
        feedlabel.pack(side="top", fill="x", pady=3)

        imageLabel = Label(self, bg="steelblue",
                           borderwidth=3, relief="groove")
        imageLabel.pack(side="top", pady=3)

        save_button = Button(
            self, text="Save", command=lambda: controller.show_frame("Save"), bg="LIGHTBLUE", font=('Comic Sans MS', 15), width=20)
        save_button.pack(side="left", pady=3)

        cancel_button = tk.Button(self, text="Cancel",
                                  command=lambda: controller.show_frame("StartPage"), bg="red", font=('Comic Sans MS', 15), width=10)
        cancel_button.pack(side="right", pady=3)


class Save(tk.Frame):

    def __init__(self, parent, controller):

        def imageBrowse():
            openDirectory = filedialog.askopenfilename(
                initialdir="YOUR DIRECTORY PATH")

            imagePath = 'E:\Graduation_project'
            imageView = Image.open(openDirectory)
            imageResize = imageView.resize((640, 480), Image.ANTIALIAS)
            imageDisplay = ImageTk.PhotoImage(imageResize)
            imageLabel.config(image=imageDisplay)
            imageLabel.photo = imageDisplay

        tk.Frame.__init__(self, parent)

        self.controller = controller

        feedlabel = Label(self, bg="steelblue", fg="white",
                          text="Save the Image", font=('Comic Sans MS', 20))
        feedlabel.pack(side="top", fill="x", pady=3)

        imageLabel = Label(self, bg="steelblue",
                           borderwidth=3, relief="groove")
        imageLabel.pack(side="top", pady=3)

        Save_button = Button(
            self, text="Save in Exceting Record ", command=imageBrowse, bg="LIGHTBLUE", font=('Comic Sans MS', 15), width=20)
        Save_button.pack(side="top", pady=3)

        Create_button = Button(
            self, text="Create new record", command=imageBrowse, bg="LIGHTBLUE", font=('Comic Sans MS', 15), width=20)
        Create_button.pack(side="top", pady=3)

        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame("StartPage"), bg="red", font=('Comic Sans MS', 15), width=10)
        back_button.pack(side="bottom")


cap = cv2.VideoCapture(0)
width, height = 640, 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

if __name__ == "__main__":

    app = SampleApp()

    app.title("Melanoziser")
    app.state('zoomed')
    app.mainloop()
