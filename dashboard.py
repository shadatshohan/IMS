from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from employee import Employeeclass
from supply import Supplyclass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed By Shadat Shohan")
        self.root.config(bg="white")
        self.icon_title=PhotoImage(file="images/logo2.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,
        font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)

        #button clock
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date:DD-MM-YYYY\t\t Time:HH:MM:SS",
        font=("times new roman",15),padx=20,bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #sidemenu
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)
        lbl_menulogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menulogo.pack(side=TOP,fill=X)

        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)

        #sidemenu button
        self.icon_side=PhotoImage(file="images/side.png")
        lbl_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,anchor="w",font=("times new roman",20,"bold"),cursor="hand2",padx=5,bg="white",bd=3).pack(side=TOP,fill=X)
        lbl_supplier=Button(LeftMenu,text="Supplier",command=self.supply,image=self.icon_side,compound=LEFT,anchor="w",font=("times new roman",20,"bold"),cursor="hand2",padx=5,bg="white",bd=3).pack(side=TOP,fill=X)
        lbl_category=Button(LeftMenu,text="Category",image=self.icon_side,compound=LEFT,anchor="w",font=("times new roman",20,"bold"),cursor="hand2",padx=5,bg="white",bd=3).pack(side=TOP,fill=X)
        lbl_product=Button(LeftMenu,text="Product",image=self.icon_side,compound=LEFT,anchor="w",font=("times new roman",20,"bold"),cursor="hand2",padx=5,bg="white",bd=3).pack(side=TOP,fill=X)
        lbl_sales=Button(LeftMenu,text="Sales",image=self.icon_side,compound=LEFT,anchor="w",font=("times new roman",20,"bold"),cursor="hand2",padx=5,bg="white",bd=3).pack(side=TOP,fill=X)
        lbl_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,anchor="w",font=("times new roman",20,"bold"),cursor="hand2",padx=5,bg="white",bd=3).pack(side=TOP,fill=X)
        #content
        self.lbl_employee=Label(self.root,text="Total Employee\n[0]",bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"),bd=5,relief=RIDGE)
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[0]",bg="#ff5722",fg="white",font=("goudy old style",20,"bold"),bd=5,relief=RIDGE)
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="Total Category\n[0]",bg="#009688",fg="white",font=("goudy old style",20,"bold"),bd=5,relief=RIDGE)
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total Product\n[0]",bg="#607d8b",fg="white",font=("goudy old style",20,"bold"),bd=5,relief=RIDGE)
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[0]",bg="#ffc107",fg="white",font=("goudy old style",20,"bold"),bd=5,relief=RIDGE)
        self.lbl_sales.place(x=650,y=300,height=150,width=300)

        #footer
        lbl_footer=Label(self.root,text="IMS-Inventory Management System |Developed by Shadat Shohan\n Any techniqucal issue contact:01793332774",font=("times new roman",12),
    
        bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Employeeclass(self.new_win)
    def supply(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Supplyclass(self.new_win)




if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()