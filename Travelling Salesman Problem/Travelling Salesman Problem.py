from Tkinter import *
root = Tk()

z1 = Label(root,text="CITY",fg="Red", font=("bold",12))
z2 = Label(root,text="LUDHIANA",fg="blue", font=("bold",12))
z3 = Label(root,text="JALLANDHAR",fg="brown", font=("bold",12))
z4 = Label(root,text="AMRITSAR",fg="green", font=("bold",12))
z5 = Label(root,text="CHANDIGARH",fg="violet", font=("bold",12))
z6 = Label(root,text="PATIALA", font=("bold",12))
z1.grid(row=1,column=0)
z2.grid(row=1,column=1)
z3.grid(row=1,column=2)
z4.grid(row=1,column=3)
z5.grid(row=1,column=4)
z6.grid(row=1,column=5)

t1 = Label(root,text="LUDHIANA",fg="blue", font=("bold",12))
t1.grid(row=2,column=0)
a1 = Entry(root)
a1.grid(row=2,column=1)
a2 = Entry(root)
a2.grid(row=2,column=2)
a3 = Entry(root)
a3.grid(row=2,column=3)
a4 = Entry(root)
a4.grid(row=2,column=4)
a5 = Entry(root)
a5.grid(row=2,column=5)
l1 = Label(root)
l1.grid(row=2,column=7)


def callback():
    total1 = sum(int(a.get()) for a in (a1, a2, a3, a4, a5))
    l1.config(text="answer = %s" % (total1*2))
a = Button(root, text="See Distance", command=callback)
a.grid(row=2,column=6)

t2 = Label(root,text="JALLANDHAR",fg="brown", font=("bold",12))
t2.grid(row=3,column=0)
b1 = Entry(root)
b1.grid(row=3,column=1)
b2 = Entry(root)
b2.grid(row=3,column=2)
b3 = Entry(root)
b3.grid(row=3,column=3)
b4 = Entry(root)
b4.grid(row=3,column=4)
b5 = Entry(root)
b5.grid(row=3,column=5)
l2 = Label(root)
l2.grid(row=3,column=7)

def callback():
    total2 = sum(int(b.get()) for b in (b1, b2, b3, b4, b5))
    l2.config(text="answer = %s" % (total2*2))
b = Button(root, text="See Distance", command=callback)
b.grid(row=3,column=6)

t3 = Label(root,text="AMRITSAR",fg="green", font=("bold",12))
t3.grid(row=4,column=0)
c1 = Entry(root)
c1.grid(row=4,column=1)
c2 = Entry(root)
c2.grid(row=4,column=2)
c3 = Entry(root)
c3.grid(row=4,column=3)
c4 = Entry(root)
c4.grid(row=4,column=4)
c5 = Entry(root)
c5.grid(row=4,column=5)
l3 = Label(root)
l3.grid(row=4,column=7)

def callback():
    total3 = sum(int(c.get()) for c in (c1, c2, c3, c4, c5))
    l3.config(text="answer = %s" % (total3*2))
c = Button(root, text="See Distance", command=callback)
c.grid(row=4,column=6)

t4 = Label(root,text="CHANDIGARH",fg="violet", font=("bold",12))
t4.grid(row=5,column=0)
d1 = Entry(root)
d1.grid(row=5,column=1)
d2 = Entry(root)
d2.grid(row=5,column=2)
d3 = Entry(root)
d3.grid(row=5,column=3)
d4 = Entry(root)
d4.grid(row=5,column=4)
d5 = Entry(root)
d5.grid(row=5,column=5)
l4 = Label(root)
l4.grid(row=5,column=7)

def callback():
    total4 = sum(int(d.get()) for d in (d1, d2, d3, d4, d5))
    l4.config(text="answer = %s" % (total4*2))
d = Button(root, text="See Distance", command=callback)
d.grid(row=5,column=6)

t5 = Label(root,text="PATIALA", font=("bold",12))
t5.grid(row=6,column=0)
e1 = Entry(root)
e1.grid(row=6,column=1)
e2 = Entry(root)
e2.grid(row=6,column=2)
e3 = Entry(root)
e3.grid(row=6,column=3)
e4 = Entry(root)
e4.grid(row=6,column=4)
e5 = Entry(root)
e5.grid(row=6,column=5)
l5 = Label(root)
l5.grid(row=6,column=7)

def callback():
    total5 = sum(int(e.get()) for e in (e1, e2, e3, e4, e5))
    l5.config(text="answer = %s" % (total5*2))
e = Button(root, text="See Distance", command=callback)
e.grid(row=6,column=6)

def clear_textbox():
    a1.delete(0, END)
    a2.delete(0, END)
    a3.delete(0, END)
    a4.delete(0, END)
    a5.delete(0, END)
    b1.delete(0, END)
    b2.delete(0, END)
    b3.delete(0, END)
    b4.delete(0, END)
    b5.delete(0, END)
    c1.delete(0, END)
    c2.delete(0, END)
    c3.delete(0, END)
    c4.delete(0, END)
    c5.delete(0, END)
    d1.delete(0, END)
    d2.delete(0, END)
    d3.delete(0, END)
    d4.delete(0, END)
    d5.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    l["text"]=""
    l1["text"]=""
    l2["text"]=""
    l3["text"]=""
    l4["text"]=""
    l5["text"]=""

bu = Button(root,text="CLEAR",command=clear_textbox,width=16)
bu.grid(row=7,column=3)
l = Label(root)
l.grid(row=7,column=1)
def least():
    T1 = sum(int(a.get()) for a in (a1, a2, a3, a4, a5))
    T2 = sum(int(b.get()) for b in (b1, b2, b3, b4, b5))
    T3 = sum(int(c.get()) for c in (c1, c2, c3, c4, c5))
    T4 = sum(int(d.get()) for d in (d1, d2, d3, d4, d5))
    T5 = sum(int(e.get()) for e in (e1, e2, e3, e4, e5))
    if(T1<T2 and T1<T3 and T1<T4 and T1<T5):
        l.config(text="From Ludhiana :%s"% (T1*2))
    elif(T2<T1 and T2<T3 and T2<T4 and T2<T5):
        l.config(text="From Jallandhar :%s"% (T2*2))
    elif(T3<T1 and T3<T2 and T3<T4 and T3<T5):
        l.config(text="From Amritsar :%s"% (T3*2))
    elif(T4<T1 and T4<T2 and T4<T3 and T4<T5):
        l.config(text="From Chandigarh :%s"% (T4*2))
    elif(T1==T2 or T1==T3 or T1==T4 or T1==T5 or T2==T1 or T2==T3 or T2==T4 or T2==T5 or T3==T1 or T3==T2 or T3==T4 or T3==T5 or T4==T1 or T4==T2 or T4==T3 or T4==T5 or T5==T1 or T5==T2 or T5==T3 or T5==T4):
        l.config(text="From Ludhiana :%s"% (T1*2))
    else:
        l.config(text="Least distance is from Patiala :%s"% (T5*2))
T = Button(root,text="Least distance",command=least,width=16)
T.grid(row=7,column=0)
def exit():
    root.destroy()
    new=Tk()
    L1=Label(new,text="Thanks for using our interface",bg="black",fg="yellow",height=3,width=40,font=("bold",20))
    L1.grid(row=0)
    def quit():
        new.destroy()
    b=Button(new,text="QUIT",command=quit,width=20)
    b.grid(row=1)
    new.mainloop()
ex=Button(root,text="EXIT",command=exit,width=16)
ex.grid(row=7,column=4,sticky=W)
root.mainloop()
