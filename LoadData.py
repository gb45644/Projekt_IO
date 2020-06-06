import pymysql


def sql(login, haslo):
    db = pymysql.connect('localhost', 'root', 'root', 'io')

    cursor = db.cursor()

    fetch_queries = 'Select * from credentials WHERE login LIKE %s;'

    cursor.execute(fetch_queries, login)
    lines=cursor.fetchall()
    for lines in lines:
        if lines[1] == login and lines[2] == haslo:
            flaga = lines[3]
            return flaga

def grafik(nazwisko):
    db = pymysql.connect('localhost', 'root', 'root', 'io')
    cursor = db.cursor()

    fetch_queries = 'Select emploee_list.id,  emploee_list.imie,  emploee_list.nazwisko, calendar.id, calendar.year, ' \
                    'calendar.month, calendar.day, calendar.work From emploee_list Join graphic ON emploee_list.id = ' \
                    'graphic.emploee_fk Join calendar ON calendar.id = graphic.calendar_fk  WHERE  nazwisko LIKE %s'


    cursor.execute(fetch_queries,nazwisko)
    lines=cursor.fetchall()
    for lines in lines:
        print(lines)


    db.commit()
    db.close()


grafik()