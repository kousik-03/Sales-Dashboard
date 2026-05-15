import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="kousik@123",
    database="Dashboard")
cursor=conn.cursor()

sql="""create table if not exists Sales(sales_id int,sales_person_name varchar(30),region_id int,amount int)"""
cursor.execute(sql)
sql="insert into Sales(sales_id, sales_person_name, region_id, amount)values (%s,%s,%s,%s)"

val=[
(24200,"Kousik",1,36000),
(24201,"Praveen",2,50000),
(24202,"Hari",3,56000),
(24203,"Harish",4,40500),
(24204,"Hema",4,44500),
(24205,"Giri",2,99500),
(24206,"Srimathi",1,39500),
(24207,"Divya",3,50000),
(24208,"Charu",1,90500),
(24209,"Rudra",1,65500)
]

cursor.executemany(sql,val)
cursor.execute("select * from Sales")
rows=cursor.fetchall()
print("\nSales records")

for row in rows:
    print(row)
conn.commit()
conn.close()
print("table created successfully")
