from tkinter import *
from tkinter import messagebox as ms
import source_destination1 
import os
import sqlite3

with sqlite3.connect('TrainTicketBooking.db') as db:
    c = db.cursor()
find_user = ('SELECT * FROM Train_details WHERE destination = ?')

root=Tk()
c.execute('SELECT * FROM Temp WHERE key = 1',)
selected = c.fetchall()

temp1=selected[0][0]
c.execute(find_user,[(temp1)])
result = c.fetchall()
print(result)
c.execute('DELETE FROM Temp WHERE key = 1')
db.commit()

root.title("AVAILABLE TRAINS")
frame = Frame(root, bg="dark slate blue")
labl = Label(frame, text='AVAILABILITY', fg='gold',bg='dark slate blue', font=("Trebuchet MS", 35)).grid(row=0,column=1)
labl11 = Label(frame, text="Train No.", fg="springgreen",padx=50, pady=15, bg="dark slate blue", font=("Trebuchet MS", 25)).grid(row=1)

labl12 = Label(frame, text="Train Name", fg="springgreen",padx=50,pady=15, bg="dark slate blue", font=("Trebuchet MS", 25)).grid(row=1, column=1)

labl13 = Label(frame, text="Available ", fg="springgreen",padx=50,pady=15, bg="dark slate blue", font=("Trebuchet MS", 25)).grid(row=1, column=2)

for i in range(2):
    for j in range(3):
        Label(frame, text=result[i][j], fg="springgreen", pady=15, bg="dark slate blue", font=("Trebuchet MS", 18)).grid(row=2+i,column=j)
selected_train=0
def onClick1():
        if(int(spin1_val.get())>3):
            ms.showerror('oops','Can\'t select more than 3 tickets.')
            spin1_val.set("0")
        else:
            root.destroy()
            if result[0][2]>=3 and int(spin1_val.get())==3:
                c.execute('INSERT INTO Trainticket_details (trainno,destination,seatno1,seatno2,seatno3) VALUES (?,?,?,?,?)',[(result[0][0]),(result[0][3]),(result[0][2]),(result[0][2]-1),(result[0][2]-2)])
                temp_available=result[0][2]
                temp_trainno=result[0][0]
                c.execute('UPDATE Train_details SET availableseats = ? WHERE trainno = ?',[(result[0][2]-3),(result[0][0])])
            if result[0][2]>=2 and int(spin1_val.get())==2:
                c.execute('INSERT INTO Trainticket_details (trainno,destination,seatno1,seatno2,seatno3) VALUES (?,?,?,?,?)',[(result[0][0]),(result[0][3]),(result[0][2]),(result[0][2]-1),(0)])
                temp_available=result[0][2]
                temp_trainno=result[0][0]
                c.execute('UPDATE Train_details SET availableseats = ? WHERE trainno = ?',[(result[0][2]-2),(result[0][0])])
            if result[0][2]>=1 and int(spin1_val.get())==1:
                c.execute('INSERT INTO Trainticket_details (trainno,destination,seatno1,seatno2,seatno3) VALUES (?,?,?,?,?)',[(result[0][0]),(result[0][3]),(result[0][2]),(0),(0)])
                temp_available=result[0][2]
                temp_trainno=result[0][0]
                c.execute('UPDATE Train_details SET availableseats = ? WHERE trainno = ?',[(result[0][2]-1),(result[0][0])])

            c.execute('SELECT * FROM Trainticket_details WHERE seatno1 = ? and trainno = ?',[(temp_available),(temp_trainno)])
            result1=c.fetchall()
            print(result1[0][0])
            c.execute('SELECT * FROM Temp WHERE key = 2')
            selected1 = c.fetchall()
            temp2=selected1[0][0]
            print(temp2)
            c.execute('UPDATE User_details SET ticketno = ? WHERE username = ?',[(result1[0][0]),(temp2)])
            c.execute('UPDATE Temp SET temp = ? WHERE key = 2',[(result1[0][0])])
            db.commit()
            os.system(" sample31.py ")

def onClick2():
    if(int(spin2_val.get())>3):
            ms.showerror('oops','Can\'t select more than 3 tickets.')
            spin2_val.set("0")
    else:
        root.destroy()
        if result[1][2]>=3 and int(spin2_val.get())==3:
            c.execute('INSERT INTO Trainticket_details (trainno,destination,seatno1,seatno2,seatno3) VALUES (?,?,?,?,?)',[(result[1][0]),(result[1][3]),(result[1][2]),(result[1][2]-1),(result[1][2]-2)])
            temp_available=result[1][2]
            temp_trainno=result[1][0]
            c.execute('UPDATE Train_details SET availableseats = ? WHERE trainno = ?',[(result[1][2]-3),(result[1][0])])
        if result[1][2]>=2 and int(spin2_val.get())==2:
            c.execute('INSERT INTO Trainticket_details (trainno,destination,seatno1,seatno2,seatno3) VALUES (?,?,?,?,?)',[(result[1][0]),(result[1][3]),(result[1][2]),(result[1][2]-1),(0)])
            temp_available=result[1][2]
            temp_trainno=result[1][0]
            c.execute('UPDATE Train_details SET availableseats = ? WHERE trainno = ?',[(result[1][2]-2),(result[1][0])])
        if result[1][2]>=1 and int(spin2_val.get())==1:
            c.execute('INSERT INTO Trainticket_details (trainno,destination,seatno1,seatno2,seatno3) VALUES (?,?,?,?,?)',[(result[1][0]),(result[1][3]),(result[1][2]),(0),(0)])
            temp_available=result[1][2]
            temp_trainno=result[1][0]
            c.execute('UPDATE Train_details SET availableseats = ? WHERE trainno = ?',[(result[1][2]-1),(result[1][0])])
        c.execute('SELECT * FROM Trainticket_details WHERE seatno1 = ? and trainno = ?',[(temp_available),(temp_trainno)])
        result1=c.fetchall()
        print(result1[0][0])
        c.execute('SELECT * FROM Temp WHERE key = 2')
        selected1 = c.fetchall()
        temp2=selected1[0][0]
        print(temp2)
        c.execute('UPDATE User_details SET ticketno = ? WHERE username = ?',[(result1[0][0]),(temp2)])
        c.execute('UPDATE Temp SET temp = ? WHERE key = 2',[(result1[0][0])])
        db.commit()
        os.system(" sample31.py ")

spin1_val=StringVar()
spin2_val=StringVar()
if result[0][2]>0:
    spin1 = Spinbox(frame, from_=0, to=3, width=5, font=("Trebuchet MS", 13),justify='center',textvariable=spin1_val).grid(row=2, column=3)
    label24=Label(frame, text='', fg="springgreen",activebackground="springgreen",font=("Trebuchet MS", 10),activeforeground="goldenrod",padx=15, bg="dark slate blue").grid(row=2,column=5)
    button24=Button(frame, text='BOOK', fg="springgreen",activebackground="springgreen",font=("Trebuchet MS", 13),activeforeground="goldenrod", relief=RAISED,padx=15, bg="dark slate blue", cursor='cross', height=1, width=5,command=onClick1).grid(row=2,column=6)
else:
    spin1 = Spinbox(frame, from_=0, to=3, width=5,state=DISABLED, font=("Trebuchet MS", 13),justify=CENTER,textvariable=spin1_val).grid(row=2, column=3)
    label24=Label(frame, text='', fg="springgreen",activebackground="springgreen",font=("Trebuchet MS", 10),activeforeground="goldenrod",padx=15, bg="dark slate blue").grid(row=2,column=5)
    button24=Button(frame, text='BOOK', fg="springgreen",activebackground="springgreen",font=("Trebuchet MS", 13),activeforeground="goldenrod", relief=RAISED,padx=15, bg="dark slate blue", cursor='cross', height=1, width=5,state=DISABLED).grid(row=2,column=6)

if result[1][2]>0:
    spin2 = Spinbox(frame, from_=0, to=3, width=5, font=("Trebuchet MS", 13),justify=CENTER,textvariable=spin2_val).grid(row=3, column=3)
    label34=Label(frame, text='', fg="springgreen",activebackground="springgreen",font=("Trebuchet MS", 13),activeforeground="goldenrod",padx=15, bg="dark slate blue").grid(row=3,column=5)
    button34=Button(frame, text='BOOK', fg="springgreen",activebackground="springgreen",font=("Trebuchet MS", 13),activeforeground="goldenrod", relief=RAISED,padx=15, bg="dark slate blue", cursor='cross', height=1, width=5,command=onClick2).grid(row=3,column=6)
else:
    spin2 = Spinbox(frame, from_=0, to=3, width=5,state=DISABLED, font=("Trebuchet MS", 13),justify=CENTER,textvariable=spin2_val).grid(row=3, column=3)
    label34=Label(frame, text='', fg="springgreen",activebackground="springgreen",font=("Trebuchet MS", 13),activeforeground="goldenrod",padx=15, bg="dark slate blue").grid(row=3,column=5)
    button34=Button(frame, text='BOOK', fg="springgreen",activebackground="springgreen",font=("Trebuchet MS", 13),activeforeground="goldenrod", relief=RAISED,padx=15, bg="dark slate blue", cursor='cross', height=1, width=5,state=DISABLED).grid(row=3,column=6)

frame.grid()
root.title('RAILWAY TICKET BOOKING SYSTEM')
root.mainloop()
