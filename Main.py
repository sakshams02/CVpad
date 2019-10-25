from tkinter import *
from PIL import ImageTk,Image  
parent = Tk()  
parent.geometry("1068x601")
def exitcoded():
    parent.destroy()
def executecoded():
    parent.destroy()
    import test2   
qbutton = Button(parent, text = "I don't want to Draw!",command=exitcoded,bg = "orange",fg="white",activeforeground="white",activebackground="red")
qbutton.pack( side ="bottom",fill="x")
stbutton = Button(parent, text = "Let's go and test out this super innovative application!",command=executecoded, bg = "orange",fg="white",activeforeground="white",activebackground="green",highlightcolor="yellow")  
stbutton.pack( side ="bottom",fill="x")
nc=Canvas(parent,bg="pink",width=1068,height=601)
nc.pack()
parent.mainloop()  
