
from Tkinter import *
import Tkinter
import tkMessageBox
import sqlite3
conn=sqlite3.connect('dbms.db')
c=conn.cursor()
top=Tkinter.Tk()
list1=[0,1,2,3,4]
a=""
b=""
b1=""
d=0
e=""
def Supervisor():
    root=Tkinter.Tk()
    b1=Tkinter.Button(root,text="Login",fg="white",height=1,width=12,bg="blue",activebackground="blue",command=login)
    b1.pack()
    b1=Tkinter.Button(root,text="New User",fg="white",height=1,width=12,bg="blue",activebackground="blue",command=New_user_Supervisor)
    b1.pack()
    
def New_user_Supervisor():
    root=Tkinter.Tk()
    l1=Label(root,text="name")
    l1.pack()
    e1=Entry(root,bd=5)
    e1.pack()
    l1=Label(root,text="UID")
    l1.pack()
    e1=Entry(root,bd=5)
    e1.pack()
    l1=Label(root,text="Specialization")
    l1.pack()
    e1=Entry(root,bd=5)
    e1.pack()
    l1=Label(root,text="Mobileno")
    l1.pack()
    e1=Entry(root,bd=5)
    e1.pack()
    l1=Label(root,text="Email Id")
    l1.pack()
    e1=Entry(root,bd=5)
    e1.pack()
    b2=Tkinter.Button(root,text="Register",fg="white",height=1,width=12,bg="blue",activebackground="blue",command=sucess)
    b2.pack()
    b1=Tkinter.Button(root,text="Supervisor",fg="white",height=1,width=12,bg="blue",activebackground="blue",command=Supervisor)
    b1.pack()
    c.fetchone()
    conn.commit()
    
   
def sucess():
    root=Tkinter.Tk()
    tkMessageBox.showinfo("","sucessfully registered")

def data():
    print list1[1]

    c.execute("INSERT INTO data2 (name,password,address,mobile,email) values(a,b,b1,c,d)")
    c.execute('select * from data2')
    print c.fetchone()
    conn.commit()
    conn.close()

def login():
    root=Tkinter.Tk()
    l1=Label(root,text="username")
    l1.pack()
    e1=Entry(root,bd=5)
    e1.pack()
    l2=Label(root,text="Password")
    l2.pack()
    e2=Entry(root,bd=5)
    e2.pack()
    b1=Tkinter.Button(root,text="Submit",fg="white",height=1,width=12,bg="blue",activebackground="blue")
    b1.pack()
    q=Tkinter.Button(root,text="EXIT",fg="black",height=1,width=12,bg="red",command=quit,activebackground="red")
    q.pack()
    root.mainloop()


def new():
    root=Tkinter.Tk()
    l1=Label(root,text="name")
    l1.pack()
    e1=Entry(root,bd=5)
    e1.pack()
    list1[1]=e1.get()
    l6=Label(root,text="Passsword")
    l6.pack()
    e5=Entry(root,bd=5)
    e5.pack()
    list1[1]=e5.get()
    l2=Label(root,text="address")
    l2.pack()
    e2=Entry(root,bd=5)
    e2.pack()
    list1[2]=e2.get()
    l3=Label(root,text="gender")
    l3.pack()
    r1= Radiobutton(root, text="male", variable=IntVar(), value=1)
    r1.pack()
    r2= Radiobutton(root, text="Female", variable=IntVar(), value=2)
    r2.pack()
    l4=Label(root,text="Mobile Number")
    l4.pack()
    e3=Entry(root,bd=5)
    e3.pack()
    list1[3]=e3.get()
    l5=Label(root,text="Email:")
    l5.pack()
    e4=Entry(root,bd=5)
    e4.pack()
    list1[4]=e4.get()
    b1=Tkinter.Button(root,text="Submit",fg="white",height=1,command=data,width=12,bg="blue",activebackground="blue")
    b1.pack()
    q=Tkinter.Button(root,text="EXIT",fg="black",height=1,width=12,bg="red",command=quit,activebackground="red")
    q.pack()
    root.mainloop()





    
    
b1=Tkinter.Button(top,text="Login",fg="black",height=1,command= login,width=12,bg="white",activebackground="blue")
b2=Tkinter.Button(top,text="New User",fg="black",height=1,command=new,width=12,bg="white",activebackground="blue")
b3=Tkinter.Button(top,text="Request for Supervisor",fg="black",height=1,width=12,bg="white",command=New_user_Supervisor,activebackground="blue")
q=Tkinter.Button(top,text="EXIT",fg="black",height=1,width=12,bg="red",command=quit,activebackground="red")
b1.pack()
b2.pack()
b3.pack()
q.pack()
top.mainloop()
