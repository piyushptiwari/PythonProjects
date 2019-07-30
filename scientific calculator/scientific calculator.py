from __future__ import division
import sys
from Tkinter import *
import Tkinter
import math
master=Tkinter.Tk()
master.title("Scientific Calculator")
master.geometry('520x388')
lL=Label(master,text="               INPUT:",bg="grey",fg="red")
lL.grid(row=0,column=1)
l1=Label(master,text="           OUTPUT:",bg="grey",fg="red")
l1.grid(row=1,column=1)
e = Entry(master,width=40,bd=4,font=10,relief=RIDGE)
e.grid(row=0,column=2,columnspan=15,pady=25)
e.focus_set()
e1 = Entry(master,width=40,bd=4,font=10,justify="right",relief=RIDGE)
e1.grid(row=1,column=2,columnspan=15,pady=25)
L=Label(master,text="First select Degree/Radian:",bg="yellow")
L.grid(row=3,column=1 ,columnspan=3)
"""--------------------------QUIT------------------------------"""
def quit1():
    master.destroy()


def abs1():
     try:
        exp1=e.get()
        q1= eval(exp1) 
     except SyntaxError or NameError:
         e.delete(0,END)
         e.insert(0,'Invalid Input!')
     else:
         abso=abs(q1)
         e1.delete(0,END)
         e1.insert(0,abso)
"""----------------------EQUAL TO-----------------------------------"""
def equals():
    
    try:
        exp=e.get()
        q=eval(exp) 
    except SyntaxError or NameError:
        e.delete(0,END)
        e.insert(0,'Invalid Input!')
    else:
        e1.delete(0,END)
        e1.insert(0,q)
"""---------------------------INSERTION------------------------------------------"""
def action(argi):
    
    e.insert(END,argi)
"""----------------------------CLEAR ALL------------------------------------------"""
def clearall():
    e.delete(0,END)
    e1.delete(0,END)
"""-------------------------CLEAR ONE CHARACTER--------------------------"""
 
def clear1():
    txt=e.get()[:-1]
    e.delete(0,END)
    e.insert(0,txt)
"""------------------------------SQUAREROOT---------------------------------"""
def sqroot():
    try:
        exp1=e.get()
        q1= eval(exp1) 
    except SyntaxError or NameError:
        e.delete(0,END)
        e.insert(0,'Invalid Input!')
    else:
        sqrtval=math.sqrt(q1)
        e1.delete(0,END)
        e1.insert(0,sqrtval)
"""--------------------------SQUARE-----------------------------------"""
def square():
    try:
        exp2=e.get()
        q2=eval(exp2)

    except SyntaxError or NameError:
        e.delete(0,END)
        e.insert(0,'Invalid Input!')
    else:
        sqval=math.pow(q2,2)
        e1.delete(0,END)
        e1.insert(0,sqval)
"""----------------------------------CUBE--------------------------"""
def Cube():
    try:
        exp2=e.get()
        q2=eval(exp2)
        
    except SyntaxError or NameError:
        e.delete(0,END)
        e.insert(0,'Invalid Input!')
    else:
        cuval=math.pow(q2,3)
        e1.delete(0,END)
        e1.insert(0,cuval)        
"""-------------------------CEIL FUNCTION----------------------------"""
def ceil1():
    try:
        x1=e.get()
        y1=eval(x1)
         
    except SyntaxError or NameError:
        e.delete(0,END)
        e.insert(0,'Invalid Input!')
    else:
        ceil=math.ceil(y1)
        e1.delete(0,END)
        e1.insert(0,ceil)
"""-------------------------FLOOR FUNCTION---------------------------"""
def floor1():
    try:
        x=e.get()
        y=eval(x)
         
    except SyntaxError or NameError:
        e.delete(0,END)
        e.insert(0,'Invalid Input!')
    else:
        floor=math.floor(y)
        e1.delete(0,END)
        e1.insert(0,floor)
"""---------------------------LOG BASE 10-----------------------------"""    
def log():
    try:
        x2=e.get()
        y2=eval(x2)
         
    except SyntaxError or NameError:
        e.delete(0,END)
        e.insert(0,'Invalid Input!')
    else:
        log1=math.log10(y2)
        e1.delete(0,END)
        e1.insert(0,log1)

def expo():
    try:
        x2=e.get()
        y2=eval(x2)
         
    except SyntaxError or NameError:
        e.delete(0,END)
        e.insert(0,'Invalid Input!')
    else:
        e12=math.exp(y2)
        e1.delete(0,END)
        e1.insert(0,e12)
"""-----------------TRIGNOMERTIC FUNCTION IN RADIANS------------------------"""    
def radians():
    def sin():
        try:
            x3=e.get()
            y3=eval(x3)
         
        except SyntaxError or NameError:
            e.delete(0,END)
            e.insert(0,'Invalid Input!')
        else:
            sin1=math.sin(y3)
            e1.delete(0,END)
            e1.insert(0,sin1)

    def cos():
        try:
            x4=e.get()
            y4=eval(x4)
         
        except SyntaxError or NameError:
            e.delete(0,END)
            e.insert(0,'Invalid Input!')
        else:
            cos1=math.cos(y4)
            e1.delete(0,END)
            e1.insert(0,cos1)

    def tan():
        try:
            x5=e.get()
            y5=eval(x5)
         
        except SyntaxError or NameError:
            e.delete(0,END)
            e.insert(0,'Invalid Input!')
        else:
            tan1=math.tan(y5)
            e1.delete(0,END)
            e1.insert(0,tan1)

    def atan():
        try:
            x6=e.get()
            y6=eval(x6)
        except SyntaxError or NameError:
            e.delete(0,END)
            e.insert(0,'Invalid Input!')
        else:
            tan2=math.atan(y6)
            e1.delete(0,END)
            e1.insert(0,tan2)

    def acos():
        x7=e.get()
        y7=eval(x7)
         
        if y7>=-1 and y7<=1:
            cosx=math.acos(y7)
            e1.delete(0,END)
            e1.insert(0,cosx)
        elif SyntaxError or NameError:
            e.delete(0,END)
            e.insert(0,'Invalid Input!')
        else:
             cosx=math.acos(y7)
             e1.delete(0,END)
             e1.insert(0,'Invalid Input!')
        

    def asin():
        x7=e.get()
        y7=eval(x7)
        if y7>=-1 and y7<=1:
            sinx=math.asin(y7)
            e1.delete(0,END)
            e1.insert(0,sinx)
        elif SyntaxError or NameError:
            e.delete(0,END)
            e.insert(0,'Invalid Input!')
        else:
             cosx=math.degrees(math.acos(y7))
             e1.delete(0,END)
             e1.insert(0,'Invalid Input!')
    Button(master,text="r_sin",bd=1,width="10",height="1",command=lambda:(sin())).grid(row=5, column=1)
    Button(master,text="r_cos",bd=1,width="7",height="1",command=lambda:cos()).grid(row=5, column=2)
    Button(master,text="r_Tan",bd=1,width="7",height="1",command=lambda:tan()).grid(row=5, column=3)
    Button(master,text="r_asin",bd=1,width="10",height="1",command=lambda:asin()).grid(row=6, column=1)
    Button(master,text="r_acos",bd=1,width="7",height="1",command=lambda:acos()).grid(row=6, column=2)
    Button(master,text="r_atan",bd=1,width="7",height="1",command=lambda:atan()).grid(row=6, column=3)
    
"""-----------------TRIGNOMETRIC FUNCTIONS IN DEGREES---------------"""   
def degrees():
    def dsin():
        try:
            x3=e.get()
            y3=eval(x3)
        except SyntaxError or NameError:
            e.delete(0,END)
            e.insert(0,'Invalid Input!')
        else:
            sin1=math.sin(math.radians(y3))
            e1.delete(0,END)
            e1.insert(0,sin1)

    def dcos():
        try:
            x4=e.get()
            y4=eval(x4)
        except SyntaxError or NameError:
            e.delete(0,END)
            e.insert(0,'Invalid Input!')
        else:
            cos1=math.cos(math.radians(y4))
            e1.delete(0,END)
            e1.insert(0,cos1)

    def dtan():
        try:
            x5=e.get()
            y5=eval(x5)
        except SyntaxError or NameError:
            e.delete(0,END)
            e.insert(0,'Invalid Input!')
        else:
            tan1=math.tan(math.radians(y5))
            e1.delete(0,END)
            e1.insert(0,tan1)

    def d_atan():
        try:
            x6=e.get()
            y6=eval(x6)
         
        except SyntaxError or NameError:
            e.delete(0,END)
            e.insert(0,'Invalid Input!')
        else:
            tan2=math.degrees(math.atan(y6)) 
            e1.delete(0,END)
            e1.insert(0,tan2)

    def d_acos():
        x7=e.get()
        y7=eval(x7)
         
        
        if y7>=-1 and y7<=1:
            cosx=math.degrees(math.acos(y7))
            e1.delete(0,END)
            e1.insert(0,cosx)
        elif SyntaxError or NameError:
            e.delete(0,END)
            e.insert(0,'Invalid Input!')
        else:
             cosx=math.degrees(math.acos(y7))
             e1.delete(0,END)
             e1.insert(0,'Invalid Input!')
        
        

    def d_asin():
        x7=e.get()
        y7=eval(x7)
        
        
        if y7>=-1 and y7<=1:
            sinx=math.degrees(math.asin(y7))
            e1.delete(0,END)
            e1.insert(0,sinx)
        elif SyntaxError or NameError:
            e.delete(0,END)
            e.insert(0,'Invalid Input!')
        else:
             cosx=math.degrees(math.asin(y7))
             e1.delete(0,END)
             e1.insert(0,'Invalid Input!')
 
    Button(master,text="d_sin",bd=1,width="10",height="1",command=lambda:(dsin())).grid(row=5, column=1)
    Button(master,text="d_cos",bd=1,width="7",height="1",command=lambda:dcos()).grid(row=5, column=2)
    Button(master,text="d_Tan",bd=1,width="7",height="1",command=lambda:dtan()).grid(row=5, column=3)
    Button(master,text="d_asin",bd=1,width="10",height="1",command=lambda:d_asin()).grid(row=6, column=1)
    Button(master,text="d_acos",bd=1,width="7",height="1",command=lambda:d_acos()).grid(row=6, column=2)
    Button(master,text="d_atan",bd=1,width="7",height="1",command=lambda:d_atan()).grid(row=6, column=3)



var=IntVar()
Degree=Radiobutton(master,text="Degree",variable=var,value=1,command=lambda:degrees())
Degree.grid(row=3,column=4,columnspan=2)
Radian=Radiobutton(master,text="Radian",variable=var,value=2,command=lambda:radians())
Radian.grid(row=3,column=6,columnspan=2)
Button(master,text="d_sin",bd=1,width="10",height="1").grid(row=5, column=1)
Button(master,text="d_cos",bd=1,width="7",height="1").grid(row=5, column=2)
Button(master,text="d_Tan",bd=1,width="7",height="1").grid(row=5, column=3)
Button(master,text="d_asin",bd=1,width="10",height="1").grid(row=6, column=1)
Button(master,text="d_acos",bd=1,width="7",height="1").grid(row=6, column=2)
Button(master,text="d_atan",bd=1,width="7",height="1").grid(row=6, column=3)
Button(master,text="DEL",bd=1,width="10",height="1",command=lambda:clear1()).grid(row=4, column=1)
Button(master,text="Log10",bd=1,width="7",height="1",command=lambda:(log())).grid(row=4 ,column=2)
Button(master,text="(",bd=1,width="7",height="1",command=lambda:action('(')).grid(row=4, column=3)
Button(master,text=")",bd=1,width="7",height="1",command=lambda:action(')')).grid(row=4, column=4)
Button(master,text="Clear",bd=1,width="15",height="1",command=lambda:clearall()).grid(row=4, column=5,columnspan=2)
Button(master,text="+",bd=1,width="7",height="1",command=lambda:action('+')).grid(row=4, column=7)
Button(master,text="Sqrt",bd=1,width="7",height="1",command=lambda:sqroot()).grid(row=4, column=8) 
Button(master,text="7",bd=1,width="7",height="1",command=lambda:action(7)).grid(row=5, column=4)
Button(master,text="8",bd=1,width="7",height="1",command=lambda:action(8)).grid(row=5, column=5)
Button(master,text="9",bd=1,width="7",height="1",command=lambda:action(9)).grid(row=5, column=6)
Button(master,text="-",bd=1,width="7",height="1",command=lambda:action('-')).grid(row=5, column=7)
Button(master,text="%",bd=1,width="7",height="1",command=lambda:action('%')).grid(row=5, column=8)
Button(master,text="4",bd=1,width="7",height="1",command=lambda:action(4)).grid(row=6, column=4)
Button(master,text="5",bd=1,width="7",height="1",command=lambda:action(5)).grid(row=6, column=5)
Button(master,text="6",bd=1,width="7",height="1",command=lambda:action(6)).grid(row=6, column=6)
Button(master,text="/",bd=1,width="7",height="1",command=lambda:action('/')).grid(row=6, column=7)
Button(master,text="//",bd=1,width="7",height="1",command=lambda:action('//')).grid(row=6, column=8)
Button(master,text="Sqr",bd=1,width="10",height="1",command=lambda:square()).grid(row=7, column=1)
Button(master,text="exp",bd=1,width="7",height="1",command=lambda:expo()).grid(row=7, column=2)
Button(master,text="Abs",bd=1,width="7",height="1",command=lambda:abs1()).grid(row=7, column=3)
Button(master,text="1",bd=1,width="7",height="1",command=lambda:action(1)).grid(row=7, column=4)
Button(master,text="2",bd=1,width="7",height="1",command=lambda:action(2)).grid(row=7, column=5)
Button(master,text="3",bd=1,width="7",height="1",command=lambda:action(3)).grid(row=7, column=6)
Button(master,text="*",bd=1,width="7",height="1",command=lambda:action('*')).grid(row=7, column=7)
Button(master,text="pow",bd=1,width="7",height="1",command=lambda:(action('**'))).grid(row=7, column=8)
Button(master,text="ceil",bd=1,width="10",height="1",command=lambda:ceil1()).grid(row=8, column=1)
Button(master,text="floor",bd=1,width="7",height="1",command=lambda:floor1()).grid(row=8, column=2)
Button(master,text="Cube",bd=1,width="7",height="1",command=lambda:Cube()).grid(row=8, column=3)
Button(master,text="0",bd=1,width="15",height="1",command=lambda:action(0)).grid(row=8, column=4, columnspan=2)
Button(master,text=".",bd=1,width="7",height="1",command=lambda:action('.')).grid(row=8, column=6)
Button(master,text="=",bd=1,width="15",height="1",command=lambda:equals()).grid(row=8, column=7 ,columnspan=2)
Button(master,text="QUIT",bd=2,width="10",height="2",bg="gray",fg="red",command=lambda:quit1()).grid(row=10, column=4 ,columnspan=2,pady=15)

#Main
master.mainloop()



