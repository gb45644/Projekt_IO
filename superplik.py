import tkinter as tk
import pandas as pd
import pymysql

# --- functions ---

def showdata():
    global table

    # destroy old frame with table
    if table:
        table.destroy()

    # create new frame with table
    table = tk.Frame(frame_data)
    table.grid(row=0, column=0)

    # fill frame with table
    row, column = df2.shape
    for r in range(row):
        for c in range(column):
            e1 = tk.Entry(table)
            e1.insert(1, df2.iloc[r, c])
            e1.grid(row=r, column=c, padx=2, pady=2)
            e1.config(state='disabled')

def on_click():
    global df2

    val = selected.get()

    if val == 'all':
        df2 = df
        #next_button.grid_forget()
    else:
        df2 = df[ df['Imie i Nazwisko'] == val ]
        #next_button.grid(row=1, column=0)

    print(df2)
    showdata()
    next_button.grid(row=1, column=0)

# --- main ---

frame_data = None

def loadcalendar():
    #database connection
    db = pymysql.connect('localhost', 'root', 'root', 'io')
    #Make sure to initiate the cursor to fetch rows
    cursor = db.cursor()
    # fetch all the queries in students_info Table
    fetch_queries ='Select emploee_list.Name, calendar.Datagr, ' \
                    'calendar.work From emploee_list Join graphic ON emploee_list.id = ' \
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

root = tk.Tk()

values = ['all'] + list(df['Imie i Nazwisko'].unique())
selected = tk.StringVar()

options = tk.OptionMenu(root, selected, *values)
options.pack()

button = tk.Button(root, text='OK', command=on_click)
button.pack()

# frame for table and button "Next Data"
frame_data = tk.Frame(root)
frame_data.pack()

exit_button = tk.Button(root, text="EXIT", command=root.destroy)
exit_button.pack()

# table with data - inside "frame_data" - without showing it
table = tk.Frame(frame_data)
#table.grid(row=0, column=0)




root.mainloop()