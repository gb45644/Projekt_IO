from tkinter import *
import pandas as pd
import pymysql

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



# --- functions ---
def grafik():

    def showdata():
        frame_data = Frame(root)
        frame_data.pack()

        # destroy old frame with table
        def destroy():
            root.destroy()
            grafik()

        des_butt = Button(root, text='Zresetuj', command=destroy)
        des_butt.pack()

        table = Frame(frame_data)
        table.grid(row=0, column=0)

        # fill frame with table
        row, column = df2.shape
        for r in range(row):
            for c in range(3):
                e1 = Entry(table)
                e1.insert(1, df2.iloc[r, c])
                e1.grid(row=r, column=c, padx=2, pady=2)
                e1.config(state='disabled')

    def on_click():
        global df2

        val = selected.get()

        if val == 'Wszystkie':
            df2 = df
            # next_button.grid_forget()
        else:
            df2 = df[df['Imie i Nazwisko'] == val]
            # next_button.grid(row=1, column=0)

        showdata()

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

    exit_button = Button(root, text="Wyjscie", command=root.destroy)  # trzepa podpiac powrót do poprzedniego menu
    exit_button.pack()

    # table with data - inside "frame_data" - without showing it
    table = Frame(frame_data)
    # table.grid(row=0, column=0)

    root.mainloop()

