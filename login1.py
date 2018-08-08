from tkinter import*
from tkinter import messagebox as ms
import sqlite3
import os
with sqlite3.connect('TrainTicketBooking.db') as db:
    a = db.cursor()

class main:

    def __init__(self,master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.widgets()

    def Login(self):

        with sqlite3.connect('TrainTicketBooking.db') as db:
            a = db.cursor()

        user = ('SELECT * FROM User_details WHERE username = ? and password = ?')
        a.execute(user,[(self.username.get()),(self.password.get())])
        result = a.fetchall()

        if result:
            a.execute('INSERT INTO Temp (temp,key) VALUES(?,2)',[(self.username.get())])
            db.commit()
            self.username.set('')
            self.password.set('')
            root.destroy()
            os.system("python source_destination1.py")

        else:
            ms.showerror('Oops!','re-enter your password or username')
            self.username.set('')
            self.password.set('')

    def SignUp(self):
        self.master.destroy()
        os.system("python form1.py")

    def widgets(self):
        self.frame=Frame(self.master,bg="dark slate blue")
        Label(self.frame,text="WELCOME TO", font=("Trebuchet MS", 40,"bold"), bg="dark slate blue", fg="gold",padx=10).grid(columnspan=4)
        Label(self.frame, text="RAIL-TICKET BOOKING SYSTEM", font=("Trebuchet MS", 40, "bold"), bg="dark slate blue", fg="gold",padx=10).grid(columnspan=4)
        Label(self.frame, text="      CUSTOMER LOGIN", font=("Trebuchet MS", 25, "bold"), bg="dark slate blue", fg="spring green",pady=25).grid(columnspan=3)
        Label(self.frame, text="USERNAME:", font=("Trebuchet MS", 20, "bold"), bg="dark slate blue", fg="spring green",padx=-20,pady=10).grid(row=4,column=0,sticky=E)
        Label(self.frame, text="PASSWORD:", font=("Trebuchet MS", 20, "bold"), bg="dark slate blue", fg="spring green",padx=-20,pady=10).grid(row=5,column=0,sticky=E)
        Entry(self.frame,textvariable=self.username,bd= 5,font = ('',12)).place(x=400,y=255)
        Entry(self.frame,textvariable=self.password, bd=5,font = ('',12),show="*").place(x=400,y=310)
        Label(self.frame, text="", bg="dark slate blue").grid(columnspan=3)
        Button(self.frame,text="Login", font=("Century Gothic", 15, "bold"), relief=RAISED, bg="goldenrod", fg="dark slate blue",
               padx=30, pady=10, activebackground="white", activeforeground="black", command=self.Login).grid(row=7,column=0,sticky=E)
        Button(self.frame, text="Sign Up", font=("Century Gothic", 15, "bold"), relief=RAISED, bg="goldenrod", fg="dark slate blue",
               padx=30, pady=10, activebackground="white", activeforeground="black", command=self.SignUp).grid( row=7,column=2,sticky=S)
        Label(self.frame, text="", bg="dark slate blue").grid(columnspan=3)
        self.frame.grid()


if __name__ == '__main__':
    root=Tk()
    root.title('RAILWAY TICKET BOOKING SYSTEM')
    root.geometry('765x450')
    main(root)
    root.mainloop()
