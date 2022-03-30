import sqlite3
import os
from tkinter import messagebox


# check db found
def isSqlite3Db(db):
    if not os.path.isfile(db): return False
    sz = os.path.getsize(db)

    # file is empty, give benefit of the doubt that its sqlite
    # New sqlite3 files created in recent libraries are empty!
    if sz == 0: return True

    # SQLite database file header is 100 bytes
    if sz < 100: return False

    # Validate file header
    with open(db, 'rb') as fd:
        header = fd.read(100)

    return (header[:16] == b'SQLite format 3\x00')


# open function
def connectdb():
    pycon = sqlite3.connect('appdb.db')
    pycon.close()


# create db
def createdb():
    pycon = sqlite3.connect('appdb.db')
    c = pycon.cursor()
    c.execute("""CREATE TABLE logintbl(
            username text,
            password text
            )""")
    pycon.commit()
    c.execute(" INSERT INTO logintbl VALUES('admin','admin')")
    pycon.commit()
    c.execute("""CREATE TABLE sessionUser(
                username text
                )""")
    pycon.commit()
    c.execute(" INSERT INTO sessionUser VALUES('User')")
    pycon.commit()
    c.execute("""CREATE TABLE componentslist(
            Racked integer,
            itemDesc text, 
            itemqty integer
            )""")
    pycon.commit()
    pycon.close()


# checkloginverify
def verifylogin(user, password):
    pycon = sqlite3.connect('appdb.db')
    c = pycon.cursor()
    c.execute("select * from logintbl where username=? AND password=?", (user, password))
    row = c.fetchone()
    if row:
        # messagebox.showinfo("info"," successful")
        c.execute(" update sessionUser set username=?", [user])
        pycon.commit()
        pycon.close()
        return True
    else:
        # messagebox.showinfo("info","not successful")
        pycon.close()
        return False


# get sessionusername
def getsessionuser():
    pycon = sqlite3.connect('appdb.db')
    c = pycon.cursor()
    c.execute("select * from sessionUser")
    row = c.fetchone()
    abc = row[0]
    pycon.close()
    return abc


# get AddingComponents
def addComponents(abc):
    # messagebox.showinfo("info",type(a)type(b)+" "+type(cc))
    pycon = sqlite3.connect('appdb.db')

    c = pycon.cursor()
    c.execute(" INSERT INTO componentslist VALUES(?,?,?)", abc)
    pycon.commit()
    pycon.close()


def addCommpQty(abc):
    pycon = sqlite3.connect('appdb.db')
    c = pycon.cursor()
    c.execute(" INSERT INTO componentslist VALUES(?,?,?)", abc)
    pycon.commit()
    pycon.close()


# showall
def showall():
    pycon = sqlite3.connect('appdb.db')
    c = pycon.cursor()
    c.execute("select rowid,* from compnents")
    items = c.fetchall()
    for item in items:
        print(item)
    pycon.commit()
    pycon.close()
