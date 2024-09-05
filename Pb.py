from tkinter import*
from tkinter.ttk import *
import time



pw=Tk()
pw.title("Please pwait")
pw.geometry("550x400+150+150")
pw.overrideredirect(True)
pw.config(bg="White")
I99=PhotoImage(file="Media\\DL.png")
llo=Label(pw,image=I99)
llo.place(x=-1.5,y=-1.5)

fop=Frame(pw,width=600,height=200)
fop.place(x=-1.5,y=100)

lbl2 = Label(pw,text="LOADING",font=("times",20,'bold'))
lbl2.place(x=200,y=100)

lbl3 = Label(pw,text="",font=("times",20,'bold'))
lbl3.place(x=160,y=100)

lbl4 = Label(pw,text="",font=("times",20,'bold'))
lbl4.place(x=140,y=100)

lbl5 = Label(pw,text="",font=("times",20,'bold'))
lbl5.place(x=120,y=100)


def bar(): 

        for i in range(1,101,1):
                progress['value'] = i
                pw.update_idletasks() 
                time.sleep(.03)
                s=str(i)+" %"
                lb1.config(text=s)
                p="Order Recived"
                d=" Lightning The Stove  "
                f=" Preparing Your meal "
            
                lb1.config(text= s)
                if i == 5:
                    lbl2.destroy()
                    lbl3.config(text= p)
                elif i == 35:
                    lbl3.destroy()
                    lbl4.config(text= d)
                
                elif i == 69:
                    lbl4.destroy()
                    lbl5.config(text= f)
                elif i==100:
                    pw.destroy()
                    import Submitscreen


lb1=Label(pw,text='0%',font=("Arial",20))
lb1.place(x=240,y=190)



progress = Progressbar(pw, orient = HORIZONTAL,length = 350)
progress
progress.place(x=100,y=150)

pw.after(1000,bar)

pw.mainloop()
