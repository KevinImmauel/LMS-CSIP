import libraryfunc
from datetime import date

print('_'*50)
print('WELCOME')
print('_'*50)
print()
print('''CHOOSE AN OPTION
1) GO TO LIBRARY DATABASE
2) GO TO LIBRARY RECORDS''')
option = int(input('Enter your choice: '))
if option==1:
    print('''
    CHOOSE AN OPTION
    1) ADD A BOOK
    2) DELETE A BOOK
    3) UPDATE A BOOK
    4) SEARCH A BOOK
    5) SEARCH AN AUTHOR''')
    optdb = int(input('Enter your choice: '))
    if optdb==1:
        libraryfunc.insertbook()
    elif optdb==2:
        book = input('Enter the name of the book to delete: ')
        libraryfunc.deletebook(book)
        print('DATABASE UPDATED SUCCESSFULLY')
    elif optdb==3:
        book = input('Enter the name of the book you would like to update: ')
        print('''
        CHOOSE AN OPTION
        1) CHANGE NAME OF THE BOOK
        2) CHANGE AUTHOR OF THE BOOK
        3) CHANGE NUMBER OF PAGES
        4) CHANGE PRICE''')
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
    elif optdb==4:
        print('''
        CHOOSE AN OPTION
        1) SEARCH BOOK BY NAME
        2) SEARCH BOOK BY AUTHOR''')
        optserbook = int(input('Enter your choice: '))
        if optserbook==1:
            book = input('Enter the name of the book: ')
            libraryfunc.getbook(book)
        elif optserbook==2:
            author = input('Enter the name of the author: ')
            libraryfunc.getbookbyauthor(author)
    elif optdb==5:
        author = input('Enter the name of the author: ')
        libraryfunc.getbookbyauthor(author)
else:
    print('''
    CHOOSE AN OPTION
    1) BORROW A BOOK
    2) RETURN A BOOK
    3) CHECK BOOK AVAILABILITY''')

    optrecord = int(input('Enter your choice: '))

    if optrecord==1:
        print('ENTER YOUR DETAILS BELOW')
        name = input('Enter your name: ')
        classs = input('Enter your class: ')
        today = date.today()
        bookno = int(input('Enter book serial number: '))

