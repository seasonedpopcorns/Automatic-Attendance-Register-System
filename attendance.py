from tkinter  import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import customtkinter as ck
import mysql.connector
import os
import csv
from tkinter import filedialog
import cv2

mydata=[]


class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        ck.set_appearance_mode("dark")

        self.root.title("Attendance")

        #variables
        self.roll_var=StringVar()
        self.name_var=StringVar()
        self.dept_var=StringVar()
        self.time_var=StringVar()
        self.date_var=StringVar()
        self.status_var=StringVar()


        main_frame=ck.CTkFrame(self.root,height=1080,width=1920)
        main_frame.place(x=0,y=0)

        #left subframe
        left_sub_frame=ck.CTkFrame(main_frame,height=600,width=1920,fg_color="grey21",border_width=1)
        left_sub_frame.place(x=0,y=200)

        roll_id=ck.CTkLabel(left_sub_frame,text="Roll No :",font=("times new roman",19),height=30,width=35,fg_color="grey19",corner_radius=10)
        roll_id.place(x=360,y=90)
        roll_entry=ck.CTkEntry(left_sub_frame,textvariable=self.roll_var,corner_radius=10,height=30)
        roll_entry.place(x=530,y=90)


        name_id=ck.CTkLabel(left_sub_frame,text="Name:",font=("times new roman",19),height=30,width=35,fg_color="grey19",corner_radius=10)
        name_id.place(x=20,y=90)
        name_entry=ck.CTkEntry(left_sub_frame,textvariable=self.name_var,corner_radius=10,height=30)
        name_entry.place(x=170,y=90)

        time_id=ck.CTkLabel(left_sub_frame,text="Time :",font=("times new roman",19),height=30,width=35,fg_color="grey19",corner_radius=10)
        time_id.place(x=20,y=150)
        time_entry=ck.CTkEntry(left_sub_frame,textvariable=self.time_var,corner_radius=10,height=30)
        time_entry.place(x=170,y=150)
        

        dep_id=ck.CTkLabel(left_sub_frame,text="Department :",font=("times new roman",19),height=30,width=35,fg_color="grey19",corner_radius=10)
        dep_id.place(x=20,y=210)
        dep_entry=ck.CTkEntry(left_sub_frame,textvariable=self.dept_var,corner_radius=10,height=30)
        dep_entry.place(x=170,y=210)


        attendance_status_id=ck.CTkLabel(left_sub_frame,text="Attendance Status :",font=("times new roman",19),height=30,width=35,fg_color="grey19",corner_radius=10)
        attendance_status_id.place(x=360,y=150)
        attendance_status_combo=ck.CTkComboBox(left_sub_frame,variable=self.status_var,corner_radius=10,height=30,values=["Present","Absent"],width=150,state="readonly")
        attendance_status_combo.place(x=530,y=150)

        date_id=ck.CTkLabel(left_sub_frame,text="Date :",font=("times new roman",19),height=30,width=35,fg_color="grey19",corner_radius=10)
        date_id.place(x=360,y=210)
        date_entry=ck.CTkEntry(left_sub_frame,textvariable=self.date_var,corner_radius=10,height=30)
        date_entry.place(x=530,y=210)

        #buttons
        b1=ck.CTkButton(left_sub_frame,command=self.importCSV,text='Import CSV',corner_radius=10)
        b1.place(x=70,y=365)

        b2=ck.CTkButton(left_sub_frame,command=self.exportcsv,text='Export CSV',corner_radius=10)
        b2.place(x=250,y=365)

        b3=ck.CTkButton(left_sub_frame,command=self.reset_data,text='Reset',corner_radius=10)
        b3.place(x=430,y=365)




        #right sub frame
        right_sub_frame=ck.CTkFrame(main_frame,height=600,width=760,fg_color="grey21",border_width=1)
        right_sub_frame.place(x=750,y=200)

        right_mini_frame=ttk.Frame(right_sub_frame)
        right_mini_frame.place(x=5,y=5,height=570,width=760)

        #scroll bar table
        scroll_x=ck.CTkScrollbar(right_mini_frame,orientation="horizontal")
        scroll_y=ck.CTkScrollbar(right_mini_frame,orientation="vertical")
        
        self.AttendanceReportTable=ttk.Treeview(right_mini_frame,column=("roll","name","department","time","date","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.configure(command=self.AttendanceReportTable.xview)
        scroll_y.configure(command=self.AttendanceReportTable.yview)

        #setting the Table style
        style = ttk.Style()
    
        style.theme_use("default")
    
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



        self.AttendanceReportTable.heading("roll",text="Roll no")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text='Date')
        self.AttendanceReportTable.heading("Status",text="Status")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.column("roll",width=15)
        self.AttendanceReportTable.column("name",width=60)
        self.AttendanceReportTable.column("department",width=60)
        self.AttendanceReportTable.column("time",width=40)
        self.AttendanceReportTable.column("date",width=60)
        self.AttendanceReportTable.column("Status",width=30)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert('',END,values=i)

    #import CSV function  
    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=',')
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No data to Export!",parent=self.root)
                return False
                
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,"w+",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=',')
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Export","Export to "+os.path.basename(fln)+" is Succesfull")


        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    #pull data from RIGHT side and display on corresponding LEFT side
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.roll_var.set(rows[0])
        self.name_var.set(rows[1])
        self.dept_var.set(rows[2])
        self.time_var.set(rows[3])
        self.date_var.set(rows[4])
        self.status_var.set(rows[5])

    
    #reset function
    def reset_data(self):
        self.roll_var.set("")
        self.name_var.set("")
        self.dept_var.set("")
        self.time_var.set("")
        self.date_var.set("")
        self.status_var.set("")





if  __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()