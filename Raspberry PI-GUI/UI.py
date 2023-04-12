from asyncio.windows_events import NULL
import os
import cv2
import glob
import os.path
import tensorflow as tf
import tkinter as tk
from tkinter import *
from tkinter import font as tkfont
from PIL import Image, ImageTk
from PIL import ImageDraw
from PIL import ImageFont
from datetime import datetime
from tkinter import messagebox, filedialog
from numpy import asarray
import numpy as np

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
        img = Image.new('RGB', (640, 480))
        for F in (StartPage, Camera, History, Capture, Send, Save):

            page_name = F.__name__
            if (page_name == 'Capture'):

                frame = F(parent=container, controller=self, image=img)

                self.frames[page_name] = frame

                # put all of the pages in the same location;

                # the one on the top of the stacking order

                # will be the one that is visible.

                frame.grid(row=0, column=0, sticky="nsew")
            else:
                frame = F(parent=container, controller=self)

                self.frames[page_name] = frame

                # put all of the pages in the same location;

                # the one on the top of the stacking order

                # will be the one that is visible.

                frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def assign_capimage(self, parent, image):
        frame = Capture(parent=parent, controller=self,image=image)


        # put all of the pages in the same location;

        # the one on the top of the stacking order

        # will be the one that is visible.

        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

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

                                  command=lambda: controller.show_frame("Camera"), bg="LIGHTBLUE",
                                  font=('Comic Sans MS', 15), width=20)

        history_button = tk.Button(self, text="History",

                                   command=lambda: controller.show_frame("History"), bg="LIGHTBLUE",
                                   font=('Comic Sans MS', 15), width=20)

        camera_button.pack(side="left", pady=30, padx=30)

        history_button.pack(side="right", pady=30, padx=30)


Captured_image = Image.new('RGB', (640, 480))


class Camera(tk.Frame):
    frame = np.zeros([640, 480, 3], dtype=np.uint8)

    def Capture(self):
        global frame
        #         image_name = datetime.now().strftime('%d-%m-%Y %H-%M-%S')

        ret, frame = cap.read()
        return frame

        # cv2.putText(frame, datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        #            (430, 460), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 255))

    def assign_image(frame):
        global Captured_image
        image_name = "image"
        imgName = "Records" + '/' + image_name + ".jpg"
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        Captured_image = Image.fromarray(img)
        cv2.imwrite(imgName, frame)

    def __init__(self, parent, controller):
        def show_frames():
            # Get the latest frame and convert into Image
            cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            cameraLabel.imgtk = imgtk
            cameraLabel.configure(image=imgtk)
            cameraLabel.after(20, show_frames)

        tk.Frame.__init__(self, parent)

        self.controller = controller

        feedlabel = Label(self, bg="steelblue", fg="white",
                          text="WEBCAM FEED", font=('Comic Sans MS', 20))
        feedlabel.pack(side="top", fill="x", pady=3)

        cameraLabel = Label(self, bg="steelblue",
                            borderwidth=3, relief="groove")
        cameraLabel.pack(side="top", pady=3)

        def delay():
            Camera.assign_image(Camera.Capture(self))
            controller.assign_capimage(parent=parent, image=Captured_image)

        captureBTN = Button(self, text="CAPTURE", command=lambda: [delay()],
                            bg="LIGHTBLUE", font=('Comic Sans MS', 15), width=20)

        captureBTN.pack(side="left", pady=3)

        history_button = tk.Button(self, text="History",
                                   command=lambda: controller.show_frame("History"), bg="LIGHTBLUE",
                                   font=('Comic Sans MS', 15), width=20)
        history_button.pack(side="right", pady=3)

        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame("StartPage"), bg="red",
                                font=('Comic Sans MS', 15), width=10)
        back_button.pack(side="bottom")

        show_frames()


class History(tk.Frame):

    def __init__(self, parent, controller):
        def imageBrowse():
            openDirectory = filedialog.askopenfilename(
                initialdir="YOUR DIRECTORY PATH")

            imagePath = 'Records'
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
            self, text="Camera", command=lambda: controller.show_frame("Camera"), bg="LIGHTBLUE",
            font=('Comic Sans MS', 15), width=20)
        camera_button.pack(side="right", pady=3)

        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame("StartPage"), bg="red",
                                font=('Comic Sans MS', 15), width=10)
        back_button.pack(side="bottom")


class Capture(Camera, tk.Frame):

    def __init__(self, parent, controller, image):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        feedlabel = Label(self, bg="steelblue", fg="white",
                          text="Image", font=('Comic Sans MS', 20))
        feedlabel.pack(side="top", fill="x", pady=3)

        imageLabel = Label(self, bg="steelblue",
                           borderwidth=3, relief="groove")
        imageLabel.pack(side="top", pady=3)

        capture_button = tk.Button(
            self, text="Capture again !", command=lambda: [controller.show_frame("Camera")], bg="LIGHTBLUE",
            font=('Comic Sans MS', 15), width=20)
        capture_button.pack(side="left", pady=3)

        send_button = tk.Button(
            self, text="Send", command=lambda: controller.show_frame("Send"), bg="LIGHTBLUE",
            font=('Comic Sans MS', 15), width=20)
        send_button.pack(side="right", pady=3)

        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame("StartPage"), bg="red",
                                font=('Comic Sans MS', 15), width=10)
        back_button.pack(side="bottom")

        #         c = Camera()
        #         Camera.assign_image()
        imgtk = ImageTk.PhotoImage(image=image)
        imageLabel.imgtk = imgtk
        imageLabel.configure(image=imgtk)


prediction = 1


# def pridect(img):
#     global prediction
#
#     def standardize(img, mean):
#         std = 55.30462222768374
#         img = (img - mean) / std
#         return img
#
#     mean = [143.33956166346746, 148.21742939479066, 190.40706684440573]
#     r_channel = standardize(asarray(img.resize((224, 224)))[:, :, 0], mean[0])
#     g_channel = standardize(asarray(img.resize((224, 224)))[:, :, 1], mean[1])
#     b_channel = standardize(asarray(img.resize((224, 224)))[:, :, 2], mean[2])
#     new_image = np.expand_dims(np.array(np.stack([r_channel, g_channel, b_channel], axis=-1)), axis=0)
#     new_image = np.float32(new_image)
#
#     interpreter = tf.lite.Interpreter('tflite_model.tflite')
#     interpreter.allocate_tensors()
#     print(interpreter.get_input_details())
#     input_details = interpreter.get_input_details()[0]
#     output_details = interpreter.get_output_details()[0]
#
#     interpreter.set_tensor(input_details["index"], new_image)
#     interpreter.invoke()
#     output = interpreter.get_tensor(output_details["index"])[0]
#
#     prediction = output.argmax()


image_text = "the image close to be malignant"


class Send(tk.Frame):
    global prediction, image_text, Captured_image

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
            self, text="Save", command=lambda: controller.show_frame("Save"), bg="LIGHTBLUE",
            font=('Comic Sans MS', 15), width=20)
        save_button.pack(side="left", pady=3)

        cancel_button = tk.Button(self, text="Cancel",
                                  command=lambda: controller.show_frame("StartPage"), bg="red",
                                  font=('Comic Sans MS', 15), width=10)
        cancel_button.pack(side="right", pady=3)
        # pridect(Captured_image)
        image_text = "the image close to be benign" if prediction == 0 else "the image close to be malignant"

        I1 = ImageDraw.Draw(Captured_image)
        myFont = ImageFont.truetype('Roboto-Bold.ttf', 18)
        I1.text((390, 420), image_text, font=myFont, fill=(255, 225, 0))
        imgtk = ImageTk.PhotoImage(image=Captured_image)
        imageLabel.imgtk = imgtk
        imageLabel.configure(image=imgtk)


class Save(tk.Frame):
    global prediction, image_text

    def __init__(self, parent, controller):
        def imageBrowse():
            openDirectory = filedialog.askopenfilename(
                initialdir="YOUR DIRECTORY PATH")

            imagePath = 'Records'
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
            self, text="Save in Exceting Record ", command=imageBrowse, bg="LIGHTBLUE", font=('Comic Sans MS', 15),
            width=20)
        Save_button.pack(side="top", pady=3)

        Create_button = Button(
            self, text="Create new record", command=imageBrowse, bg="LIGHTBLUE", font=('Comic Sans MS', 15), width=20)
        Create_button.pack(side="top", pady=3)

        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame("StartPage"), bg="red",
                                font=('Comic Sans MS', 15), width=10)
        back_button.pack(side="bottom")
        # pridect(Captured_image)
        image_text = "the image close to be benign" if prediction == 0 else "the image close to be malignant"

        I1 = ImageDraw.Draw(Captured_image)
        myFont = ImageFont.truetype('Roboto-Bold.ttf', 18)
        I1.text((390, 420), image_text, font=myFont, fill=(255, 225, 0))
        imgtk = ImageTk.PhotoImage(image=Captured_image)
        imageLabel.imgtk = imgtk
        imageLabel.configure(image=imgtk)


cap = cv2.VideoCapture(0)
width, height = 640, 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

if __name__ == "__main__":
    app = SampleApp()

    app.title("Melanoziser")
    app.state('zoomed')
    app.mainloop()
