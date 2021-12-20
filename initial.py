from tkinter import *
root=Tk()
root.title("Simple registration")
root.geometry("600x600")
lbl=Label(root,text="simple registration",font=("times new roman",20,"bold"),bg="yellow",fg="red").pack(fill=X)
lbl1=Label(root,text="username").place(x=100,y=100)
lbl1_entry=Entry(root,text="enter text")
root.mainloop()