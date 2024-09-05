from tkinter import *
import webbrowser



hp=Tk()
hp.config(bg="Cyan")
hp.geometry('250x350+350+100')
hp.title("Help")

l1=Label(hp,text='HELP CORNER',font=("verdana",20), bg="red",fg="grey24")
l1.place(x=4,y=30)

l2=Label(hp,text='''For any query
and problem,
feel free
to email
us.We will
appreciate
your suggestions''',bg="lightsalmon",fg="grey24")
l2.place(x=70,y=100)

def opn():
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=CllgCJZZQlnQLPCNgszdjxmJDckLJNNKWqFHvMnRvBXjWqZrfmHwDZqcsftVCPNNgMlwnNxHnwL")
def opn1():
    webbrowser.open('https://mail.google.com/mail/u/0/#inbox?compose=XBcJlDMdDMZscKLxwjzBPXNQTQKbBfpVgmXZqVVNVQlGMdbFtHBXTrdmndQrFTJWLwkNZGchbdcqZcmb')
    
b1=Button(hp,text='''@Singhrakshit739@gmail.com''',font=('verdana',7),bg="RoyalBlue1",fg="grey24",command=opn)
b1.place(x=25,y=260)

b2=Button(hp,text='''@Rushilchittora@gmail.com''',font=('verdana',7),bg="RoyalBlue1",fg="grey24",command=opn)
b2.place(x=35,y=290)


hp.mainloop()