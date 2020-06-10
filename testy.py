import pymysql
import pandas as pd
from tkinter import *
from pandastable import Table, TableModel
import numpy as np
import pandastable
import sys
import os
import datetime


# def insertsqldb():
#     #database connection
#     db = pymysql.connect('localhost', 'root', 'root', 'test')
#     #Make sure to initiate the cursor to fetch rows
#     cursor = db.cursor()
#     #Create a Table
#     zlecenia = """CREATE TABLE zlecenia(
#     ID INT(20) PRIMARY KEY AUTO_INCREMENT,
#     WORKORDER  INT(20) NOT NULL,
#     ITEM INT(20), DATE_WO DATE)"""
#     # insert queries
#     row1 = "INSERT INTO zlecenia(WORKORDER, ITEM, DATE_WO) VALUES(54325, 1234, '2020-05-09');"
#     row2 = "INSERT INTO zlecenia(WORKORDER, ITEM, DATE_WO) VALUES(54326, 1235, '2020-05-10');"
#     row3 = "INSERT INTO zlecenia(WORKORDER, ITEM, DATE_WO) VALUES(54327, 1234, '2020-05-08');"
#     row4 = "INSERT INTO zlecenia(WORKORDER, ITEM, DATE_WO) VALUES(54328, 1235, '2020-05-10');"
#     row5 = "INSERT INTO zlecenia(WORKORDER, ITEM, DATE_WO) VALUES(54329, 1234, '2020-05-09');"
#     row6 = "INSERT INTO zlecenia(WORKORDER, ITEM, DATE_WO) VALUES(54330, 1235, '2020-05-06');"
#     row7 = "INSERT INTO zlecenia(WORKORDER, ITEM, DATE_WO) VALUES(54331, 1234, '2020-05-05');"
#     row8 = "INSERT INTO zlecenia(WORKORDER, ITEM, DATE_WO) VALUES(54332, 1235, '2020-05-07');"
#     #executing the quires
#     cursor.execute(row1)
#     cursor.execute(row2)
#     cursor.execute(row3)
#     cursor.execute(row4)
#     cursor.execute(row5)
#     cursor.execute(row6)
#     cursor.execute(row7)
#     cursor.execute(row8)
#     print(db)
#     #commit the connection
#     db.commit()
#     # make a habit to close the database connection once you create it
#     db.close()
#
# def loadwos():
#     #database connection
#     db = pymysql.connect('localhost', 'root', 'root', 'test')
#     #Make sure to initiate the cursor to fetch rows
#     cursor = db.cursor()
#     # fetch all the queries in students_info Table
#     fetch_queries = "Select * from zlecenia;"
#     #queries execution
#     cursor.execute(fetch_queries)
#     lines = cursor.fetchall()
#     check = []
#     for line in lines:
#        check.append(line)
#     #commit the connection
#     check = pd.DataFrame(check)
#     db.commit()
#     # make a habit to close the database connection once you create it
#     db.close()
#     return check
#
# def loadcalendar():
#     #database connection
#     db = pymysql.connect('localhost', 'root', 'root', 'io')
#     #Make sure to initiate the cursor to fetch rows
#     cursor = db.cursor()
#     # fetch all the queries in students_info Table
#     fetch_queries ='Select emploee_list.Name, calendar.Datagr, ' \
#                     'graphic.work, graphic.calendar_fk, graphic.emploee_list_fk From emploee_list Join graphic ON emploee_list.id = ' \
#                     'graphic.emploee_list_fk Join calendar ON calendar.id = graphic.calendar_fk '
#
#
#     #queries execution
#     cursor.execute(fetch_queries)
#     lines = cursor.fetchall()
#     check = []
#     for line in lines:
#        check.append(line)
#     #commit the connection
#     check = pd.DataFrame(check)
#     check.columns = ['Imie i Nazwisko', 'Data', 'Praca', 'id calendar', 'id emploee']
#     check['Praca'] = check['Praca'].replace({0:'Wolne', 1: 'Praca'})
#     db.commit()
#     # make a habit to close the database connection once you create it
#     db.close()
#     print(check)
#     return check
#
#
#
#
# def releasecalendar():
#     var1 = 0
#     var2 = 1
#     var3 = 1
#     db = pymysql.connect('localhost', 'root', 'root', 'io')
#     cursor = db.cursor()
#     fetch_queries = "UPDATE graphic SET work= %s WHERE calendar_fk = %s AND emploee_list_fk=%s;"
#
#     cursor.execute(fetch_queries, (var1 ,var2 , var3))
#
#     db.commit()
#     db.close()
#
#
# releasecalendar()
#
#
#
#
#
# class TestApp(Frame):
#     """Basic test frame for the table"""
#     def __init__(self, parent=None):
#         droplist()
#         self.parent = parent
#         Frame.__init__(self)
#         self.main = self.master
#
#         f = Frame(self.main)
#         f.pack(fill=BOTH,expand=1)
#         df = loadcalendar()
#         self.table = pt = Table(f, dataframe=df[df['Imie i Nazwisko'] == selected],
#                                 showtoolbar=True, showstatusbar=True)
#         myButton30 = Button(self.main, text='Zapisz')
#         myButton30.pack()
#
#
#
#         pt.show()
#         return
# def droplist():
#     df1 = loadcalendar()
#     df1 = df1.drop(['Data','Praca'],axis=1)
#     df1 = df1.drop_duplicates()
#
#     main = Tk()
#     main.geometry("600x400")
#
#     # options = df1['Imie i Nazwisko']
#     # clicked = StringVar(main)
#     # myLabel = Label(main, text=clicked.get()).pack()
#     # drop = OptionMenu(main, clicked, *options)
#     # drop.pack()
#     #
#     # def change_dropdown(*args):
#     #     print(clicked.get())
#     #
#     # clicked.trace('w', change_dropdown)
#     def callback(selected):
#         print(selected)
#
#     options = StringVar()
#     menu = OptionMenu(main, options, 'Bartosz Galka', 'Lukasz Turowski', command=callback)
#     menu.pack()
#     options.set('Bartosz Galka')
#
# # app = TestApp()
# #
# # #launch the app
# # app.mainloop()
#
# def garphicdisp():
#     global df
#     def callback(selected):
#         print(selected)
#
#
#     root = Tk()
#     frame = Frame(root)
#     root.geometry('800x600+200+100')
#     root.title('Grafik pracy')
#     f = Frame(root)
#     frame.pack(fill=BOTH,expand=1)
#     df = loadcalendar()
#     df1 = df
#     df1 = df1.drop(['Data', 'Praca'], axis=1)
#     df1 = df1.drop_duplicates()
#
#
#
#
#     def filter():
#         root.destroy()
#         garphicdisp()
#
#     filtrbutt = Button(root, text='Szukaj', command=filter)
#     filtrbutt.pack()
#
#
#     options = StringVar()
#     menu = OptionMenu(root, options, 'Bartosz Galka', 'Lukasz Turowski', command=callback)
#     menu.pack()
#     flag = 0
#     def ok(flag):
#         print("value is", options.get())
#         root.destroy()
#         flag = 1
#         garphicdisp()
#         return options.get(), flag
#
#
#
#     options.set('')
#     pt = Table(frame, dataframe=df)
#     pt.show()
#     button = Button(root, text="OK", command=ok(flag))
#     button.pack()
#     if flag == 1:
#         df = df[df['Imie i Nazwisko'] == options.get()]
#
#
#     root.mainloop()

def loadcapcal():

    db = pymysql.connect('localhost', 'root', 'root', 'io')
    cursor = db.cursor()

    fetch_queries = 'Select calendar.id, calendar.Datagr From calendar ' \

    # queries execution
    cursor.execute(fetch_queries)
    lines = cursor.fetchall()
    calendarcap = []
    for line in lines:
        calendarcap.append(line)
    calendarcap = pd.DataFrame(calendarcap)

    db.commit()
    db.close()
    return calendarcap

def loadWO():
    db = pymysql.connect('localhost', 'root', 'root', 'io')
    cursor = db.cursor()

    fetch_queries ='Select wo.id, wo.quantity, wo.start_date, items.id, items.description, ' \
                    'std_op.line, std_op.speed From wo Join wo_item ON wo.id = ' \
                    'wo_fk Join items ON wo_item.item_fk = items.id Join item_std ON ' \
                    'items.id = item_std.item_fk Join std_op ON item_std.std_op_fk = std_op.id'

    # queries execution
    cursor.execute(fetch_queries)
    lines = cursor.fetchall()
    wolist = []
    for line in lines:
        wolist.append(line)
    wolist = pd.DataFrame(wolist)

    db.commit()
    db.close()
    return wolist



def capacity_loading():
    calendar = pd.DataFrame(loadcapcal())
    wolist = pd.DataFrame(loadWO())
    root = Tk()
    root.title('Capacity loading')
    root.geometry("800x600")


    #calendar['1'].dt.week

    calendar.columns = ['byle jak','Data']
    # print(calendar.dtypes)
    # calendar[['rok','miesiac','dzien']]=calendar.Data.str.split("-",expand=True)
    # print(calendar)
    #print(calendar.Data.apply(lambda x: pd.Series(str(x).split("-"))))
    calendar['Data']= pd.to_datetime(calendar['Data'])
    wolist[2] = pd.to_datetime(wolist[2])
    # calendar.dropna(inplace=True)
    # cal = calendar["Data"].split("-", n=2, expand=True)
    # calendar["Rok"]=cal[1]
    # calendar["Miesiac"]=cal[2]
    # calendar["Dzien"]=cal[3]
    # calendar.drop(columns=["Data"],inplace=True)
    # print(calendar)

    calendar['Nr tygodnia'] = calendar['Data'].dt.week
    wolist[7] = wolist[2].dt.week
    header = calendar['Nr tygodnia']
    header.columns = ['num tyg']





    linesdrop = wolist.drop(columns=[0,1,2,3,4,6,7])
    linesdrop = linesdrop.drop_duplicates(subset=[5])
    wolist.columns = ['numer zlecenia', 'ilosc', 'data', 'indeks', 'opis', 'linia', 'predkosc', 'num tyg']
    wolist['lin cap'] = wolist['predkosc'] * 24 * 5
    demandreport = pd.pivot_table(wolist, values=['ilosc', 'lin cap'], index=['num tyg',], columns=['linia'], aggfunc={'ilosc': np.sum, 'lin cap': np.mean}).transpose()
    print(demandreport)
    frame_data = Frame(root)


    pt = Table(frame_data, dataframe=demandreport, showtoolbar=True, showstatusbar=True)
    pt.show()
    frame_data.pack(fill=BOTH, expand=1)
    #both = pd.merge(spacereport, demandreport, 'left', on= 'linia')

    root.mainloop()

    #isowekk = calendar.assign(wkiso = calendar[1].dt.week)
    #print(calendar)



capacity_loading()





