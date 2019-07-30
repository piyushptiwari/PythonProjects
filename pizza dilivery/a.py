from Tkinter import *
import Tkinter
import sqlite3
import tkMessageBox
from PIL import Image,ImageTk

def Enter_db(Name,Email,phone,ptype):
        plist=[phone,Name,Email,phone,ptype]
        conn=sqlite3.connect('pizza2.db')
        c=conn.cursor()
        #c.execute('CREATE TABLE PIZZA2(ID INT(10),NAME VARCHAR(30),EMAIL VARCHAR(50),PHONE INT(10),PTYPE INT(2))')
        c.execute('INSERT INTO PIZZA2 VALUES(?,?,?,?,?)',plist)
        conn.commit()
        conn.close()
        tkMessageBox.showinfo("ORDER ID","Your Order id is : "+str(phone))
        #print c.execute('select * from pizza2')
               # print row
def delete_db(pid):
        conn=sqlite3.connect('pizza2.db')
        c=conn.cursor()
        lpid=[pid]
        #c.execute('create table cancel (ID INT(10),NAME VARCHAR(30),EMAIL VARCHAR(50),PHONE INT(10),PTYPE INT(2))')
        c.execute('select * from pizza2  where ID=(?)',lpid)
        list1=c.fetchmany()
        print list1
        c.execute('insert into cancel values (?,?,?,?,?)',list1[0])
        c.execute('delete from pizza2 where ID=(?)',lpid)
        
        tkMessageBox.showinfo("ORDER ID","Your Order id:"+str(pid)+" is cancelled")
        conn.commit()
        conn.close()
       
        
def cancel_pizza():
        root=Tkinter.Tk()
        command=lambda :delete_db(Entry_1.get())
        label_1=Label(root,text="order ID")
        Entry_1=Entry(root,width=50)
        Button_1=Button(root,text="Cancel Order",command=command)
        
        label_1.grid(row=2,column=2,padx=10,pady=10)
        Entry_1.grid(row=2,column=3,padx=10,pady=10,columnspan=3)
        Button_1.grid(row=4,column=2,padx=10,pady=10)
        root.mainloop()

def served_pizza():
        root1=Tkinter.Tk()
        root1.configure(background="#a1dbcd")
        RTitle=root1.title("windows")
        RWidth=1080
        RHeight=700
        root1.geometry(("%dx%d")%(RWidth,RHeight))
        label_1=Label(root1,text="Served Order description are as follows:")
        label_1.grid(row=2,column=2,padx=10,pady=10)
        conn=sqlite3.connect('pizza2.db')
        c=conn.cursor()
        n=6
        label_2=Label(root1,text="ID")
        label_2.grid(row=4,column=0,padx=10,pady=10)

        label_3=Label(root1,text="NAME")
        label_3.grid(row=4,column=1,padx=10,pady=10)

        label_4=Label(root1,text="EMAIL")
        label_4.grid(row=4,column=2,padx=10,pady=10)

        label_5=Label(root1,text="PHONE")
        label_5.grid(row=4,column=3,padx=10,pady=10)

        label_6=Label(root1,text="PIZZA TYPE")
        label_6.grid(row=4,column=4,padx=10,pady=10)
        
        for row1 in c.execute('select * from pizza2'):
                n+=1
                label_7=Label(root1,text=str(row1[0]),justify="left")
                label_7.grid(row=n,column=0,padx=0,pady=10)
                label_8=Label(root1,text=str(row1[1]))
                label_8.grid(row=n,column=1,padx=10,pady=10)
                label_9=Label(root1,text=str(row1[2]))
                label_9.grid(row=n,column=2,padx=10,pady=10)
                label_10=Label(root1,text=str(row1[3]))
                label_10.grid(row=n,column=3,padx=10,pady=10)
                label_11=Label(root1,text=str(row1[4]))
                label_11.grid(row=n,column=4,padx=10,pady=10)
                
        root1.mainloop()
                
def abc(a):
        b=str(a);
        if len(b) > 0:
                root=Tkinter.Toplevel()
                root.configure(background="#a1dbcd")
                RTitle=root.title("windows")
                RWidth=1080
                RHeight=700
                root.geometry(("%dx%d")%(RWidth,RHeight))
                im = Image.open('C:\\Users\\aman\\Desktop\\python py files\\python\\abc1.jpeg')
                tkimage = ImageTk.PhotoImage(im)
                myvar=Tkinter.Label(root,image = tkimage)
                myvar.place(x=0, y=0, relwidth=1, relheight=1)
                root.mainloop()
        else:
                tkMessageBox.showinfo("ERROR..!!!","Please Enter Valid order No.")
                
def track_pizza():
        root=Tkinter.Tk()
        label_1=Label(root,text="order ID")
        Entry_1=Entry(root,width=50)
        command2=lambda :abc(Entry_1.get())
        Button_1=Button(root,text="track Order",command=command2)
        label_1.grid(row=2,column=2,padx=10,pady=10)
        Entry_1.grid(row=2,column=3,padx=10,pady=10,columnspan=3)
        
        Button_1.grid(row=4,column=2,padx=10,pady=10)
        root.mainloop()


        

def canceled_pizza():
        root1=Tkinter.Tk()
        root1.configure(background="#a1dbcd")
        RTitle=root1.title("windows")
        RWidth=1080
        RHeight=700
        root1.geometry(("%dx%d")%(RWidth,RHeight))
        
        label_1=Label(root1,text="Cancelled Order description are as follows:")
        label_1.grid(row=2,column=2,padx=10,pady=10)
        conn=sqlite3.connect('pizza2.db')
        c=conn.cursor()
        n=6
        label_2=Label(root1,text="ID")
        label_2.grid(row=4,column=0,padx=10,pady=10)

        label_3=Label(root1,text="NAME")
        label_3.grid(row=4,column=1,padx=10,pady=10)

        label_4=Label(root1,text="EMAIL")
        label_4.grid(row=4,column=2,padx=10,pady=10)

        label_5=Label(root1,text="PHONE")
        label_5.grid(row=4,column=3,padx=10,pady=10)

        label_6=Label(root1,text="PIZZA TYPE")
        label_6.grid(row=4,column=4,padx=10,pady=10)
        
        for row1 in c.execute('select * from cancel'):
                n+=1
                label_7=Label(root1,text=str(row1[0]),justify="left")
                label_7.grid(row=n,column=0,padx=0,pady=10)
                label_8=Label(root1,text=str(row1[1]))
                label_8.grid(row=n,column=1,padx=10,pady=10)
                label_9=Label(root1,text=str(row1[2]))
                label_9.grid(row=n,column=2,padx=10,pady=10)
                label_10=Label(root1,text=str(row1[3]))
                label_10.grid(row=n,column=3,padx=10,pady=10)
                label_11=Label(root1,text=str(row1[4]))
                label_11.grid(row=n,column=4,padx=10,pady=10)
                
        root1.mainloop()
        


def order_pizza():
        root2=Tkinter.Tk()
        root2.configure(background="#a1dbcd")
        RTitle=root2.title("windows")
        RWidth=1080
        RHeight=700
        root2.geometry(("%dx%d")%(RWidth,RHeight))
        var1=IntVar()
        
        label_1=Label(root2,text="Name")
        label_2=Label(root2,text="Pizza type")
        label_3=Label(root2,text="E-Mail")
        label_4=Label(root2,text="Phone")
        
        

        
        OPTIONS = [
            "Small Pizza (100 Rs)",
            "Medium Pizza(250 Rs)",
            "Large Pizza (400 Rs)"
        ]

        

        variable = StringVar(root2)
        variable.set(OPTIONS[0]) # default value

        w = apply(OptionMenu, (root2, variable) + tuple(OPTIONS))
        w.grid(row=3,column=3,padx=10,pady=10)
        
        Entry_1=Entry(root2,width=50)
        Entry_2=Entry(root2,width=50)
        Entry_3=Entry(root2,width=50)
        
        command=lambda :Enter_db(Entry_1.get(),Entry_2.get(),Entry_3.get(),variable.get())
        Button_1=Button(root2,text="Order pizza",command=command)
        label_1.grid(row=2,column=2,padx=10,pady=10)
        label_2.grid(row=3,column=2,padx=10,pady=10)
        label_3.grid(row=4,column=2,padx=10,pady=10)
        label_4.grid(row=5,column=2,padx=10,pady=10)
        
        Entry_1.grid(row=2,column=3,padx=10,pady=10,columnspan=3)
        Entry_2.grid(row=4,column=3,padx=10,pady=10,columnspan=3)
        Entry_3.grid(row=5,column=3,padx=10,pady=10,columnspan=3)
        Button_1.grid(row=6,column=2,padx=10,pady=10)
      
        root2.mainloop()
def customer():
        root=Tkinter.Toplevel()
        root.configure(background="#a1dbcd")
        RTitle=root.title("windows")
        RWidth=1080
        RHeight=700
        root.geometry(("%dx%d")%(RWidth,RHeight))
        im = Image.open('C:\\Users\\aman\\Desktop\\python py files\\python\\pizzabackground.jpg')
        tkimage = ImageTk.PhotoImage(im)
        myvar=Tkinter.Label(root,image = tkimage)
        myvar.place(x=0, y=0, relwidth=1, relheight=1)
        command=lambda :order_pizza()
        command1=lambda :cancel_pizza()
        command2=lambda :track_pizza()
        command4=lambda :ex(root)
        Button_1=Button(root,text="Order pizza",relief=GROOVE,font=("Arial",12,"bold"),bg="white",fg="black",width=15,height=5,command=command)
        Button_2=Button(root,text="Cancel Order",relief=GROOVE,font=("Arial",12,"bold"),bg="white",fg="black",width=15,height=5,command=command1)
        Button_3=Button(root,text="Track Order",relief=GROOVE,font=("Arial",12,"bold"),bg="white",fg="black",width=15,height=5,command=command2)
        Button_4=Button(root,text="Back",relief=GROOVE,font=("Arial",12,"bold"),bg="white",fg="black",width=5,height=2,command=command4)
        Button_1.grid(row=2,column=1,padx=50,pady=280)
        Button_2.grid(row=2,column=2,padx=90,pady=280)
        Button_3.grid(row=2,column=3,padx=70,pady=280)
        Button_4.grid(row=1,column=1,padx=20,pady=10)
        root.mainloop()
def ex(root):
        root.destroy()
def vendor():
        root=Tkinter.Toplevel()
        root.configure(background="#a1dbcd")
        RTitle=root.title("windows")
        RWidth=1080
        RHeight=700
        root.geometry(("%dx%d")%(RWidth,RHeight))
        im = Image.open('C:\\Users\\aman\\Desktop\\python py files\\python\\pizzabackground.jpg')
        tkimage = ImageTk.PhotoImage(im)
        myvar=Tkinter.Label(root,image = tkimage)
        myvar.place(x=0, y=0, relwidth=1, relheight=1)
        
        command=lambda :order_pizza()
        command1=lambda :cancel_pizza()
        command2=lambda :served_pizza()
        command3=lambda :canceled_pizza()
        command4=lambda :ex(root)
        Button_1=Button(root,text="New pizza Order",relief=GROOVE,font=("Arial",12,"bold"),bg="white",fg="black",width=15,height=5,command=command)
        Button_2=Button(root,text="Cancel order",relief=GROOVE,font=("Arial",12,"bold"),bg="white",fg="black",width=15,height=5, command=command1)
        Button_3=Button(root,text="Served Order",relief=GROOVE,font=("Arial",12,"bold"),bg="white",fg="black",width=15,height=5,command=command2)
        Button_4=Button(root,text="Canceled Orders",relief=GROOVE,font=("Arial",12,"bold"),bg="white",fg="black",width=15,height=5,command=command3)
        Button_5=Button(root,text="Back",relief=GROOVE,font=("Arial",12,"bold"),bg="white",fg="black",width=5,height=2,command=command4)
        
        Button_1.grid(row=1,column=2,padx=70,pady=90)
        Button_2.grid(row=1,column=4,padx=70,pady=90)
        Button_3.grid(row=2,column=2,padx=70,pady=10)
        Button_4.grid(row=2,column=4,padx=70,pady=10)
        Button_5.grid(row=0,column=1,padx=20,pady=10)
        root.mainloop()

        
def main():        
        root=Tkinter.Tk()
        root.configure(background="#a1dbcd")
        RTitle=root.title("windows")
        RWidth=1080
        RHeight=700
        root.geometry(("%dx%d")%(RWidth,RHeight))
        command=lambda :vendor()
        command_1=lambda :customer()
        im = Image.open('C:\\Users\\aman\\Desktop\\python py files\\python\\pizzabackground.jpg')
        tkimage = ImageTk.PhotoImage(im)
        myvar=Tkinter.Label(root,image = tkimage)
        myvar.place(x=0, y=0, relwidth=1, relheight=1)
        Button_1=Button(root,text="Vendor",activebackground="Red",relief=SUNKEN,font=("Arial",12,"bold"),bg="white",fg="black",width=15,height=5,command=command)
        Button_2=Button(root,text="Customer",activebackground="Green",relief=GROOVE,font=("Arial",12,"bold"),bg="white",fg="black",width=15,height=5,command=command_1)
        Button_1.grid(row=2,column=2,padx=260,pady=280)
        Button_2.grid(row=2,column=4,padx=20,pady=280)

        root.mainloop()

main()
