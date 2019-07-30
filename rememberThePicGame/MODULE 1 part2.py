import Tkinter
from Tkinter import*
top3=Tkinter.Tk()
C=Tkinter.Canvas(top3,bg='red',height=600,width=600)
filename=PhotoImage(file="py1.gif")
image=C.create_image(150,50,anchor=N,image=filename)
name=PhotoImage(file="py2.gif")
image=C.create_image(450,50,anchor=N,image=name)
name1=PhotoImage(file="py3.gif")
image=C.create_image(150,300,anchor=N,image=name1)
name2=PhotoImage(file="py4.gif")
image=C.create_image(450,300,anchor=N,image=name2)
C.pack()
top3.mainloop()
