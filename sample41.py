#this page is of the final ticket generation. This code is copied in sample3.py for establishing connection.
from tkinter import *
from tkinter import messagebox
import random
import time
import datetime
import sqlite3

with sqlite3.connect('TrainTicketBooking.db') as db:
    c = db.cursor()

class MyProj:
    def quit(self):
        root1.destroy()
        
    def trainticket(self):
        #Temp_1=StringVar()
        c.execute('SELECT * FROM Temp WHERE key==2')
        temp_det=c.fetchall()
        print(temp_det)
        
        c.execute('SELECT * FROM User_details WHERE ticketno == ?',[(int(temp_det[0][0]))])
        temp_usr=c.fetchall()
        print(temp_usr)
        
        c.execute('SELECT * FROM Travelling_passengers WHERE ticketno == ?',[(int(temp_det[0][0]))])
        temp_pas=c.fetchall()
        print(temp_pas)
        #print(len(temp_pas))
        
        c.execute('SELECT * FROM Trainticket_details WHERE ticketno == ?',[(int(temp_det[0][0]))])
        temp_ticket=c.fetchall()
        print(temp_ticket)
        
        c.execute('SELECT * FROM Train_details WHERE trainno == ?',[(int(temp_ticket[0][2]))])
        temp_train=c.fetchall()
        print(temp_train)
        c.execute('DELETE FROM temp WHERE key = 2')
        db.commit()
        DateOfOrder=StringVar()
        DateOfOrder.set(time.strftime("%d/%m/%Y"))

         
        #Temp_1 = '\n Train No.: ' + str(temp_usr[0][4])
        self.txttik.insert(INSERT,'\nTrain No.: ' + str(temp_train[0][0]))
        self.txttik.insert(INSERT,'\t \t \t \t  Train Name.: ' + str(temp_train[0][1]))
        self.txttik.insert(INSERT,'\nFrom : Mumbai \t \t \t \t  To : ' + str(temp_train[0][3]))
        self.txttik.insert(INSERT,'\nDate : ' + DateOfOrder.get() + "\n")
        self.txttik.insert(INSERT,'Ticket No. : ' + str(temp_usr[0][4]))
        self.txttik.insert(INSERT,'\n \nPassengers Details : \n')
        self.txttik.insert(INSERT,'Sr. No.\t \t    Name \t \t   Age \t Gender    \tSeat No. \n')
        
        for i in range(len(temp_pas)) :
            for j in range(5) :
                if j==0:#Sr no.
                    self.txttik.insert(INSERT,str(i+1))
                if j==1:#name.
                    self.txttik.insert(INSERT,'\t\t' + str(temp_pas[i][2]))
                if j==2:#age
                    self.txttik.insert(INSERT,'\t \t    ' + str(temp_pas[i][3]))
                if j==4:#seatno
                    self.txttik.insert(INSERT,'         \t ' + str(temp_pas[i][1]))
                if j==3:#gender
                    self.txttik.insert(INSERT,'\t ' + str(temp_pas[i][4]))
            self.txttik.insert(INSERT,'\n')
        self.txttik.config(state=DISABLED)
        
    def __init__(self,master):
        self.frame = Frame(master, bg="dark slate blue").grid()
        #self.frame.grid()
        #self.labl1 = Label(self.frame, text="                             E-TICKET BOOKING-IRCTC                   ", pady=5, font=("Trebuchet MS", 35), bg="dark slate blue",fg="goldenrod")
        #self.labl1.grid(row=0,column=1, columnspan=20)
        self.labl2 = Label(self.frame, text="           BOOKING STATUS", pady=5, font=("Trebuchet MS", 40), bg="dark slate blue", fg="gold",padx=20)
        self.labl2.grid(row=1, column=1, columnspan=20)
        #self.labl7 = Label(self.frame, text="                          ----------------------------------------------------------------------------------", pady=5, font=("Trebuchet MS", 20), bg="dark slate blue", fg="gold",
        #         padx=20)
        #self.labl7.grid(row=2, column=0, columnspan=20)
        self.labl3 = Label(self.frame, text="               Booked Ticket Details:", fg="goldenrod", pady=5, bg="dark slate blue", font=("Trebuchet MS", 25))
        self.labl3.grid(row=10,column=12,sticky=W)
        self.txttik = Text(self.frame, font=('Trebuchet MS', 12, 'bold'),bd=4,bg='white',width=64,height=12)
        self.txttik.place(x=125,y=125)
        self.labl4 = Label(self.frame, text="\nTICKET CONFIRMED!!", pady=5, font=("Trebuchet MS", 25), bg="dark slate blue",fg="gold")
        self.labl4.place(x=250,y=400)
        self.but1=Button(self.frame, text='DONE',fg="blue",activebackground="goldenrod",font=("Trebuchet MS", 14),activeforeground="gold", bg="gold", height=1, width=8,command=self.quit)
        self.but1.place(x=350,y=500)
        
            
            
            
root1=Tk()
root1.title('RAILWAY TICKET BOOKING SYSTEM')
root1.geometry("800x575")
root1.configure(background='dark slate blue')
mypr=MyProj(root1)
mypr.trainticket()
root1.mainloop()            
