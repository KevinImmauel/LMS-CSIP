import libraryfunc
import recordfunc
from datetime import date

def mainscreen():
    print('''
    WELCOME TO THE SCHOOL LIBRARY
    
    CHOOSE AN OPTION
    1) THE LIBRARY DATABSE
    2) THE LIBRARY RECORDS
    3) ABOUT THE LIBRARY MANGEMENT SYSTEM
    4) EXIT
    ''')
    opt = int(input('Enter you choice: '))
    if opt==1:
        libscreen()
    elif opt==2:
        recscreen()
    elif opt==3:
        abtscreen()
    else:
        print('YOU WILL NOW EXIT THE PROGRAM')
        exit()
    
def libscreen():
    print('''
    CHOOSE AN OPTION
    1) ADD A BOOK
    2) DELETE A BOOK
    3) UPDATE A BOOK
    4) SEARCH A BOOK
    5) GO BACK TO MAIN SCREEN
    ''')
    optdb = int(input('Enter your choice: '))
    if optdb==1:
        libraryfunc.insertbook()
        print('DATABASE UPDATED SUCCESSFULLY')
        libscreen()
    elif optdb==2:
        book = input('Enter the name of the book to delete: ')
        libraryfunc.deletebook(book)
        print('DATABASE UPDATED SUCCESSFULLY')
        libscreen()
    elif optdb==3:
        book = input('Enter the name of the book you would like to update: ')
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
            libraryfunc.updatebook(book,'name',newpropval)
        elif optupbook==2:
            newpropval = input('Enter new name of the author: ')
            libraryfunc.updatebook(book,'author',newpropval)
        elif optupbook==3:
            newpropval = int(input('Enter new number of pages: '))
            libraryfunc.updatebook(book,'pages',newpropval)
        elif optupbook==4:
            newpropval = int(input('Enter new price: '))
            libraryfunc.updatebook(book,'price',newpropval)
        libscreen()
    elif optdb==4:
        print('''
        CHOOSE AN OPTION
        1) SEARCH BOOK BY NAME
        2) SEARCH BOOK BY AUTHOR
        ''')
        optserbook = int(input('Enter your choice: '))
        if optserbook==1:
            book = input('Enter the name of the book: ')
            libraryfunc.getbook(book)
        elif optserbook==2:
            author = input('Enter the name of the author: ')
            libraryfunc.getbookbyauthor(author)
        libscreen()
    elif optdb==5:
        mainscreen()

def recscreen():
    print('''
    CHOOSE AN OPTION
    1) BORROW A BOOK
    2) RETURN A BOOK
    3) CHECK BOOK AVAILABILITY
    4) BACK TO MAIN PAGE
    ''')

    optrecord = int(input('Enter your choice: '))

    if optrecord==1:
        print('ENTER YOUR DETAILS BELOW')
        name = input('Enter your name: ')
        classs = input('Enter your class: ')
        today = date.today()
        bookno = int(input('Enter book serial number: '))
        libraryfunc.borrowbook(bookno)
        recordfunc.insertrecord(name,classs,today,bookno)
        print('BORROWED BOOK SUCCESSFULLY!')
        recscreen()
    elif optrecord==2:
        print('ENTER YOUR DETAILS BELOW')
        name = input('Enter your name: ')
        classs = input('Enter your class: ')
        today = date.today()
        bookno = int(input('Ent(er book serial number: '))
        recordfunc.insertrecord(name,classs,today,bookno)
        libraryfunc.returnbook(bookno)
        recscreen()
    elif optrecord==3:
        bookno = int(input('Enter Book serial number: '))
        libraryfunc.checkbookavail(bookno)
        recscreen()
    elif optrecord==4:
        mainscreen()

def abtscreen():
    print('''
    SCHOOL LIBRARY MANAGEMENT SYSTEM
    PROGRAM MADE BY STUDENTS OF KENDRIYA VIDYALAYA NO.2 :
    AVINASH
    KEVIN IMMANUEL
    SANCHIT SAINI
    ''')
    abtopt = input('Enter to go back to main screen')
    if abtopt!='':
        mainscreen()
    else:
        mainscreen()