from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class Supplyclass:
   def __init__(self,root):
       self.root=root
       self.root.geometry("1100x500+220+130")
       self.root.title("Inventory Management System | Developed by Shadat Shohan")
       self.root.config(bg="white")
       self.root.focus_force()

       #variables
       self.var_searchtxt=StringVar()
       self.var_invoice=StringVar()
       self.var_name=StringVar()
       self.var_contact=StringVar()

       #searchframe
       lbl_search=Label(self.root,text="Invoice no:",font=("goudy old style",15),bg="white").place(x=700,y=80)
       txt_search=Entry(self.root,font=("goudy old style",15),textvariable=self.var_searchtxt,bg="lightyellow").place(x=800,y=80,width=160)
       btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=980,y=80,width=100,height=28)

       #title
       title=Label(self.root,text="Supplier Details",font=("goudy old style",20,"bold"),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)

       #content
       lbl_invoice=Label(self.root,text="Invoice No",font=("goudy old style",15),bg="white").place(x=50,y=80)
       lbl_name=Label(self.root,text="Supplier name",font=("goudy old style",15),bg="white").place(x=50,y=120)
       lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=160)
       lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=200)

       ent_invoice=Entry(self.root,textvariable=self.var_invoice,bg="lightyellow").place(x=180,y=80,width=180,height=27)
       ent_name=Entry(self.root,textvariable=self.var_name,bg="lightyellow").place(x=180,y=120,width=180,height=27)
       ent_contact=Entry(self.root,textvariable=self.var_contact,bg="lightyellow").place(x=180,y=160,width=180,height=27)
       self.var_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
       self.var_desc.place(x=180,y=200,width=470,height=120)

       #buttons
       btn_add=Button(self.root,text="Save",command=self.add,bg="#2196f3",font=("goudy old style",15),fg="white",cursor="hand2").place(x=180,y=370,width=110,height=35)
       btn_update=Button(self.root,text="Update",command=self.update,bg="#4caf50",font=("goudy old style",15),fg="white",cursor="hand2").place(x=300,y=370,width=110,height=35)
       btn_delete=Button(self.root,text="Delete",command=self.delete,bg="#f44336",font=("goudy old style",15),fg="white",cursor="hand2").place(x=420,y=370,width=110,height=35)
       btn_clear=Button(self.root,text="Clear",command=self.clear,bg="#607d8b",font=("goudy old style",15),fg="white",cursor="hand2").place(x=540,y=370,width=110,height=35)

       #employee details
       sup_frame=Frame(self.root,bd=3,relief=RIDGE)
       sup_frame.place(x=700,y=120,width=380,height=350)
       #scrollbar with treeview
       scrolly=Scrollbar(sup_frame,orient=VERTICAL)
       scrollx=Scrollbar(sup_frame,orient=HORIZONTAL)
       self.SupplyTable=ttk.Treeview(sup_frame,columns=("invoice","name","contact","description"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
       scrollx.pack(side=BOTTOM,fill=X)
       scrolly.pack(side=RIGHT,fill=Y)
       scrollx.config(command=self.SupplyTable.xview)
       scrolly.config(command=self.SupplyTable.yview)
       #hedaing and column set
       self.SupplyTable.heading("invoice",text="Invoice no")
       self.SupplyTable.heading("name",text="Name")
       self.SupplyTable.heading("contact",text="Contact")
       self.SupplyTable.heading("description",text="Description")

       self.SupplyTable["show"]="headings"

       self.SupplyTable.column("invoice",width=90)
       self.SupplyTable.column("name",width=100)
       self.SupplyTable.column("contact",width=100)
       self.SupplyTable.column("description",width=100)
       self.SupplyTable.pack(fill=BOTH,expand=1)
       self.SupplyTable.bind("<ButtonRelease-1>",self.get_data)
       self.show()

   #database creation
   # Save    
   def add(self):
       con=sqlite3.connect(database=r'IMS.db')
       cur=con.cursor()
       try:
           if self.var_invoice.get()=="":
               messagebox.showerror("Error","Supplier ID must be required",parent=self.root)
           else:
               cur.execute("Select * from supply where invoice=?",(self.var_invoice.get(),))
               row=cur.fetchone()
               if row!=None:
                   messagebox.showerror("Error","Supplier ID already assigned,try different",parent=self.root)
               else:
                   cur.execute("Insert into supply(invoice,name,contact,desc) values(?,?,?,?)",(
                       self.var_invoice.get(),
                       self.var_name.get(),
                       self.var_contact.get(),
                       self.var_desc.get('1.0',END),
                      ))
                   con.commit()
                   messagebox.showinfo("Success","Supplier added successfully",parent=self.root)
                   self.show()
                    

       except Exception as ex:
           messagebox.showerror("error",f"error due to:{str(ex)}",parent=self.root)
     
    #show to panel
   def show(self):
    con=sqlite3.connect(database=r'IMS.db')
    cur=con.cursor()
    try:
        cur.execute("Select * from supply")
        rows=cur.fetchall()
        self.SupplyTable.delete(*self.SupplyTable.get_children())
        for row in rows:
            self.SupplyTable.insert('',END,values=row)

    except Exception as ex:
        messagebox.showerror("Error",f"Error due to:{str(ex)}")

   #getdata
   def get_data(self,ev):
       f=self.SupplyTable.focus()
       content=self.SupplyTable.item(f)
       row=content['values']
       self.var_invoice.set(row[0])
       self.var_name.set(row[1])
       self.var_contact.set(row[2])
       self.var_desc.delete('1.0',END)
       self.var_desc.insert(END,row[3])

    #update date
   def update(self):
       con=sqlite3.connect(database=r'IMS.db')
       cur=con.cursor()
       try:
           if self.var_invoice.get()=="":
               messagebox.showerror("Error","Supplier ID must be required",parent=self.root)
           else:
               cur.execute("Select * from supply where invoice=?",(self.var_invoice.get(),))
               row=cur.fetchone()
               if row==None:
                   messagebox.showerror("Error","Invalid Supplier Id",parent=self.root)
               else:
                   cur.execute("Update supply set name=?,contact=?,desc=? where invoice=?",(
                       self.var_name.get(),
                       self.var_contact.get(),
                       self.var_desc.get('1.0',END),
                       self.var_invoice.get(),
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
           if self.var_invoice.get()=="":
               messagebox.showerror("Error","Supplier ID must be needed",parent=self.root)
           else:
               cur.execute("Select * from supply where invoice=?",self.var_invoice.get(),)
               row=cur.fetchone()
               if row==None:
                   messagebox.showerror("Error","Invalid Supplier ID",parent=self.root)
               else:
                   op=messagebox.askyesno("Confirm","Are you sure you want to delete?",parent=self.root)
                   if op==True:
                       cur.execute("delete from supply where invoice=?",self.var_invoice.get(),)
                       con.commit()
                       messagebox.showinfo("Success","Supplier deleted successfully",parent=self.root)
                       self.clear()
       except Exception as ex:
           messagebox.showerror("Error",f"error due to {str(ex)}",parent=self.root)
    
   #clear
   def clear(self):
        self.var_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_desc.delete('1.0',END)
        self.show()

   #search
   def search(self):
       con=sqlite3.connect(database=r'IMS.db')
       cur=con.cursor()
       try:
           if self.var_searchtxt.get()=="":
               messagebox.showerror("Error","Search input must be required",parent=self.root)
           else:
               cur.execute("Select * from supply where invoice=?",(self.var_searchtxt.get(),))
               row=cur.fetchone()
               if row!=None:
                   self.SupplyTable.delete(*self.SupplyTable.get_children())
                   self.SupplyTable.insert('',END,values=row)
               else:
                   messagebox.showerror("Error","No record found",parent=self.root)

       except Exception as ex:
           messagebox.showerror("Error",f"error due to {str(ex)}",parent=self.root)




             


       