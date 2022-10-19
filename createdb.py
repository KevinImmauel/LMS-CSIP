import mysql.connector

db = mysql.connector.connect(user='root',password='root',host='localhost')
cur = db.cursor()

def createdb():
    cur.execute('create database library')
    cur.execute('use library')
    cur.execute('create table lib (snobook int primary key not null, name varchar(30) not null, author varchar(30) not null, price int not null, pages int not null, available boolean not null);')
    cur.execute('create table record (sno int primary key not null, dofentry date not null, name varchar(30) not null, class varchar(10) not null, snobook int not null')
    db.commit()
