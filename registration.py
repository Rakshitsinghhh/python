from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import random
import mysql.connector

w=Tk()
w.title("main menu")
w.geometry("600x400+150+150")
I99=PhotoImage(file="Media\\DL.png")
llo=Label(w,image=I99)
llo.place(x=-1.5,y=0)

l21=Label(w,text="Welcome to Our Resturant",font=("Helvetica",'15'),fg="RED",bg="grey25")
l21.place(x=130,y=15)

def abtop():
    w.destroy()
    import abt


Iabt=PhotoImage(file="Media\\ablogo.png")
Babt=Button(w,image=Iabt,command=abtop)
Babt.place(x=470,y=12)

def hpop():
    import help

Ihp=PhotoImage(file="Media\\hplogo.png")
Bhp=Button(w,image=Ihp,command=hpop)
Bhp.place(x=535,y=12)

#--------------------------Entry--------------------------#
e10=Entry(w)
e10.place(x=300,y=60)

e20=Entry(w)
e20.place(x=300,y=110)

e30=Entry(w)
e30.place(x=300,y=160)

e40=Entry(w)
e40.place(x=300,y=210)

e50=Entry(w)
e50.place(x=300,y=260)

#--------------------------Label--------------------------#

l10=Label(w,text="   USER NAME ",font=('Helvetica',15),fg="light salmon",bg="chartreuse4")
l10.place(x=90,y=55)

l20=Label(w,text="  PASSWORD  ",font=('Helvetica',15),fg="light salmon",bg="chartreuse4")
l20.place(x=90,y=105)

l30=Label(w,text="       EMAIL        ",font=('Helvetica',15),fg="light salmon",bg="chartreuse4")
l30.place(x=90,y=155)

l40=Label(w,text="    PHONE.NO.  ",font=('Helvetica',15),fg="light salmon",bg="chartreuse4")
l40.place(x=90,y=205)

l50=Label(w,text="         CITY         ",font=('Helvetica',15),fg="light salmon",bg="chartreuse4")
l50.place(x=90,y=255)

#--------------------------Commands--------------------------#

def bkt():
    w.destroy()
    import log
    
    
def submit1():
    tit='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoprstuvwxyz'
    aas='0123456789'
    blwjb='''!@#$%^&*()_~=+-..,/';;>:"?:>>"'''
    uname=e10.get()
    passw=e20.get()
    email=e30.get()
    pn=e40.get()
    ct=e50.get()
    
   
#=================== error ===============
    if uname=="":
        messagebox.showerror("Try Again","User Name is required")
    if uname in aas:
        messagebox.showerror("Try Again","Invalid username")
    if uname in blwjb:
        messagebox.showerror("Try Again","Invalid username")
        
        
    if passw=="":
        messagebox.showerror("Try Again","Password is required")
    
    if email=="":
        messagebox.showerror("Try Again","Email is required")
    if pn=="":
        messagebox.showerror("Try Again","Mobile Number is required")
        
    if pn in blwjb:
        messagebox.showerror("Try Again","Invalid mobile number")
    if pn in tit:
        messagebox.showerror("Try Again","Invalid mobile number")
    if ct=="":
        messagebox.showerror("Try Again","City is required")
        
    if ct in aas:
        messagebox.showerror("Try Again","Please enter correct city")
    if ct in blwjb:
        messagebox.showerror("Try Again","Please enter correct city")
        
    else:
        print("Record Saved ")
        messagebox.showinfo("Successfull","Registration is successful")
                    
    record= f'''insert into lgninfo values('{uname}','{passw}','{email}','{pn}','{ct}');'''
        
    print(uname,passw,email,pn,ct)
    
    con=mysql.connector.connect(host='localhost',user='root')
    cur=con.cursor()
    cur.execute("create database if not exists restdb;")
    cur.execute("use restdb;")
    cur.execute('''create table if not exists lgninfo
    (uname char(20),
    pass char(8),
    email varchar(20),
    phnno int(10),
    city char(20));''')
    print('rec')
    cur.execute(record)
    
    print()
    print()
    while True:
        w.destroy()
        import log
    
   
        
        
#--------------------------Buttons--------------------------#

b10=Button(w,text="  Back  ",font=('Helvetica',16),fg="forestgreen",bg="grey25",command=bkt)
b10.place(x=130,y=300)

b20=Button(w,text=" Register ",font=('Helvetica',16),fg="forestgreen",bg="grey25",command=submit1)
b20.place(x=310,y=300)

w.mainloop()