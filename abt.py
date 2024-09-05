from tkinter import *
import webbrowser

def rak2():
    webbrowser.open('https://linktr.ee/rakshitsinghhh?utm_source=linktree_profile_share&ltsid=89d0d709-2aa7-4c14-a635-74a7b4aff30a')

def ru1():
    webbrowser.open('https://linktr.ee/Rushilchittora')
    
    
    
aw=Tk()
aw.title("About")
aw.geometry("355x490+10+10")
aw.config(bg="pink")

I1=PhotoImage(file="Media\\ru1.png")
I2=PhotoImage(file="Media\\rak1.png")


def rusop():
    arus= Toplevel(aw)  
    arus.title("About Rushil")
    arus.geometry("355x490+370+10")
    arus.config(bg="cyan")
    rul1=Label(arus,text='''My
Name is
Rushil
Chittora.
I am
17 years
old.
I study in
Class 12th of 
St. Anthony
Sr. Sec.
School
''',font=("",15), fg="MintCream",bg="RoyalBlue4",height=13,width=13)
    rul1.place(x=70,y=10)
    btn=Button(arus,text="contact us",command=ru1)
    btn.place(x=120,y=400)
    arus.mainloop()
    
    
def rakop():
    arak=Tk()
    arak.title("About Rakshit")
    arak.config(bg="cyan")
    arak.geometry("355x490+370+10")
    rak1=Label(arak,text='''My
Name is
Rakshit
Singh.
I am
17 years
old.
I study in
Class 12th of 
St. Anthony
Sr. Sec.
School
''',font=("",15), fg="MintCream",bg="RoyalBlue4",height=13,width=13)
    rak1.place(x=70,y=10)
    btn=Button(arak,text="contact us",command=rak2)
    btn.place(x=120,y=400)
    

    
B1=Button(aw,image=I1,border=4,command=rusop)
B1.place(x=10,y=320)

B2=Button(aw,image=I2,border=4,command=rakop)
B2.place(x=180,y=320)

l25=Label(aw,text='''Click on images to
view more
information

This Program Is
devloped by 2 
Students of your
School:)'''
,font=('Verdana',15),bg='pink',fg="grey24",height=10,width=21)
l25.place(x=5,y=5)

def pop():
    aw.destroy()
    import log

I99=PhotoImage(file="Media\\back.png")

b999=Button(aw,image=I99,command=pop)
b999.place(x=5,y=5)


aw.mainloop()