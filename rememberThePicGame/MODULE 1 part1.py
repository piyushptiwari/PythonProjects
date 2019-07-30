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
C.pack()
top.mainloop()
