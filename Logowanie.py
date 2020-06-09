# from LoadData import *
from tkinter import *
import pandas as pd
import pymysql
from pandastable import Table
import numpy as np
from tkinter import messagebox



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

    theLabel1 = Label(root, text='Ultimate planning tool', font=('Arial', 24))
    theLabel1.configure(background='white')
    theLabel1.pack()

    theLabel2 = Label(root, text='Login:', font=('Arial', 18))
    theLabel2.configure(background='white')
    theLabel2.pack()

    polelogin = Entry(root, width=50)
    polelogin.pack()

    theLabel3 = Label(root, text='Hasło:', font=('Arial', 18))
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
        elif access == 4:
            root.destroy()
            kierownikm1()
        else:
            wrong()
    def wrong():
        top = Tk()
        top.eval('tk::PlaceWindow %s center' % top.winfo_toplevel())
        top.withdraw()
        messagebox.showwarning(title="Blad", message='Zly login i/lub haslo!')
        top.deiconify()
        top.destroy()
    def myClick2():
        root.destroy()
    def zmiana_hasla():
        root.destroy()
        haslo()
    myButton = Button(root, text='Zaloguj się', command=myClick)
    myButton.pack()


    zmiana = Button(root, text='Zmien haslo', command=zmiana_hasla)
    zmiana.pack()
    myButton2 = Button(root, text='Wyjdź', command=myClick2)
    myButton2.pack()
    root.mainloop()
def haslo():

    db = pymysql.connect('localhost', 'root', 'root', 'io')
    cursor = db.cursor()
    root = Tk()
    root.configure(background='white')
    login_u = Label(root, text='Login:', font=('Arial', 10))
    login_u.configure(background='white')
    login_u.pack()
    polelogin = Entry(root, width=50)
    polelogin.pack()
    st_haslo = Label(root, text='Stare Hasło:', font=('Arial', 10))
    st_haslo.configure(background='white')
    st_haslo.pack()
    pole_st = Entry(root, width=50, show='*')
    pole_st.pack()
    new_haslo = Label(root, text='Nowe Hasło(Min. 8 znakow):', font=('Arial', 10))
    new_haslo.configure(background='white')
    new_haslo.pack()
    new_pole = Entry(root, width=50, show='*')
    new_pole.pack()
    pow_haslo = Label(root, text='Powtorz Hasło:', font=('Arial', 10))
    pow_haslo.configure(background='white')
    pow_haslo.pack()
    pow_pole = Entry(root, width=50, show='*')
    pow_pole.pack()

    def zmiana():
        log = polelogin.get()
        new_haslo = new_pole.get()
        pow_haslo = pow_pole.get()
        st_haslo = pole_st.get()
        fetch_queries = 'Select * from credentials WHERE login LIKE %s;'
        cursor.execute(fetch_queries, log)
        lines = cursor.fetchall()
        for lines in lines:
            if lines[1] == log and lines[2] == st_haslo:
                if len(new_haslo) == 0 and len(pow_haslo) == 0:
                    empty()
                elif new_haslo == pow_haslo:
                    if len(new_haslo) < 8:
                        short()
                    else:
                        cursor.execute("UPDATE credentials SET pass = %s WHERE pass = %s ", (new_haslo, st_haslo))
                        db.commit()
                        success()
                else:
                    not_same()
            else:
                wrong()

    def empty():
        top = Tk()
        top.eval('tk::PlaceWindow %s center' % top.winfo_toplevel())
        top.withdraw()
        messagebox.showwarning(title="Blad", message='Pole/a PUSTE!')
        top.deiconify()
        top.destroy()
    def success():
        top = Tk()
        top.eval('tk::PlaceWindow %s center' % top.winfo_toplevel())
        top.withdraw()
        messagebox.showinfo(title="Zmiana", message='Zmieniono haslo!!')
        top.deiconify()
        top.destroy()
        root.destroy()
        logowanie()

    def not_same():
        top = Tk()
        top.eval('tk::PlaceWindow %s center' % top.winfo_toplevel())
        top.withdraw()
        messagebox.showwarning(title="Blad", message='Hasla roznia sie!')
        top.deiconify()
        top.destroy()
    def wrong():
        top = Tk()
        top.eval('tk::PlaceWindow %s center' % top.winfo_toplevel())
        top.withdraw()
        messagebox.showwarning(title="Blad", message='Zly login i/lub haslo!')
        top.deiconify()
        top.destroy()
    def short():
        top = Tk()
        top.eval('tk::PlaceWindow %s center' % top.winfo_toplevel())
        top.withdraw()
        messagebox.showwarning(title="Blad", message='Haslo jest za krotkie!')
        top.deiconify()
        top.destroy()
    def accept():
        zmiana()
    akceptuj = Button(root, text='Zmien', command= accept)
    akceptuj.pack()
    def back():
        root.destroy()
        logowanie()

    wyloguj = Button(root, text='Wstecz', command=back)
    wyloguj.pack()

    root.mainloop()

def nowy():
    root = Tk()
    root.geometry("800x600")
    db = pymysql.connect('localhost', 'root', 'root', 'io')
    imie = Label(root, text='Imie:', font=('Arial', 10))
    imie.configure(background='white')
    imie.pack()

    poleimie = Entry(root, width=20)
    poleimie.pack()

    nazwisko = Label(root, text='Nazwisko:', font=('Arial', 10))
    nazwisko.configure(background='white')
    nazwisko.pack()

    polenazwisko = Entry(root, width=20)
    polenazwisko.pack()

    def add():
        name = poleimie.get()
        sur = polenazwisko.get()
        name_digit = False
        sur_digit = False
        for character in name:
            if character.isdigit():
                name_digit = True
        for letter in sur:
            if letter.isdigit():
                sur_digit = True

        def empty():
            top = Tk()
            top.eval('tk::PlaceWindow %s center' % top.winfo_toplevel())
            top.withdraw()
            messagebox.showwarning(title="Blad", message='Pole Imie i/lub Nazwisko jest PUSTE!')
            top.deiconify()
            top.destroy()

        def nodigit():
            top = Tk()
            top.eval('tk::PlaceWindow %s center' % top.winfo_toplevel())
            top.withdraw()
            messagebox.showwarning(title="Blad", message='Imie i/lub Nazwisko zawiera LICZBE!')
            top.deiconify()
            top.destroy()

        def success():
            top = Tk()
            top.eval('tk::PlaceWindow %s center' % top.winfo_toplevel())
            top.withdraw()
            messagebox.showinfo(title="Zrobione", message='Dodano pracownika!!')
            top.deiconify()
            top.destroy()

        if len(name) == 0 or len(sur) == 0:
            empty()
        elif name_digit == True or sur_digit == True:
            nodigit()
        else:
            success()

            cursor = db.cursor()
            id_em = 'SELECT COUNT(*) FROM emploee_list'
            cursor.execute(id_em)
            id_emp = cursor.fetchall()
            last_id = id_emp[0][0] + 1

            id_cal = 'SELECT COUNT(*) FROM graphic'
            cursor.execute(id_cal)
            id_cale = cursor.fetchall()
            last_cal = id_cale[0][0] + 1
            full = name + ' ' + sur

            insert_name = 'INSERT INTO emploee_list (Name, id) VALUES (%s,%s);'

            cursor.execute(insert_name, (full, last_id))

            select_id = 'SELECT id FROM emploee_list WHERE Name LIKE %s;'
            cursor.execute(select_id, full)
            em_fk = cursor.fetchall()
            emp_fk = em_fk[0][0]
            num_cal = 'SELECT COUNT(*) FROM calendar;'
            cursor.execute(num_cal)
            cal_cnt = cursor.fetchall()
            end = cal_cnt[0][0]
            temp = np.arange(1, end + 1, 1)
            for i in range(np.size(temp)):
                cursor.execute("INSERT INTO graphic (id, calendar_fk, emploee_list_fk, work) VALUES (%s, %s, %s, 1);",
                               (last_cal + i, i + 1, emp_fk))
                db.commit()

    dodajcos = Button(root, text='Dodaj pracownika', command=add)
    dodajcos.pack()

    def back():
        root.destroy()
        kierownikm1()

    back = Button(root, text='Wstecz', command=back)
    back.pack()
    root.mainloop()


def usun():
    root = Tk()
    root.geometry("800x600")
    db = pymysql.connect('localhost', 'root', 'root', 'io')

    cursor = db.cursor()
    cursor.execute("SELECT Name FROM emploee_list")
    lines = cursor.fetchall()
    df = []
    for line in lines:
        df.append(line)
    df = pd.DataFrame(df)
    df.columns = ['Imie i Nazwisko']
    select_d = df['Imie i Nazwisko'].unique()
    sel2 = StringVar()
    list = OptionMenu(root, sel2, *select_d)
    list.pack()

    def sure():
        top = Tk()
        top.eval('tk::PlaceWindow %s center' % top.winfo_toplevel())
        top.withdraw()

        response = messagebox.askyesno(title="Usun", message='Czy na pewno chcesz to zrobic?', )
        if response == False:
            print("nieee")
            root.destroy()
            usun()
        top.deiconify()
        top.destroy()

    def remove(dele):
        full = dele

        def success():
            top = Tk()
            top.eval('tk::PlaceWindow %s center' % top.winfo_toplevel())
            top.withdraw()
            messagebox.showinfo(title="Zrobione", message='Usunieto pracownika!!')
            top.deiconify()
            top.destroy()
            root.destroy()
            usun()

        select_id = 'SELECT id FROM emploee_list WHERE Name LIKE %s;'
        cursor.execute(select_id, full)
        em_fk = cursor.fetchall()
        emp_fk = em_fk[0][0]
        num_cal = 'SELECT COUNT(*) FROM calendar;'
        cursor.execute(num_cal)
        cal_cnt = cursor.fetchall()
        end = cal_cnt[0][0]
        temp = np.arange(1, end + 1, 1)
        for i in range(np.size(temp)):
            cursor.execute("DELETE FROM graphic WHERE calendar_fk = %s AND emploee_list_fk = %s;", (i + 1, emp_fk))

        cursor.execute("DELETE FROM emploee_list WHERE Name = %s;", full)
        db.commit()
        success()

    def delete():
        sure()
        dele = sel2.get()
        remove(dele)

    del_button = Button(root, text='Usun pracownika', command=delete)
    del_button.pack()

    def back():
        root.destroy()
        kierownikm1()

    back = Button(root, text='Wstecz', command=back)
    back.pack()
    root.mainloop()


def grafik():
    def showdata(df2):
        frame_data = Frame(root)

        frame_data.pack(fill=BOTH, expand=1)

        df2 = df2.drop(['id calendar', 'id emploee'], axis=1)
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

    def add_work():
        root.destroy()
        nowy()

    dodaj_n = Button(root, text='Dodaj pracownika', command=add_work)
    dodaj_n.pack()

    def del_work():
        root.destroy()
        usun()

    dodaj_n = Button(root, text='Usun pracownika', command=del_work)
    dodaj_n.pack()

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


# def planistam1():
#     root = Tk()
#     root.title('Menu 1 - Planista')
#     root.geometry("800x600")
#
#     def myClick3():
#         root.destroy()
#         planistam2()
#
#     myButton3 = Button(root, text='Planowanie srednio terminowe', command=myClick3)
#     myButton3.pack()
#
#     def logout():
#         root.destroy()
#         logowanie()
#
#     wyloguj = Button(root, text='Wyloguj', command=logout)
#     wyloguj.pack()


def planistam1():
    root = Tk()
    root.title('Menu planowania srednio terminowego - Planista')
    root.geometry("800x600")



    def myClick4():
        root.destroy()
        planistam2()

    def logout():
        root.destroy()
        logowanie()


    myButton4 = Button(root, text='Capacity loading', command=myClick4)
    myButton4.pack()
    wyloguj = Button(root, text='Wyloguj', command=logout)
    wyloguj.pack()


def planistam2():
    capacity_loading()


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






    linesdrop = wolist.drop(columns=[0,1,2,3,4,6,7])
    linesdrop = linesdrop.drop_duplicates(subset=[5])
    wolist.columns = ['numer zlecenia', 'amount', 'data', 'indeks', 'opis', 'line', 'predkosc', 'week']
    wolist['lin cap'] = wolist['predkosc'] * 24 * 5
    # wolist = wolist.drop(['numer zlecenia','data','indeks','opis','predkosc'], axis=1)
    # wolist = wolist[['num tyg','linia','ilosc','lin cap']]
    # wolist = wolist.sort_values(by=['num tyg'])
    # temp = wolist.groupby('num tyg')['ilosc'].sum()
    demandreport = pd.pivot_table(wolist, values=['amount', 'lin cap'], index=['week'], columns=['line'], aggfunc={'amount': np.sum, 'lin cap': np.mean})
    demandreport = demandreport.replace(to_replace=np.nan, value=0)

    frame_data = Frame(root)

    frame_data.pack(fill=BOTH, expand=1)

    pt = Table(frame_data, dataframe=demandreport, width=100, showtoolbar=True, showstatusbar=True)
    pt.showIndex()
    pt.show()

    #both = pd.merge(spacereport, demandreport, 'left', on= 'linia')

    def back():
        root.destroy()
        planistam1()

    back = Button(root, text="Powrot", command=back)
    back.pack()
    root.mainloop()

logowanie()
