import sqlite3
from tkinter import *

class MyWindow:
    def __init__(self, win,frame1,frame2,frame3):
        self.lbl1 = Label(frame1, text = 'Name', font='arial 12 bold').pack(side=LEFT)
        self.lbl2 = Label(frame2, text = 'Phone', font='arial 12 bold').pack(side=LEFT)
        self.lbl3 = Label(frame3, text = 'Address', font='arial 10 bold').pack(side=LEFT)
        self.t1 = Entry(frame1, textvariable = Name,width=40).pack()
        self.t2 = Entry(frame2, textvariable = Phone,width=40).pack()
        self.t3 = Entry(frame3, textvariable= Address, width=40).pack()
        # self.address =Text(frame3,width=27,height=5)
        # self.address.pack()

        self.btn1 = Button(win, text="Add", font="arial 12 bold", command=self.add).place(x=60, y=170)
        self.btn2 = Button(win, text="Search", font="arial 12 bold", command=self.search).place(x=60, y=210)
        self.btn3 = Button(win, text="Delete", font="arial 12 bold", command=self.delete).place(x=60, y=250)
        self.btn4 = Button(win, text="Edit", font="arial 12 bold", command=self.edit).place(x=60, y=290)
        self.btn5 = Button(win, text="Show Database", font="arial 12 bold", command=self.show_database).place(x=60, y=330)

    def add(self):
        global cur
        #datas.append([Name.get(), Phone.get(), Address.get()])
        cur.execute("INSERT INTO AddressBook1 VALUES (?,?,?)",(Name.get(),Phone.get(), Address.get()))
        self.update_book()
        con.commit()

    def search(self):
        global cur
        row = []
        select.delete(0, END)
        for row in cur.execute("SELECT * FROM AddressBook1 WHERE Name=:n", {"n": Name.get()}):
        #for row in cur.execute("SELECT * FROM AddressBook1 WHERE Name like ?",(Name.get())):
            select.insert(END, row)
        if(len(row) ==0):
            select.insert(END, "Dosen't exist! ")
        con.commit()

    def delete(self):
        global cur
        row = []
        select.delete(0, END)
        for row in cur.execute("SELECT * FROM AddressBook1 WHERE Name=:n", {"n": Name.get()}):
            cur.execute("Delete from AddressBook1 where Name=:n", {"n": Name.get()})
            select.insert(END, "Deleted! ")
        if(len(row) == 0):
            select.insert(END, "Dosen't exist! ")
        con.commit()

    def edit(self):
        global cur
        select.delete(0, END)
        row = []
        for row in cur.execute("SELECT * FROM AddressBook1 WHERE Name=:n", {"n": Name.get()}):
            cur.execute("Update AddressBook1 set address=? ,phone=? where name=?", (Address.get(),Phone.get(),Name.get()))
            select.insert(END, "Edited! ")
        if (len(row) == 0):
            select.insert(END, "Dosen't exist! ")
        con.commit()

    def show_database(self):
        global cur
        select.delete(0, END)
        for row in cur.execute("SELECT * FROM AddressBook1"):
            select.insert(END, row)

    # Update Information
    def update_book(self):
        global cur
        select.delete(0, END)
        for row in cur.execute("SELECT * FROM AddressBook1"):
            select.insert(END, row[0])


con = sqlite3.connect('Addressbook1.db')
cur = con.cursor()
print("Database connection established")

# Create table
# Just Fisrt Time
cur.execute('''create table AddressBook1(Name VARCHAR(20),Phone VARCHAR(30), Address VARCHAR(50))''')

window=Tk()
Name, Phone, Address = StringVar(),StringVar(),StringVar()
window.title('AddressBook')
window.geometry("400x400")

frame1 = Frame()
frame1.pack(pady=10)
frame2 = Frame()
frame2.pack()
frame3 = Frame()
frame3.pack(pady=10)

scroll_bar = Scrollbar(window, orient=VERTICAL)
select = Listbox(window, yscrollcommand=scroll_bar.set, height=14)
scroll_bar.config(command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.place(x=200, y=160)
mywin=MyWindow(window,frame1,frame2,frame3)

# Execute Tkinter
window.mainloop()
con.close()