import pymysql
import pandas as pd
from tkinter import *
from pandastable import Table, TableModel
import pandastable
import sys
import os

def insertsqldb():
    #database connection
    db = pymysql.connect(host="localhost",
      user="root",
      passwd="root",database="test")
    #Make sure to initiate the cursor to fetch rows
    cursor = db.cursor()
    #Create a Table
    zlecenia = """CREATE TABLE zlecenia(
    ID INT(20) PRIMARY KEY AUTO_INCREMENT,
    WORKORDER  INT(20) NOT NULL,
    ITEM INT(20), DATE_WO DATE)"""
    # insert queries
    row1 = "INSERT INTO zlecenia(WORKORDER, ITEM, DATE_WO) VALUES(54325, 1234, '2020-05-09');"
    row2 = "INSERT INTO zlecenia(WORKORDER, ITEM, DATE_WO) VALUES(54326, 1235, '2020-05-10');"
    row3 = "INSERT INTO zlecenia(WORKORDER, ITEM, DATE_WO) VALUES(54327, 1234, '2020-05-08');"
    row4 = "INSERT INTO zlecenia(WORKORDER, ITEM, DATE_WO) VALUES(54328, 1235, '2020-05-10');"
    row5 = "INSERT INTO zlecenia(WORKORDER, ITEM, DATE_WO) VALUES(54329, 1234, '2020-05-09');"
    row6 = "INSERT INTO zlecenia(WORKORDER, ITEM, DATE_WO) VALUES(54330, 1235, '2020-05-06');"
    row7 = "INSERT INTO zlecenia(WORKORDER, ITEM, DATE_WO) VALUES(54331, 1234, '2020-05-05');"
    row8 = "INSERT INTO zlecenia(WORKORDER, ITEM, DATE_WO) VALUES(54332, 1235, '2020-05-07');"
    #executing the quires
    cursor.execute(row1)
    cursor.execute(row2)
    cursor.execute(row3)
    cursor.execute(row4)
    cursor.execute(row5)
    cursor.execute(row6)
    cursor.execute(row7)
    cursor.execute(row8)
    print(db)
    #commit the connection
    db.commit()
    # make a habit to close the database connection once you create it
    db.close()

def loadwos():
    #database connection
    db = pymysql.connect(host="localhost",
      user="root",
      passwd="root",
      database="test")
    #Make sure to initiate the cursor to fetch rows
    cursor = db.cursor()
    # fetch all the queries in students_info Table
    fetch_queries = "Select * from zlecenia;"
    #queries execution
    cursor.execute(fetch_queries)
    lines = cursor.fetchall()
    check = []
    for line in lines:
       check.append(line)
    #commit the connection
    check = pd.DataFrame(check)
    db.commit()
    # make a habit to close the database connection once you create it
    db.close()
    return check

class TestApp(Frame):
    """Basic test frame for the table"""
    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('600x400+200+100')
        self.main.title('Capacity loading')
        f = Frame(self.main)
        f.pack(fill=BOTH,expand=1)
        df = loadwos()
        self.table = pt = Table(f, dataframe=df,
                                showtoolbar=True, showstatusbar=True)
        pt.show()
        return

app = TestApp()
#launch the app
app.mainloop()


