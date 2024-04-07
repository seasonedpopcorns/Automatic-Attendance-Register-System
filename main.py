from tkinter  import *
from tkinter import ttk
from PIL import Image,ImageTk
import os
import customtkinter as ck

from student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from credits import Credits




class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        # title of the window
        self.root.title("AARS")
                
        main_frame=ck.CTkFrame(self.root,height=1080,width=1920,fg_color="light slate grey")
        main_frame.place(x=0,y=0)

        #label1
        label_frame=ck.CTkFrame(main_frame,border_width=2,height=90,width=750,fg_color="slate grey")
        label_frame.place(x=400,y=50)
        title_lbl=ck.CTkLabel(label_frame,text="Automatic Attendance Recognition System",font=("Helvetica",35,"bold"),text_color="black")
        title_lbl.place(x=30,y=25)

        #button 1 - Students
        b1=ck.CTkButton(main_frame,text="Students",cursor="hand2",command=self.student_details,font=('courier',20,'bold'),height=135,width=200)
        b1.place(x=300+70,y=300)

        #button 2 - Detect face
        b2=ck.CTkButton(main_frame,text="Detect Face",cursor="hand2",command=self.face_data,font=('courier',20,'bold'),height=135,width=200)
        b2.place(x=600+70,y=300)

        #button 3 - Attendance
        b3=ck.CTkButton(main_frame,text="Attendance",command=self.attendance_data,cursor="hand2",font=('courier',20,'bold'),height=135,width=200)
        b3.place(x=900+70,y=300)

        #button 4 - Train
        b4=ck.CTkButton(main_frame,text="Train Data",cursor="hand2",command=self.train_data,font=('courier',20,'bold'),height=135,width=200)
        b4.place(x=300+70,y=540)

        #button 5 - Credits
        b5=ck.CTkButton(main_frame,text="Credits",command=self.credit_page,cursor="hand2",font=('courier',20,'bold'),height=135,width=200)
        b5.place(x=900+70,y=540)

        #button 6 - Show Photos 
        b6=ck.CTkButton(main_frame,text="View Photos",cursor="hand2",command=self.open_image,font=('courier',20,'bold'),height=135,width=200)
        b6.place(x=600+70,y=540)



    #Functions buttons //
        
    def open_image(self):
        os.startfile('C:/Users/Maria Viveka/Desktop/Projects/AARS/model3/data')

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def exitnow(self):
        exit(0)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)


    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def credit_page(self):
        self.new_window=Toplevel(self.root)
        self.app=Credits(self.new_window)




if  __name__ == "__main__":
    root= Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()