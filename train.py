from tkinter  import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import mysql.connector
import numpy as np
import cv2
import customtkinter as ck


class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("800x500+350+150")
        self.root.title("Train Data")


        title_frame=ck.CTkFrame(self.root,border_width=2,height=1080,width=1920)
        title_frame.place(x=0,y=0)

        #button
        b1=ck.CTkButton(title_frame,text="Train",command=self.train_classifier,cursor="hand2",font=('times new roman',23,'bold'),height=50,width=100)
        b1.place(x=330,y=250)


    def train_classifier(self):
        data_dir=("C:/Users/Maria Viveka/Desktop/Projects/AARS/model3/data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #grey scale conversion
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1]) #extracting the user name from image

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #Train the Classifier and Save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("C:/Users/Maria Viveka/Desktop/Projects/AARS/model3/classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Data Trained")





if  __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()