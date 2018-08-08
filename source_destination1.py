from tkinter import *
import os
selected=""

import sqlite3

class main():

    def __init__(self, master):
        self.master=master
        self.widgets()

    def onClick(self):
        root.destroy()
        os.system(" train11.py ")

    def widgets(self):
        self.frame = Frame(self.master,bg="dark slate blue")
        self.frame.pack()

        self.title1 = Label(self.frame ,text=' ENTER SOURCE AND DESTINATION  ', font = ("Trebuchet MS",40,'bold'), fg="gold", bg="dark slate blue", pady=40)
        self.title1.grid(columnspan=4)

        self.source = Label(self.frame, text="Source: ", font=("Trebuchet MS", 30), bg="dark slate blue", fg="goldenrod", pady=10)
        self.source.grid(row=1,column=0,sticky=E)

        self.sourcelist=['Mumbai']

        self.slist = StringVar()
        self.slist.set(self.sourcelist[0])

        self.SourceMenu = OptionMenu(self.frame, self.slist, *self.sourcelist)
        self.SourceMenu.grid(row=1,column=1)
        self.SourceMenu.config(font=("Trebuchet MS", 20), width=10, bg='dark slate blue', fg='springgreen')

        self.dest = Label(self.frame, text="Destination: ", font=("Trebuchet MS", 30), bg="dark slate blue", fg="goldenrod", pady=30)
        self.dest.grid(row=2,column=0,sticky=E)

        self.destlist = ['Select','Pune','Bangalore','Goa','Delhi']

        self.dlist = StringVar()
        self.dlist.set(self.destlist[0])

        self.destMenu = OptionMenu(self.frame, self.dlist, *self.destlist,command=self.func)
        self.destMenu.grid(row=2,column=1)
        self.destMenu.config(font=("Trebuchet MS", 20), width=10, bg='dark slate blue', fg='springgreen') 

        self.button1 = Button(self.frame, text='Find Trains', font=("Trebuchet MS", 20,'bold'), bg='goldenrod', fg='dark slate blue',command=self.onClick)
        self.button1.grid(row=5,column=0,sticky=E,padx=10,pady=70)

        self.button2 = Button(self.frame, text='Cancel Ticket', font=("Trebuchet MS", 20,'bold'), bg='goldenrod', fg='dark slate blue',command=self.onCancel)
        self.button2.grid(row=5,column=2,padx=10,pady=70)

    def func(self,value):
        global selected
        selected=value
        db=sqlite3.connect('TrainTicketBooking.db')
        a = db.cursor()
        a.execute('INSERT INTO Temp (temp,key) VALUES(?,1)',[(selected)])
        db.commit()
        result = a.fetchall()
        db.close()

    def onCancel(self):
        root.destroy()
        os.system(" Cancel1.py ")



if __name__=="__main__":
    root = Tk()
    root.title('RAILWAY TICKET BOOKING SYSTEM')
    root.geometry('860x550')
    root.configure(background='dark slate blue')
    m = main(root)
    root.mainloop()
