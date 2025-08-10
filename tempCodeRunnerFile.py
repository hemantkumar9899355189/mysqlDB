import mysql.connector
from config import MYSQL_USER, MYSQL_PASSWORD


conn = mysql.connector.connect(
    host="localhost",
    user=MYSQL_USER,
    password=MYSQL_PASSWORD
)

t="customer2"
cursor = conn.cursor()
cursor.execute("create database if not exists joins_database  ")
cursor.execute("use joins_database")

cursor.execute("create table if not exists employee(id int primary key AUTO_INCREMENT,firstName varchar(30),lastName varchar(30),age int ,emailId varchar(200), phoneNumber int ,city varchar(30) )")
cursor.execute("show tables") 
for i in cursor:
    print(i)

cursor.execute("desc employee")
for i in cursor:
    print(i)


cursor.execute("create table if not exists client(id int primary key auto_increment,firstName varchar(30),lastName varchar(30),age int ,emailId varchar(200),phoneNumber int ,city varchar(30),employeeId int , foreign key (employeeId) references employee(id) ON DELETE set null)")

cursor.execute("show tables") 
for i in cursor:
    print(i)

cursor.execute("desc client")
for i in cursor:
    print(i)
cursor.execute("create table if not exists project(id int primary key auto_increment ,employeeId int ,projectName varchar(20),startdate datetime,clientId int, foreign key(employeeId) references employee(id) ON DELETE set null,foreign key(clientId) references client(id) ON DELETE CASCADE)")
cursor.execute("show tables") 
for i in cursor:
    print(i)

cursor.execute("desc project")
for i in cursor:
    print(i)

cursor.execute('''insert into employee(id,firstName,lastName,age,emailId,phoneNumber,city)
 values 
 (1,'aman ','prot',32,'aman@gmail.com',898 ,'delhi'),
 (2,'yagya ','narayan',44,'yagya@gmail.com',222 ,'palam'),
 (3,'rahul ','bd',22,'rahul@gmail.com',444 ,'kolkata'),
 (4,'jatin ','hermit',31,'jatin@gmail.com',666 ,'raipur'),
 (5,'pk ','pandey',21,'pk@gmail.com',555 ,'jaipur')
 ''')
cursor.execute("select * from employee")
for i in cursor:print(i)

cursor.execute('''insert into client(id,firstName,lastName,age,emailId,phoneNumber,city,employeeId)
values
(1,'mac','rogers',47,'mac@hotmail.com',333,'kolkata',3),
(2,'max','poirier',27,'max@gmail.com',222,'kolkata',3),
(3,'peter','jain',24,'peter@abc.com',111,'delhi',1),
(4,'shushant','aggarwal',23,'shushant@yahoo.com',45454,'hyderabad',5),
(5,'pratap','singh',36,'p@xyz.com',77767,'mumbai',2)
''')
cursor.execute("select * from client")
for i in cursor:print(i)