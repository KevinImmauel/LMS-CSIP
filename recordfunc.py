import mysql.connector

db2 = mysql.connector.connect(user='root',password='root',host='localhost')

cur2 = db2.cursor()

cur2.execute('use library')
cur2.execute('select * from record')

data = cur2.fetchall()
lenofdata = len(data)

def insertrecord(name,classs,date,bookno):
    cur2.execute('''insert into record values(%d,"%s","%s","%s",%d)'''%(lenofdata+1,date,name,classs,bookno))
    db2.commit()

#THIS FILE CONTAINS 17 LINES