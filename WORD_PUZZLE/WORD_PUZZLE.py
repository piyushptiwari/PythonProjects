from Tkinter import *
from string import *
import tkMessageBox
import string
import Tkinter as tk


def close_win(root):
    root.destroy()

def start(root,frame):
    frame.pack_forget()

    def inst1(root,frame):
        frame.pack_forget()
        frame1=Frame(root)
        photo1=PhotoImage(file="bgi.gif")
        frame1.config(background="yellow")
        #frame2=Frame(root)
        command=lambda:Easy(root,frame1)
        #l1=Label(frame2,text="instruction",fg="red",font=("Helvetica", 16))
        #l1.pack()
        button1=Button(frame1,text="  BACK  ",bg="green",command=command)
        button1.grid(row=9,column=5,padx=85,pady=20)
        ba=Button(frame1,text="ANIMAL NAME WORD PUZZLE",width=100,height=2,bg="deepskyblue1")
        ba.grid(row=1,padx=85,pady=20)
        bb=Button(frame1,text="1.There are 9 words to find",width=100,height=2,bg="goldenrod2")
        bb.grid(row=2,padx=85,pady=10)
        bc=Button(frame1,text="2.Word matching works from LEFT-->RIGHT and TOP-->BOTTOM",width=100,height=2,bg="goldenrod2")
        bc.grid(row=3,padx=85,pady=10)
        bd=Button(frame1,text="3.Get default puzzle by using RESET",width=100,height=2,bg="goldenrod2")
        bd.grid(row=4,padx=85,pady=10)
        be=Button(frame1,text="4.Click SUBMIT to get result when you are done",width=100,height=2,bg="goldenrod2")
        be.grid(row=5,padx=85,pady=10)
        bf=Button(frame1,text="5.On submit you get your score",width=100,height=2,bg="goldenrod2")
        bf.grid(row=6,padx=85,pady=10)
        bi=Button(frame1,text="6.Under score GREEN COLOURED are words you found while RED COLOURED are words you missed",width=100,height=2,bg="goldenrod2")
        bi.grid(row=7,padx=85,pady=10)
        bj=Button(frame1,text="7.STARS are given to you as achievements as per your score",width=100,height=2,bg="goldenrod2")
        bj.grid(row=8,padx=85,pady=10)
        frame1.pack()
        
                       
        

    def Easy(root,frame):
        frame.pack_forget()
        frame1=Frame(root)
        p=[0,0,0,0,0,0,0,0,0,0]
        b=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        A=[['D','Z','O','R','B','G'],['T','U','M','C','A','M'],['S','T','O','T','H','L'],['W','L','F','K','L','O'],['E','B','T','E','A','L'],['R','A','H','A','L','E']]
        A1=["D O G","R A T","E E L","B A T","B U L L","H A R E","S L O T H","C A T","W O L F","C O W"]
        '''RTitle=root.title("Windows")
        RWidth=root.winfo_screenwidth()
        RHeight=root.winfo_screenheight()
        root.geometry(("%dx%d")%(RWidth,RHeight))'''
        root.title("Puzzle Game")
        frame1.configure(background="yellow")
        J=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        '''Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)

        #Create & Configure frame 
        frame=Frame(root)
        frame.grid(row=0, column=0, sticky=N+S+E+W)'''

        def check1(root,frame):
            frame.pack_forget()
            frame1=Frame(root)
            frame1.configure(background="yellow")
                
            g=0
            z=1
            counter=0
            for i in range(6):
                for j in range(6):
                         J[g]=b[i][j]["text"]
                         g=g+1
                
            for i in range(6):
                for j in range(6):
                         J[g]=b[j][i]["text"]
                         g=g+1
            k=string.join(J)
            for i in range(0,10):
                if A1[i] in k:
                        print A1[i]
                        counter=counter+1
                        
            result1=(counter*100)/10
            print result1
            if(result1==0):
                    z=0
                   
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=20,height=2,bg="deepskyblue1")
                    l2.grid(row=2,padx=10,pady=10)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,text="YOU FAILED,SORRY! NO STAR FOR YOU ",bg="navajowhite2")
                    bi.grid(row=4,column=2)
                    
            elif(result1>0 and result1<=20):
                    z=1
                    #l1=Button(frame1,text="ACHIEVEMENT",width=12,height=2,bg="olivedrab1")
                    #l1.grid(row=2,column=2)
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=20,height=2,bg="deepskyblue1")
                    l2.grid(row=2,padx=10,pady=10)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
            elif(result1>20 and result1<=40):
                    z=3
                    #l1=Button(frame1,text="ACHIEVEMENT",width=10,height=2,bg="olivedrab1")
                    #l1.grid(row=2,column=2)
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=20,height=2,bg="deepskyblue1")
                    l2.grid(row=2,padx=10,pady=10)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
                    bi1=Button(frame1,image=photo,width="36",height="30")
                    bi1.grid(row=3,column=5)
            elif(result1>40 and result1<=60):
                    z=4
                    #l1=Button(frame1,text="ACHIEVEMENT",width=12,height=2,bg="olivedrab1")
                    #l1.grid(row=2,column=2)
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=20,height=2,bg="deepskyblue1")
                    l2.grid(row=2,padx=10,pady=10)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=5)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=6)
            elif(result1>60 and result1<81):
                    z=5
                    #l1=Button(frame1,text="ACHIEVEMENT",width=12,height=2,bg="olivedrab1")
                    #l1.grid(row=2,column=3)
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=20,height=2,bg="deepskyblue1")
                    l2.grid(row=2,padx=10,pady=10)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=7)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=6)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=5)
            else :
                    z=6
                    #l1=Button(frame1,text="ACHIEVEMENT",width=12,height=2,bg="olivedrab1")
                    #l1.grid(row=2,column=2)
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=20,height=2,bg="deepskyblue1")
                    l2.grid(row=2,padx=10,pady=10)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=8)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=7)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=5)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=6)
                
            c1=lambda:Easy(root,frame1)
            c2=lambda:close_win(root)
            button3=Button(frame1,text="TRY AGAIN",width=11,height=2,bg="springgreen3",command=c1)
            button3.grid(row=9,column=3,padx=50,pady=5)
            button4=Button(frame1,text="EXIT",width=11,height=2,bg="indianred1",command=c2)
            button4.grid(row=11,column=3,padx=50)
            for i in range(9):
                if A1[i] in k:
                        p[i]=Button(frame1,text=A1[i],bg="green2")
                        p[i].grid(row=3+i,padx=85,pady=5)
            for i in range(9):
                if A1[i] not in k:
                        p[i]=Button(frame1,text=A1[i],bg="red")
                        p[i].grid(row=3+i,padx=85,pady=5)
            RTitle=root.title("Windows")
            RWidth=420
            RHeight=400
            root.geometry(("%dx%d")%(RWidth,RHeight))
            root.configure(background="yellow")
            frame1.pack()
            root.mainloop()

        for i in range(6):
                for j in range(6):
                    b[i][j] = Button(frame1,text=A[i][j],width=7,height=2,bg="black",fg="white") 
                    b[i][j].grid(row=i, column=j,padx=5,pady=5)
                    
        def reset_1():
            for i in range(6):
                for j in range(6):
                    b[i][j] = Button(frame1,text=A[i][j],width=7,height=2,bg="black",fg="white") 
                    b[i][j].grid(row=i, column=j,padx=5,pady=5)
                    
        def mouse_L(event):
            try:
                grid_info = event.widget.grid_info()
                print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
                if(int(grid_info["column"])>0):
                    b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])-1]["text"]=b[int(grid_info["row"])][int(grid_info["column"])-1]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
                else:
                   tkMessageBox.showwarning("Alert","Wrong Move")
            except Exception:
                print
        def mouse_U(event):
            grid_info = event.widget.grid_info()
            print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
            if(int(grid_info["row"])>0):
                b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])-1][int(grid_info["column"])]["text"]=b[int(grid_info["row"])-1][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
            else:
                tkMessageBox.showwarning("Alert","Wrong Move")
        def mouse_R(event):
            grid_info = event.widget.grid_info()
            print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
            if (int(grid_info["column"])<5):
                b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])+1]["text"]=b[int(grid_info["row"])][int(grid_info["column"])+1]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
            else:
                tkMessageBox.showwarning("Alert","Wrong Move")
        def mouse_D(event):
            grid_info = event.widget.grid_info()
            print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
            if (int(grid_info["row"])<5):
                b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])+1][int(grid_info["column"])]["text"]=b[int(grid_info["row"])+1][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
            else:
                tkMessageBox.showwarning("Alert","Wrong Move")

        command=lambda :check1(root,frame1)
        command1=lambda :inst1(root,frame1)
        ok=Button(frame1,text="SUBMIT",height=2,width=7,bg="cyan3",command=command)
        ok.grid(row=7,column=2,pady=5)
        re=Button(frame1,text="RESET",height=2,width=7,bg="deeppink3",command=reset_1)
        re.grid(row=7,column=3,pady=5)
        ok1=Button(frame1,text="INSTRUCTION",height=2,width=10,bg="gold3",command=command1)
        ok1.grid(row=8,column=7,pady=5)
        frame1.pack()   
        root.bind("<Button-1>", mouse_L)
        root.bind("<Button-2>", mouse_U)
        root.bind("<Button-3>", mouse_R)
        root.bind("<Double-Button-1>", mouse_D)

        root.mainloop()

    def inst2(root,frame):
        frame.pack_forget()
        frame1=Frame(root)
        frame1.config(background="yellow")
        #frame2=Frame(root)
        command=lambda:Medium(root,frame1)
        #l1=Label(frame2,text="instruction",fg="red",font=("Helvetica", 16))
        #l1.pack()
        button1=Button(frame1,text="  BACK  ",bg="green",command=command)
        button1.grid(row=9,column=5,padx=85,pady=20)
        ba=Button(frame1,text="SCIENTISTS LAST NAME WORD PUZZLE",width=100,height=2,bg="deepskyblue1")
        ba.grid(row=1,padx=85,pady=20)
        bb=Button(frame1,text="1.There are 10 words to find",width=100,height=2,bg="goldenrod2")
        bb.grid(row=2,padx=85,pady=10)
        bc=Button(frame1,text="2.Word matching works from LEFT-->RIGHT and TOP-->BOTTOM",width=100,height=2,bg="goldenrod2")
        bc.grid(row=3,padx=85,pady=10)
        bd=Button(frame1,text="3.Get default puzzle by using RESET",width=100,height=2,bg="goldenrod2")
        bd.grid(row=4,padx=85,pady=10)
        be=Button(frame1,text="4.Click SUBMIT to get result when you are done",width=100,height=2,bg="goldenrod2")
        be.grid(row=5,padx=85,pady=10)
        bf=Button(frame1,text="5.On submit you get your score",width=100,height=2,bg="goldenrod2")
        bf.grid(row=6,padx=85,pady=10)
        bi=Button(frame1,text="6.Under score GREEN COLOURED are words you found while RED COLOURED are words you missed",width=100,height=2,bg="goldenrod2")
        bi.grid(row=7,padx=85,pady=10)
        bj=Button(frame1,text="7.STARS are given to you as achievements as per your score",width=100,height=2,bg="goldenrod2")
        bj.grid(row=8,padx=85,pady=10)
        
        frame1.pack()
    
    def Medium(root,frame):
        frame.pack_forget()
        frame1=Frame(root)
        RTitle=root.title("Windows")
        RWidth=620
        RHeight=500
        root.geometry(("%dx%d")%(RWidth,RHeight))
        p=[0,0,0,0,0,0,0,0,0,0]
        b=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        A=[['P','C','W','N','L','K','T','A'],['E','A','C','R','X','E','S','D'],['U','S','B','F','U','D','T','N'],['I','E','E','O','H','L','R','C'],['A','I','E','H','X','S','S','W'],['L','E','R','R','Q','O','L','T'],['G','A','O','S','U','N','A','S'],['L','K','Z','P','E','E','R','N']]
        A1=["P L A N C K","T E S L A","G A U S S","N E W T O N","K E P L E R","E D I S O N","B O H R","P A S C A L","C U R I E","E U L E R"]
        '''RTitle=root.title("Windows")
        RWidth=root.winfo_screenwidth()
        RHeight=root.winfo_screenheight()
        root.geometry(("%dx%d")%(RWidth,RHeight))'''
        root.title("Puzzle Game")
        frame1.configure(background="yellow")
        J=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        '''Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)

        #Create & Configure frame 
        frame=Frame(root)
        frame.grid(row=0, column=0, sticky=N+S+E+W)'''

        def check2(root,frame):
            frame.pack_forget()
            frame1=Frame(root)
            frame1.configure(background="yellow")    
            g=0
            z=1
            counter=0
            for i in range(8):
                for j in range(8):
                         J[g]=b[i][j]["text"]
                         g=g+1
                
            for i in range(8):
                for j in range(8):
                         J[g]=b[j][i]["text"]
                         g=g+1
            k=string.join(J)
            for i in range(0,10):
                if A1[i] in k:
                        print A1[i]
                        counter=counter+1
                        
            result1=(counter*100)/10
            print result1
            if(result1==0):
                    z=0
                   
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=20,height=2,bg="deepskyblue1")
                    l2.grid(row=2,padx=10,pady=10)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,text="YOU FAILED,SORRY! NO STAR FOR YOU ",bg="navajowhite2")
                    bi.grid(row=4,column=2)
                    
            elif(result1>0 and result1<=20):
                    z=1
                    #l1=Button(frame1,text="ACHIEVEMENT",width=12,height=2,bg="olivedrab1")
                    #l1.grid(row=2,column=2)
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=20,height=2,bg="deepskyblue1")
                    l2.grid(row=2,padx=10,pady=10)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
            elif(result1>20 and result1<=40):
                    z=3
                    #l1=Button(frame1,text="ACHIEVEMENT",width=10,height=2,bg="olivedrab1")
                    #l1.grid(row=2,column=2)
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=20,height=2,bg="deepskyblue1")
                    l2.grid(row=2,padx=10,pady=10)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
                    bi1=Button(frame1,image=photo,width="36",height="30")
                    bi1.grid(row=3,column=5)
            elif(result1>40 and result1<=60):
                    z=4
                    #l1=Button(frame1,text="ACHIEVEMENT",width=12,height=2,bg="olivedrab1")
                    #l1.grid(row=2,column=2)
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=20,height=2,bg="deepskyblue1")
                    l2.grid(row=2,padx=10,pady=10)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=5)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=6)
            elif(result1>60 and result1<81):
                    z=5
                    #l1=Button(frame1,text="ACHIEVEMENT",width=12,height=2,bg="olivedrab1")
                    #l1.grid(row=2,column=3)
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=20,height=2,bg="deepskyblue1")
                    l2.grid(row=2,padx=10,pady=10)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=7)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=6)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=5)
            else :
                    z=6
                    #l1=Button(frame1,text="ACHIEVEMENT",width=12,height=2,bg="olivedrab1")
                    #l1.grid(row=2,column=2)
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=20,height=2,bg="deepskyblue1")
                    l2.grid(row=2,padx=10,pady=10)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=8)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=7)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=5)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=6)
                
            c1=lambda:Medium(root,frame1)
            c2=lambda:close_win(root)
            button3=Button(frame1,text="TRY AGAIN",width=11,height=2,bg="springgreen3",command=c1)
            button3.grid(row=9,column=3,padx=50,pady=5)
            button4=Button(frame1,text="EXIT",width=11,height=2,bg="indianred1",command=c2)
            button4.grid(row=11,column=3,padx=50)
            for i in range(10):
                if A1[i] in k:
                        p[i]=Button(frame1,text=A1[i],bg="green2")
                        p[i].grid(row=3+i,padx=85,pady=5)
            for i in range(10):
                if A1[i] not in k:
                        p[i]=Button(frame1,text=A1[i],bg="red")
                        p[i].grid(row=3+i,padx=85,pady=5)
            RTitle=root.title("Windows")
            RWidth=420
            RHeight=400
            root.geometry(("%dx%d")%(RWidth,RHeight))
            #photo1=PhotoImage(file="bg.gif")
            root.configure(background="yellow")
            frame1.pack()
            root.mainloop()

        for i in range(8):
                for j in range(8):
                    b[i][j] = Button(frame1,text=A[i][j],width=7,height=2,bg="black",fg="white") 
                    b[i][j].grid(row=i, column=j,padx=5,pady=5)
                    
        def reset_1():
            for i in range(8):
                for j in range(8):
                    b[i][j] = Button(frame1,text=A[i][j],width=7,height=2,bg="black",fg="white") 
                    b[i][j].grid(row=i, column=j,padx=5,pady=5)
                    
        def mouse_L(event):
            try:
                grid_info = event.widget.grid_info()
                print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
                if(int(grid_info["column"])>0):
                    b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])-1]["text"]=b[int(grid_info["row"])][int(grid_info["column"])-1]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
                else:
                   tkMessageBox.showwarning("Alert","Wrong Move")
            except Exception:
                print
        def mouse_U(event):
            grid_info = event.widget.grid_info()
            print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
            if(int(grid_info["row"])>0):
                b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])-1][int(grid_info["column"])]["text"]=b[int(grid_info["row"])-1][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
            else:
                tkMessageBox.showwarning("Alert","Wrong Move")
        def mouse_R(event):
            grid_info = event.widget.grid_info()
            print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
            if (int(grid_info["column"])<7):
                b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])+1]["text"]=b[int(grid_info["row"])][int(grid_info["column"])+1]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
            else:
                tkMessageBox.showwarning("Alert","Wrong Move")
        def mouse_D(event):
            grid_info = event.widget.grid_info()
            print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
            if (int(grid_info["row"])<7):
                b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])+1][int(grid_info["column"])]["text"]=b[int(grid_info["row"])+1][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
            else:
                tkMessageBox.showwarning("Alert","Wrong Move")

        command=lambda :check2(root,frame1)
        command1=lambda :inst2(root,frame1)
        ok=Button(frame1,text="SUBMIT",height=2,width=7,bg="cyan3",command=command)
        ok.grid(row=10,column=3,pady=5)
        re=Button(frame1,text="RESET",height=2,width=7,bg="deeppink3",command=reset_1)
        re.grid(row=10,column=4,pady=5)
        ok1=Button(frame1,text="INSTRUCTION",height=2,width=10,bg="gold3",command=command1)
        ok1.grid(row=11,column=11,pady=5)
        frame1.pack()   
        root.bind("<Button-1>", mouse_L)
        root.bind("<Button-2>", mouse_U)
        root.bind("<Button-3>", mouse_R)
        root.bind("<Double-Button-1>", mouse_D)

        root.mainloop()

    def inst3(root,frame):
        frame.pack_forget()
        frame1=Frame(root)
        frame1.config(background="yellow")
        #frame2=Frame(root)
        command=lambda:Hard(root,frame1)
        #l1=Label(frame2,text="instruction",fg="red",font=("Helvetica", 16))
        #l1.pack()
        button1=Button(frame1,text="  BACK  ",bg="green",command=command)
        button1.grid(row=9,column=5,padx=85,pady=20)
        ba=Button(frame1,text="MARVEL's UNIVERSE WORD PUZZLE",width=100,height=2,bg="deepskyblue1")
        ba.grid(row=1,padx=85,pady=20)
        bb=Button(frame1,text="1.There are 15 words to find",width=100,height=2,bg="goldenrod2")
        bb.grid(row=2,padx=85,pady=10)
        bc=Button(frame1,text="2.Word matching works from LEFT-->RIGHT and TOP-->BOTTOM",width=100,height=2,bg="goldenrod2")
        bc.grid(row=3,padx=85,pady=10)
        bd=Button(frame1,text="3.Get default puzzle by using RESET",width=100,height=2,bg="goldenrod2")
        bd.grid(row=4,padx=85,pady=10)
        be=Button(frame1,text="4.Click SUBMIT to get result when you are done",width=100,height=2,bg="goldenrod2")
        be.grid(row=5,padx=85,pady=10)
        bf=Button(frame1,text="5.On submit you get your score",width=100,height=2,bg="goldenrod2")
        bf.grid(row=6,padx=85,pady=10)
        bi=Button(frame1,text="6.Under score GREEN COLOURED are words you found while RED COLOURED are words you missed",width=100,height=2,bg="goldenrod2")
        bi.grid(row=7,padx=85,pady=10)
        bj=Button(frame1,text="7.STARS are given to you as achievements as per your score",width=100,height=2,bg="goldenrod2")
        bj.grid(row=8,padx=85,pady=10)
        
        frame1.pack()
    
    def Hard(root,frame):
        frame.pack_forget()
        frame1=Frame(root)
        RTitle=root.title("Windows")
        RWidth=820
        RHeight=700
        root.geometry(("%dx%d")%(RWidth,RHeight))
        p=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        b=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
        A=[['N','I','A','T','P','A','C','S','H','T'],['A','A','K','L','U','H','T','A','L','L'],['M','G','M','P','S','A','W','O','O','R'],['N','T','T','R','R','K','B','O','E','E'],['O','O','M','L','E','K','P','H','N','F'],['R','O','O','Y','C','D','T','O','A','R'],['I','R','E','A','A','N','I','L','K','O'],['D','G','L','E','A','S','C','P','E','H'],['M','B','D','P','I','O','C','K','S','T'],['Y','E','I','V','N','A','M','T','N','A']]
        A1=["A N T M A N","D E A D P O O L","P A N T H E R","B L A C K B O L T","F A L C O N","S P I D E R M A N","V I S I O N","C A P T A I N","G R O O T","I R O N M A N","S T A R L O R D","T H O R","H A W K E Y E","H U L K","W A S P"]
        '''RTitle=root.title("Windows")
        RWidth=root.winfo_screenwidth()
        RHeight=root.winfo_screenheight()
        root.geometry(("%dx%d")%(RWidth,RHeight))'''
        root.title("Puzzle Game")
        frame1.configure(background="yellow")
        J=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        '''Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)

        #Create & Configure frame 
        frame=Frame(root)
        frame.grid(row=0, column=0, sticky=N+S+E+W)'''

        def check3(root,frame):
            frame.pack_forget()
            frame1=Frame(root)
            frame1.configure(background="yellow")   
            g=0
            z=1
            counter=0
            for i in range(10):
                for j in range(10):
                         J[g]=b[i][j]["text"]
                         g=g+1
                
            for i in range(10):
                for j in range(10):
                         J[g]=b[j][i]["text"]
                         g=g+1
            k=string.join(J)
            for i in range(0,15):
                if A1[i] in k:
                        print A1[i]
                        counter=counter+1
                        
            result1=(counter*100)/15
            print result1
            if(result1==0):
                    z=0
                   
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=20,height=2,bg="deepskyblue1")
                    l2.grid(row=2,padx=10,pady=10)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,text="YOU FAILED,SORRY! NO STAR FOR YOU ",bg="navajowhite2")
                    bi.grid(row=4,column=2)
                    
            elif(result1>0 and result1<=20):
                    z=1
                    #l1=Button(frame1,text="ACHIEVEMENT",width=12,height=2,bg="olivedrab1")
                    #l1.grid(row=2,column=2)
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=20,height=2,bg="deepskyblue1")
                    l2.grid(row=2,padx=10,pady=10)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
            elif(result1>20 and result1<=40):
                    z=3
                    #l1=Button(frame1,text="ACHIEVEMENT",width=10,height=2,bg="olivedrab1")
                    #l1.grid(row=2,column=2)
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=20,height=2,bg="deepskyblue1")
                    l2.grid(row=2,padx=10,pady=10)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
                    bi1=Button(frame1,image=photo,width="36",height="30")
                    bi1.grid(row=3,column=5)
            elif(result1>40 and result1<=60):
                    z=4
                    #l1=Button(frame1,text="ACHIEVEMENT",width=12,height=2,bg="olivedrab1")
                    #l1.grid(row=2,column=2)
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=20,height=2,bg="deepskyblue1")
                    l2.grid(row=2,padx=10,pady=10)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=5)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=6)
            elif(result1>60 and result1<81):
                    z=5
                    #l1=Button(frame1,text="ACHIEVEMENT",width=12,height=2,bg="olivedrab1")
                    #l1.grid(row=2,column=3)
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=20,height=2,bg="deepskyblue1")
                    l2.grid(row=2,padx=10,pady=10)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=7)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=6)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=5)
            else :
                    z=6
                    #l1=Button(frame1,text="ACHIEVEMENT",width=12,height=2,bg="olivedrab1")
                    #l1.grid(row=2,column=2)
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=20,height=2,bg="deepskyblue1")
                    l2.grid(row=2,padx=10,pady=10)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=8)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=7)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=5)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=6)
                
            c1=lambda:Hard(root,frame1)
            c2=lambda:close_win(root)
            button3=Button(frame1,text="TRY AGAIN",width=11,height=2,bg="springgreen3",command=c1)
            button3.grid(row=9,column=3,padx=50,pady=5)
            button4=Button(frame1,text="EXIT",width=11,height=2,bg="indianred1",command=c2)
            button4.grid(row=11,column=3,padx=50)
            for i in range(15):
                if A1[i] in k:
                        p[i]=Button(frame1,text=A1[i],bg="green2")
                        p[i].grid(row=3+i,padx=85,pady=5)
            for i in range(15):
                if A1[i] not in k:
                        p[i]=Button(frame1,text=A1[i],bg="red")
                        p[i].grid(row=3+i,padx=85,pady=5)
            RTitle=root.title("Windows")
            RWidth=420
            RHeight=400
            root.geometry(("%dx%d")%(RWidth,RHeight))
            #photo1=PhotoImage(file="bg.gif")
            root.configure(background="yellow")
            frame1.pack()
            root.mainloop()
            
        for i in range(10):
                for j in range(10):
                    b[i][j] = Button(frame1,text=A[i][j],width=7,height=2,bg="black",fg="white") 
                    b[i][j].grid(row=i, column=j,padx=5,pady=5)
                    
        def reset_1():
            for i in range(10):
                for j in range(10):
                    b[i][j] = Button(frame1,text=A[i][j],width=7,height=2,bg="black",fg="white") 
                    b[i][j].grid(row=i, column=j,padx=5,pady=5)
                    
        def mouse_L(event):
            try:
                grid_info = event.widget.grid_info()
                print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
                if(int(grid_info["column"])>0):
                    b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])-1]["text"]=b[int(grid_info["row"])][int(grid_info["column"])-1]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
                else:
                   tkMessageBox.showwarning("Alert","Wrong Move")
            except Exception:
                print
        def mouse_U(event):
            grid_info = event.widget.grid_info()
            print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
            if(int(grid_info["row"])>0):
                b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])-1][int(grid_info["column"])]["text"]=b[int(grid_info["row"])-1][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
            else:
                tkMessageBox.showwarning("Alert","Wrong Move")
        def mouse_R(event):
            grid_info = event.widget.grid_info()
            print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
            if (int(grid_info["column"])<9):
                b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])+1]["text"]=b[int(grid_info["row"])][int(grid_info["column"])+1]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
            else:
                tkMessageBox.showwarning("Alert","Wrong Move")
        def mouse_D(event):
            grid_info = event.widget.grid_info()
            print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
            if (int(grid_info["row"])<9):
                b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])+1][int(grid_info["column"])]["text"]=b[int(grid_info["row"])+1][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
            else:
                tkMessageBox.showwarning("Alert","Wrong Move")
        command=lambda :check3(root,frame1)
        command1=lambda :inst3(root,frame1)
        ok=Button(frame1,text="SUBMIT",height=2,width=7,bg="cyan3",command=command)
        ok.grid(row=12,column=4,pady=5)
        re=Button(frame1,text="RESET",height=2,width=7,bg="deeppink3",command=reset_1)
        re.grid(row=12,column=5,pady=5)
        ok1=Button(frame1,text="INSTRUCTION",height=2,width=12,bg="gold4",command=command1)
        ok1.grid(row=13,column=13,pady=5)
        frame1.pack()   
        root.bind("<Button-1>", mouse_L)
        root.bind("<Button-2>", mouse_U)
        root.bind("<Button-3>", mouse_R)
        root.bind("<Double-Button-1>", mouse_D)

        root.mainloop()


    

    
    frame1=Frame(root)
    frame1.configure(background="yellow")
    command=lambda :Easy(root,frame1)
    command1=lambda :Medium(root,frame1)
    command2=lambda :Hard(root,frame1)
    ok=Button(frame1,text=" EASY ",height=2,width=7,bg="turquoise1",command=command)
    ok1=Button(frame1,text=" MEDIUM ",height=2,width=7,bg="orange",command=command1)
    ok2=Button(frame1,text=" HARD ",height=2,width=7,bg="red",command=command2)
    ok.grid(row=7,padx=85,pady=10)
    ok1.grid(row=8,padx=85,pady=10)
    ok2.grid(row=9,padx=85,pady=10)
    frame1.pack()
    root.mainloop()

root=Tk()
root.title("Puzzle Game")
#root.resizable(0,0)
RTitle=root.title("Windows")
RWidth=420
RHeight=400
root.geometry(("%dx%d")%(RWidth,RHeight))
root.configure(background="yellow")
frame=Frame(root,width=300)
frame.configure(background="yellow")
command=lambda :start(root,frame)
command1=lambda :close_win(root)
ok=Button(frame,text=" START GAME ",height=2,width=11,bg="green",command=command)
ok1=Button(frame,text=" EXIT ",height=2,width=7,bg="red",command=command1)

ok.grid(row=7,padx=100,pady=20)
ok1.grid(row=9,padx=20,pady=100)
frame.pack_propagate(0)
frame.pack()

root.mainloop()


