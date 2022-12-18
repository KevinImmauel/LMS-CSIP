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
    while True:
        try:
            opt = int(input('Enter you choice: '))
            break
        except ValueError:
            print('Value Error! Please try again')
            mainscreen()
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
    5) CHECK BOOK AVAILABILITY
    6) GO BACK TO MAIN SCREEN
    ''')
    while True:
        try:
            optdb = int(input('Enter you choice: '))
            break
        except ValueError:
            print('Value Error! Please try again')
            libscreen()
    if optdb==1:
        libraryfunc.insertbook()
        print('DATABASE UPDATED SUCCESSFULLY')
        libscreen()
    elif optdb==2:
        libraryfunc.deletebook()
        print('DATABASE UPDATED SUCCESSFULLY')
        libscreen()
    elif optdb==3:
        libraryfunc.updatebook()
        print('DATABASE UPDATED SUCCESSFULLY')
        libscreen()
    elif optdb==4:
        libraryfunc.getbook()
        libscreen()
    elif optdb==5:
        while True:
            try:
                bookno = int(input('Enter book serial number: '))
                break
            except ValueError:
                print('Value Error! Please try again!')
        libraryfunc.checkbookavail(bookno)
        libscreen()
    elif optdb==6:
        mainscreen()

def recscreen():
    print('''
    CHOOSE AN OPTION
    1) BORROW A BOOK
    2) RETURN A BOOK
    3) CHECK BOOK AVAILABILITY
    4) BACK TO MAIN PAGE
    ''')

    while True:
        try:
            optrecord = int(input('Enter you choice: '))
            break
        except ValueError:
            print('Value Error! Please try again')
            recscreen()

    if optrecord==1:
        print('ENTER YOUR DETAILS BELOW')
        name = input('Enter your name: ')
        classs = input('Enter your class: ')
        today = date.today()
        while True:
            try:
                bookno = int(input('Enter book serial number: '))
                break
            except ValueError:
                print('Value Error! Please try again!')
        if libraryfunc.checksno(bookno) == True:
            libraryfunc.borrowbook(bookno)
            recordfunc.insertrecord(name,classs,today,bookno)
            print('BORROWED BOOK SUCCESSFULLY!')
        else:
            print('Try again!')
        recscreen()
    elif optrecord==2:
        print('ENTER YOUR DETAILS BELOW')
        name = input('Enter your name: ')
        classs = input('Enter your class: ')
        today = date.today()
        while True:
            try:
                bookno = int(input('Enter book serial number: '))
                break
            except ValueError:
                print('Value Error! Please try again!')
        if libraryfunc.checksno(bookno) == True:
            libraryfunc.returnbook(bookno)
            recordfunc.insertrecord(name,classs,today,bookno)
            print('RETURNED BOOK SUCCESSFULLY!')
        else:
            print('Try again!')
        recscreen()
    elif optrecord==3:
        while True:
            try:
                bookno = int(input('Enter book serial number: '))
                break
            except ValueError:
                print('Value Error! Please try again!')
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

    AND WITH THE SPECIAL GUIDANCE OF OUR COMPUTER SCIENCE TEACHER MRS.LEENA

    ''')
    abtopt = input('Enter to go back to main screen')
    if abtopt!='':
        mainscreen()
    else:
        mainscreen()