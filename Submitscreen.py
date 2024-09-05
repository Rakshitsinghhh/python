from tkinter import *  
  
sw= Tk()
sw.title("Billing")
sw.geometry("600x400+150+150")  

I99=PhotoImage(file="Media\\DL.png")
llo=Label(sw,image=I99)
llo.place(x=-1.5,y=0)

l1=Label(sw,text="Thanks For Using Our Software",font=('Helvetica',20),fg="RoyalBlue2",bg="lightpink")
l1.place(x=105,y=35)

f25=Frame(sw,height=250,width=400,bg="lightblue")
f25.place(x=100,y=100)

l25=Label(f25,text="How Would You like to Eat",font=('Helvetica',15),fg="RoyalBlue2",bg="lightpink")
l25.place(x=43,y=10)

l26=Label(f25,text="Enter Your Choice",font=('Helvetica',15),fg="RoyalBlue2",bg="lightpink")
l26.place(x=90,y=100)



var = IntVar()

r1 = Radiobutton(f25, text=" Delivery ", variable=var, value=1,font=('Helvetica',10),fg="RoyalBlue2",bg="mintcream")
r1.place(x=30,y=170)
 
r2 = Radiobutton(f25, text=" Take Away ", variable=var, value=2,font=('Helvetica',10),fg="RoyalBlue2",bg="mintcream")
r2.place(x=225,y=170)

def why():
    rd=var.get()
    if rd==1:
        f25.place_forget()
        f26.place(x=100,y=100)
    else:
        f25.place_forget()
        f27.place(x=100,y=100)

B6=Button(f25,text="Submit",command=why,font=('Helvetica',12),fg="grey6",bg="mintcream")
B6.place(x=145,y=205)
#==============================================================================================================

f26=Frame(sw,height=250,width=400,bg="lightblue")
f26.place_forget()

l28=Label(f26,text="How Would You like to Pay",font=('Helvetica',15),fg="RoyalBlue2",bg="lightpink")
l28.place(x=43,y=10)

l29=Label(f26,text="Enter Your Choice",font=('Helvetica',15),fg="RoyalBlue2",bg="lightpink")
l29.place(x=100,y=100)



var2 = IntVar()

r1 = Radiobutton(f26, text=" Cash On Delivery ", variable=var, value=1,font=('Helvetica',10),fg="RoyalBlue2",bg="mintcream")
r1.place(x=30,y=170)
 
r2 = Radiobutton(f26, text=" Net Banking ", variable=var, value=2,font=('Helvetica',10),fg="RoyalBlue2",bg="mintcream")
r2.place(x=225,y=170)

def pay():
    rd2=var2.get()
    if rd2==1:    
        pass
    else:
        sw.destroy()
        import bill3
B6=Button(f26,text="Submit",command=pay,font=('Helvetica',12),fg="grey6",bg="mintcream")
B6.place(x=160,y=205)

f27=Frame(sw,height=250,width=400,bg="lightblue")
f27.place_forget()

l30=Label(f27,text="Your Order will get Ready",font=('Helvetica',15),fg="RoyalBlue2",bg="lightpink")
l30.place(x=60,y=10)

l301=l30=Label(f27,text="In 30 minutes",font=('Helvetica',15),fg="RoyalBlue2",bg="lightpink")
l301.place(x=120,y=50)

l31=Label(f27,text="Kindly Be Present :)",font=('Helvetica',15),fg="RoyalBlue2",bg="lightpink")
l31.place(x=80,y=150)

sw.mainloop()
