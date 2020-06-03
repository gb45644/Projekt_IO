import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='io')

cursor = db.cursor()

fetch_queries = 'Select * from standardy;'

cursor.execute(fetch_queries)
lines=cursor.fetchall()
for lines in lines:
    print(lines)




db.commit()
db.close()