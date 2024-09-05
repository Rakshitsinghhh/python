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
values(1,"DalBaatiChurma",140),
(2,"BajraRoti",120),
(3,"DALChawalKutt",130),
(4,"MasalaGatta",140),
(5,"PyaazPanner",100),
(6,"BaiganMasala",130),
(7,"TawaRoti",100),
(8,"DalBanjari",120),
(9,"BajrakaKhichda",150),
(10,"BesankiSabzi",130),
(11,"SevTamatar",130),
(12,"PittodkiSabzi",100);
''')



cur.execute('''create table if not exists gujrati
(NO int(20),
naam char(29),
pric int(4));''')

cur.execute('''insert into gujrati
values(1,'Sev-tamatar',130),
(2,'LasaniyiaBataka',140),
(3,'RasalaBataka',140),
(4,'SevDungri',130),
(5,'DungriBataka',140),
(6,'BaiganMasala',130),
(7,'KadhiPakoda',120),
(8,'BessanGatta',100),
(9,'MungMasala',100),
(10,'VanghareloRotlo4',140),
(11,'BajrinoRotlo',120),
(12,'MakainoRotlo',130)
''')



cur.execute('''create table if not exists multi
(NO int(20),
naam char(29),
pric int(4));''')

cur.execute('''insert into multi
values(1,'pavbhaji',140),
(2,'Bhelchaat',130),
(3,'Pasta',130),
(4,'Noodles',120),
(5,'Alloparatha',110),
(6,'ChooleBhataure',100),
(7,'Burger',130),
(8,'Pizza',140),
(9,'FrenchFries',110),
(10,'CheeseMaggi',100),
(11,'Momos',120),
(12,'Idlesambar',140)
''')

ms=Tk()
ms.title("main menu")
ms.geometry("600x400+150+150")

I99=PhotoImage(file="Media\\DL.png")
llo=Label(ms,image=I99)
llo.place(x=-1.5,y=0)

l2=Label(ms,text="What Would You Like To Have Today",font=('Helvetica',16),fg="RoyalBlue2",bg="grey6")
l2.place(x=80,y=40)

#=================Frame1============#
def sel():
    rd=var.get()
    if rd==1:
        f1.place_forget()
        f2.place(x=0,y=0)
    elif rd==2:
        f1.place_forget()
        f3.place(x=0,y=0)
    elif rd==3:
        f1.place_forget()
        f4.place(x=0,y=0)
    else:
        messagebox.showerror("Sed Lyf","Select Someting")
        
    

f1=Frame(ms,width=600,height=200,bg='grey')
f1.place(x=0,y=100)
I1=PhotoImage(file="Media\\Dext.png")
l1=Label(f1,image=I1)
l1.place(x=-1.5,y=-1.80)



var = IntVar()


r1 = Radiobutton(f1, text="    Rajasthani   ", variable=var, value=1,font=('Helvetica',16),fg="forestgreen",bg="grey6")
r1.place(x=200,y=0)
 
r2 = Radiobutton(f1, text="     Gujratii      ", variable=var, value=2,font=('Helvetica',16),fg="forestgreen",bg="grey6")
r2.place(x=200,y=55)

r3 = Radiobutton(f1, text=" Multi-cusional ", variable=var, value=3,font=('Helvetica',16),fg="forestgreen",bg="grey6")
r3.place(x=200,y=110)

B6=Button(f1,text="Submit",command=sel,font=('Helvetica',12),fg="Yellow",bg="grey6")
B6.place(x=270,y=160)

#=================Frame2============#
f2=Frame(ms,width=600,height=400,bg='grey')
f2.place_forget()
I2=PhotoImage(file="Media\\DL.png")
lr1=Label(f2,image=I2)
lr1.place(x=-1.5,y=-1.80)

def pop():
    f1.place(x=0,y=100)
    f2.place_forget()
    

I23=PhotoImage(file="Media\\back.png")

b999=Button(f2,image=I23,command=pop)
b999.place(x=5,y=5)

#================Rajasthani=============#
lr2=Label(f2,text="Rajasthani",font=('Helvetica',16),fg="Red",bg="grey6")
lr2.place(x=240,y=20)
r1 = IntVar()
r2 = IntVar()
r3 = IntVar()
r4 = IntVar()
r5 = IntVar()
r6 = IntVar()
r7 = IntVar()
r8 = IntVar()
r9 = IntVar()
r10 = IntVar()
r11= IntVar()
r12= IntVar()

Cr1= Checkbutton(f2, text = "Dal Baati Churma",font=('Sans',13),fg="RoyalBlue3", variable = r1,onvalue = 1, offvalue = 0,bg="grey6")
Cr1["cursor"] = "plus"
Cr1.place(x=25,y=70)

Cr2= Checkbutton(f2, text = "  Bajra Roti(x4)   ",font=('Sans',13),fg="RoyalBlue3", variable = r2,onvalue = 1, offvalue = 0,bg="grey6")
Cr2["cursor"] = "plus"
Cr2.place(x=25,y=120)

Cr3= Checkbutton(f2, text = "Dal Chawal Kutt ",font=('Sans',13),fg="RoyalBlue3", variable =r3,onvalue = 1, offvalue = 0,bg="grey6")
Cr3["cursor"] = "plus"
Cr3.place(x=25,y=170)

Cr4= Checkbutton(f2, text = "   Masala Gatta  ",font=('Sans',13),fg="RoyalBlue3", variable =r4,onvalue = 1, offvalue = 0,bg="grey6")
Cr4["cursor"] = "plus"
Cr4.place(x=25,y=220)

Cr5= Checkbutton(f2, text = "  Pyaaz Paneer  ",font=('Sans',13),fg="RoyalBlue3", variable = r5,onvalue = 1, offvalue = 0,bg="grey6")
Cr5["cursor"] = "plus"
Cr5.place(x=25,y=270)

Cr6= Checkbutton(f2, text = "  Baigan Masala ",font=('Sans',13),fg="RoyalBlue3", variable = r6,onvalue = 1, offvalue = 0,bg="grey6")
Cr6["cursor"] = "plus"
Cr6.place(x=25,y=320)

Cr7= Checkbutton(f2, text = "  Tawa roti (x4)  ",font=('Sans',13),fg="RoyalBlue3", variable =r7,onvalue = 1, offvalue = 0,bg="grey6")
Cr7["cursor"] = "plus"
Cr7.place(x=330,y=70)

Cr8= Checkbutton(f2, text = "     Dal Banjari      ",font=('Sans',13),fg="RoyalBlue3", variable =r8,onvalue = 1, offvalue = 0,bg="grey6")
Cr8.place(x=330,y=120)

Cr9= Checkbutton(f2, text = " Bajra ka Khichda",font=('Sans',13),fg="RoyalBlue3", variable =r9,onvalue = 1, offvalue = 0,bg="grey6")
Cr9["cursor"] = "plus"
Cr9.place(x=330,y=170)

Cr10= Checkbutton(f2, text = "  Besan ki Sabzi  ",font=('Sans',13),fg="RoyalBlue3", variable =r10,onvalue = 1, offvalue = 0,bg="grey6")
Cr10["cursor"] = "plus"
Cr10.place(x=330,y=220)

Cr11= Checkbutton(f2, text = "    Sev Tamatar   ",font=('Sans',13),fg="RoyalBlue3", variable = r11,onvalue = 1, offvalue = 0,bg="grey6")
Cr11["cursor"] = "plus"
Cr11.place(x=330,y=270)

Cr12= Checkbutton(f2, text = "   Pittod ki sabzi   ",font=('Sans',13),fg="RoyalBlue3", variable = r12,onvalue = 1, offvalue = 0,bg="grey6")
Cr12["cursor"] = "plus"
Cr12.place(x=330,y=320)
#----------------------------------------------------#
Rj1=Label(f2,text ="140",font=('Sans',13),fg="Green",bg="grey6")
Rj1.place(x=250,y=70)

Rj1=Label(f2,text ="120",font=('Sans',13),fg="Green",bg="grey6")
Rj1.place(x=250,y=125)

Rj1=Label(f2,text ="130",font=('Sans',13),fg="Green",bg="grey6")
Rj1.place(x=250,y=175)

Rj1=Label(f2,text ="140",font=('Sans',13),fg="Green",bg="grey6")
Rj1.place(x=250,y=225)

Rj1=Label(f2,text ="100",font=('Sans',13),fg="Green",bg="grey6")
Rj1.place(x=250,y=275)

Rj1=Label(f2,text ="130",font=('Sans',13),fg="Green",bg="grey6")
Rj1.place(x=250,y=325)

Rj1=Label(f2,text ="100",font=('Sans',13),fg="Green",bg="grey6")
Rj1.place(x=540,y=75)

Rj1=Label(f2,text ="120",font=('Sans',13),fg="Green",bg="grey6")
Rj1.place(x=540,y=125)

Rj1=Label(f2,text ="150",font=('Sans',13),fg="Green",bg="grey6")
Rj1.place(x=540,y=175)

Rj1=Label(f2,text ="130",font=('Sans',13),fg="Green",bg="grey6")
Rj1.place(x=540,y=225)

Rj1=Label(f2,text ="130",font=('Sans',13),fg="Green",bg="grey6")
Rj1.place(x=540,y=275)

Rj1=Label(f2,text ="100",font=('Sans',13),fg="Green",bg="grey6")
Rj1.place(x=540,y=325)


def suresh():
    rj1=r1.get()
    rj2=r2.get()
    rj3=r3.get()
    rj4=r4.get()
    rj5=r5.get()
    rj6=r6.get()
    rj7=r7.get()
    rj8=r8.get()
    rj9=r9.get()
    rj10=r10.get()
    rj11=r11.get()
    rj12=r12.get()
    
    toop=0
    if rj1==1:
        cur.execute("select distinct pric from rajasthani where naam='DalBaatiChurma';")
        bl1=cur.fetchall()
        ss1=bl1[0]
        pol1=int(ss1[0])
        toop=toop+pol1
    else:
        pass
    if rj2==1:
        cur.execute("select distinct pric from rajasthani where naam='BajraRoti';")
        bl2=cur.fetchall()
        ss2=bl2[0]
        pol2=int(ss2[0])
        toop=toop+pol2
    else:
        pass
    if rj3==1: 
        cur.execute("select distinct pric from rajasthani where naam='DALChawalKutt';")
        bl3=cur.fetchall()
        ss3=bl3[0]
        pol3=int(ss3[0])
        toop=toop+pol3
    else:
        pass
    if rj4==1:
        cur.execute("select distinct pric from rajasthani where naam='MasalaGatta';")
        bl4=cur.fetchall()
        ss4=bl4[0]
        pol4=int(ss4[0])
        toop=toop+pol4
    else:
        pass
    if rj5==1:
        cur.execute("select distinct pric from rajasthani where naam='PyaazPanner';")
        bl5=cur.fetchall()
        ss5=bl5[0]
        pol5=int(ss5[0])
        toop=toop+pol5
    else:
        pass
    if rj6==1:
        cur.execute("select distinct pric from rajasthani where naam='BaiganMasala'")
        bl6=cur.fetchall()
        ss6=bl6[0]
        pol6=int(ss6[0])
        toop=toop+pol6
    else:
        pass
    if rj7==1:
        cur.execute("select distinct pric from rajasthani where naam='TawaRoti';")
        bl7=cur.fetchall()
        ss7=bl7[0]
        pol7=int(ss7[0])
        toop=toop+pol7
    else:
        pass
    if rj8==1:
        cur.execute("select distinct pric from rajasthani where naam='DalBanjari';")
        bl8=cur.fetchall()
        ss8=bl8[0]
        pol8=int(ss8[0])
        toop=toop+pol8
    else:
        pass
    if rj9==1:
        bl9=cur.fetchall()
        ss9=bl9[0]
        pol9=int(ss9[0])
        toop=toop+pol9
    else:
        pass
    if rj10==1:
        cur.execute("select distinct pric from rajasthani where naam='BesankiSabzi';")
        bl10=cur.fetchall()
        ss10=bl10[0]
        pol10=int(ss10[0])
        toop=toop+pol10
    else:
        pass
    if rj11==1:
        cur.execute("select distinct pric from rajasthani where naam='SevTamatar';")
        bl11=cur.fetchall()
        ss11=bl12[0]
        pol11=int(ss11[0])
        toop=toop+pol11
    else:
        pass
    if rj12==1:
        cur.execute("select distinct pric from rajasthani where naam='PittodkiSabzi';")
        bl12=cur.fetchall()
        ss12=bl12[0]
        pol12=int(ss12[0])
        toop=toop+pol12
        
    else:
        pass
    
    messagebox.showinfo("Thanks","Your Order has been recieved")
  
    cur.execute('''create table if not exists billing
    (Price int(5));''')
    print(toop)
    ms.destroy()
    import Pb
Rj1=Button(f2,text="Submit",font=('Sans',10),fg="yellow",bg="grey6",command=suresh)
Rj1.place(x=270,y=360)
    



#=================Frame3============#
f3=Frame(ms,width=600,height=400,bg='grey')
f3.place_forget()
I3=PhotoImage(file="Media\\DL.png")
lg1=Label(f3,image=I3)
lg1.place(x=-1.5,y=-1.80)

def pop3():
    f1.place(x=0,y=100)
    f3.place_forget()
    

I24=PhotoImage(file="Media\\back.png")

b999=Button(f3,image=I24,command=pop3)
b999.place(x=5,y=5)

#================Gujutari=============#
lg2=Label(f3,text="Gujrati",font=('Helvetica',20),fg="Red",bg="grey6")
lg2.place(x=250,y=15)

g1 = IntVar()
g2 = IntVar()
g3 = IntVar()
g4 = IntVar()
g5 = IntVar()
g6 = IntVar()
g7 = IntVar()
g8 = IntVar()
g9 = IntVar()
g10 = IntVar()
g11= IntVar()
g12= IntVar()

Cg1= Checkbutton(f3, text = "   Sev - Tameta   ",font=('Sans',13),fg="RoyalBlue3", variable = g1,onvalue = 1, offvalue = 0,bg="grey6")
Cg1["cursor"] = "plus"
Cg1.place(x=25,y=70)

Cg2= Checkbutton(f3, text = "Lasaniyia Bataka",font=('Sans',13),fg="RoyalBlue3", variable = g2,onvalue = 1, offvalue = 0,bg="grey6")
Cg2["cursor"] = "plus"
Cg2.place(x=25,y=120)

Cg3= Checkbutton(f3, text = " Rasala   Bataka",font=('Sans',13),fg="RoyalBlue3", variable =g3,onvalue = 1, offvalue = 0,bg="grey6")
Cg3["cursor"] = "plus"
Cg3.place(x=25,y=170)

Cg4= Checkbutton(f3, text = "   Sev    Dungri   ",font=('Sans',13),fg="RoyalBlue3", variable =g4,onvalue = 1, offvalue = 0,bg="grey6")
Cg4["cursor"] = "plus"
Cg4.place(x=25,y=220)

Cg5= Checkbutton(f3, text = "  Dungri  Bataka ",font=('Sans',13),fg="RoyalBlue3", variable = g5,onvalue = 1, offvalue = 0,bg="grey6")
Cg5["cursor"] = "plus"
Cg5.place(x=25,y=270)

Cg6= Checkbutton(f3, text = "  Baigan Masala ",font=('Sans',13),fg="RoyalBlue3", variable = g6,onvalue = 1, offvalue = 0,bg="grey6")
Cg6["cursor"] = "plus"
Cg6.place(x=25,y=320)

Cg7= Checkbutton(f3, text = "  Kadhi  Pakoda  ",font=('Sans',13),fg="RoyalBlue3", variable =g7,onvalue = 1, offvalue = 0,bg="grey6")
Cg7["cursor"] = "plus"
Cg7.place(x=330,y=70)

Cg8= Checkbutton(f3, text = "   Besan  Gatta    ",font=('Sans',13),fg="RoyalBlue3", variable =g8,onvalue = 1, offvalue = 0,bg="grey6")
Cg8.place(x=330,y=120)

Cg9= Checkbutton(f3, text = "    Mung  Masala ",font=('Sans',13),fg="RoyalBlue3", variable =g9,onvalue = 1, offvalue = 0,bg="grey6")
Cg9["cursor"] = "plus"
Cg9.place(x=330,y=170)

Cg10= Checkbutton(f3, text = "Vangharelo Rotlo4",font=('Sans',13),fg="RoyalBlue3", variable =g10,onvalue = 1, offvalue = 0,bg="grey6")
Cg10["cursor"] = "plus"
Cg10.place(x=330,y=220)

Cg11= Checkbutton(f3, text = " Bajrino  Rotlo (x4)  ",font=('Sans',13),fg="RoyalBlue3", variable = g11,onvalue = 1, offvalue = 0,bg="grey6")
Cg11["cursor"] = "plus"
Cg11.place(x=330,y=270)

Cg12= Checkbutton(f3, text = "Makaino  Rotlo (x4) ",font=('Sans',13),fg="RoyalBlue3", variable = g12,onvalue = 1, offvalue = 0,bg="grey6")
Cg12["cursor"] = "plus"
Cg12.place(x=330,y=320)
#----------------------------------------------------#
Gl3=Label(f3,text ="130",font=('Sans',13),fg="Green",bg="grey6")
Gl3.place(x=250,y=70)

Gl3=Label(f3,text ="140",font=('Sans',13),fg="Green",bg="grey6")
Gl3.place(x=250,y=125)

Gl3=Label(f3,text ="140",font=('Sans',13),fg="Green",bg="grey6")
Gl3.place(x=250,y=175)

Gl3=Label(f3,text ="130",font=('Sans',13),fg="Green",bg="grey6")
Gl3.place(x=250,y=225)

Gl3=Label(f3,text ="140",font=('Sans',13),fg="Green",bg="grey6")
Gl3.place(x=250,y=275)

Gl3=Label(f3,text ="130",font=('Sans',13),fg="Green",bg="grey6")
Gl3.place(x=250,y=325)

Gl3=Label(f3,text ="120",font=('Sans',13),fg="Green",bg="grey6")
Gl3.place(x=540,y=75)

Gl3=Label(f3,text ="100",font=('Sans',13),fg="Green",bg="grey6")
Gl3.place(x=540,y=125)

Gl3=Label(f3,text ="100",font=('Sans',13),fg="Green",bg="grey6")
Gl3.place(x=540,y=175)

Gl3=Label(f3,text ="140",font=('Sans',13),fg="Green",bg="grey6")
Gl3.place(x=540,y=225)

Gl3=Label(f3,text ="120",font=('Sans',13),fg="Green",bg="grey6")
Gl3.place(x=540,y=275)

Gl3=Label(f3,text ="130",font=('Sans',13),fg="Green",bg="grey6")
Gl3.place(x=540,y=325)

def ramesh():
    gv1=g1.get()
    gv2=g2.get()
    gv3=g3.get()
    gv4=g4.get()
    gv5=g5.get()
    gv6=g6.get()
    gv7=g7.get()
    gv8=g8.get()
    gv9=g9.get()
    gv10=g10.get()
    gv11=g11.get()
    gv12=g12.get()
    toop=0
    if gv1==1:
        cur.execute('select distinct pric from gujrati where naam="Sev-Tamatar";')
        bl1=cur.fetchall()
        ss1=bl1[0]
        pol1=int(ss1[0])
        toop=toop+pol1
    else:
        pass
    if gv2==1:
        cur.execute('select distinct pric from gujrati where naam="LasaniyiaBataka";')
        bl2=cur.fetchall()
        ss2=bl2[0]
        pol2=int(ss2[0])
        toop=toop+pol2
    else:
        pass
    if gv3==1: 
        cur.execute('select distinct pric from gujrati where naam="RasalaBataka";')
        bl3=cur.fetchall()
        ss3=bl3[0]
        pol3=int(ss3[0])
        toop=toop+pol3
    else:
        pass
    if gv4==1:
        cur.execute('select distinct pric from gujrati where naam="SevDungri";')
        bl4=cur.fetchall()
        ss4=bl4[0]
        pol4=int(ss4[0])
        toop=toop+pol4
    else:
        pass
    if gv5==1:
        cur.execute('select distinct pric from gujrati where naam="DungriBataka";')
        bl5=cur.fetchall()
        ss5=bl5[0]
        pol5=int(ss5[0])
        toop=toop+pol5
        
    else:
        pass
    if gv6==1:
        cur.execute('select distinct pric from gujrati where naam="BaiganMasala";')
        bl6=cur.fetchall()
        ss6=bl6[0]
        pol6=int(ss6[0])
        toop=toop+pol6
    else:
        pass
    if gv7==1:
        cur.execute('select distinct pric from gujrati where naam="KadhiPakoda";')
        bl7=cur.fetchall()
        ss7=bl7[0]
        pol7=int(ss7[0])
        toop=toop+pol7
    else:
        pass
    if gv8==1:
        cur.execute('select distinct pric from gujrati where naam="BessanGatta";')
        bl8=cur.fetchall()
        ss8=bl8[0]
        pol8=int(ss8[0])
        toop=toop+pol8
    else:
        pass
    if gv9==1:
        cur.execute('select distinct pric from gujrati where naam="MungMasala";')
        bl9=cur.fetchall()
        ss9=bl9[0]
        pol9=int(ss9[0])
        toop=toop+pol9
    else:
        pass
    if gv10==1:
        cur.execute('select distinct pric from gujrati where naam="VanghareloRotlo4";')
        bl10=cur.fetchall()
        ss10=bl10[0]
        pol10=int(ss10[0])
        toop=toop+pol10
    else:
        pass
    if gv11==1:
        cur.execute('select distinct pric from gujrati where naam="BajrinoRotlo";')
        bl11=cur.fetchall()
        ss11=bl11[0]
        pol11=int(ss11[0])
        toop=toop+pol11
    else:
        pass
    if gv12==1:
        cur.execute('select distinct pric from gujrati where naam="MakainoRotlo";')
        bl12=cur.fetchall()
        ss12=bl12[0]
        pol12=int(ss12[0])
        toop=toop+pol12
    else:
        pass

    
    messagebox.showinfo("Thanks","Your Order has been recieved")
    print(toop)
    ms.destroy()
    import Pb
    
Gb1=Button(f3,text="Submit",font=('Sans',10),fg="yellow",bg="grey6",command=ramesh)
Gb1.place(x=270,y=360)
#=================Frame4============#
f4=Frame(ms,width=600,height=400,bg='grey')
f4.place_forget()
I4=PhotoImage(file="Media\\DL.png")
li1=Label(f4,image=I4)
li1.place(x=-1.5,y=-1.80)

def pop4():
    f1.place(x=0,y=100)
    f4.place_forget()
    

I25=PhotoImage(file="Media\\back.png")

b999=Button(f4,image=I25,command=pop4)
b999.place(x=5,y=5)
#================Multi-cusional=============#

li2=Label(f4,text="Multi-cusional",font=('Helvetica',16),fg="Red",bg="grey6")
li2.place(x=220,y=20)

m1 = IntVar()
m2 = IntVar()
m3 = IntVar()
m4 = IntVar()
m5 = IntVar()
m6 = IntVar()
m7 = IntVar()
m8 = IntVar()
m9 = IntVar()
m10 = IntVar()
m11 = IntVar()
m12 = IntVar()
 
Cm1= Checkbutton(f4, text = "     Pav-Bhaji      ",font=('Sans',13),fg="RoyalBlue3", variable = m1,onvalue = 1, offvalue = 0,bg="grey6")
Cm1["cursor"] = "plus"
Cm1.place(x=25,y=70)

Cm2= Checkbutton(f4, text = "    Bhel Chaat    ",font=('Sans',13),fg="RoyalBlue3", variable = m2,onvalue = 1, offvalue = 0,bg="grey6")
Cm2["cursor"] = "plus"
Cm2.place(x=25,y=120)

Cm3= Checkbutton(f4, text = "        Pasta         ",font=('Sans',13),fg="RoyalBlue3", variable =m3,onvalue = 1, offvalue = 0,bg="grey6")
Cm3["cursor"] = "plus" 
Cm3.place(x=25,y=170)

Cm4= Checkbutton(f4, text = "       Noddles      ",font=('Sans',13),fg="RoyalBlue3", variable =m4,onvalue = 1, offvalue = 0,bg="grey6")
Cm4["cursor"] = "plus"
Cm4.place(x=25,y=220)

Cm5= Checkbutton(f4, text = "     Allo Paratha  ",font=('Sans',13),fg="RoyalBlue3", variable = m5,onvalue = 1, offvalue = 0,bg="grey6")
Cm5["cursor"] = "plus"
Cm5.place(x=25,y=270)

Cm6= Checkbutton(f4, text = " Choole Bhature ",font=('Sans',13),fg="RoyalBlue3", variable = m6,onvalue = 1, offvalue = 0,bg="grey6")
Cm6["cursor"] = "plus"
Cm6.place(x=25,y=320)

Cm7= Checkbutton(f4, text = "         Burger        ",font=('Sans',13),fg="RoyalBlue3", variable =m7,onvalue = 1, offvalue = 0,bg="grey6")
Cm7["cursor"] = "plus" 
Cm7.place(x=330,y=70)

Cm8= Checkbutton(f4, text = "         Pizaa         ",font=('Sans',13),fg="RoyalBlue3", variable =m8,onvalue = 1, offvalue = 0,bg="grey6")
Cm8.place(x=330,y=120)

Cm9= Checkbutton(f4, text = "    French Fries    ",font=('Sans',13),fg="RoyalBlue3", variable =m9,onvalue = 1, offvalue = 0,bg="grey6")
Cm9["cursor"] = "plus"
Cm9.place(x=330,y=170)

Cm10= Checkbutton(f4, text = "   Cheese Maggi ",font=('Sans',13),fg="RoyalBlue3", variable =m10,onvalue = 1, offvalue = 0,bg="grey6")
Cm10["cursor"] = "plus"
Cm10.place(x=330,y=220)

Cm11= Checkbutton(f4, text = "        Momos       ",font=('Sans',13),fg="RoyalBlue3", variable = m11,onvalue = 1, offvalue = 0,bg="grey6")
Cm11["cursor"] = "plus"
Cm11.place(x=330,y=270)

Cm12= Checkbutton(f4, text = "     Idle sambar    ",font=('Sans',13),fg="RoyalBlue3", variable = m12,onvalue = 1, offvalue = 0,bg="grey6")
Cm12["cursor"] = "plus"
Cm12.place(x=330,y=320)
#----------------------------------------------------#

Mc=Label(f4,text ="140",font=('Sans',13),fg="Green",bg="grey6")
Mc.place(x=250,y=70)

Mc=Label(f4,text ="130",font=('Sans',13),fg="Green",bg="grey6")
Mc.place(x=250,y=125)

Mc=Label(f4,text ="130",font=('Sans',13),fg="Green",bg="grey6")
Mc.place(x=250,y=175)

Mc=Label(f4,text ="120",font=('Sans',13),fg="Green",bg="grey6")
Mc.place(x=250,y=225)

Mc=Label(f4,text ="110",font=('Sans',13),fg="Green",bg="grey6")
Mc.place(x=250,y=275)

Mc=Label(f4,text ="100",font=('Sans',13),fg="Green",bg="grey6")
Mc.place(x=250,y=325)

Mc=Label(f4,text ="130",font=('Sans',13),fg="Green",bg="grey6")
Mc.place(x=540,y=75)

Mc=Label(f4,text ="140",font=('Sans',13),fg="Green",bg="grey6")
Mc.place(x=540,y=125)

Mc=Label(f4,text ="110",font=('Sans',13),fg="Green",bg="grey6")
Mc.place(x=540,y=175)

Mc=Label(f4,text ="100",font=('Sans',13),fg="Green",bg="grey6")
Mc.place(x=540,y=225)

Mc=Label(f4,text ="120",font=('Sans',13),fg="Green",bg="grey6")
Mc.place(x=540,y=275)

Mc=Label(f4,text ="140",font=('Sans',13),fg="Green",bg="grey6")
Mc.place(x=540,y=325)


def himesh():
    mv1=m1.get()
    mv2=m2.get()
    mv3=m3.get()
    mv4=m4.get()
    mv5=m5.get()
    mv6=m6.get()
    mv7=m7.get()
    mv8=m8.get()
    mv9=m9.get()
    mv10=m10.get()
    mv11=m11.get()
    mv12=m12.get()
    bill=()
    toop=0
    if mv1==1:
        cur.execute('select distinct pric from multi where naam="PavBhaji";')
        bl1=cur.fetchall()
        ss1=bl1[0]
        pol1=int(ss1[0])
        toop=toop+pol1
    else:
        pass
    if mv2==1:
        cur.execute('select distinct pric from multi where naam="Bhelchaat";')
        bl2=cur.fetchall()
        ss2=bl2[0]
        pol2=int(ss2[0])
        toop=toop+pol2
    else:
        pass
    if mv3==1: 
        cur.execute('select distinct pric from multi where naam="Pasta";')
        bl3=cur.fetchall()
        ss3=bl3[0]
        pol3=int(ss3[0])
        toop=toop+pol3
    else:
        pass
    if mv4==1:
        cur.execute('select distinct pric from multi where naam="Noodles";')
        bl4=cur.fetchall()
        ss4=bl4[0]
        pol4=int(ss4[0])
        toop=toop+pol4
    else:
        pass
    if mv5==1:
        cur.execute('select distinct pric from multi where naam="AlloParatha";')
        bl5=cur.fetchall()
        ss5=bl5[0]
        pol5=int(ss5[0])
        toop=toop+pol5
    else:
        pass
    if mv6==1:
        cur.execute('select distinct pric from multi where naam="ChooleBhataure";')
        bl6=cur.fetchall()
        ss6=bl6[0]
        pol6=int(ss6[0])
        toop=toop+pol6
    else:
        pass
    if mv7==1:
        cur.execute('select distinct pric from multi where naam="Burger";')
        bl7=cur.fetchall()
        ss7=bl7[0]
        pol7=int(ss7[0])
        toop=toop+pol7
    else:
        pass
    if mv8==1:
        cur.execute('select distinct pric from multi where naam="Pizza";')
        bl8=cur.fetchall()
        ss8=bl8[0]
        pol8=int(ss8[0])
        toop=toop+pol8
    else:
        pass
    if mv9==1:
        cur.execute('select distinct pric from multi where naam="FrenchFries";')
        bl9=cur.fetchall()
        ss9=bl9[0]
        pol9=int(ss9[0])
        toop=toop+pol9
    else:
        pass
    if mv10==1:
        cur.execute('select distinct pric from multi where naam="CheeseMaggi";')
        bl10=cur.fetchall()
        ss10=bl10[0]
        pol10=int(ss10[0])
        toop=toop+pol10
    else:
        pass
    if mv11==1:
        cur.execute('select distinct pric from multi where naam="Momos";')
        bl11=cur.fetchall()
        ss11=bl11[0]
        pol11=int(ss11[0])
        toop=toop+pol11
    
    
    else:
        pass
    if mv12==1:
        cur.execute('select distinct pric from multi where naam="Idlesambar";')
        bl12=cur.fetchall()
        ss12=bl12[0]
        pol12=int(ss12[0])
        toop=toop+pol12
        
        
    else:
        pass


    
    messagebox.showinfo("Thanks","Your Order has been recieved")
    print(toop)
    ms.destroy()
    import Pb
Mi1=Button(f4,text="Submit",font=('Sans',10),fg="yellow",bg="grey6",command=himesh)
Mi1.place(x=270,y=360)




ms.mainloop()
