from Tkinter import *
import Tkinter
import tkMessageBox


def andexplain():
    top=Tkinter.Tk()
    L0 = Label(top, text="!! EXPLANATION !!",
           bg='red',fg="black",
           font="Times").grid(row=0,column=1)
    N0=Label(top, text="Number 1: ",
           fg="blue",
           font="Times",relief=RAISED,anchor = Tkinter.W,
                               justify = Tkinter.RIGHT).grid(row=1,column=0)
    F1 = Entry(top,bd=3)
    F1.grid(row=2,column=0)
    N0=Label(top, text="Number 2: ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=1,column=2)
    F2 = Entry(top,bd=3)
    F2.grid(row=2,column=2)
    Np=Label(top, text="Binary(Number 1.) ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=4,column=0)
    F3 = Entry(top,bd=3)
    F3.grid(row=5,column=0)
    Nu=Label(top, text="Binary(Number 2.) ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=4,column=2)
    F4 = Entry(top,bd=3)
    F4.grid(row=5,column=2)
    su=Label(top, text="AND ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=6,column=0)
    F5 = Entry(top,bd=3)
    F5.grid(row=6,column=1)
    tu=Label(top, text="Decimal Result ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=7,column=0)
    F6 = Entry(top,bd=3)
    F6.grid(row=7,column=1)
    def abc():
        if((str(F1.get())=="")&(str(F2.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            exp()

            
    def exp():
        no1=str(F1.get())
        no2=str(F2.get())
        btd = int(no1)
        btd1= int(no2)
        res=btd&btd1
        F6.insert(0,res)
        dtb=bin(btd)
        str(dtb)
        dtb=dtb[2:]
        F3.insert(0,dtb)
        dtb1=bin(btd1)
        str(dtb1)
        dtb1=dtb1[2:]
        F4.insert(0,dtb1)
        dtb2=bin(res)
        str(dtb2)
        dtb2=dtb2[2:]
        F5.insert(0,dtb2)
    B3=Tkinter.Button(top,relief=RAISED,text="EXPLAIN",fg='green',command=abc)
    B3.grid(row=8,column=1)

    
    def clear_textbox():
        F1.delete(0, END)
        F2.delete(0, END)
        F3.delete(0, END)
        F4.delete(0, END)
        F5.delete(0, END)
        F6.delete(0, END)
    B14=Button(top, text='RESET ALL ENTRIES',command=clear_textbox)
    B14.grid(row=9,column=1)
    """-------------TO RESET ALL ENTRIES ENDED---------------"""

    def close_window ():
        top.destroy()
    B15=Button(top,text='EXIT',command=close_window)
    B15.grid(row=9,column=2)
    """------------------------------------------------"""
    
def bitwiseand():
    top=Tkinter.Tk()
    L0 = Label(top, text="!! BITWISE AND OPERATIONS !!",
           fg="blue",bg="skyblue",
           font="Times").grid(row=0,column=1)

    N0=Label(top, text="Number 1: ",
           fg="blue",
           font="Times",relief=RAISED,anchor = Tkinter.W,
                               justify = Tkinter.RIGHT).grid(row=1,column=0)
    F1 = Entry(top,bd=3,fg="red")
    F1.grid(row=2,column=0)
    N0=Label(top, text="Number 2: ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=1,column=2)
    F2 = Entry(top,bd=3 ,fg="red")
    F2.grid(row=2,column=2)
    E22=Entry(top,bd=5,fg="red")
    E22.grid(row=3,column=2)

    def abc():
        if((str(F1.get())=="")&(str(F2.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            result()
                      
    def result():
        no1=str(F1.get())
        no2=str(F2.get())
        btd = int(no1)
        btd1= int(no2)
        res=btd&btd1
        E22.insert(0,res)
    
    B2=Tkinter.Button(top,relief=RAISED,text="RESULT",fg='green',anchor = Tkinter.W,
                               justify = Tkinter.RIGHT,command=abc)
    B2.grid(row=3,column=0)
    B9=Tkinter.Button(top,relief=RAISED,text="RESULT IS: ",fg='blue',anchor = Tkinter.W,
                               justify = Tkinter.RIGHT,command=abc)
    B9.grid(row=3,column=1)
    
    B3=Tkinter.Button(top,relief=RAISED,text="EXPLANATION",fg='green',command=andexplain)
    B3.grid(row=4,column=0)

    def clear_textbox():
        F1.delete(0, END)
        F2.delete(0, END)
        E22.delete(0,END)
    B14=Button(top, text='RESET ALL ENTRIES',command=clear_textbox)
    B14.grid(row=9,column=1)
    """-------------TO RESET ALL ENTRIES ENDED---------------"""

    def close_window ():
        top.destroy()
    B15=Button(top,text='EXIT',command=close_window)
    B15.grid(row=9,column=2)
"""------------------------------------------------------------------------------------"""
def orexplain():
    top=Tkinter.Tk()
    L0 = Label(top, text="!! EXPLANATION !!",
           bg='red',fg="black",
           font="Times").grid(row=0,column=1)
    N0=Label(top, text="Number 1: ",
           fg="blue",
           font="Times",relief=RAISED,anchor = Tkinter.W,
                               justify = Tkinter.RIGHT).grid(row=1,column=0)
    F1 = Entry(top,bd=3,fg="red")
    F1.grid(row=2,column=0)
    N0=Label(top, text="Number 2: ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=1,column=2)
    F2 = Entry(top,bd=3,fg="red")
    F2.grid(row=2,column=2)
    Np=Label(top, text="Binary(Number 1.) ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=4,column=0)
    F3 = Entry(top,bd=3,fg="red")
    F3.grid(row=5,column=0)
    Nu=Label(top, text="Binary(Number 2.) ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=4,column=2)
    F4 = Entry(top,bd=3,fg="red")
    F4.grid(row=5,column=2)
    su=Label(top, text="OR ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=6,column=0)
    F5 = Entry(top,bd=3,fg="red")
    F5.grid(row=6,column=1)
    tu=Label(top, text="Decimal Result ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=7,column=0)
    F6 = Entry(top,bd=3,fg="red")
    F6.grid(row=7,column=1)

    
    def abc():
        if((str(F1.get())=="")&(str(F2.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            exp()
            
    def exp():
        no1=str(F1.get())
        no2=str(F2.get())
        btd = int(no1)
        btd1= int(no2)
        res=btd|btd1
        F6.insert(0,res)
        dtb=bin(btd)
        str(dtb)
        dtb=dtb[2:]
        F3.insert(0,dtb)
        dtb1=bin(btd1)
        str(dtb1)
        dtb1=dtb1[2:]
        F4.insert(0,dtb1)
        dtb2=bin(res)
        str(dtb2)
        dtb2=dtb2[2:]
        F5.insert(0,dtb2)
    B3=Tkinter.Button(top,relief=RAISED,text="EXPLAIN",fg='green',command=abc)
    B3.grid(row=8,column=1)
    
    def clear_textbox():
        F1.delete(0, END)
        F2.delete(0, END)
        F3.delete(0, END)
        F4.delete(0, END)
        F5.delete(0, END)
        F6.delete(0, END)
    B14=Button(top, text='RESET ALL ENTRIES',command=clear_textbox)
    B14.grid(row=9,column=1)
    """-------------TO RESET ALL ENTRIES ENDED---------------"""

    def close_window ():
        top.destroy()
        
    B15=Button(top,text='EXIT',command=close_window)
    B15.grid(row=9,column=2)
    """-----------------------------------------------"""

def bitwiseor():
    top=Tkinter.Tk()
    L0 = Label(top, text="!! BITWISE OR OPERATIONS !!",
           fg="blue",bg="skyblue",
           font="Times").grid(row=0,column=1)

    N0=Label(top, text="Number 1: ",
           fg="blue",
           font="Times",relief=RAISED,anchor = Tkinter.W,
                               justify = Tkinter.RIGHT).grid(row=1,column=0)
    F1 = Entry(top,bd=3,fg="red")
    F1.grid(row=2,column=0)
    N0=Label(top, text="Number 2: ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=1,column=2)
    F2 = Entry(top,bd=3,fg="red")
    F2.grid(row=2,column=2)
    E22=Entry(top,bd=5,fg="red")
    E22.grid(row=3,column=2)

    def abc():
        if((str(F1.get())=="")&(str(F2.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            result()
            
    def result():
        no1=str(F1.get())
        no2=str(F2.get())
        btd = int(no1)
        btd1= int(no2)
        res=btd|btd1
        E22.insert(0,res)
    
    B2=Tkinter.Button(top,relief=RAISED,text="RESULT",fg='green',anchor = Tkinter.W,
                               justify = Tkinter.RIGHT,command=abc)
    B2.grid(row=3,column=0)
    B9=Tkinter.Button(top,relief=RAISED,text="RESULT IS: ",fg='blue',anchor = Tkinter.W,
                               justify = Tkinter.RIGHT,command=abc)
    B9.grid(row=3,column=1)
    
    B3=Tkinter.Button(top,relief=RAISED,text="EXPLANATION",fg='green',command=orexplain)
    B3.grid(row=4,column=0)
    
    def clear_textbox():
        F1.delete(0, END)
        F2.delete(0, END)
        E22.delete(0, END)
    B14=Button(top, text='RESET ALL ENTRIES',command=clear_textbox)
    B14.grid(row=9,column=1)
    """-------------TO RESET ALL ENTRIES ENDED---------------"""

    def close_window ():
        top.destroy()
    B15=Button(top,text='EXIT',command=close_window)
    B15.grid(row=9,column=2)
"""------------------------------------------------------------------------------------"""
def xorexplain():
    top=Tkinter.Tk()
    L0 = Label(top, text="!! EXPLANATION !!",
           bg='red',fg="black",
           font="Times").grid(row=0,column=1)
    N0=Label(top, text="Number 1: ",
           fg="blue",
           font="Times",relief=RAISED,anchor = Tkinter.W,
                               justify = Tkinter.RIGHT).grid(row=1,column=0)
    F1 = Entry(top,bd=3,fg="red")
    F1.grid(row=2,column=0)
    N0=Label(top, text="Number 2: ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=1,column=2)
    F2 = Entry(top,bd=3,fg="red")
    F2.grid(row=2,column=2)
    Np=Label(top, text="Binary(Number 1.) ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=4,column=0)
    F3 = Entry(top,bd=3,fg="red")
    F3.grid(row=5,column=0)
    Nu=Label(top, text="Binary(Number 2.) ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=4,column=2)
    F4 = Entry(top,bd=3,fg="red")
    F4.grid(row=5,column=2)
    su=Label(top, text="XOR ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=6,column=0)
    F5 = Entry(top,bd=3,fg="red")
    F5.grid(row=6,column=1)
    tu=Label(top, text="Decimal Result ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=7,column=0)
    F6 = Entry(top,bd=3,fg="red")
    F6.grid(row=7,column=1)
    
    def abc():
        if((str(F1.get())=="")&(str(F2.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            exp()
            
    def exp():
        no1=str(F1.get())
        no2=str(F2.get())
        btd = int(no1)
        btd1= int(no2)
        res=btd^btd1
        F6.insert(0,res)
        dtb=bin(btd)
        str(dtb)
        dtb=dtb[2:]
        F3.insert(0,dtb)
        dtb1=bin(btd1)
        str(dtb1)
        dtb1=dtb1[2:]
        F4.insert(0,dtb1)
        dtb2=bin(res)
        str(dtb2)
        dtb2=dtb2[2:]
        F5.insert(0,dtb2)
    B3=Tkinter.Button(top,relief=RAISED,text="EXPLAIN",fg='green',command=abc)
    B3.grid(row=8,column=1)
    def clear_textbox():
        F1.delete(0, END)
        F2.delete(0, END)
        F3.delete(0, END)
        F4.delete(0, END)
        F5.delete(0, END)
        F6.delete(0, END)
    B14=Button(top, text='RESET ALL ENTRIES',command=clear_textbox)
    B14.grid(row=9,column=1)
    """-------------TO RESET ALL ENTRIES ENDED---------------"""

    def close_window ():
        top.destroy()
        
    B15=Button(top,text='EXIT',command=close_window)
    B15.grid(row=9,column=2)
    """--------------------------------------------------"""
def bitwisexor():
    top=Tkinter.Tk()
    L0 = Label(top, text="!! BITWISE XOR OPERATIONS !!",
           fg="blue",bg="skyblue",
           font="Times").grid(row=0,column=1)

    N0=Label(top, text="Number 1: ",
           fg="blue",
           font="Times",relief=RAISED,anchor = Tkinter.W,
                               justify = Tkinter.RIGHT).grid(row=1,column=0)
    F1 = Entry(top,bd=3,fg="red")
    F1.grid(row=2,column=0)
    N0=Label(top, text="Number 2: ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=1,column=2)
    F2 = Entry(top,bd=3,fg="red")
    F2.grid(row=2,column=2)
    E22=Entry(top,bd=5,fg="red")
    E22.grid(row=3,column=2)

    def abc():
        if((str(F1.get())=="")&(str(F2.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            result()
            
    def result():
        no1=str(F1.get())
        no2=str(F2.get())
        btd = int(no1)
        btd1= int(no2)
        res=btd^btd1
        E22.insert(0,res)
    
    B2=Tkinter.Button(top,relief=RAISED,text="RESULT",fg='green',anchor = Tkinter.W,
                               justify = Tkinter.RIGHT,command=abc)
    B2.grid(row=3,column=0)
    B9=Tkinter.Button(top,relief=RAISED,text="RESULT IS: ",fg='blue',anchor = Tkinter.W,
                               justify = Tkinter.RIGHT,command=abc)
    B9.grid(row=3,column=1)
    
    B3=Tkinter.Button(top,relief=RAISED,text="EXPLANATION",fg='green',command=xorexplain)
    B3.grid(row=4,column=0)
    
    def clear_textbox():
        F1.delete(0, END)
        F2.delete(0, END)
        E22.delete(0, END)
    B14=Button(top, text='RESET ALL ENTRIES',command=clear_textbox)
    B14.grid(row=9,column=1)
    """-------------TO RESET ALL ENTRIES ENDED---------------"""

    def close_window ():
        top.destroy()
        
    B15=Button(top,text='EXIT',command=close_window)
    B15.grid(row=9,column=2)
"""------------------------------------------------------------------------------------"""
def notexplain():
    top=Tkinter.Tk()
    L0 = Label(top, text="!! EXPLANATION !!",
           bg='red',fg="black",
           font="Times").grid(row=0,column=1)
    N0=Label(top, text="Number 1: ",
           fg="blue",
           font="Times",relief=RAISED,anchor = Tkinter.W,
                               justify = Tkinter.RIGHT).grid(row=1,column=0)
    F1 = Entry(top,bd=3,fg="red")
    F1.grid(row=1,column=1)
    Np=Label(top, text="Binary : ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=2,column=0)
    F3 = Entry(top,bd=3,fg="red")
    F3.grid(row=2,column=1)
    su=Label(top, text="NOT ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=3,column=0)
    F5 = Entry(top,bd=3,fg="red")
    F5.grid(row=3,column=1)
    tu=Label(top, text="Decimal Result ",
               fg="blue",
               font="Times",relief=RAISED).grid(row=4,column=0)
    F6 = Entry(top,bd=3,fg="red")
    F6.grid(row=4,column=1)
    
    def abc():
        if((str(F1.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            exp()
            
    def exp():
        no1=str(F1.get())
        btd = int(no1)
        res=~btd
        F6.insert(0,res)
        dtb=bin(btd)
        str(dtb)
        dtb=dtb[2:]
        F3.insert(0,dtb)
        dtb2=bin(res)
        str(dtb2)
        dtb2=dtb2[2:]
        F5.insert(0,dtb2)
    B3=Tkinter.Button(top,relief=RAISED,text="EXPLAIN",fg='green',command=abc)
    B3.grid(row=5,column=1)
    def clear_textbox():
        F1.delete(0, END)
        F3.delete(0, END)
        F5.delete(0, END)
        F6.delete(0, END)
    B14=Button(top, text='RESET ALL ENTRIES',command=clear_textbox)
    B14.grid(row=6,column=1)
    """-------------TO RESET ALL ENTRIES ENDED---------------"""

    def close_window ():
        top.destroy()
        
    B15=Button(top,text='EXIT',command=close_window)
    B15.grid(row=6,column=2)
    """--------------------------------------------------"""
def bitwisenot():
    top=Tkinter.Tk()
    L0 = Label(top, text="!! BITWISE NOT OPERATIONS !!",
           fg="blue",bg="skyblue",
           font="Times").grid(row=0,column=1)

    N0=Label(top, text="Number 1: ",
           fg="blue",
           font="Times",relief=RAISED,anchor = Tkinter.W,
                               justify = Tkinter.RIGHT).grid(row=1,column=0)
    F1 = Entry(top,bd=3,fg="red")
    F1.grid(row=1,column=2)
    E22=Entry(top,bd=5,fg="red")
    E22.grid(row=2,column=2)

    def abc():
        if((str(F1.get())=="")):
           tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
        else:
            result()
            
    def result():
        no1=str(F1.get())
        btd = int(no1)
        res=~btd
        E22.insert(0,res)
    
    B2=Tkinter.Button(top,relief=RAISED,text="RESULT",fg='green',anchor = Tkinter.W,
                               justify = Tkinter.RIGHT,command=abc)
    B2.grid(row=2,column=0)
    B9=Tkinter.Button(top,relief=RAISED,text="RESULT IS: ",fg='blue',anchor = Tkinter.W,
                               justify = Tkinter.RIGHT,command=abc)
    B9.grid(row=2,column=1)
    
    B3=Tkinter.Button(top,relief=RAISED,text="EXPLANATION",fg='green',command=notexplain)
    B3.grid(row=3,column=0)
    
    def clear_textbox():
        F1.delete(0, END)
        E22.delete(0, END)
    B14=Button(top, text='RESET ALL ENTRIES',command=clear_textbox)
    B14.grid(row=4,column=1)
    """-------------TO RESET ALL ENTRIES ENDED---------------"""

    def close_window ():
        top.destroy()
        
    B15=Button(top,text='EXIT',command=close_window)
    B15.grid(row=4,column=2)
"""------------------------------------------------------------------------------------"""

top1=Tkinter.Tk()
I0 = Label(top1, text="!!  BITWISE OPERATIONS !!",
           fg="blue",bg="skyblue",
           font="Times").grid(row=0,column=1)
NT=Label(top1, text="( 1 ) ",
           fg="blue",
           font="Times").grid(row=1,column=0)
BTO=Tkinter.Button(top1,relief=RAISED,text="BITWISE AND",fg='green',command=bitwiseand)
BTO.grid(row=1,column=1)
NY=Label(top1, text="( 2 ) ",
           fg="blue",
           font="Times").grid(row=2,column=0)
DTO=Tkinter.Button(top1,relief=RAISED,text="BITWISE OR",fg='green',command=bitwiseor)
DTO.grid(row=2,column=1)
NI=Label(top1, text="( 3 ) ",
           fg="blue",
           font="Times").grid(row=3,column=0)
HTO=Tkinter.Button(top1,relief=RAISED,text="BITWISE XOR",fg='green',command=bitwisexor)
HTO.grid(row=3,column=1)
TI=Label(top1, text="( 4 ) ",
           fg="blue",
           font="Times").grid(row=4,column=0)
UTO=Tkinter.Button(top1,relief=RAISED,text="BITWISE NOT",fg='green',command=bitwisenot)
UTO.grid(row=4,column=1)

"""----------------------------------------------------------"""
def home():
    top1=Tkinter.Tk()

    I0 = Label(top1, text="!!  BITWISE OPERATIONS !!",
               fg="blue",bg="skyblue",
               font="Times").grid(row=0,column=1)
    NT=Label(top1, text="( 1 ) ",
               fg="blue",
               font="Times").grid(row=1,column=0)
    BTO=Tkinter.Button(top1,relief=RAISED,text="BITWISE AND",fg='green',command=bitwiseand)
    BTO.grid(row=1,column=1)
    NY=Label(top1, text="( 2 ) ",
               fg="blue",
               font="Times").grid(row=2,column=0)
    DTO=Tkinter.Button(top1,relief=RAISED,text="BITWISE OR",fg='green',command=bitwiseor)
    DTO.grid(row=2,column=1)
    NI=Label(top1, text="( 3 ) ",
               fg="blue",
               font="Times").grid(row=3,column=0)
    HTO=Tkinter.Button(top1,relief=RAISED,text="BITWISE XOR",fg='green',command=bitwisexor)
    HTO.grid(row=3,column=1)
    TI=Label(top1, text="( 4 ) ",
               fg="blue",
               font="Times").grid(row=4,column=0)
    UTO=Tkinter.Button(top1,relief=RAISED,text="BITWISE NOT",fg='green',command=bitwisenot)
    UTO.grid(row=4,column=1)
    def close_window():
        top1.destroy()
        top5=Tkinter.Tk()
        D=Label(top5,text="Submitted By:-",relief=RAISED,bg='red',fg="black")
        D.grid(row=0,column=0)
        D1=Label(top5,text="1.Charchit  Bakliwal -11505605",relief=GROOVE,fg='blue')
        D1.grid(row=1,column=0)
        D2=Label(top5,text="2.Jasdeep Singh Mahrok-11508260",relief=GROOVE,fg='blue')
        D2.grid(row=2,column=0)
        D3=Label(top5,text="3.Manjeet  Patel-11510884",relief=GROOVE,fg='blue')
        D3.grid(row=3,column=0)
        D4=Label(top5,text="Submitted To:-",relief=RAISED,fg='black',bg='red')
        D4.grid(row=4,column=0)
        D5=Label(top5,text="Mr. Aditya Khamparia",relief=GROOVE,fg='blue')
        D5.grid(row=5,column=0)                         
        def close_window1():
            top5.destroy()
            home()
        def close_window2():
            top5.destroy()
        B15=Button(top5,text = "EXIT",command=close_window2,relief=GROOVE,fg='black')
        B15.grid(row=6,column=1)
        B16=Button(top5,text = "HOME",command=close_window1,relief=GROOVE,fg='black')
        B16.grid(row=6,column=0)
    B15=Button (top1,text = "EXIT",command=close_window,relief=GROOVE,fg='black')
    B15.grid(row=5,column=1)
    
def close_window():
    top1.destroy()
    top5=Tkinter.Tk()
    D=Label(top5,text="Submitted By:-",relief=RAISED,bg='red',fg="black")
    D.grid(row=0,column=0)
    D1=Label(top5,text="1.Charchit  Bakliwal -11505605",relief=GROOVE,fg='blue')
    D1.grid(row=1,column=0)
    D2=Label(top5,text="2.Jasdeep Singh Mahrok-11508260",relief=GROOVE,fg='blue')
    D2.grid(row=2,column=0)
    D3=Label(top5,text="3.Manjeet  Patel-11510884",relief=GROOVE,fg='blue')
    D3.grid(row=3,column=0)
    D4=Label(top5,text="Submitted To:-",relief=RAISED,fg='black',bg='red')
    D4.grid(row=4,column=0)
    D5=Label(top5,text="Mr. Aditya Khamparia",relief=GROOVE,fg='blue')
    D5.grid(row=5,column=0)
    def close_window1():
        top5.destroy()
        home()
    def close_window2():
        top5.destroy()
    B15=Button(top5,text = "EXIT",command=close_window2,relief=GROOVE,fg='black')
    B15.grid(row=6,column=1)
    B16=Button(top5,text = "HOME",command=close_window1,relief=GROOVE,fg='black')
    B16.grid(row=6,column=0)

B18=Button (top1,text = "EXIT",command=close_window,relief=GROOVE,fg='black')
B18.grid(row=5,column=1)
top1.mainloop()
