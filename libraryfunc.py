import mysql.connector
import main
from mysql.connector.errors import Error

db = mysql.connector.connect(user='root',password='root',host='localhost')

cur = db.cursor()

cur.execute('use library')
cur.execute('select * from lib')

data = cur.fetchall()
lenofdata = len(data)

def checkbook(book):
    names=[]
    for x in data:
        names.append(x[1])
    if book in names:
        return True
    else:
        False

def checkauthor(author):
    authors=[]
    for x in data:
        authors.append(x[2])
    if author in authors:
        return True
    else:
        return False

def checksno(sno):
    if sno >= len(data):
        return False
    else:
        return True

def insertbook():
    while True:
        try:
            name = input('Enter the name of the book: ')
            author = input( 'Enter the name of the author: ')
            price = int(input('Enter the price of the book: '))
            pages = int(input('Enter the number of pages ini the book: '))
            break
        except ValueError:
            print('Value Error! Please try again!')
    cur.execute('''insert into lib values("%d","%s","%s","%d","%d","%s")'''%(lenofdata+1,name,author,price,pages,'1'))
    try:
        db.commit()
        print('Book added successfully!')
    except mysql.connector.Error as err:
            print('ERROR! please try again...')
            print(err)
            insertbook()

def deletebook():
    book = input('Enter the name of the book to delete: ')
    if checkbook(book) == True:
        for i in data:
            if i[1]==book:
                cur.execute('''delete from lib where name="%s"'''%(book))
                db.commit()
                print('Book deleted successfully!')
    else:
        print('Book not in database! Please try again!')
        deletebook()

def updatebook():
    def inupbook(book,prop,newpropval):
        for i in data:
            if i[1]==book:
                cur.execute('''update lib set %s="%s" where name="%s"'''%(prop,newpropval,book))
                db.commit()
    book = input('Enter the name of the book you would like to update: ')
    if checkbook(book) == True:
        print('''
        CHOOSE AN OPTION
        1) CHANGE NAME OF THE BOOK
        2) CHANGE AUTHOR OF THE BOOK
        3) CHANGE NUMBER OF PAGES
        4) CHANGE PRICE
        ''')
        optupbook = int(input('Enter your choice: '))
        if optupbook==1:
            newpropval = input('Enter new name of the book: ')
            inupbook(book,'name',newpropval)
        elif optupbook==2:
            newpropval = input('Enter new name of the author: ')
            inupbook(book,'author',newpropval)
        elif optupbook==3:
            newpropval = int(input('Enter new number of pages: '))
            inupbook(book,'pages',newpropval)
        elif optupbook==4:
            while True:
                try:
                    newpropval = int(input('Enter new price: '))
                    inupbook(book,'price',newpropval)
                except ValueError:
                    print('Please enter an integer')
                    updatebook()
        print('Book updated successfully!')
    else:
        print('Book not in database! Please try again')
        updatebook()

def getbook():
    print('''
        CHOOSE AN OPTION
        1) SEARCH BOOK BY NAME
        2) SEARCH BOOK BY AUTHOR
        3) GO BACK
        ''')
    optgb = int(input('Enter your choice :'))
    if optgb == 1:
        book = input('Enter a book name: ')
        if checkbook(book) == True:
            for i in data:
                if i[1] == book:
                    print(f'Book No.{i[0]}, {i[1]} written by {i[2]}.')
        else:
            print('Book does not exist! Try again!')
            getbook()
    elif optgb == 2:
        author = input('Enter an author name: ')
        if checkauthor(author) == True:
            for i in data:
                if i[2] == author:
                    print(f'Book No.{i[0]}, {i[1]} written by {i[2]}.')
        else:
            print('Author does not exist! Try again!')
            getbook()
    elif optgb == 3:
        main.libscreen()

def borrowbook(bookno):
    for i in data:
        if i[0]==bookno:
            cur.execute('''update lib set available="0" where snobook="%s"'''%(bookno))
            db.commit()
            print('UPDATED DATABASE SUCCESFULLY')

def returnbook(bookno):
    for i in data:
        if i[0]==bookno:
            cur.execute('''update lib set available="1" where snobook="%s"'''%(bookno))
            db.commit()
            print('UPDATED DATABASE SUCCESFULLY')

def checkbookavail(bookno):
    for i in data:
        if i[0]==bookno:
            if i[-1]==1:
                print('Book is Available!')
            else:
                print('Book is not available!')

#THIS FILE CONTAINS 159 LINES