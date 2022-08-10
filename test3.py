import mysql.connector as connection
mydb=connection.connect(host='localhost',user='root',passwd='Nksdr957.',database='aaa')
cursor=mydb.cursor()

##### create and insert into table .........................
cursor.execute('create table if not exists aa(id int primary key,name varchar(20),dob date)')
cursor.execute('show tables')
tables=cursor.fetchall()
print(tables)

table=input('write table name :- ')
if (table,) in tables:
    cursor.execute(f"insert into {table} values(100,'rahul','1999-12-12') ")
    cursor.execute(f'select * from {table}')
    tbl=cursor.fetchall()
    for tb in tbl:
        print(tb)
