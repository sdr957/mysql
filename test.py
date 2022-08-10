import mysql.connector as conn
mydb=conn.connect(host='localhost',user='root',passwd='Nksdr957.')
cursor=mydb.cursor()

cursor.execute('show databases')
databases=cursor.fetchall()

        ##  create database , if not exists...............
db=input("Enter database name ")
if (db,)in databases:
    print('Database already exists....')
else:
    cursor.execute(f"create database if not exists {db}")
    print(f'{db} Database created successfully....')
