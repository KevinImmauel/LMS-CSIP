import mysql.connector

db = mysql.connector.connect(user='root',password='root',host='localhost')
cur = db.cursor()

cur.execute('create database library')
cur.execute('use library')
cur.execute('create table lib (sno int primary key not null, name varchar(30) not null, author varchar(30) not null, price int not null, pages int not null, available boolean not null);')
db.commit()
