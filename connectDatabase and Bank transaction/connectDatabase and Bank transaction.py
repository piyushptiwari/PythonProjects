import Tkinter as tk
LARGE_FONT=("manoj",14)
LARGE_FONT1=("manoj",12)
class main(tk.Tk):
    def __init__(self,*a,**b):
        tk.Tk.__init__(self,*a,**b)
        container=tk.Frame(self,)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames={}
        for F in (startpage,sub,bal,deposit,withdraw,pinchange,pinchange1,check7,check5,c1,c2,c3,c4,c5,c6,c7):
            frame=F(container,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(startpage)
    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()
class startpage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller
        #canvas=tk.Canvas()
        #gif1 = tk.PhotoImage(file = "C:\Users\DELL\Desktop\python project\manoj.gif")
        #canvas.create_image(50, 50, anchor=NE, image=gif1)
        #canvas.pack()
        f4=tk.Frame(self)
        f4.pack()
        f3=tk.Frame(self)
        f3.pack()
        f5=tk.Frame(self)
        f5.pack()
        f=tk.Frame(self)
        f.pack()
        f1=tk.Frame(self)
        f1.pack()
        f2=tk.Frame(self)
        f2.pack()
        label=tk.Label(f4,text="WELCOME TO STATE BANK OF INDIA\nATM",font=LARGE_FONT)
        label.pack(side="top",expand="yes")
        Label = tk.Label(f3, text = "Login With Your Account And Pin Numbers", font = LARGE_FONT)
        Label.pack(side ="top", expand = "yes")
        global acc
        acc=tk.StringVar()
        l1=tk.Label(f5,text="Enter Account Number",font=LARGE_FONT1)
        l1.pack(pady=10,padx=10,side="left",expand="yes")
        global e1
        global e
        e=tk.Entry(f5,bd=5,text=acc,font=LARGE_FONT1)
        e.pack(pady=10,padx=10,side="right",expand="yes")
        global a
        a=tk.StringVar()
        l2=tk.Label(f,text="  Enter 4 Digit Pin        ",font=LARGE_FONT1)
        l2.pack(pady=10,padx=10,side="left",expand="yes")
        e1=tk.Entry(f,bd=5,text=a,show="*",font=LARGE_FONT1)
        e1.pack(pady=10,padx=10,side="right",expand="yes")
        b=tk.Button(f1,text="submit",font=LARGE_FONT1,command=self.check)
        b.pack(pady=10,padx=10,side="bottom",expand="yes")
        b=tk.Button(f2,text="exit",font=LARGE_FONT1,command=exit)
        b.pack(pady=10,padx=10,side="bottom",expand="yes")
    def check(self):
        #e1.delete(0,tk.END)
        b=str(a.get())
        print b
        k=str(acc.get())
        #print k
        #print str(a.get())
        import sqlite3
        conn=sqlite3.connect('example.db')
        c=conn.cursor()
        c.execute("UPDATE bank1 set accno='%s'"%k)
        conn.commit()
        conn.close()
        import sqlite3
        conn=sqlite3.connect('example.db')
        c=conn.cursor()
        c.execute("SELECT pin FROM bank where accno='%s'"%k)
        d=c.fetchone()
        #print d
        conn.commit()
        conn.close()
            
        if d==None or d[0]!=b:
            e.delete(0,tk.END)
            e1.delete(0,tk.END)
            self.controller.show_frame(c1)
        else:
            e.delete(0,tk.END)
            e1.delete(0,tk.END)            
            self.controller.show_frame(sub)
class c1(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller
        l3=tk.Label(self,text="pin number is incorrect",font=LARGE_FONT1)
        l3.pack(pady=10,padx=10,expand="yes")
        b=tk.Button(self,bd=5,text="  EXIT  ",font=LARGE_FONT1,relief=tk.RAISED,command=lambda:controller.show_frame(startpage))
        b.pack(pady=10,padx=10)
        
            
            
class sub(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller
        #print "2",a.get()
        self.parent=parent
        l=tk.Label(self,text="HOME PAGE",font=LARGE_FONT)
        l.pack(pady=10,padx=10)
        f1=tk.Frame(self)
        f1.pack()
        f2=tk.Frame(self)
        f2.pack()
        f3=tk.Frame(self)
        f3.pack()
        b=tk.Button(f1,bd=5,text="BALANCE INQUIRY",font=LARGE_FONT1,relief=tk.RAISED ,command=lambda:controller.show_frame(bal))
        b.pack(pady=10,padx=10,side="left",expand="yes")
        b=tk.Label(f1,text="          ")
        b.pack(pady=10,padx=10,side="left")
        b=tk.Button(f1,bd=5,text="DEPOSITE        ",font=LARGE_FONT1,relief=tk.RAISED,command=lambda:controller.show_frame(deposit))
        b.pack(pady=10,padx=10,side="right",expand="yes")
       
        b=tk.Label(f2,text="")
        b.pack(pady=10,padx=10)
        
        b=tk.Button(f3,bd=5,text="WITHDRAW          ",font=LARGE_FONT1,relief=tk.RAISED,command=lambda:controller.show_frame(withdraw))      
        b.pack(pady=10,padx=10,side="left",expand="yes")
        b=tk.Label(f3,text="          ")
        b.pack(pady=10,padx=10,side="left")
        b=tk.Button(f3,bd=5,text="PINCHANGE    ",font=LARGE_FONT1,relief=tk.RAISED,command=lambda:controller.show_frame(pinchange))
        b.pack(pady=10,padx=10,side="right",expand="yes")
        b=tk.Button(self,bd=5,text="  EXIT  ",font=LARGE_FONT1,relief=tk.RAISED,command=lambda:controller.show_frame(startpage))
        b.pack(pady=10,padx=10,expand="yes")
       
class bal(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller
        b=tk.Button(self,bd=5,text="PLEASE CLICK HERE",font=LARGE_FONT1,relief=tk.RAISED,command=self.bal1)
        b.pack(pady=10,padx=10,side="top",expand="yes")
        
    def bal1(self):
        import sqlite3
        conn=sqlite3.connect('example.db')
        c=conn.cursor()
        c.execute("SELECT * FROM bank1")
        a=c.fetchone()
        print a
        conn.commit()
        conn.close()
        import sqlite3
        conn=sqlite3.connect('example.db')
        c=conn.cursor()
        c.execute("SELECT amount FROM bank where accno='%s'"%str(a[0]))
        global d
        d=c.fetchone()
        #print d
        c.execute("SELECT name FROM bank where accno='%s'"%str(a[0]))
        global n
        n=c.fetchone()
        #print n
        conn.commit()
        conn.close()
        f1=tk.Frame(self)
        f1.pack()
        f2=tk.Frame(self)
        f2.pack()
        global b
        global b1 
        global button1
        b=tk.Label(f1,text="HELLO       "+str(n[0]),font=LARGE_FONT1)
        b.pack(pady=10,padx=10,expand="yes")
        b1=tk.Label(f2,text="YOUR ACCOUNT BALANCE IS    "+str(d[0])+"  RS/-",font=LARGE_FONT1)
        b1.pack(pady=10,padx=10,expand="yes")    
        button1=tk.Button(self,bd=5,text="BACK TO HOME",font=LARGE_FONT1,command=self.bal2)
        button1.pack(pady=5,padx=5,expand="yes")
    def bal2(self):
        b.pack_forget()
        b1.pack_forget()
        button1.destroy()
        self.controller.show_frame(sub)
    def bal3(self):
        b.pack_forget()
        b1.pack_forget()
        button1.destroy()
        self.controller.show_frame(startpage)
class deposit(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller
        l=tk.Label(self,text="DEPOSIT PAGE",font=LARGE_FONT)
        l.pack(pady=10,padx=10)
        f1=tk.Frame(self)
        f1.pack(pady=10,padx=10,expand="yes")
        f3=tk.Frame(self)
        f3.pack(pady=10,padx=10)
        f2=tk.Frame(self)
        f2.pack(pady=10,padx=10)
        b=tk.Label(f1,text="Please Enter Amount   ",font=LARGE_FONT1)
        b.pack(side="left",pady=10,padx=10)
        global y
        y=tk.IntVar()
        global entry5
        entry5=tk.Entry(f1,bd=5,text=y,font=LARGE_FONT1)
        entry5.pack(pady=10,padx=10,side="right")
        button1=tk.Button(self,text="BACK TO HOME",font=LARGE_FONT1,command=lambda:controller.show_frame(sub))
        button1.pack(pady=5,padx=5)
        button1=tk.Button(self,text="SUBMIT",font=LARGE_FONT1,command=self.check4)
        button1.pack()
    def check4(self):
        print y.get()
        import sqlite3
        conn=sqlite3.connect('example.db')
        c=conn.cursor()
        c.execute("SELECT * FROM bank1")
        global f
        f=c.fetchone()
        conn.commit()
        #print f[0]
        import sqlite3
        conn=sqlite3.connect('example.db')
        c=conn.cursor()
        c.execute("select amount from bank where accno='%s'"%str(f[0]))
        global preamount
        preamount=c.fetchone()
        conn.commit()
        conn.close()
        if y.get()>40000:
            entry5.delete(0,tk.END)
            self.controller.show_frame(c2)
        elif y.get()<0:
            entry5.delete(0,tk.END)
            self.controller.show_frame(c3)
        else:
            import sqlite3
            conn=sqlite3.connect('example.db')
            c=conn.cursor()
            c.execute("UPDATE bank set amount=amount+'%d' where accno='%s'"%(y.get(),str(f[0])))
            conn.commit()
            conn.close()
            entry5.delete(0,tk.END)
            self.controller.show_frame(check5)
class c2(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller
        l=tk.Label(self,text="You cannot deposit more than 40000 RS/- at once ",font=LARGE_FONT1)
        l.pack(pady=10,padx=10,expand="yes")
        button1=tk.Button(self,text="BACK TO DEPOSIT PAGE",font=LARGE_FONT1,command=lambda:controller.show_frame(deposit))
        button1.pack(pady=10,padx=10)
class c3(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller
        l=tk.Label(self,text="INVALID ENTERED AMOUNT",font=LARGE_FONT1)
        l.pack(pady=10,padx=10,expand="yes")
        button1=tk.Button(self,text="BACK TO DEPOSIT PAGE",font=LARGE_FONT1,command=lambda:controller.show_frame(deposit))
        button1.pack(pady=10,padx=10)
class check5(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        l=tk.Label(self,text="YOUR AMOUNT IS SUCCESSFULLY DEPOSITED",font=LARGE_FONT1)
        l.pack(pady=10,padx=10,expand="yes")
        button1=tk.Button(self,text="BACK TO HOME",font=LARGE_FONT1,command=lambda:controller.show_frame(sub))
        button1.pack(pady=10,padx=10)                
        button1=tk.Button(self,text="  EXIT  ",font=LARGE_FONT1,command=lambda:controller.show_frame(startpage))
        button1.pack(pady=10,padx=10)
class withdraw(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller
        l=tk.Label(self,text="WITHDRAW PAGE",font=LARGE_FONT)
        l.pack(pady=10,padx=10)
        f1=tk.Frame(self)
        f1.pack(pady=10,padx=10,expand="yes")
        f3=tk.Frame(self)
        f3.pack(pady=10,padx=10)
        f2=tk.Frame(self)
        f2.pack(pady=10,padx=10)
        b=tk.Label(f1,text="Please Enter Amount   ",font=LARGE_FONT1)
        b.pack(side="left",pady=10,padx=10,)
        global p
        p=tk.IntVar()
        global entry6
        entry6=tk.Entry(f1,bd=5,text=p,font=LARGE_FONT1)
        entry6.pack(pady=10,padx=10,side="right",)
        button1=tk.Button(self,text="BACK TO HOME",font=LARGE_FONT1,command=lambda:controller.show_frame(sub))
        button1.pack(pady=5,padx=5)
        button1=tk.Button(self,text="SUBMIT",font=LARGE_FONT1,command=self.check6)
        button1.pack(pady=10,padx=10)
    def check6(self):
        #print y.get()
        #print h[0]
        import sqlite3
        conn=sqlite3.connect('example.db')
        c=conn.cursor()
        c.execute("SELECT * FROM bank1")
        global h
        h=c.fetchone()
        conn.commit()
        conn.close()
        import sqlite3
        conn=sqlite3.connect('example.db')
        c=conn.cursor()
        c.execute("select amount from bank where accno='%s'"%str(h[0]))
        global preamount1
        preamount1=c.fetchone()
        conn.commit()
        conn.close()
        #print p.get()
        #print preamount1       
        if p.get()<preamount1[0]:
            import sqlite3
            conn=sqlite3.connect('example.db')
            c=conn.cursor()
            c.execute("UPDATE bank set amount=amount-'%d' where accno='%s'"%(p.get(),str(h[0])))
            conn.commit()
            conn.close()
            entry6.delete(0,tk.END)
            self.controller.show_frame(check7)
        else:
            entry6.delete(0,tk.END)
            self.controller.show_frame(c4)
class c4(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)            
        l=tk.Label(self,text="YOUR ACCOUNT HAVE NOT SUFFICIENT BALANCE",font=LARGE_FONT1)
        l.pack(pady=10,padx=10,expand="yes")
        button1=tk.Button(self,text="BACK TO WITHDRAW PAGE",font=LARGE_FONT1,command=lambda:controller.show_frame(withdraw))
        button1.pack(pady=10,padx=10)
class check7(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)
        b=tk.Label(self,text=" PLEASE COLLECT YOUR AMOUNT ",font=LARGE_FONT1)
        b.pack(pady=10,padx=10,expand="yes")
        button1=tk.Button(self,text="BACK TO HOME",font=LARGE_FONT1,command=lambda:controller.show_frame(sub))
        button1.pack(pady=10,padx=10)
        button1=tk.Button(self,text="  EXIT  ",font=LARGE_FONT1,command=lambda:controller.show_frame(startpage))
        button1.pack(pady=10,padx=10)
       # self.controller.show_frame(startpage)
class pinchange(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)
        l=tk.Label(self,text="PIN CHANGE PAGE",font=LARGE_FONT)
        l.pack(pady=10,padx=10)
        f=tk.Frame(self)
        f.pack()
        f1=tk.Frame(self)
        f1.pack()
        f2=tk.Frame(self)
        f2.pack()
        l=tk.Label(f,text="Enter Old Pin Number",font=LARGE_FONT1)
        l.pack(pady=10,padx=10,side="left")
        global old
        global entry7
        global entry8
        global entry9
        old=tk.StringVar()
        entry7=tk.Entry(f,bd=5,text=old,show="*",font=LARGE_FONT1)
        entry7.pack(pady=10,padx=10,side="right")
        l1=tk.Label(f1,text="Enter New Pin Number",font=LARGE_FONT1)
        l1.pack(pady=10,padx=10,side="left")
        global new
        new=tk.StringVar()
        entry8=tk.Entry(f1,bd=5,text=new,show="*",font=LARGE_FONT1)
        entry8.pack(pady=10,padx=10,side="right")
        l2=tk.Label(f2,text="Re-Enter Pin Number",font=LARGE_FONT1)
        l2.pack(pady=10,padx=10,side="left")
        global re
        re=tk.StringVar()
        entry9=tk.Entry(f2,bd=5,text=re,show="*",font=LARGE_FONT1)
        entry9.pack(pady=10,padx=10,side="right")
        button1=tk.Button(self,text="BACK TO HOME",font=LARGE_FONT1,command=lambda:controller.show_frame(sub))
        button1.pack(pady=5,padx=5)
        button1=tk.Button(self,text="SUBMIT",font=LARGE_FONT1,command=self.check1)
        button1.pack(pady=10,padx=10)
    def check1(self):
        import sqlite3
        conn=sqlite3.connect('example.db')
        c=conn.cursor()
        c.execute("SELECT * FROM bank1")
        global r
        r=c.fetchone()
        #print r[0]
        conn.commit()
        conn.close()
        x=old.get()
        #print x
        z=new.get()
        #print z 
        import sqlite3
        conn=sqlite3.connect('example.db')
        c=conn.cursor()
        c.execute("select pin from bank where accno='%s'"%str(r[0]))
        global old1
        old1=c.fetchone()
        print old1
        conn.commit()
        conn.close()
        if str(old.get())!=str(old1[0]):
            entry7.delete(0,tk.END)
            entry8.delete(0,tk.END)
            entry9.delete(0,tk.END)
            self.controller.show_frame(c5)
        elif len(new.get())>4:
            entry7.delete(0,tk.END)
            entry8.delete(0,tk.END)
            entry9.delete(0,tk.END)
            self.controller.show_frame(c6)
        elif new.get()!=re.get():
            entry7.delete(0,tk.END)
            entry8.delete(0,tk.END)
            entry9.delete(0,tk.END)
            self.controller.show_frame(c7)
        
        else:
            import sqlite3
            conn=sqlite3.connect('example.db')
            c=conn.cursor()                   
            c.execute("UPDATE bank SET pin='%s' where accno='%s'"%(str(z),str(r[0])))
            conn.commit()
            conn.close()
            entry7.delete(0,tk.END)
            entry8.delete(0,tk.END)
            entry9.delete(0,tk.END)
            self.controller.show_frame(pinchange1)
class c5(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)
        l=tk.Label(self,text="OLD PIN NUMBER IS WRONG",font=LARGE_FONT1)
        l.pack(pady=10,padx=10,expand="yes")
        button1=tk.Button(self,text="BACK TO PIN CHANGE PAGE",font=LARGE_FONT1,command=lambda:controller.show_frame(pinchange))
        button1.pack(pady=10,padx=10)
class c6(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)
        l=tk.Label(self,text="NEW PIN NUMBER NOT EXCIDES 4 DIGITS",font=LARGE_FONT1)
        l.pack(pady=10,padx=10,expand="yes")
        button1=tk.Button(self,text="BACK TO PIN CHANGE PAGE",font=LARGE_FONT1,command=lambda:controller.show_frame(pinchange))
        button1.pack(pady=10,padx=10)
class c7(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)
        l=tk.Label(self,text="NEW PIN AND RE-ENTER PIN NUMBET ARE NOT MATCHING",font=LARGE_FONT1)
        l.pack(pady=10,padx=10,expand="yes")
        button1=tk.Button(self,text="BACK TO PIN CHANGE PAGE",font=LARGE_FONT1,command=lambda:controller.show_frame(pinchange))
        button1.pack(pady=10,padx=10)
class pinchange1(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)
        l=tk.Label(self,text="YOUR PIN NUMBER IS SUCCESSFULLY CHANGED",font=LARGE_FONT1)
        l.pack(pady=10,padx=10,expand="yes")
        button1=tk.Button(self,text="  EXIT  ",font=LARGE_FONT1,command=lambda:controller.show_frame(startpage))
        button1.pack(pady=10,padx=10)
    
app=main()
app.mainloop()
