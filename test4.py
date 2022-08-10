import mysql.connector as connection
mydb=connection.connect(host='localhost',user='root',passwd='Nksdr957.',database='aaa')

cur=mydb.cursor()
cur.execute('create table if not exists bank_details(age int,job varchar(20),marital varchar(20),education varchar(20),`default` varchar(20),balance int,housing varchar(20),loan varchar(20),contact varchar(20),`day` int,`month` varchar(20),duration int,campaign int,pdays int,previous int,poutcome varchar(20),y varchar(20))')

cur.execute('select * from bank_details')
table=cur.fetchall()
for tb in table:
    print(tb)
cur.execute('select age,job from bank_details')
print([x for x in cur.fetchall()])

# where
cur.execute('select marital from bank_details where age=42')
print(cur.fetchall())
cur.execute('select age,job,marital from bank_details where `default`="no"')
print([x for x in cur.fetchall()])
cur.execute('select * from bank_details where age=42 and balance<100')
print([x for x in cur.fetchall()])

#order by
cur.execute('select * from bank_details order by age')
print([x for x in cur.fetchall()])
cur.execute('select * from bank_details order by age desc')
print([x for x in cur.fetchall()])

# group by
cur.execute('select marital,count(*),sum(balance),avg(balance) from bank_details group by marital')
print([x for x in cur.fetchall()])
cur.execute('select marital,count(*),sum(balance),avg(balance) from bank_details group by marital having sum(balance)>300')
print([x for x in cur.fetchall()])
cur.execute('select marital,count(*),sum(balance),avg(balance) from bank_details group by marital having sum(balance)<300')
print([x for x in cur.fetchall()])

## updates
#set sql_safe_updates=0
#update bank_details set `default`=NULL where `default`='no'
#update bank_details set balance=0 where contact='unknown'
#delete from bank_details where job='unknown'
