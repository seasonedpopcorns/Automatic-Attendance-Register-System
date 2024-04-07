from tkinter  import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import customtkinter as ck
import mysql.connector
import cv2


class Student:
    def __init__(self,root):

        style = ttk.Style()
    
        style.theme_use("default")

        self.root = root
        self.root.geometry("1920x1080+0+0")


        #variables
        self.var_dep=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_dob=StringVar()
        self.var_advisor=StringVar()
        self.var_phno=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()



        # title of the window
        self.root.title("Student Details")


        #Frame
        filler_frame=ck.CTkFrame(self.root,height=200,width=1920)
        filler_frame.place(x=0,y=0)
        main_frame=ck.CTkFrame(self.root,border_width=2,height=1080,width=1920,fg_color="grey19",bg_color="grey19")
        main_frame.place(x=0,y=200)

        #left label frame
        left_frame=ck.CTkFrame(main_frame,height=500,width=750,border_width=5,fg_color="grey19",bg_color="grey19")
        left_frame.place(x=0,y=0)

        #current course
        cur_course=ck.CTkFrame(left_frame,height=85,width=650,border_width=5,fg_color="grey19",bg_color="grey19")
        cur_course.place(x=5,y=20)

        #dept label and combobox
        dept_lab=ck.CTkLabel(cur_course,text="Department : ")
        dept_lab.grid(row=0,column=0,padx=10)

        dep_combo=ck.CTkComboBox(cur_course,variable=self.var_dep,state="readonly",values=("Computer Science","Electrical","Electronics","Mechanical","Artificial Intelligence"),corner_radius=10)
        dep_combo.grid(row=0,column=1,padx=10,pady=10)

        #semester label and combobox
        sem_lab=ck.CTkLabel(cur_course,text="Semester : ")
        sem_lab.grid(row=0,column=3,padx=10)

        sem_combo=ck.CTkComboBox(cur_course,variable=self.var_sem,state="readonly",values=("1","2","3","4","5","6","7","8"),corner_radius=10)
        sem_combo.grid(row=0,column=4,padx=10,pady=10)


        #Student details
        stu_det=ck.CTkFrame(left_frame,height=200,width=700,border_width=5)
        stu_det.place(x=5,y=100)

        #name Label and Entry
        name_lab=ck.CTkLabel(stu_det,text="Name :")
        name_lab.grid(row=0,column=0,pady=10)

        name_ent=ck.CTkEntry(stu_det,textvariable=self.var_name,width=180,font=("times new roman",13))
        name_ent.grid(row=0,column=1,padx=10)

        #id label and entry
        id_lab=ck.CTkLabel(stu_det,text="ID :")
        id_lab.grid(row=1,column=0,pady=10)

        id_ent=ck.CTkEntry(stu_det,width=180,textvariable=self.var_id,font=("times new roman",13))
        id_ent.grid(row=1,column=1,padx=10)

        #rollno label and entry
        rollno_lab=ck.CTkLabel(stu_det,text="Roll_No. :")
        rollno_lab.grid(row=2,column=0,pady=10,padx=5)

        roll_ent=ck.CTkEntry(stu_det,textvariable=self.var_roll,width=180,font=("times new roman",13))
        roll_ent.grid(row=2,column=1,padx=10)

        #staff advisor Label and conbobox
        staff_advisory_lab=ck.CTkLabel(stu_det,text="Advisor :")
        staff_advisory_lab.grid(row=0,column=3,pady=10)

        staff_combo=ck.CTkComboBox(stu_det,variable=self.var_advisor,font=("times new roman",12,"bold"),state="readonly",values=("Nisha J R","Dhanya Naren"),width=180)
        staff_combo.grid(row=0,column=4,padx=10)

        #DOB label and entry
        dob_lab = ck.CTkLabel(stu_det, text = "Date of Birth: ") 
        dob_lab.grid(row = 1, column = 3, pady = 10)

        dob_ent=ck.CTkEntry(stu_det,textvariable=self.var_dob, width =180, font = ("times new roman", 13))
        dob_ent.grid(row=1,column=4,padx=10)

        #phno label and entry
        phno_lab=ck.CTkLabel(stu_det,text="Phone Number :")
        phno_lab.grid(row=2,column=3,pady=10)

        phno_ent=ck.CTkEntry(stu_det,textvariable=self.var_phno, width =180, font = ("times new roman", 13))
        phno_ent.grid(row=2,column=4,padx=10)


        #Button Frame
        button_frame=ck.CTkFrame(left_frame,height=20,width=650,corner_radius=10,border_width=5)
        button_frame.place(x=0,y=255)

        #radio Buttons
        self.var_radio1=StringVar()
        radiobutton1=ck.CTkRadioButton(button_frame,text="Take photo",variable=self.var_radio1,value="Yes")
        radiobutton1.grid(row=0,column=0,pady=10,padx=12)

        radiobutton2=ck.CTkRadioButton(button_frame,text="No photo",variable=self.var_radio1,value="NO")
        radiobutton2.grid(row=0,column=1,padx=10)

        #Buttons
        save_button=ck.CTkButton(button_frame,command=self.add_data,text="Save",fg_color="seagreen",width=15,height=30,corner_radius=15)
        save_button.grid(row=1,column=1,pady=10)

        reset_button=ck.CTkButton(button_frame,command=self.reset_data,text="Reset",fg_color="SlateBlue2",width=15,height=30,corner_radius=15)
        reset_button.grid(row=1,column=2)

        delete=ck.CTkButton(button_frame,command=self.delete_data,text="Delete",fg_color="indianred",width=15,height=30,corner_radius=15)
        delete.grid(row=1,column=3,padx=23)

        update=ck.CTkButton(button_frame,text="Update",command=self.update_data,fg_color="medium purple",width=15,height=30,corner_radius=15)
        update.grid(row=1,column=4)

        take_photo_button=ck.CTkButton(button_frame,command=self.generate_dateset,text="Take photo",width=30,height=25,corner_radius=15)
        take_photo_button.grid(row=0,column=5)

        update_photo_button=ck.CTkButton(button_frame,text="Update Photo",width=30,height=25,corner_radius=10)
        update_photo_button.grid(row=0,column=6,padx=10,pady=20)


        

        #right label frame
        right_frame=ck.CTkFrame(main_frame,height=500,width=800,border_width=5)
        right_frame.place(x=750,y=0)

        #search by
        searchby=ck.CTkFrame(right_frame,height=70,width=650)
        searchby.place(x=0,y=10,)      
        #table frame
        table_frame=LabelFrame(right_frame,bg="grey19")
        table_frame.place(x=10,y=10,height=330,width=760)

        scroll_x=ck.CTkScrollbar(table_frame,orientation="horizontal",bg_color="grey18")
        scroll_y=ck.CTkScrollbar(table_frame,orientation="vertical",bg_color="grey18")
        self.student_table=ttk.Treeview(table_frame,column=("Name","Std_No","Department","Semester","Roll_no","Advisor","Date of Birth","Phno"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_x.configure(command=self.student_table.xview)

        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.configure(command=self.student_table.yview)

        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Std_No",text="Std No")
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Semester",text="Semester")  
        self.student_table.heading("Roll_no",text="Rollno")
        self.student_table.heading("Advisor",text="Advisor")
        self.student_table.heading("Date of Birth",text="DOB")
        self.student_table.heading("Phno",text="Ph no")
        self.student_table["show"]="headings"


        style.configure("Treeview",
                            background="#2a2d2e",
                            foreground="white",
                            fieldbackground="#343638",
                            bordercolor="#343638",
                            borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
    
        style.configure("Treeview.Heading",
                            background="#565b5e",
                            foreground="white",
                            relief="flat")
        style.map("Treeview.Heading",
                      background=[('active', '#3484F0')])


        self.student_table.column("Department",width=100)
        self.student_table.column("Std_No",width=20)
        self.student_table.column("Advisor",width=100)
        self.student_table.column("Roll_no",width=38)
        self.student_table.column("Date of Birth",width=100)
        self.student_table.column("Phno",width=100)
        self.student_table.column("Semester",width=46)
        self.student_table.column("Name",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #functions declarations
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get=="":
            messagebox.showerror("Error","Please fill all fields.",parent=self.root)
        else:
            try:
                
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
                cursor=conn.cursor()
                cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_name.get(),
                                                                                        self.var_id.get(),
                                                                                        self.var_dep.get(),
                                                                                        self.var_sem.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_advisor.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_phno.get(),
                                                                                        self.var_radio1.get()

                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Data entered",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    #fetch data into table
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
        cursor=conn.cursor()
        cursor.execute("Select * from student")
        data=cursor.fetchall()

        if len(data)!=0 :
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('',END,values=i)
            conn.commit()
        conn.close()


    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content['values']

        self.var_dep.set(data[2])
        self.var_sem.set(data[3])
        self.var_name.set(data[0])
        self.var_roll.set(data[4])
        self.var_advisor.set(data[5])
        self.var_dob.set(data[6])
        self.var_phno.set(data[7])
        self.var_id.set(data[1])
        self.var_radio1.set(data[8])


    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get=="":
            messagebox.showerror("Error","Please fill all fields.",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Confirm Update ?",parent=self.root)
                if(Update>0):
                    conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
                    cursor=conn.cursor()
                    cursor.execute("update student set Name=%s,Dept=%s,Semester=%s,Roll_no=%s,Advisor=%s,DOB=%s,PHNO=%s,PhotoSample=%s where Student_Number=%s",(
                                                                                                                                        self.var_name.get(),
                                                                                                                                        self.var_dep.get(),
                                                                                                                                        self.var_sem.get(),
                                                                                                                                        self.var_roll.get(),
                                                                                                                                        self.var_advisor.get(),
                                                                                                                                        self.var_dob.get(),
                                                                                                                                        self.var_phno.get(),
                                                                                                                                        self.var_radio1.get(),
                                                                                                                                        self.var_id.get()                                                                                                                                                                                                              
                                                                                                                                                                            ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Updated !!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)


    #delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","ID required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Deletion","Confirm Delete ?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
                    cursor=conn.cursor()
                    sql="DELETE FROM student where Student_Number=%s"
                    val=(self.var_id.get(),)
                    cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                messagebox.showinfo("Success","Updated !!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)
    

    #function reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_sem.set("")
        self.var_name.set("")
        self.var_id.set("")
        self.var_advisor.set("")
        self.var_phno.set("")
        self.var_radio1.set("")
        self.var_roll.set("")
        self.var_dob.set("")




    #Generate dataset and take photo sample
    def generate_dateset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get=="":
            messagebox.showerror("Error","Please fill all fields.",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
                cursor=conn.cursor()
                cursor.execute("Select * from student")
                myresult=cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                cursor.execute("update student set Name=%s,Dept=%s,Semester=%s,Roll_no=%s,Advisor=%s,DOB=%s,PHNO=%s,PhotoSample=%s where Student_Number=%s",(
                                                                                                                                        self.var_name.get(),
                                                                                                                                        self.var_dep.get(),
                                                                                                                                        self.var_sem.get(),
                                                                                                                                        self.var_roll.get(),
                                                                                                                                        self.var_advisor.get(),
                                                                                                                                        self.var_dob.get(),
                                                                                                                                        self.var_phno.get(),
                                                                                                                                        self.var_radio1.get(),
                                                                                                                                        self.var_id.get()==id+1                                                                                                                                                                                                              
                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #load predifined data on face frontal from open cv

                face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path='C:/Users/Maria Viveka/Desktop/Projects/AARS/model3/data/user.'+str(id)+'.'+str(img_id)+'.jpg'
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:  #press enter
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data set completed")
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)   





if  __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()