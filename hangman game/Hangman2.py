from Tkinter import *
import Tkinter
import tkMessageBox
import sqlite3

n=1
counter=3
score=0
def play(root,f):
        #Function to Enter value in text box
        def select(value,entry):
            if value==" SPACE ":
                entry.insert(Tkinter.END,' ')
            else:
                entry.insert(Tkinter.END,value)

        def new(entry,label,label_1,label_2):
            global n
            global counter
            global score
            counter=3
            n+=1
            entry.delete(0,END)
            label_1.config(text='Attempts left : '+str(counter))
            pic=PhotoImage(master=root,file=str(n)+".gif")
            label.configure(image = pic)
            label.image=pic
            if(n>=12):
                tkMessageBox.showwarning("Game Over!!"," Your Score is : "+str(score))
                n=0
                score=0
                label_2.config(text='Your score is : '+str(score))
                new(entry,label,label_1,label_2)
                

        def check(entry,label,label_1,label_2):
            global counter
            global score
            counter-=1
            label_1.config(text='Attempts left : '+str(counter))
            if(counter==0):
                tkMessageBox.showwarning("No attemps left","No attemps left!! Sorry try again")
                counter=3
                label_1.config(text='Attempts left : '+str(counter))
                new(entry,label,label_1,label_2)

            #Database work
            conn= sqlite3.connect('Hangman.db')
            c=conn.cursor()
            c.execute('CREATE TABLE IF NOT  EXISTS HANGMAN (ID INT(2),N VARCHAR(20))')
            c.execute('INSERT INTO HANGMAN VALUES(1,"EAGLE")')
            c.execute('INSERT INTO HANGMAN VALUES(2,"CAR")')
            c.execute('INSERT INTO HANGMAN VALUES(3,"CAT")')
            c.execute('INSERT INTO HANGMAN VALUES(4,"DEER")')
            c.execute('INSERT INTO HANGMAN VALUES(5,"OWL")')
            c.execute('INSERT INTO HANGMAN VALUES(6,"SKULL")')
            c.execute('INSERT INTO HANGMAN VALUES(7,"JOKER")')
            c.execute('INSERT INTO HANGMAN VALUES(8,"PEAR")')
            c.execute('INSERT INTO HANGMAN VALUES(9,"PIKACHU")')
            c.execute('INSERT INTO HANGMAN VALUES(10,"RABBIT")')
            c.execute('INSERT INTO HANGMAN VALUES(11,"DONKEY")')
            c.execute('INSERT INTO HANGMAN VALUES(12,"TREE")')
            ln=[n]
            for row in c.execute('SELECT N FROM HANGMAN WHERE ID=(?)',ln):
                lname=row
            
            
            if(entry.get()==lname[0]):
                score+=1
                label_2.config(text='Your score is : '+str(score))
                new(entry,label,label_1,label_2)
            

        f.pack_forget()
        root.title("Hangman")
        root.resizable(0,0)

        photo=PhotoImage(master=root,file="1.gif")
        label=Label(root,image=photo,width=150,height=140)
        label.grid(row=0,column=0,padx=50,pady=50,rowspan=2)

        label_1=Label(root,text="Attempts left : "+str(counter))
        label_1.grid(row=2,column=0,padx=10,pady=10)

        label_2=Label(root,text="Your score is : "+str(score))
        label_2.grid(row=3,column=0,padx=10,pady=10)

        command=lambda :new(entry,label,label_1,label_2)
        B1=Tkinter.Button(root,text="Next Image",width=40,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        B1.grid(row=0,column=1,padx=50,pady=50,columnspan=5)

        entry=Entry(root,width=100)
        entry.grid(row=1,column=1,columnspan=5,padx=50,pady=50)

        command=lambda x='A': select(x,entry)
        Button_A=Tkinter.Button(root,text="A",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_A.grid(row=2,column=1,padx=10,pady=10)

        command=lambda x='B': select(x,entry)
        Button_B=Tkinter.Button(root,text="B",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_B.grid(row=2,column=2,padx=10,pady=10)

        command=lambda x='C': select(x,entry)
        Button_C=Tkinter.Button(root,text="C",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_C.grid(row=2,column=3,padx=10,pady=10)

        command=lambda x='D': select(x,entry)
        Button_D=Tkinter.Button(root,text="D",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_D.grid(row=2,column=4,padx=10,pady=10)

        command=lambda x='E': select(x,entry)
        Button_E=Tkinter.Button(root,text="E",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_E.grid(row=2,column=5,padx=10,pady=10)

        command=lambda x='F': select(x,entry)
        Button_F=Tkinter.Button(root,text="F",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_F.grid(row=3,column=1,padx=10,pady=10)

        command=lambda x='G': select(x,entry)
        Button_G=Tkinter.Button(root,text="G",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_G.grid(row=3,column=2,padx=10,pady=10)

        command=lambda x='H': select(x,entry)
        Button_H=Tkinter.Button(root,text="H",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_H.grid(row=3,column=3,padx=10,pady=10)

        command=lambda x='I': select(x,entry)
        Button_I=Tkinter.Button(root,text="I",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_I.grid(row=3,column=4,padx=10,pady=10)

        command=lambda x='J': select(x,entry)
        Button_J=Tkinter.Button(root,text="J",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_J.grid(row=3,column=5,padx=10,pady=10)

        command=lambda x='K': select(x,entry)
        Button_K=Tkinter.Button(root,text="K",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_K.grid(row=4,column=1,padx=10,pady=10)

        command=lambda x='L': select(x,entry)
        Button_L=Tkinter.Button(root,text="L",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_L.grid(row=4,column=2,padx=10,pady=10)

        command=lambda x='M': select(x,entry)
        Button_M=Tkinter.Button(root,text="M",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_M.grid(row=4,column=3,padx=10,pady=10)

        command=lambda x='N': select(x,entry)
        Button_N=Tkinter.Button(root,text="N",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_N.grid(row=4,column=4,padx=10,pady=10)

        command=lambda x='O': select(x,entry)
        Button_O=Tkinter.Button(root,text="O",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_O.grid(row=4,column=5,padx=10,pady=10)

        command=lambda x='P': select(x,entry)
        Button_P=Tkinter.Button(root,text="P",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_P.grid(row=5,column=1,padx=10,pady=10)

        command=lambda x='Q': select(x,entry)
        Button_Q=Tkinter.Button(root,text="Q",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_Q.grid(row=5,column=2,padx=10,pady=10)

        command=lambda x='R': select(x,entry)
        Button_R=Tkinter.Button(root,text="R",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_R.grid(row=5,column=3,padx=10,pady=10)

        command=lambda x='S': select(x,entry)
        Button_S=Tkinter.Button(root,text="S",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_S.grid(row=5,column=4,padx=10,pady=10)

        command=lambda x='T': select(x,entry)
        Button_T=Tkinter.Button(root,text="T",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_T.grid(row=5,column=5,padx=10,pady=10)

        command=lambda x='U': select(x,entry)
        Button_U=Tkinter.Button(root,text="U",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_U.grid(row=6,column=1,padx=10,pady=10)

        command=lambda x='V': select(x,entry)
        Button_V=Tkinter.Button(root,text="V",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_V.grid(row=6,column=2,padx=10,pady=10)

        command=lambda x='W': select(x,entry)
        Button_W=Tkinter.Button(root,text="W",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_W.grid(row=6,column=3,padx=10,pady=10)

        command=lambda x='X': select(x,entry)
        Button_X=Tkinter.Button(root,text="X",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_X.grid(row=6,column=4,padx=10,pady=10)

        command=lambda x='Y': select(x,entry)
        Button_Y=Tkinter.Button(root,text="Y",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_Y.grid(row=6,column=5,padx=10,pady=10)

        command=lambda x='Z': select(x,entry)
        Button_Z=Tkinter.Button(root,text="Z",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_Z.grid(row=7,column=3,padx=10,pady=10)

        command=lambda x=' SPACE ': select(x,entry)
        Button_SPACE=Tkinter.Button(root,text="SPACE",command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000",width=50)
        Button_SPACE.grid(row=8,column=2,padx=10,pady=10,columnspan=3)

        command=lambda : check(entry,label,label_1,label_2)
        Button_Z=Tkinter.Button(root,text="Check",width=10,command=command,bg="#000000",fg="#ffffff"
      ,activebackground="#ffffff",activeforeground="#000000")
        Button_Z.grid(row=8,column=5,padx=10,pady=10)
        
        root.mainloop()

def main():
    root=Tkinter.Tk()
    root.title("Hangman")
    root.resizable(0,0)

    frame=Frame(root,width=900,height=500)
    frame.pack()
    frame.pack_propagate(False)
    
    command=lambda : play(root,frame)
    Button_1=Tkinter.Button(frame,text="PLAY",width=40,height=10,command=command,bg="#000000",fg="#ffffff"
    ,activebackground="#ffffff",activeforeground="#000000")
    Button_1.pack()

    command=lambda : root.destroy()
    Button_2=Tkinter.Button(frame,text="QUIT",width=40,height=10,command=command,bg="#000000",fg="#ffffff"
    ,activebackground="#ffffff",activeforeground="#000000")
    Button_2.pack()
    root.mainloop()
main()
