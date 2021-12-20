from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class Employeeclass:
   def __init__(self,root):
       self.root=root
       self.root.geometry("1100x500+220+130")
       self.root.title("Inventory Management System | Developed by Shadat Shohan")
       self.root.config(bg="white")
       self.root.focus_force()

       #variables
       self.var_searchtype=StringVar()
       self.var_searchtxt=StringVar()
       self.var_empid=StringVar()
       self.var_gender=StringVar()
       self.var_contact=StringVar()
       self.var_name=StringVar()
       self.var_dob=StringVar()
       self.var_doj=StringVar()
       self.var_email=StringVar()
       self.var_pass=StringVar()
       self.var_utype=StringVar()
       self.var_salary=StringVar()

       #searchframe
       SearchFrame=LabelFrame(self.root,text="Search Employee",bg="white",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
       SearchFrame.place(x=250,y=20,width=600,height=70)
       cmb_search=ttk.Combobox(SearchFrame,values=("Select","Email","Name","Contact"),textvariable=self.var_searchtype,state="readonly",justify=CENTER,font=("goudy old style",15))
       cmb_search.place(x=10,y=10,width=180)
       cmb_search.current(0)

       txt_search=Entry(SearchFrame,font=("goudy old style",15),textvariable=self.var_searchtxt,bg="lightyellow").place(x=200,y=10)
       btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=10,width=150,height=30)

       #title
       title=Label(self.root,text="Employee Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)

       #content
       #row1
       lbl_empid=Label(self.root,text="Emp ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
       lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
       lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)

       ent_empid=Entry(self.root,textvariable=self.var_empid,bg="lightyellow").place(x=150,y=150,width=180,height=27)
       ent_gender=ttk.Combobox(self.root,values=("Select","Male","Female","Other"),textvariable=self.var_gender,state="readonly",justify=CENTER,font=("goudy old style",15))
       ent_gender.place(x=500,y=150,width=180)
       ent_gender.current(0)
       ent_contact=Entry(self.root,textvariable=self.var_contact,bg="lightyellow").place(x=850,y=150,width=180,height=27)

       #row2
       lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
       lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=350,y=190)
       lbl_doj=Label(self.root,text="D.O.J",font=("goudy old style",15),bg="white").place(x=750,y=190)

       ent_name=Entry(self.root,textvariable=self.var_name,bg="lightyellow").place(x=150,y=190,width=180,height=27)
       ent_dob=Entry(self.root,textvariable=self.var_dob,bg="lightyellow").place(x=500,y=190,width=180,height=27)
       ent_doj=Entry(self.root,textvariable=self.var_doj,bg="lightyellow").place(x=850,y=190,width=180,height=27)

       #row3
       lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=230)
       lbl_pass=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=350,y=230)
       lbl_utype=Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=750,y=230)

       ent_email=Entry(self.root,textvariable=self.var_email,bg="lightyellow").place(x=150,y=230,width=180,height=27)
       ent_pass=Entry(self.root,textvariable=self.var_pass,bg="lightyellow").place(x=500,y=230,width=180,height=27)
       ent_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Select","Admin","Employee"),state="readonly",justify=CENTER,font=("goudy old style",15))
       ent_utype.place(x=850,y=230,width=180,height=27)
       ent_utype.current(0)

       #row4
       lbl_address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=270)
       lbl_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=500,y=270)
       self.var_address=Text(self.root,bg="lightyellow")
       self.var_address.place(x=150,y=270,width=300,height=60)
       ent_salary=Entry(self.root,textvariable=self.var_salary,bg="lightyellow").place(x=600,y=270,width=180,height=27)

       #buttons
       btn_add=Button(self.root,text="Save",command=self.add,bg="#2196f3",font=("goudy old style",15),fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
       btn_update=Button(self.root,text="Update",command=self.update,bg="#4caf50",font=("goudy old style",15),fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
       btn_delete=Button(self.root,text="Delete",command=self.delete,bg="#f44336",font=("goudy old style",15),fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
       btn_clear=Button(self.root,text="Clear",command=self.clear,bg="#607d8b",font=("goudy old style",15),fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)

       #employee details
       emp_frame=Frame(self.root,bd=3,relief=RIDGE)
       emp_frame.place(x=0,y=350,relwidth=1,height=150)
       #scrollbar with treeview
       scrolly=Scrollbar(emp_frame,orient=VERTICAL)
       scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
       self.EmployeeTable=ttk.Treeview(emp_frame,columns=("empid","name","email","gender","contact","dob","doj","pass","utype","address","sallary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
       scrollx.pack(side=BOTTOM,fill=X)
       scrolly.pack(side=RIGHT,fill=Y)
       scrollx.config(command=self.EmployeeTable.xview)
       scrolly.config(command=self.EmployeeTable.yview)
       #hedaing and column set
       self.EmployeeTable.heading("empid",text="Emp ID")
       self.EmployeeTable.heading("name",text="Name")
       self.EmployeeTable.heading("email",text="Email")
       self.EmployeeTable.heading("gender",text="Gender")
       self.EmployeeTable.heading("contact",text="Contact")
       self.EmployeeTable.heading("dob",text="D.O.B")
       self.EmployeeTable.heading("doj",text="D.O.J")
       self.EmployeeTable.heading("pass",text="Pass")
       self.EmployeeTable.heading("utype",text="UTYPE")
       self.EmployeeTable.heading("address",text="Address")
       self.EmployeeTable.heading("sallary",text="Sallary")

       self.EmployeeTable["show"]="headings"

       self.EmployeeTable.column("empid",width=90)
       self.EmployeeTable.column("name",width=100)
       self.EmployeeTable.column("email",width=100)
       self.EmployeeTable.column("gender",width=100)
       self.EmployeeTable.column("contact",width=100)
       self.EmployeeTable.column("dob",width=100)
       self.EmployeeTable.column("doj",width=100)
       self.EmployeeTable.column("pass",width=100)
       self.EmployeeTable.column("utype",width=100)
       self.EmployeeTable.column("address",width=100)
       self.EmployeeTable.column("sallary",width=100)
       self.EmployeeTable.pack(fill=BOTH,expand=1)
       self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
       self.show()

   #database creation
   # Save    
   def add(self):
       con=sqlite3.connect(database=r'IMS.db')
       cur=con.cursor()
       try:
           if self.var_empid.get()=="":
               messagebox.showerror("Error","Employee ID must be required",parent=self.root)
           else:
               cur.execute("Select * from employee where empid=?",(self.var_empid.get(),))
               row=cur.fetchone()
               if row!=None:
                   messagebox.showerror("Error","Employee ID already assigned,try different",parent=self.root)
               else:
                   cur.execute("Insert into employee(empid,name,email,gender,contact,dob,doj,pass,utype,address,sallary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                       self.var_empid.get(),
                       self.var_name.get(),
                       self.var_email.get(),
                       self.var_gender.get(),
                       self.var_contact.get(),
                       self.var_dob.get(),
                       self.var_doj.get(),
                       self.var_pass.get(),
                       self.var_utype.get(),
                       self.var_address.get('1.0',END),
                       self.var_salary.get(),
                      ))
                   con.commit()
                   messagebox.showinfo("Success","Employee added successfully",parent=self.root)
                   self.show()
                    

       except Exception as ex:
           messagebox.showerror("error",f"error due to:{str(ex)}",parent=self.root)
     
    #show to panel
   def show(self):
    con=sqlite3.connect(database=r'IMS.db')
    cur=con.cursor()
    try:
        cur.execute("Select * from employee")
        rows=cur.fetchall()
        self.EmployeeTable.delete(*self.EmployeeTable.get_children())
        for row in rows:
            self.EmployeeTable.insert('',END,values=row)

    except Exception as ex:
        messagebox.showerror("Error",f"Error due to:{str(ex)}")

   #getdata
   def get_data(self,ev):
       f=self.EmployeeTable.focus()
       content=self.EmployeeTable.item(f)
       row=content['values']
       self.var_empid.set(row[0])
       self.var_name.set(row[1])
       self.var_email.set(row[2])
       self.var_gender.set(row[3])
       self.var_contact.set(row[4])
       self.var_dob.set(row[5])
       self.var_doj.set(row[6])
       self.var_pass.set(row[7])
       self.var_utype.set(row[8])
       self.var_address.delete('1.0',END)
       self.var_address.insert(END,row[9])
       self.var_salary.set(row[10])

    #update date
   def update(self):
       con=sqlite3.connect(database=r'IMS.db')
       cur=con.cursor()
       try:
           if self.var_empid.get()=="":
               messagebox.showerror("Error","Employee ID must be required",parent=self.root)
           else:
               cur.execute("Select * from employee where empid=?",(self.var_empid.get(),))
               row=cur.fetchone()
               if row==None:
                   messagebox.showerror("Error","Invalid Employee Id",parent=self.root)
               else:
                   cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,sallary=? where empid=?",(
                       self.var_name.get(),
                       self.var_email.get(),
                       self.var_gender.get(),
                       self.var_contact.get(),
                       self.var_dob.get(),
                       self.var_doj.get(),
                       self.var_pass.get(),
                       self.var_utype.get(),
                       self.var_address.get('1.0',END),
                       self.var_salary.get(),
                       self.var_empid.get(),
                   ))
                   con.commit()
                   messagebox.showinfo("Success","Updated successfully",parent=self.root)
                   self.show()
       except Exception as ex:
           messagebox.showerror("Error",f"error due to:{str(ex)}",parent=self.root)
   
    #delete
   def delete(self):
       con=sqlite3.connect(database=r'IMS.db')
       cur=con.cursor()
       try:
           if self.var_empid.get()=="":
               messagebox.showerror("Error","Employee ID must be needed",parent=self.root)
           else:
               cur.execute("Select * from employee where empid=?",self.var_empid.get(),)
               row=cur.fetchone()
               if row==None:
                   messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
               else:
                   op=messagebox.askyesno("Confirm","Are you sure you want to delete?",parent=self.root)
                   if op==True:
                       cur.execute("delete from employee where empid=?",self.var_empid.get(),)
                       con.commit()
                       messagebox.showinfo("Success","Employee deleted successfully",parent=self.root)
                       self.clear()
       except Exception as ex:
           messagebox.showerror("Error",f"error due to{str(ex)}",parent=self.root)
    
   #clear
   def clear(self):
        self.var_empid.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Select")
        self.var_address.delete('1.0',END)
        self.var_salary.set("")
        self.var_searchtype.set("Select")
        self.show()

   #search
   def search(self):
       con=sqlite3.connect(database=r'IMS.db')
       cur=con.cursor()
       try:
           if self.var_searchtype.get()=="Select":
               messagebox.showerror("Error","Select search by option",parent=self.root)
           elif self.var_searchtxt.get()=="":
               messagebox.showerror("Error","Search input must be required",parent=self.root)
           else:
               cur.execute("Select * from employee where "+self.var_searchtype.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
               rows=cur.fetchall()
               if len(rows)!=0:
                   self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                   for row in rows:
                       self.EmployeeTable.insert('',END,values=row)
               else:
                   messagebox.showerror("Error","No record found",parent=self.root)

       except Exception as ex:
           messagebox.showerror("Error",f"error due to {str(ex)}",parent=self.root)




             


       