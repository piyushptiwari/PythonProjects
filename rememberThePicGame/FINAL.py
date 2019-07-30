

"""------------------------------------MODULE 1------------------------------------"""

from Tkinter import*
import Tkinter
top=Tkinter.Tk()
C=Tkinter.Canvas(top,bg='red',height=600,width=600)
filename=PhotoImage(file="imagepyth1.gif")
image=C.create_image(150,50,anchor=N,image=filename)
name=PhotoImage(file="imagespyth2.gif")
image=C.create_image(450,50,anchor=N,image=name)
name1=PhotoImage(file="imagespyth3.gif")
image=C.create_image(150,300,anchor=N,image=name1)
name2=PhotoImage(file="imagespyth4.gif")
image=C.create_image(450,300,anchor=N,image=name2)



def fun():
    def fin():
        top1=Tk()
        filename=PhotoImage(file="imagepyth1.gif")
        image=C.create_image(150,50,anchor=N,image=filename)
        name=PhotoImage(file="imagespyth2.gif")
        image=C.create_image(450,50,anchor=N,image=name)
        name1=PhotoImage(file="imagespyth3.gif")
        image=C.create_image(150,300,anchor=N,image=name1)
        name2=PhotoImage(file="imagespyth4.gif")
        image=C.create_image(450,300,anchor=N,image=name2)
        top1.mainloop()


    """------------------------------------MODULE 2------------------------------------"""


    def fin1():
        def fin2():       
            """print a.get(),b.get(),c.get(),d.get(),e.get(),f.get(),\
                  g.get(),h.get(),i.get(),j.get(),k.get(),l.get()"""
            if(a.get()==0 and b.get()==0 and c.get()==0\
               and d.get()==0 and e.get()==0 and f.get()==0\
               and g.get()==1 and h.get()==1 and i.get()==1\
               and j.get()==0 and k.get()==1 and l.get()==0):
                selection='correct options selected\nYOU WIN!!'
                label.config(text=selection)
            else:
                selection='incorrect options\nYOU LOSE!!'
                label.config(text=selection)
            
        top2=Tk()
        L4=Label(top2,text='Check those which were there in canvas')
        L4.pack(side=TOP)
        a=IntVar()
        b=IntVar()
        c=IntVar()
        d=IntVar()
        e=IntVar()
        f=IntVar()
        g=IntVar()
        h=IntVar()
        i=IntVar()
        j=IntVar()
        k=IntVar()
        l=IntVar()
        C1=Checkbutton(top2,text='Cat',variable=a,\
                   onvalue=1,offvalue=0,height=2,width=30)
        C2=Checkbutton(top2,text='Dog',variable=b,\
                   onvalue=1,offvalue=0,height=2,width=30)
        C3=Checkbutton(top2,text='Earth',variable=c,\
                   onvalue=1,offvalue=0,height=2,width=30)
        C4=Checkbutton(top2,text='Tiger',variable=d,\
                   onvalue=1,offvalue=0,height=2,width=30)
        C5=Checkbutton(top2,text='Ear',variable=e,\
                   onvalue=1,offvalue=0,height=2,width=30)
        C6=Checkbutton(top2,text='Lion',variable=f,\
                   onvalue=1,offvalue=0,height=2,width=30)
        C7=Checkbutton(top2,text='Smiley',variable=g,\
                   onvalue=1,offvalue=0,height=2,width=30)
        C8=Checkbutton(top2,text='Sunset',variable=h,\
                   onvalue=1,offvalue=0,height=2,width=30)
        C9=Checkbutton(top2,text='Rose',variable=i,\
                   onvalue=1,offvalue=0,height=2,width=30)
        C10=Checkbutton(top2,text='Laptop',variable=j,\
                   onvalue=1,offvalue=0,height=2,width=30)
        C11=Checkbutton(top2,text='Teddy',variable=k,\
                   onvalue=1,offvalue=0,height=2,width=30)
        C12=Checkbutton(top2,text='Goat',variable=l,\
                   onvalue=1,offvalue=0,height=2,width=30)
        C1.pack()
        C2.pack()
        C3.pack()
        C4.pack()
        C5.pack()
        C6.pack()
        C7.pack()
        C8.pack()
        C9.pack()
        C10.pack()
        C11.pack()
        C12.pack()
        label=Label(top2)
        label.pack()
        C7=Tkinter.Button(top2,text='Submit',command=fin2)
        C7.pack(side=BOTTOM)
        top2.mainloop()        
    top3=Tk()
    filename=PhotoImage(file="py1.gif")
    image=C.create_image(150,50,anchor=N,image=filename)
    name=PhotoImage(file="py2.gif")
    image=C.create_image(450,50,anchor=N,image=name)
    name1=PhotoImage(file="py3.gif")
    image=C.create_image(150,300,anchor=N,image=name1)
    name2=PhotoImage(file="py4.gif")
    image=C.create_image(450,300,anchor=N,image=name2)
    B1=Tkinter.Button(top3,text='Submit 2nd set',command=fin1)
    B1.pack()  
    B2=Tkinter.Button(top3,text='Refresh',command=fin)
    B2.pack(side=BOTTOM)
    top3.mainloop()
    top.destroy()

"""------------------------------------MODULE 3------------------------------------"""

def fun1():
    def fun2():
        print a.get(),b.get(),c.get(),d.get(),e.get(),f.get(),\
                  g.get(),h.get(),i.get(),j.get(),k.get(),l.get()
        if(a.get()==1 and b.get()==0 and c.get()==1\
           and d.get()==1 and e.get()==1 and f.get()==0\
           and g.get()==0 and h.get()==0 and i.get()==0\
           and j.get()==0 and k.get()==0 and l.get()==0):
            selection='correct options selected\nYOU WIN!!'
            label.config(text=selection)
        else:
            selection='incorrect options\nYOU LOSE!!'
            label.config(text=selection)
    top4=Tk()
    L1=Label(top4,text='Check those which were there in canvas')
    L1.pack(side=TOP)
    a=IntVar()
    b=IntVar()
    c=IntVar()
    d=IntVar()
    e=IntVar()
    f=IntVar()
    g=IntVar()
    h=IntVar()
    i=IntVar()
    j=IntVar()
    k=IntVar()
    l=IntVar()
    C1=Checkbutton(top4,text='Cat',variable=a,\
               onvalue=1,offvalue=0,height=2,width=30)
    C2=Checkbutton(top4,text='Dog',variable=b,\
               onvalue=1,offvalue=0,height=2,width=30)
    C3=Checkbutton(top4,text='Earth',variable=c,\
               onvalue=1,offvalue=0,height=2,width=30)
    C4=Checkbutton(top4,text='Tiger',variable=d,\
               onvalue=1,offvalue=0,height=2,width=30)
    C5=Checkbutton(top4,text='Ear',variable=e,\
               onvalue=1,offvalue=0,height=2,width=30)
    C6=Checkbutton(top4,text='Lion',variable=f,\
               onvalue=1,offvalue=0,height=2,width=30)
    C7=Checkbutton(top4,text='Smiley',variable=g,\
               onvalue=1,offvalue=0,height=2,width=30)
    C8=Checkbutton(top4,text='Sunset',variable=h,\
               onvalue=1,offvalue=0,height=2,width=30)
    C9=Checkbutton(top4,text='Rose',variable=i,\
               onvalue=1,offvalue=0,height=2,width=30)
    C10=Checkbutton(top4,text='Laptop',variable=j,\
               onvalue=1,offvalue=0,height=2,width=30)
    C11=Checkbutton(top4,text='Teddy',variable=k,\
               onvalue=1,offvalue=0,height=2,width=30)
    C12=Checkbutton(top4,text='Goat',variable=l,\
               onvalue=1,offvalue=0,height=2,width=30)
    C1.pack()
    C2.pack()
    C3.pack()
    C4.pack()
    C5.pack()
    C6.pack()
    C7.pack()
    C8.pack()
    C9.pack()
    C10.pack()
    C11.pack()
    C12.pack()
    label=Label(top4)
    label.pack()
    C7=Tkinter.Button(top4,text='Submit',command=fun2)
    C7.pack(side=BOTTOM)
    top4.mainloop()
B=Tkinter.Button(top,text='Refresh',command=fun)
B.pack(side=BOTTOM)
D=Tkinter.Button(top,text='Submit 1st set',command=fun1)
D.pack(side=BOTTOM)
C.pack()
top.mainloop()
