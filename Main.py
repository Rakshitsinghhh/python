from tkinter import *
import time
import random as r


from pygame import mixer
mixer.init()
mixer.music.load("Media\\kb.mp3")

root = Tk()
root.geometry("580x490+200+200")
root.overrideredirect(True)


from PIL import Image
fnm="Media\\tenor.gif"
imageObject = Image.open(fnm)



frameCnt = imageObject.n_frames
frames = [PhotoImage(file=fnm,format = 'gif -index %i' %(i)) for i in range(frameCnt)]
def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)

label = Label(root)
label.pack()

Label(root,text=" ST. ANTHONY'S SR. SEC. SCHOOL UDAIPUR",font=('Arial Black',14)).place(x=50,y=0)
Label(root,bg='YELLOW',fg='red',text="PROJECT ON RESTURANT",font=("Arial Black",14)).place(x=150,y=50)


l1 = Label(root,text="",font= ('Helvetica' ,'18'),width=31)
l1.place(x=65,y=375)
l1.configure(anchor="center")


  
colo=["black", "red", "green", "blue", "cyan", "Gold", "magenta" ]    
    
titl=["Project Submitted By",
      "Rakshit Singh",
      "Class : CBSE XII",
      "Computer Science(083)",
      "Session 2022-23",
      "Under Guidance of ",
      "Sunil Kumar Sharma",
      "PGT Computer Science",
      "Project on Resturant "]

def dispname(sss):
    mixer.music.play()
    l=len(sss)
    l1.config(fg=colo[r.randint(0,6)])
    for i in range(l):
        l1.config(text=sss[:i+1])
        time.sleep(.1)
        root.update_idletasks ()
    mixer.music.stop()
    
def showtitle():
    
    for i in titl:
        dispname(i)
        time.sleep(.3)
        
    

def callback(event):
    mixer.music.stop()
    root.destroy()
    exit()
    
root.bind("<Button-1>", callback)
root.after(0, update, 0)
root.after(1000, showtitle)

def apneaap():
    root.destroy()
    import log

root.after(4000,apneaap)
root.mainloop()