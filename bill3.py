from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import random
import mysql.connector

con=mysql.connector.connect(host='localhost',user='root')
cur=con.cursor()
cur.execute("create database if not exists restdb;")
cur.execute("use restdb;")
cur.execute('''create table if not exists rajasthani
(NO int(20),
naam char(29),
pric int(4));''')

cur.execute('''insert into rajasthani
values(1,"Dal Baati Churma",140),
(2,"Bajra Roti",120),
(3,"DAL Chawal Kutt",130),
(4,"Masala Gatta",140),
(5,"Pyaaz Panner",100),
(6,"Baigan Masala",130),
(7,"Tawa Roti",100),
(8,"Dal Banjari",120),
(9,"Bajra ka Khichda",150),
(10,"Besan ki Sabzi",130),
(11,"Sev Tamatar",130),
(12,"Pittod ki Sabzi",100)
''')



cur.execute('''create table if not exists gujrati
(NO int(20),
naam char(29),
pric int(4));''')

cur.execute('''create table if not exists multi
(NO int(20),
naam char(29),
pric int(4));''')




bop=Tk()
bop.title("Bill")
bop.geometry("600x400+150+150")

I99=PhotoImage(file="Media\\DL.png")
llo=Label(bop,image=I99)
llo.place(x=-1.5,y=0)

lpop=Label(bop,text="Bill",font=('Helvetica',30),fg="Red",bg="grey6")
lpop.place(x=260,y=15)

filename='Yourorders.txt'
f=open(filename)
s=f.readlines()
f.close()

qwe=s 
        

f25=Frame(bop,height=250,width=550,bg="lightblue")
f25.place(x=25,y=100)



lko=Label(f25,text='''Amount to be paid is:
presented below including
50 Rs. for Delivery

''',height=8,width=30,fg="RoyalBlue2",bg="grey6")
lko.place(x=10,y=70)

def np():
    f25.place_forget()
    f26.place(x=100,y=100)

e1=Text(f25,height=2,width=20)
e1.place(x=270,y=10)

le=Label(f25,text="Your Address",fg="RoyalBlue2",bg="grey6",font=("times",17))
le.place(x=50,y=20)

B23=Button(bop,text="Next",command=np)
B23.place(x=130,y=290)

i89=PhotoImage(file="Media\\names.png")
l1=Label(f25,image=i89)
l1.place(x=280,y=60)

def paytm():
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
        messagebox.showinfo("Correct OTP","Payment Successful")
    else:
        messagebox.showerror("Try Again","OTP is Incorrect")



f26=Frame(bop,height=250,width=400,bg="lightblue")
f26.place_forget()

l27=Label(f26,text="Enter Your Details",font=('Helvetica',15),fg="RoyalBlue2",bg="lightpink")
l27.place(x=110,y=10)

l28=Label(f26,text=" Mobile Number ",font=('Helvetica',15),fg="RoyalBlue2",bg="grey6")
l28.place(x=20,y=80)

l28=Label(f26,text="        O.T.P.        ",font=('Helvetica',15),fg="RoyalBlue2",bg="grey6")
l28.place(x=20,y=150)

abc=random.randrange(1000,9999,1)

def genotp():
    messagebox.showinfo("Rember,Your Otp is",abc)
    print("Your O.T.P. is : ",abc)

b99=Button(f26,text="Generate an O.T.P.",font=('Helvetica',10),fg="White",bg="grey25",command=genotp)
b99.place(x=30,y=190)

e1=Entry(f26,font=(20),width='10',justify='center',show='*')
e1.place(x=230,y=85)

e2=Entry(f26,font=(20),width='10',justify='center',show='*')
e2.place(x=230,y=150)

b98=Button(f26,text="PAY",font=('Helvetica',10),fg="White",bg="grey25",command=paytm)
b98.place(x=230,y=190)


bop.mainloop()