from tkinter import *
import pandas as pd
import pymysql

# --- functions ---

def showdata():
    global table

    # destroy old frame with table
    if table:
        table.destroy()

    # create new frame with table
    table = Frame(frame_data)
    table.grid(row=0, column=0)

    # fill frame with table
    row, column = df2.shape
    for r in range(row):
        for c in range(column):
            e1 = Entry(table)
            e1.insert(1, df2.iloc[r, c])
            e1.grid(row=r, column=c, padx=2, pady=2)
            e1.config(state='disabled')

def on_click():
    global df2

    val = selected.get()

    if val == 'Wszystkie':
        df2 = df
        #next_button.grid_forget()
    else:
        df2 = df[ df['Imie i Nazwisko'] == val ]
        #next_button.grid(row=1, column=0)

    showdata()
    next_button.grid(row=1, column=0)




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
    selected = StringVar()

    options = OptionMenu(root, selected, *values)
    options.pack()

    values2 = list(df['Data'].unique())
    selected2 = StringVar()

    options2 = OptionMenu(root, selected2, *values2)
    options2.pack()

    values3 = list(df['Praca'].unique())
    selected3 = StringVar()

    options3 = OptionMenu(root, selected3, *values3)
    options3.pack()




def loadcalendar():
    #database connection
    db = pymysql.connect('localhost', 'root', 'root', 'io')
    #Make sure to initiate the cursor to fetch rows
    cursor = db.cursor()
    # fetch all the queries in students_info Table
    fetch_queries ='Select emploee_list.Name, calendar.Datagr, ' \
                    'graphic.work From emploee_list Join graphic ON emploee_list.id = ' \
                    'graphic.emploee_list_fk Join calendar ON calendar.id = graphic.calendar_fk '


    #queries execution
    cursor.execute(fetch_queries)
    lines = cursor.fetchall()
    check = []
    for line in lines:
       check.append(line)
    #commit the connection
    check = pd.DataFrame(check)
    check.columns = ['Imie i Nazwisko', 'Data', 'Praca']
    check['Praca'] = check['Praca'].replace({0:'Wolne', 1: 'Praca'})
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

exit_button = Button(root, text="Wyjscie", command=root.destroy) #trzepa podpiac powrót do poprzedniego menu
exit_button.pack()

# table with data - inside "frame_data" - without showing it
table = Frame(frame_data)
#table.grid(row=0, column=0)




root.mainloop()