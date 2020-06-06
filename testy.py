import pymysql
import pandas as pd
from tkinter import *
from pandastable import Table, TableModel
import pandastable
import sys
import os

def insertsqldb():
    #database connection
    db = pymysql.connect('localhost', 'root', 'root', 'test')
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
    db = pymysql.connect('localhost', 'root', 'root', 'test')
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

def loadcalendar():
    #database connection
    db = pymysql.connect('localhost', 'root', 'root', 'io')
    #Make sure to initiate the cursor to fetch rows
    cursor = db.cursor()
    # fetch all the queries in students_info Table
    fetch_queries =     fetch_queries = 'Select emploee_list.imie,  emploee_list.nazwisko, calendar.year, ' \
                    'calendar.month, calendar.day, calendar.work From emploee_list Join graphic ON emploee_list.id = ' \
                    'graphic.emploee_fk Join calendar ON calendar.id = graphic.calendar_fk'


    #queries execution
    cursor.execute(fetch_queries)
    lines = cursor.fetchall()
    check = []
    for line in lines:
       check.append(line)
    #commit the connection
    check = pd.DataFrame(check)
    check['Data'] = check[2].astype(str) + '-' + check[3].astype(str) + '-' + check[4].astype(str)
    check.columns = ['Imie', 'Nazwisko', 'rok', 'miesiac', 'dzien', 'Praca', 'Data']
    check = check.drop(['rok', 'miesiac', 'dzien'], axis=1)
    check = check.reindex(columns=['Imie', 'Nazwisko', 'Data', 'Praca'])
    check['Praca'] = check['Praca'].replace({0:'Wolne', 1: 'Praca'})
    check['Nazwa'] = check["Imie"] + ' ' + check["Nazwisko"]
    check.columns = ['Imie', 'Nazwisko', 'Praca', 'Data', 'Imie i Nazwisko']
    check = check.drop(['Imie','Nazwisko'], axis=1)
    check = check[['Imie i Nazwisko','Data', 'Praca']]
    db.commit()
    # make a habit to close the database connection once you create it
    db.close()
    return check




class TestApp(Frame):
    """Basic test frame for the table"""
    def __init__(self, parent=None):
        droplist()
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('800x600+200+100')
        self.main.title('Grafik pracy')
        f = Frame(self.main)
        f.pack(fill=BOTH,expand=1)
        df = loadcalendar()
        self.table = pt = Table(f, dataframe=df,
                                showtoolbar=FALSE, showstatusbar=True)
        myButton30 = Button(self.main, text='Zapisz')
        myButton30.pack()



        pt.show()
        return
def droplist():
    df1 = loadcalendar()
    df1 = df1.drop(['Data','Praca'],axis=1)
    df1 = df1.drop_duplicates()
    main = Tk()
    main.geometry("600x400")

    options = df1['Imie i Nazwisko']
    clicked = StringVar(main)
    myLabel = Label(main, text=clicked.get()).pack()
    drop = OptionMenu(main, clicked, *options)
    drop.pack()

    def change_dropdown(*args):
        print(clicked.get())

    clicked.trace('w', change_dropdown)


app = TestApp()

#launch the app
app.mainloop()


