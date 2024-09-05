from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import random
import mysql.connector


#window
lw=Tk()
lw.title("Welcome To Our Resturant")
lw.geometry("600x400+150+150")
lw.config(bg="light salmon")

I100=PhotoImage(file="Media\\DL.png")
ll=Label(lw,image=I100)
ll.place(x=-1.5,y=0)

def abtop():
   
    lw.destroy()
    import abt


Iabt=PhotoImage(file="Media\\ablogo.png")
Babt=Button(lw,image=Iabt,command=abtop)
Babt.place(x=470,y=12)

def hpop():
    import help

Ihp=PhotoImage(file="Media\\hplogo.png")
Bhp=Button(lw,image=Ihp,command=hpop)
Bhp.place(x=535,y=12)

l21=Label(lw,text="Welcome to Our Resturant",font=("Helvetica",'17'),fg="RED",bg="grey25")
l21.place(x=120,y=65)



def showf3():
    fop.place_forget()
    f3.place(x=0,y=100)
    f5.place(x=0,y=302)
def showf4():
    fop.place_forget()
    f4.place(x=0,y=100)
    f6.place(x=0,y=302)
#--------Buttons for Pass or OTP------#

fop=Frame(lw,width=600,height=200,bg='grey')
fop.place(x=0,y=100)

I=PhotoImage(file="Media\\Dext.png")
Label(fop,image=I).place(x=-1.5,y=-1.80)

b1=Button(fop,text="Log In With Paaword",font=('Helvetica',16),fg="forestgreen",bg="grey25",command=showf4)
b1.place(x=20,y=50)

b2=Button(fop,text=" Log in With O.T.P. ",font=('Helvetica',16),fg="forestgreen",bg="grey25",command=showf3)
b2.place(x=315,y=50)

l22=Label(fop,text="Please Log In to Order Food",font=("Helvetica",'15'),fg="RoyalBlue2",bg="grey25")
l22.place(x=130,y=160)

#--------Frame for Otp------#

f3=Frame(lw,width=600,height=200,bg='grey')
f3.place_forget()

I4=PhotoImage(file="Media\\Dext.png")
Label(f3,image=I4).place(x=-1.5,y=-2)

lb=Label(f3,text="                 LOGIN WITH OTP                 ",font=('Helvetica',17),fg="light salmon",bg="chartreuse4")
lb.place(x=60,y=10)

lb1=Label(f3,text="Mobile Number",font=('Helvetica',16),fg="light salmon",bg="grey25")
lb1.place(x=80,y=70)

abc=random.randrange(1000,9999,1)

def genotp():
    messagebox.showinfo("Rember,Your Otp is",abc)
    print("Your O.T.P. is : ",abc)

b99=Button(f3,text="Generate an O.T.P.",font=('Helvetica',10),fg="White",bg="grey25",command=genotp)
b99.place(x=230,y=160)

lb2=Label(f3,text="     O. T. P.      ",font=('Helvetica',16),fg="light salmon",bg="grey25")
lb2.place(x=80,y=120)

e1=Entry(f3,font=(20),width='20',justify='center',show='*')
e1.place(x=330,y=75)

e2=Entry(f3,font=(20),width='20',justify='center',show='*')
e2.place(x=330,y=125)

#-------Frame for Password-----#

f4=Frame(lw,width=600,height=150,bg='grey')
f4.place_forget()

I5=PhotoImage(file="Media\\Dext.png")
Label(f4,image=I5).place(x=-2,y=-1.75)

lb3=Label(f4,text="            LOGIN WITH PASSWORD          ",font=('Helvetica',17),fg="light salmon",bg="chartreuse4")
lb3.place(x=50,y=10)

lb4=Label(f4,text=" USER NAME ",font=('Helvetica',16),fg="light salmon",bg="grey25")
lb4.place(x=80,y=70)

lb5=Label(f4,text=" PASSWORD ",font=('Helvetica',16),fg="light salmon",bg="grey25")
lb5.place(x=80,y=120)

e3=Entry(f4,font=(20),width='20',justify='center')
e3.place(x=330,y=75)


e4=Entry(f4,font=(20),width='20',justify='center',show='*')
e4.place(x=330,y=125)

#-------Frame for Password-----#

f5=Frame(lw,width=600,height=150,bg='grey')
f5.place_forget()

I6=PhotoImage(file="Media\\DR.png")
Label(f5,image=I6).place(x=-2,y=-1.75)

#------Buttons------#



def reg():
    lw.destroy()
    import registration    

def submit1():
    if e1.get()=="":
        messagebox.showerror("Try Again","Mobile Number is required")
    else:
        pass
    if e2.get()=="":
        messagebox.showerror("Try Again","O.T.P. is required")
    else:
        pass
    try:
        int(e2.get())
    except ValueError:
        messagebox.showerror("Try Again", "OTP is Incorrect")
    try:
        int(e1.get())
    except ValueError:
        messagebox.showerror("Try Again", "Enter a valid Mobile Number")
    if str(e2.get())==str(abc):
        messagebox.showinfo("Correct OTP","Login Successful")
        lw.destroy()
        import mainmenu
    else:
        messagebox.showerror("Try Again","OTP is Incorrect")
        
       

b3=Button(f5,text="Register",font=('Helvetica',16),fg="forestgreen",bg="grey25",command=reg)
b3.place(x=150,y=5)

b4=Button(f5,text=" Submit ",font=('Helvetica',16),fg="forestgreen",bg="grey25",command=submit1)
b4.place(x=350,y=5)

def reg2():
    lw.destroy()
    import registration
    

def submit2():
    unam=e3.get()
    paws=e4.get()
    
    
    if unam=="":
        messagebox.showerror("Try Again","User Name is required")
    else:
        pass
    if paws=="":
        messagebox.showerror("Try Again","Password is required")
        
    con=mysql.connector.connect(host='localhost',user='root')
    cur=con.cursor()
    cur.execute("create database if not exists restdb;")
    cur.execute("use restdb;")
    sss="select uname,pass from lgninfo where uname=%s and pass=%s"
    cur.execute(sss,[(unam),(paws)])
    rre=cur.fetchall()

    if rre:
        messagebox.showinfo("Succesfull","Login Succesfull")
        print()
        print()
        lw.destroy()
        import mainmenu
    else:
        messagebox.showerror("Try Again","User Name or Password is Incorrect")


f6=Frame(lw,width=600,height=150,bg='grey')
f6.place_forget()

I7=PhotoImage(file="Media\\DR.png")
Label(f6,image=I7).place(x=-2,y=-1.75)

b5=Button(f6,text="Register",font=('Helvetica',16),fg="forestgreen",bg="grey25",command=reg2)
b5.place(x=150,y=5)

b6=Button(f6,text=" Submit ",font=('Helvetica',16),fg="forestgreen",bg="grey25",command=submit2)
b6.place(x=350,y=5)


lw.mainloop()