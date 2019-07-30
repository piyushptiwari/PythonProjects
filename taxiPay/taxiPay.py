from Tkinter import*
import Tkinter
import tkMessageBox
top = Tkinter.Tk()
log="admin"
passw="1234"
fare = IntVar()
k = IntVar()
fare = IntVar()
var=IntVar()
def login():
    print log
    print passw
    L1=Label(top,text="username")
    L1.pack(side = LEFT)
    UN = Entry(top,bd =5)
    UN.pack(side = LEFT)
    L2=Label(top,text="password")
    L2.pack(side = LEFT)
    PW = Entry(top,bd=5) 
    PW.pack(side = LEFT)
    def check():
        if (UN.get() == log and PW.get() == passw):
            book()
        else:
            
            def error():
                L2=Label(top,text="error")
                L2.pack(side = RIGHT)
            error()
        print UN.get()
        print PW.get()   
    s1=Tkinter.Button(top,text="Check",fg="red",bg="yellow",command = check)
    s1.pack(side = LEFT)
def newuser():
    U=Label(top,text="username")
    U.grid(row=2, column=0)
    UN = Entry(top,bd =5)
    UN.grid(row=2, column=1)
    P = Label(top,text="password")
    P.grid(row=2, column=2)
    PW = Entry(top,bd =5)
    PW.grid(row=2, column=3)
    R1=Radiobutton(top,text="Male",variable=var,value=1)   
    R1.grid(row=3, column=0)
    R2=Radiobutton(top,text="Female",variable=var,value=2)
    R2.grid(row=3, column=1)
    MN = Label(top,text="Mobile number")
    MN.grid(row=4, column=0)
    MNE = Entry(top,bd =5)
    MNE.grid(row=4, column=1)
    EM = Label(top,text="Email")
    EM.grid(row=5, column=0)
    EME = Entry(top,bd =5)
    EME.grid(row=6, column=1)
    def func():
        log=UN.get()
        passw=PW.get()
        print log
        print passw
        login()
    L1=Tkinter.Button(top,text="login",command = func)
    L1.grid(row=7, column=0)
def book():    
    U=Label(top,text="To")
    U.grid(row=1, column=10)
    UNu= Entry(top,bd =5)
    UNu.grid(row=2, column=10)
    P = Label(top,text="From")
    P.grid(row=3, column=10)
    PWu= Entry(top,bd =5)
    PWu.grid(row=4, column=10)
    def cal():
        print UNu.get()
        print PWu.get()
        if(UNu.get()=="maingate"):
            t=0
        elif(UNu.get()=="GH1"):
            t=1
        elif(UNu.get()=="GH2"):
            t=2
        elif(UNu.get()=="GH3"):
            t=3
        elif(UNu.get()=="addmissionblock"):
            t=4
        elif(UNu.get()=="BH1"):
            t=5
        elif(UNu.get()=="BH2"):
            t=6
        elif(UNu.get()=="BH3"):
            t=7
        elif(UNu.get()=="BH4"):
            t=8
        elif(UNu.get()=="BH5"):
            t=9 
        elif(UNu.get()=="BH6"):
            t=10
        else:
            t=11
        if(PWu.get()=="maingate"):
            f=0
        elif(PWu.get()=="GH1"):
            f=1
        elif(PWu.get()=="GH2"):
            f=2
        elif(PWu.get()=="GH3"):
            f=3
        elif(PWu.get()=="addmissionblock"):
            f=4
        elif(PWu.get()=="BH1"):
            f=5
        elif(PWu.get()=="BH2"):
            f=6
        elif(PWu.get()=="BH3"):
            f=7
        elif(PWu.get()=="BH4"):
            f=8
        elif(PWu.get()=="BH5"):
            f=9 
        elif(PWu.get()=="BH6"):
            f=10
        else:
            f=11
        k=t-f
        if(k<0):
            k=-k
            fare=10*k
        else:
            k=k
            fare=10*k
        def prin():
            top2=Tkinter.Tk()
            k1=Label(top2,text="kilometers")
            k1.grid(row=4, column=0)
            ki= Entry(top2,bd =5)
            ki.grid(row=5, column=0)
            f= Label(top2,text="Fare")
            f.grid(row=6, column=0)
            fi= Entry(top2,bd =5)
            fi.grid(row=7, column=0)
            ki.insert(0,k)
            fi.insert(0,fare)
            top2.mainloop()
        prin()
    a=Tkinter.Button(top,text="submit",fg="red",bg="yellow",command = cal)
    a.grid(row=5 ,column = 10)               
            
                
L=Tkinter.Button(top,text="login",command = login)
L.grid(row=0, column=0)
N=Tkinter.Button(top,text="newuser",command = newuser)
N.grid(row=0, column=1)
AR=Menubutton(top,text="Available Routes",relief=RAISED)
AR.grid(row=0,column=2)
AR.menu = Menu(AR,tearoff = 0 )
AR["menu"] = AR.menu

maingate  = IntVar()
admissionbl = IntVar()
bh1 = IntVar()
bh2 = IntVar()
bh3 = IntVar()
bh4 = IntVar()
bh5 = IntVar()
gh1 = IntVar()
gh2 = IntVar()
gh3 = IntVar()
law = IntVar()
buisness = IntVar()
AR.menu.add_checkbutton ( label="maingate",variable=maingate )
AR.menu.add_checkbutton ( label="admission block",variable=admissionbl )
AR.menu.add_checkbutton ( label="BH 1",variable=bh1 )
AR.menu.add_checkbutton ( label="BH 2",variable=bh2 )
AR.menu.add_checkbutton ( label="BH 3",variable=bh3 )
AR.menu.add_checkbutton ( label="BH 4",variable=bh4 )
AR.menu.add_checkbutton ( label="BH 5 & BH 6",variable=bh5)
AR.menu.add_checkbutton ( label="GH 1",variable=gh1)
AR.menu.add_checkbutton ( label="GH 2",variable=gh2)
AR.menu.add_checkbutton ( label="GH 3",variable=gh3)
AR.menu.add_checkbutton ( label="Law Block",variable=law)
AR.menu.add_checkbutton ( label="Buisness Block",variable=buisness)

top.mainloop()
