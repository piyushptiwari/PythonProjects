import Tkinter
from Tkinter import*
def fin2():
    print a.get(),b.get(),c.get(),d.get(),e.get(),f.get(),\
                  g.get(),h.get(),i.get(),j.get(),k.get(),l.get()
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
B1=Tkinter.Button(top2,text='Submit',command=fin2)
B1.pack()
top2.mainloop()
