from tkinter import *
from tkinter import messagebox
import sqlite3
import os
root1=Tk()
gender=[]
with sqlite3.connect('TrainTicketBooking.db') as db:
    c = db.cursor()
c.execute('SELECT * FROM Temp WHERE key = 2')
select=c.fetchall()
c.execute('SELECT * FROM Trainticket_details WHERE ticketno = ?',[(select[0][0])])
result=c.fetchall()
print(result)
class MyProj:
    global gender
    def func1(self,value):
        #global gender
        gender.append(value)
        print(gender)
    def payandconfirm(self):
            #c.execute('DELETE FROM temp WHERE key = 2')
            #db.commit()
            if (not result[0][5] and not result[0][4]):
                #1 seat booked
                print("1 seat")
                print(result[0][2],result[0][3],self.text1.get(),self.text4.get(),gender[0])
                c.execute('INSERT INTO Travelling_passengers (ticketno,seatno,name,age,gender) VALUES(?,?,?,?,?)',[(result[0][0]),(result[0][3]),(self.text1.get()),(self.text4.get()),(gender[0])])
                db.commit()
            elif(not result[0][5]):
                #2 seats booked
                print("2 seats")
                print(result[0][2],result[0][4],self.text1.get(),self.text4.get(),gender[0])
                print(result[0][2],result[0][3],self.text2.get(),self.text4.get(),gender[1])
                c.execute('INSERT INTO Travelling_passengers (ticketno,seatno,name,age,gender) VALUES(?,?,?,?,?)',[(result[0][0]),(result[0][4]),(self.text1.get()),(self.text4.get()),(gender[0])])
                c.execute('INSERT INTO Travelling_passengers (ticketno,seatno,name,age,gender) VALUES(?,?,?,?,?)',[(result[0][0]),(result[0][3]),(self.text2.get()),(self.text5.get()),(gender[1])])
                db.commit()
            else:
                #3 seats booked
                print("3 seats")
                print(result[0][2],result[0][5],self.text1.get(),self.text4.get(),gender[0])
                print(result[0][2],result[0][4],self.text2.get(),self.text5.get(),gender[1])
                print(result[0][2],result[0][3],self.text3.get(),self.text6.get(),gender[2])
                c.execute('INSERT INTO Travelling_passengers (ticketno,seatno,name,age,gender) VALUES(?,?,?,?,?)',[(result[0][0]),(result[0][5]),(self.text1.get()),(self.text4.get()),(gender[1])])
                c.execute('INSERT INTO Travelling_passengers (ticketno,seatno,name,age,gender) VALUES(?,?,?,?,?)',[(result[0][0]),(result[0][4]),(self.text2.get()),(self.text5.get()),(gender[1])])
                c.execute('INSERT INTO Travelling_passengers (ticketno,seatno,name,age,gender) VALUES(?,?,?,?,?)',[(result[0][0]),(result[0][3]),(self.text3.get()),(self.text6.get()),(gender[1])])
                db.commit()
            root1.destroy()
            os.system('sample41.py')
                        
    def __init__(self,master):
            self.m=master
            self.text1=StringVar()
            self.text2=StringVar()
            self.text3=StringVar()
            self.text4=StringVar()
            self.text5=StringVar()
            self.text6=StringVar()
            self.frame = Frame(master, bg="dark slate blue").grid()
            self.labl2 = Label(self.frame, text="PASSENGER DETAILS",pady=20, font=("Trebuchet MS", 40,'bold'), bg="dark slate blue", fg="gold")
            self.labl2.grid(row=0, column=1, columnspan=20)
            #self.labl7 = Label(self.frame, text="                    ----------------------------------------------------------------------------------------", pady=5, font=("Trebuchet MS", 20), bg="dark slate blue", fg="gold",
            #     padx=20)
            #self.labl7.grid(row=2, column=0, columnspan=20)
            self.labl3 = Label(self.frame, text="Sr.\nNo.", fg="goldenrod", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
            self.labl3.grid(row=4)
            self.labl3 = Label(self.frame, text="    1.  ", fg="goldenrod", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
            self.labl3.grid(row=5)
            self.labl3 = Label(self.frame, text="    2.  ", fg="goldenrod", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
            self.labl3.grid(row=7)
            self.labl3 = Label(self.frame, text="    3.  ", fg="goldenrod", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
            self.labl3.grid(row=9)
            self.labl3 = Label(self.frame, text=" Name of \nPassengers  ", fg="goldenrod", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
            self.labl3.grid(row=4,column=1)
            
            OPTIONS1 = ['Male','Female']
            OPTIONS = ['No Choice','Window Side']

            self.txt1 = Entry(self.frame, font=('Trebuchet MS', 12, 'bold'),textvariable=self.text1, bd=4, justify='left',width=25)
            self.txt1.grid(row=5,column=1)
            #self.txt1.config(state=DISABLED)
            variable = StringVar()
            variable.set(OPTIONS[0])
            w11 = OptionMenu(self.frame, variable, *OPTIONS1,command=self.func1)
            w11.grid(row=5, column=2)
            #w1.config(state=DISABLED)
            self.txt4 = Entry(self.frame, font=('Trebuchet MS', 12, 'bold'),textvariable=self.text4, bd=4, justify='left',width=4)
            self.txt4.grid(row=5,column=3)
            variable4 = StringVar()
            variable4.set(OPTIONS[0])
            w12 = OptionMenu(self.frame, variable4, *OPTIONS)
            w12.grid(row=5, column=4)
            
            self.txt2 = Entry(self.frame, font=('Trebuchet MS', 12, 'bold'),textvariable=self.text2, bd=4, justify='left',width=25)
            self.txt2.grid(row=7,column=1)
            variable2 = StringVar()
            variable2.set(OPTIONS[0])
            w21 = OptionMenu(self.frame, variable2, *OPTIONS1,command=self.func1)
            w21.grid(row=7, column=2)
            self.txt5 = Entry(self.frame, font=('Trebuchet MS', 12, 'bold'),textvariable=self.text5, bd=4, justify='left',width=4)
            self.txt5.grid(row=7,column=3)
            variable5 = StringVar()
            variable5.set(OPTIONS[0])
            w22 = OptionMenu(self.frame, variable5, *OPTIONS)
            w22.grid(row=7, column=4)
            
            self.txt3 = Entry(self.frame, font=('Trebuchet MS', 12, 'bold'),textvariable=self.text3, bd=4, justify='left',width=25)
            self.txt3.grid(row=9,column=1)
            variable3 = StringVar()
            variable3.set(OPTIONS[0])
            w31 = OptionMenu(self.frame, variable3, *OPTIONS1,command=self.func1)
            w31.grid(row=9, column=2)
            self.txt6 = Entry(self.frame, font=('Trebuchet MS', 12, 'bold'),textvariable=self.text6, bd=4, justify='left',width=4)
            self.txt6.grid(row=9,column=3)
            variable6 = StringVar()
            variable6.set(OPTIONS[0])
            w32 = OptionMenu(self.frame, variable6, *OPTIONS)
            w32.grid(row=9, column=4)
            
            if(result[0][5]==0 and result[0][4]==0):
                #1 seat booked
                self.txt2.config(state=DISABLED)
                self.txt5.config(state=DISABLED)
                w21.config(state=DISABLED)
                w22.config(state=DISABLED)
                self.txt3.config(state=DISABLED)
                self.txt6.config(state=DISABLED)
                w31.config(state=DISABLED)
                w32.config(state=DISABLED)
            
            elif(result[0][5]==0):
                #2 seats booked
                self.txt3.config(state=DISABLED)
                self.txt6.config(state=DISABLED)
                w31.config(state=DISABLED)
                w32.config(state=DISABLED)
                
            

            self.labl4 = Label(self.frame, text="  Gender   ", fg="goldenrod", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
            self.labl4.grid(row=4, column=2)
            
            self.labl5 = Label(self.frame, text=" Age  ", fg="goldenrod", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
            self.labl5.grid(row=4, column=3)
            
            self.labl6 = Label(self.frame, text=" Choice ", fg="goldenrod", padx=8, pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
            self.labl6.grid(row=4, column=4)
            

            self.labl5 = Label(self.frame, text="\n     Mobile No.:", fg="goldenrod", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
            self.labl5.grid(row=12,column=0)
            self.txt8 = Entry(self.frame, font=('Trebuchet MS', 12, 'bold'), bd=4, justify='left',width=20)
            self.txt8.place(x=250,y=350)
            self.but1=Button(self.frame, text='PAY AND CONFIRM', fg="blue",activebackground="goldenrod",font=("Trebuchet MS", 14), bg="gold", height=2, width=20,relief=RAISED,command=self.payandconfirm)
            self.but1.place(x=300,y=450)
            self.but1.bind("<Button-1>",self.database)
            
    c.execute('SELECT * FROM User_details WHERE ticketno = ?',[(select[0][0])])
    temp_mobile=c.fetchall()
    print("in the db")
    print(temp_mobile)
    mobile=temp_mobile[0][3]

    def database(self,event):
        if(self.txt1.get()=="" or self.txt4.get()==""):
            messagebox.showerror(parent=self.m,message="Please fill atleast one entry!!",title="Error")
        if(len(self.txt8.get())!=10): 
            messagebox.showerror(parent=self.m, message="Please enter a valid phone number !!", title="Error")
        #if not (self.txt8.get()==self.temp_mobile[0][3]):
        #    print("HERE",self.txt8.get(),self.temp_mobile[0][3])
        #    messagebox.showerror(parent=self.m, message="Please enter a valid registered phone number !!", title="Error")
            

root1.title('RAILWAY TICKET BOOKING SYSTEM')
root1.geometry("850x550")
root1.configure(background='dark slate blue')
mypr=MyProj(root1)
root1.mainloop()
