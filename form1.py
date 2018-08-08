from tkinter import*
from tkinter import messagebox
import sqlite3
import os

class Proj:

    def new_user(self):
        with sqlite3.connect('TrainTicketBooking.db') as db:
            a = db.cursor()

        insert = 'INSERT INTO User_details (username,password,email,mobile,ticketno) VALUES(?,?,?,?,NULL)'
        a.execute(insert,[(self.username.get()),(self.password.get()),(self.email.get()),(self.mobile.get())])
        db.commit()
        self.master.destroy()
        os.system("python login1.py")

    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.email = StringVar()
        self.mobile = StringVar()
        self.frame = Frame(self.master,bg="dark slate blue").grid()
        Label(self.frame, text="          REGISTRATION   FORM          ", font=("Trebuchet MS", 40, "bold"), bg="dark slate blue", fg="gold").grid(columnspan=3)
        Label(self.frame,text="USERNAME :",bg="dark slate blue", fg="spring green", font=("Trebuchet MS", 20,"bold"),padx=20,pady=20).grid(row=3,column=0,sticky=E)
        Label(self.frame,text="PASSWORD :",bg="dark slate blue", fg="spring green", font=("Trebuchet MS", 20,"bold"),padx=20,pady=20).grid(row=5,column=0,sticky=E)
        Label(self.frame, text="EMAIL ID :",bg="dark slate blue" ,fg="spring green", font=("Trebuchet MS", 20, "bold"),padx=20,pady=20).grid(row=7, column=0, sticky=E)
        Label(self.frame, text="MOBILE NO. :",bg="dark slate blue", fg="spring green", font=("Trebuchet MS", 20, "bold"),padx=20,pady=20).grid(row=9, column=0, sticky=E)
        Entry(self.frame, textvariable=self.username, bd=5,width=25).grid(row=3, column=1, sticky=E)
        Entry(self.frame, textvariable=self.password, bd=5,show='*',width=25).grid(row=5, column=1, sticky=E)
        Entry(self.frame, textvariable=self.email, bd=5,width=25).grid(row=7, column=1, sticky=E)
        Entry(self.frame, textvariable=self.mobile, bd=5,width=25).grid(row=9, column=1, sticky=E)
        Label(self.frame, text="", bg="dark slate blue").grid(columnspan=3)
        self.but1=Button(self.frame, text="SUBMIT", font=("Trebuchet MS", 18), relief=RAISED, bg="goldenrod", fg="dark slate blue",padx=30,
                        pady=5, activebackground="springgreen", command=self.database,activeforeground="goldenrod")
        self.but1.grid(columnspan=3)
    
    def database(self):
        if(self.username.get()=="" or self.password.get()=="" or self.email.get()=="" or self.mobile.get()==""):
            messagebox.showerror(parent=self.master,message="Please fill all the entries!!",title="Error")
        elif(len(self.mobile.get())!=10):
            messagebox.showerror(parent=self.master,message="Please enter valid number!!",title="Error")
        elif not (self.email.get().endswith('.com') or self.email.get().endswith('.in')):
            messagebox.showerror(parent=self.master,message="Please enter valid Email ID!!",title="Error")
        elif not('@' in self.email.get()):
            messagebox.showerror(parent=self.master,message="Please enter valid Email ID!!",title="Error")
        else :
            self.new_user()

if __name__ == '__main__':
    root=Tk()
    root.title('RAILWAY TICKET BOOKING SYSTEM')
    root.configure(background='dark slate blue')
    root.geometry('950x500')
    mypr=Proj(root)
    root.mainloop()
