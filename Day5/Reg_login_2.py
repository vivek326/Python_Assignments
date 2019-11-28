from tkinter import *
import pymysql


def sel():
    db = pymysql.connect("localhost", "root", "", "test")
    cursor = db.cursor()
    data = cursor.execute("Select * from form")
    # data = cursor.execute(
    #     '''CREATE TABLE FORM(FNAME CHAR(20) NOT NULL, PASSWORD CHAR(20), GENDER CHAR(2), CHECKBOX CHAR(100) )''')

    s = fn.get()
    t = passw.get()

    data = cursor.fetchall()
    for row in data:
        if row[0] == s:
            print("Valid Username")
            if row[1] == t:
                print('login success')
                break


        else:
            print("invalid username")


    db.commit()
    db.close()


tkit = Tk()
fn = StringVar()
L1 = Entry(tkit, text="First Name", textvariable=fn)
L1.pack(side=TOP)
passw = StringVar()
L2 = Entry(tkit, text="password", textvariable=passw)
L2.pack(side=TOP)
label = Label(tkit)

E1 = Button(tkit, bd=5, text='Submit', command=sel)
E1.pack(side=BOTTOM)

label.pack()

tkit.mainloop()
