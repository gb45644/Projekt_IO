#from LoadData import *
from tkinter import *
import pandas as pd
import pymysql
from pandastable import Table

def sql(login, haslo):
    db = pymysql.connect('localhost', 'root', 'root', 'io')

    cursor = db.cursor()

    fetch_queries = 'Select * from credentials WHERE login LIKE %s;'

    cursor.execute(fetch_queries, login)
    lines = cursor.fetchall()
    for lines in lines:
        if lines[1] == login and lines[2] == haslo:
            flaga = lines[3]
            return flaga

def logowanie():
    root = Tk()
    root.title('Logowanie')
    root.geometry("800x600")
    root.configure(background='white')

    theLabel1 = Label(root, text='Ultimate planning tool', font=('Arial',24))
    theLabel1.configure(background='white')
    theLabel1.pack()


    theLabel2 = Label(root, text='Login:', font=('Arial',18))
    theLabel2.configure(background='white')
    theLabel2.pack()


    polelogin = Entry(root, width=50)
    polelogin.pack()

    theLabel3 = Label(root, text='Hasło:', font=('Arial',18))
    theLabel3.configure(background='white')
    theLabel3.pack()

    polehaslo = Entry(root, width=50, show='*')
    polehaslo.pack()

    def myClick():
        login2 = polelogin.get()
        haslo2 = polehaslo.get()
        access = sql(login2, haslo2)
        if access == 2:
            root.destroy()
            planistam1()
        if access == 4:
            root.destroy()
            kierownikm1()
        else:
            myLabel = Label(root, text='Zly login lub haslo')
            myLabel.pack()

    def myClick2():
        root.destroy()



    myButton = Button(root, text='Zaloguj się', command=myClick)
    myButton.pack()

    myButton2 = Button(root, text='Wyjdź', command=myClick2)
    myButton2.pack()

    root.mainloop()

def grafik():

    def showdata(df2):
        frame_data = Frame(root)

        frame_data.pack(fill=BOTH, expand=1)


        df2 = df2.drop(['id calendar','id emploee'], axis=1)
        table = pt = Table(frame_data, dataframe=df2, showtoolbar=False, showstatusbar=True)
        pt.show()


        # destroy old frame with table
        def destroy():
            root.destroy()
            grafik()

        des_butt = Button(root, text='Zresetuj', command=destroy)
        des_butt.pack()

        return

    def on_click():
        global df2

        val = selected.get()

        if val == 'Wszystkie':
            df2 = df
            # next_button.grid_forget()
        else:
            df2 = df[df['Imie i Nazwisko'] == val]
            # next_button.grid(row=1, column=0)

        showdata(df2)

    # --- main ---

    frame_data = None

    def graphiconn_button():
        root.destroy()
        grapg_changew()

    def grapg_changew():
        root = Tk()
        root.title('Grafik pracy')
        root.geometry("800x600")

        values = loadcalendar()

        values = list(df['Imie i Nazwisko'].unique())
        drop1 = StringVar()

        options = OptionMenu(root, drop1, *values)
        options.pack()

        values2 = list(df['Data'].unique())
        drop2 = StringVar()

        options2 = OptionMenu(root, drop2, *values2)
        options2.pack()

        values3 = list(df['Praca'].unique())
        drop3 = StringVar()

        options3 = OptionMenu(root, drop3, *values3)
        options3.pack()

        def rlscalnd():

            set_val = drop3.get()
            calend_fk = drop2.get()
            empl_fk = drop1.get()

            if set_val == "Wolne":
                set_val = 0
            else:
                set_val = 1

            releasecalendar(set_val, calend_fk, empl_fk)

        load_button = Button(root, text='Zaladuj', command=rlscalnd)
        load_button.pack()
        def back():
            root.destroy()
            grafik()
        back_button = Button(root, text='Wstecz', command=back)
        back_button.pack()

    def releasecalendar(var1, var2, var3):
        db = pymysql.connect('localhost', 'root', 'root', 'io')
        cursor = db.cursor()
        fetch_queries = "UPDATE graphic JOIN emploee_list ON emploee_list.id = graphic.emploee_list_fk JOIN calendar ON " \
                        "calendar.id = graphic.calendar_fk SET work= %s WHERE Datagr = %s AND Name =%s; "
        var = var1, var2, var3
        cursor.execute(fetch_queries, var)
        db.commit()
        db.close()

    def loadcalendar():
        # database connection
        db = pymysql.connect('localhost', 'root', 'root', 'io')
        # Make sure to initiate the cursor to fetch rows
        cursor = db.cursor()
        # fetch all the queries in students_info Table
        fetch_queries = 'Select emploee_list.Name, calendar.Datagr, ' \
                        'graphic.work, graphic.calendar_fk, graphic.emploee_list_fk From emploee_list Join graphic ON emploee_list.id = ' \
                        'graphic.emploee_list_fk Join calendar ON calendar.id = graphic.calendar_fk '

        # queries execution
        cursor.execute(fetch_queries)
        lines = cursor.fetchall()
        check = []
        for line in lines:
            check.append(line)
        # commit the connection
        check = pd.DataFrame(check)
        check.columns = ['Imie i Nazwisko', 'Data', 'Praca', 'id calendar', 'id emploee']
        check['Praca'] = check['Praca'].replace({0: 'Wolne', 1: 'Praca'})
        db.commit()

        # make a habit to close the database connection once you create it
        db.close()
        return check

    df = loadcalendar()

    root = Tk()
    root.geometry('800x600')
    root.title('Grafik pracy')
    values = ['Wszystkie'] + list(df['Imie i Nazwisko'].unique())
    selected = StringVar()

    options = OptionMenu(root, selected, *values)
    options.pack()

    disp_button = Button(root, text='Pokaz grafik', command=on_click)
    disp_button.pack()

    # frame for table and button "Next Data"
    frame_data = Frame(root)
    frame_data.pack()

    changegra_button = Button(root, text="Zmiana grafiku", command=graphiconn_button)
    changegra_button.pack()

    def logout():
        root.destroy()
        logowanie()
    wyloguj = Button(root, text='Wyloguj', command=logout)
    wyloguj.pack()

    # table with data - inside "frame_data" - without showing it
    table = Frame(frame_data)
    # table.grid(row=0, column=0)

    root.mainloop()


def kierownikm1():
    grafik()




def logout(root):
    root.destroy()
    logowanie()


def planistam1():
    root = Tk()
    root.title('Menu 1 - Planista')
    root.geometry("800x600")


    def myClick3():
        root.destroy()
        planistam2()

    myButton3 = Button(root, text='Planowanie srednio terminowe', command=myClick3)
    myButton3.pack()

    def logout():
        root.destroy()
        logowanie()
    wyloguj = Button(root, text='Wyloguj', command=logout)
    wyloguj.pack()


def planistam2():
    root = Tk()
    root.title('Menu planowania srednio terminowego - Planista')
    root.geometry("800x600")
    def back():
        root.destroy()
        planistam1()

    def myClick4():
        root.destroy()
        planistam3()


    myButton4 = Button(root, text='Capacity loading', command=myClick4)
    myButton4.pack()
    back = Button(root,text="Powrot",command=back)
    back.pack()

def planistam3():
    root = Tk()
    root.title('Capacity loading')
    root.geometry("800x600")
    def back():
        root.destroy()
        planistam2()
    back = Button(root,text="Powrot",command=back)
    back.pack()
logowanie()