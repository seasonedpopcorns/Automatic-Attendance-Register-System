from tkinter  import *
from tkinter import ttk
from PIL import Image,ImageTk
import os
import customtkinter as ck

from student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance


ck.set_appearance_mode("dark")

class Credits:
    def __init__(self,root):

        self.root = root
        self.root.geometry("1920x1080+0+0")
        # title of the window
        self.root.title("Credits")
        

        '''self.bg_image = ck.CTkImage(Image.open("C:/Users/Maria Viveka/Desktop/Projects/AARS/Extras/bg_gradient.jpg"),size=(1920,1080))
        self.bg_image_label = ck.CTkLabel(self.root,image=self.bg_image,text="")
        self.bg_image_label.grid(row=0, column=0)
'''
        main_frame=ck.CTkFrame(self.root,width=1920,height=1080)
        main_frame.pack()
        #frame 1
        frame1=ck.CTkFrame(main_frame,height=500,width=650,border_width=5)
        frame1.place(x=50,y=100)

        #details
        details=ck.CTkLabel(frame1,text="Automatic Attendance Register System [ AARS] uses a \nHaarcascade Image Recognition Model. \n\nFirst the Training Data is \ncollected and turned into greyscale. \n\nThen Haarcascade Frontal \nFace Classifier is used by the model to generate our own Classifier. \n\nThat classifer is used by the webcam through opencv functions \nto Detect Faces. \n\nFor each Detected Face the corresponding\nAttendance is marked in a CSV file on the same directory."
                            ,font=(None,20),justify='left')
        details.place(x=36,y=100)

        #name frame and labels
        label1=ck.CTkFrame(main_frame,border_width=5,height=100,width=450)
        label1.place(x=900,y=100)
        name1=ck.CTkLabel(label1,text="Chris John",font=('courier',30,'bold'))
        name1.place(x=120,y=30)


        label2=ck.CTkFrame(main_frame,border_width=5,height=100,width=450)
        label2.place(x=900,y=250)
        name2=ck.CTkLabel(label2,text="Nandana Narayan",font=('courier',30,'bold'))
        name2.place(x=120,y=30)


        label3=ck.CTkFrame(main_frame,border_width=5,height=100,width=450)
        label3.place(x=900,y=400)
        name3=ck.CTkLabel(label3,text="Maria Viveka",font=('courier',30,'bold'))
        name3.place(x=120,y=30)


        label4=ck.CTkFrame(main_frame,border_width=5,height=100,width=450)
        label4.place(x=900,y=550)
        name4=ck.CTkLabel(label4,text="Anamika Suresh",font=('courier',30,'bold'))
        name4.place(x=120,y=30)










if  __name__ == "__main__":
    root= Tk()
    obj=Credits(root)
    root.mainloop()