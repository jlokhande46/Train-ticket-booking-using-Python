from tkinter import *
from tkinter import messagebox
import sqlite3
import os

class MyProj:
    def CancelTik(self):
        print(self.password.get())
        with sqlite3.connect('TrainTicketBooking.db') as db:
            c = db.cursor()
        c.execute('SELECT * FROM Temp where key == 2')
        temp_username=c.fetchall()
        print(temp_username[0][0])
        
        c.execute('SELECT * FROM User_details where username == ?',[(temp_username[0][0])])
        temp_password=c.fetchall()
        print(temp_password)
        if (temp_password[0][1] == self.password.get()):
            c.execute('UPDATE User_details SET ticketno = NULL WHERE password = ?',[(temp_password[0][1])])
            c.execute('DELETE FROM Travelling_passengers WHERE ticketno = ?',[(temp_password[0][4])])
            c.execute('DELETE FROM Trainticket_details WHERE ticketno = ?',[(temp_password[0][4])])
            c.execute('DELETE FROM temp WHERE key = 2')
            db.commit()
            root1.destroy()
        else:
            messagebox.showerror(parent=self.m,message="Please enter correct password!!",title="Error")
    def __init__(self,master):
        self.m=master
        self.password=StringVar()
        self.frame = Frame(master, bg="dark slate blue").grid()
        self.labl2 = Label(self.frame, text="     TICKET CANCELLATION", pady=5, font=("Trebuchet MS", 40), bg="dark slate blue", fg="gold",padx=20)
        self.labl2.grid(columnspan=20)
        
        self.labl3 = Label(self.frame, text="  Please Confirm Your Password \n Cancel The Ticket:", fg="goldenrod", pady=5, bg="dark slate blue", font=("Trebuchet MS", 25))
        self.labl3.grid(row=5,column=2,sticky=W)
        self.txt1 = Entry(self.frame, font=('Trebuchet MS', 12, 'bold'),bd=4,bg='white',width=20,textvariable=self.password,show='*')
        self.txt1.place(x=500,y=135)
        self.labl3 = Label(self.frame, text="",bg="dark slate blue").grid(columnspan=20)
        self.but1=Button(self.frame, text='CONFIRM',fg="blue",activebackground="goldenrod",font=("Trebuchet MS", 14),activeforeground="gold", bg="gold", height=1, width=11,command =self.CancelTik)
        self.but1.grid(columnspan=20)
        self.labl3 = Label(self.frame, text="",bg="dark slate blue").grid(columnspan=20)
root1=Tk()
root1.title('RAILWAY TICKET BOOKING SYSTEM')
root1.geometry("725x300")
root1.configure(background='dark slate blue')
mypr=MyProj(root1)
root1.mainloop()            
