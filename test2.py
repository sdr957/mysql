import mysql.connector as connection


mydb=connection.connect(host='localhost',user='root',passwd='Nksdr957.')
cursor=mydb.cursor()

cursor.execute('show databases')
databases=cursor.fetchall()


####### Fetching  and establishing connection databases for manupulation........

for dbs in databases:
    print(dbs)

print('             ')
# choosing database for established
db = input('choose any database :> ')

if (db,) in databases:
    mydb2=connection.connect(host='localhost',user='root',passwd='Nksdr957.',database=f'{db}')
    print(' databases connection established ..')
    curr=mydb2.cursor()

#   insert data into existing table OR, create new table  .................
    curr.execute('show tables')
    tabless=curr.fetchall()
    print(tabless)

    x= input('1 -> create table  \n2 -> choose table\nenter 1 or 2 :-')
    if x=='1':
        table_name=input('Enter table name ')
        curr.execute(f'create table {table_name}(id int,name varchar(20),dob DATE)')
        print(f'{table_name} table created successfully...')
        id = int(input('enter id :-'))
        name= input('enter name :-')
        dob = input('date of birth :-')
        curr.execute(f'insert into {table_name} values({id},"{name}","{dob}")')
        mydb2.commit()
        value = input('yes :> to show tables or no :> do not show tables')
        if value =='yes':
            curr.execute(f'select * from {table_name}')
            tbl=curr.fetchall()
            for tb in tbl:
                print(tb)


    else:
        tables=input('choose table :-')
        if (tables,) in tabless:
            id=int(input('enter id :-'))
            name=input('enter name :-')
            dob=input('date of birth :-')
            curr.execute(f'insert into {tables} values({id},"{name}","{dob}")')
            mydb2.commit()
            value = input('yes :> to show tables or\n no :> do not show tables\n yes or no :> ')
            if value =='yes':
                curr.execute(f'select * from {tables}')
                tbl=curr.fetchall()
                for tb in tbl:
                    print(tb)

else:
    print(f'{db} database not exists')




