import libraryfunc

print('_'*50)
print('WELCOME')
print('_'*50)
print()
print('Chose your option: ')
print('1. Insert a book')
print('2. Search a book')
print('1. Insert a book')
print('1. Insert a book')

option = int(input('Enter your choice: '))

if option==1:
    libraryfunc.insertbook()
elif option==2:
    print('Chose your option: ')
    print('1. Search book by name')
    print('2. Search a book by author')

    opt2 = int(input('ChOSE AN OPTION: '))

    if opt2==1:
        libraryfunc.getbook()
    elif opt2==2:
        libraryfunc.getbookbyauthor()
