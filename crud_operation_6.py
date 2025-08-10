import mysql.connector
from config import MYSQL_USER, MYSQL_PASSWORD


conn = mysql.connector.connect(
    host="localhost",
    user=MYSQL_USER,
    password=MYSQL_PASSWORD
)

t="customer2"
cursor = conn.cursor()
cursor.execute("create database if not exists bankDb  ")
cursor.execute("use bankDb")

cursor.execute("create table  if not exists  department1 (empId int primary key auto_increment,name varchar(30),role varchar(30))")
cursor.execute('''
INSERT IGNORE INTO department1 (empId, name, role)
VALUES 
(1, 'A', 'engineer'),
(2, 'B', 'salesman'),
(3, 'C', 'manager'),
(4, 'D', 'salesman'),
(5, 'E', 'engineer')
''')
cursor.execute("create table  if not exists  department2 (empId int primary key auto_increment,name varchar(30),role varchar(30))")
cursor.execute('''
INSERT IGNORE INTO department2 (empId, name, role)
VALUES 
(3, 'C', 'manager'),
(6, 'F', 'marketing'),
(7, 'G','salesman' )
''')

# set operations start from here 

# list out all the employees (union operation)

cursor.execute(''' 
select name from  department1
union
select name from department2
''')
for i in cursor:print(i)


# find out all the employees working in salesman role (union operation)

cursor.execute(''' 
select name from  department1 where role='salesman'
union
select name from department2 where role='salesman'
''')
for i in cursor:print(i)

# list out employee who are working in both the department(intersection operation )


cursor.execute(''' 
select d1.name from  department1 as d1 inner join department2 as d2  on d1.empId=d2.empId

''')
for i in cursor:print(i)

# list out all employees who are working in only in department1 not in department2  (minus operation)
print("****************************")
cursor.execute(''' 
select d1.name from  department1 as d1 left join department2 as d2  on d1.empId=d2.empId
where d2.empId is null

''')
for i in cursor:print(i)

# sub queries 
# it is alternative to joins 
# there is two query one is outerquery another ins innerquery
# most of the time outerquery dependes on innerquery 
# here we are going to use same data set as was used in joins 
#  

cursor.execute("use joins_database")
cursor.execute("show tables")
for i in cursor:print(i)

cursor.execute("desc employee")
for i in cursor:print(i)

cursor.execute("select * from  employee")
for i in cursor:print(i)



cursor.execute("desc client")
for i in cursor:print(i)

cursor.execute("select * from  client")
for i in cursor:print(i)


cursor.execute("desc project")
for i in cursor:print(i)  

cursor.execute("select * from  project")
for i in cursor:print(i)



cursor.execute("select * from employee where age in (select age from employee where age>30)")
for i in cursor:print(i)


cursor.execute("select * from employee where id in(select employeeId from project group by employeeId having count(employeeId)>1) ")
for i in cursor:print(i)


# single value query 

cursor.execute("select * from employee where age>(select avg(age) from employee)")
for i in cursor:print(i)
print("*******************************************")

cursor.execute("select max(age) from (select * from employee where firstName like '%k%') as temp")
for i in cursor:print(i)

# in following case  the inner will depend on  outerquery query 
# find the 3rd oldest employee using sub query 

cursor.execute("select * from employee as e1 where 3=(select count(e2.age) from employee as e2 where e2.age>=e1.age)")
for i in cursor:print(i)
# what is view in mysql 
# it is a way to watch abstracted portion of table 
# here i can control how much rows and columns i want to see


cursor.execute("DROP VIEW IF EXISTS customView")
cursor.execute("CREATE VIEW customView AS SELECT firstName, age, id FROM employee")
cursor.execute("select * from customView ")
for i in cursor:print(i)
print("hii")