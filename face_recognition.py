from tkinter  import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import mysql.connector
import numpy as np
import cv2
import customtkinter as ck
from time import strftime
from datetime import  datetime


class Face_recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("800x500+350+150")

        main_frame=ck.CTkFrame(self.root,width=1920,height=1080)
        main_frame.place(x=0,y=0)

        b1=ck.CTkButton(main_frame,command=self.face_recog,text="Detect",cursor="hand2",font=('times new roman',23,'bold'),height=50,width=100)
        b1.place(x=330,y=250)

    #Attendance
    
    def mark_attendance(self,n,r,d):
        with open("C:/Users/Maria Viveka/Desktop/Projects/AARS/model3/Attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in  myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((n not in name_list) and (r not in name_list) and (d not in name_list)) :
                now = datetime.now()
                d1=now.strftime(("%d/%m/%Y"))
                dtString=now.strftime(("%H:%M:%S"))
                f.writelines(f"\n{r},{n},{d},{dtString},{d1},Present")
                




    #face recognition
        
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]


            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                print(id)

                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
                cursor=conn.cursor()

                cursor.execute("select Name from student where Student_Number="+str(id))
                n=cursor.fetchone()
                n="+".join(n)

                cursor.execute("select Dept from student where Student_Number ="+str(id))
                d=cursor.fetchone()
                d="+".join(d)

                cursor.execute("select Roll_no from student where Student_Number ="+str(id))
                r=cursor.fetchone()
                r="+".join(r)

                if confidence>75:
                    cv2.putText(img,f"Name: {n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    #cv2.putText(img,f"Roll: {r}",(x,y-90),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(n,r,d)


                else:
                   cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
                   cv2.putText(img,"Unknown Face",(x,y-70),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)    
 
                coord=[x,y,w,h]
            
            return coord

        def recognise(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml') #cv2.data.haarcascades + 
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("C:/Users/Maria Viveka/Desktop/Projects/AARS/model3/classifier.xml")


        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognise(img,clf,faceCascade)
            cv2.imshow('Webcam',img)
            
            if cv2.waitKey(1)==13:    
                break
        video_cap.release()
        cv2.destroyAllWindows()


if  __name__ == "__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()