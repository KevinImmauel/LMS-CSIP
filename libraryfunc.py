import mysql.connector

db = mysql.connector.connect(user='root',password='root',host='localhost')

cur = db.cursor()

cur.execute('use library')
cur.execute('select * from lib')

data = cur.fetchall()
lenofdata = len(data)

def insertbook():
    name = input('Enter the name of the book: ')
    author = input( 'Enter the name of the author: ')
    price = int(input('Enter the price of the book: '))
    pages = int(input('Enter the number of pages ini the book: '))
    cur.execute('''insert into lib values("%d","%s","%s","%d","%d","%s")'''%(lenofdata+1,name,author,price,pages,'1'))
    db.commit()
    print('Book added successfully!')

def deletebook(book):
    for i in data:
        if i[1]==book:
            cur.execute('''delete from table lib where name="%s"'''%(book))
            db.commit()
            print('Book deleted successfully!')

def updatebook(book,prop,newpropval):
    for i in data:
        if i[1]==book:
            cur.execute('''update lib set %s="%s" where name="%s"'''%(prop,newpropval,book))
            db.commit()

def getbook(book):
    for i in data:
        if i[1] == book:
            print(f'{i[1]}, A book written by {i[2]}, contains {i[4]} pages only for {i[3]}$')

def getbookbyauthor(author):
    for i in data:
        if i[2]==author:
            print(f'{i[1]}, A book written by {i[2]}, contains {i[4]} pages only for {i[3]}$')

def getbooksbyauthor(author):
    for i in data:
        if i[2]==author:
            print()

def borrowbook(bookno):
    for i in data:
        if i[0]==bookno:
            cur.execute('''update lib set available="0" where sno="%s"'''%(bookno))
            db.commit()
            print('UPDATED DATABASE SUCCESFULLY')

def returnbook(bookno):
    for i in data:
        if i[0]==bookno:
            cur.execute('''update lib set available="1" where sno="%s"'''%(bookno))
            db.commit()
            print('UPDATED DATABASE SUCCESFULLY')

def checkbookavail(bookno):
    for i in data:
        if i[0]==bookno:
            if i[-1]==1:
                print('Book is Available!')
            else:
                print('Book is not available!')