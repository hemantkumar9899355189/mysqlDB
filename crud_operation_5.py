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

print("***************************************************************************************************************************************************")
cursor.execute('''insert ignore into employee(id,firstName,lastName,age,emailId,phoneNumber,city)
 values 
 (1,'aman ','prot',32,'aman@gmail.com',898 ,'delhi'),
 (2,'yagya ','narayan',44,'yagya@gmail.com',222 ,'palam'),
 (3,'rahul ','bd',22,'rahul@gmail.com',444 ,'kolkata'),
 (4,'jatin ','hermit',31,'jatin@gmail.com',666 ,'raipur'),
 (5,'pk ','pandey',21,'pk@gmail.com',555 ,'jaipur')
 ''')
cursor.execute("select * from employee")
for i in cursor:print(i)
print("***************************************************************************************************************************************************")

cursor.execute('''insert ignore into client(id,firstName,lastName,age,emailId,phoneNumber,city,employeeId)
values
(1,'mac','rogers',47,'mac@hotmail.com',333,'kolkata',3),
(2,'max','poirier',27,'max@gmail.com',222,'kolkata',3),
(3,'peter','jain',24,'peter@abc.com',111,'delhi',1),
(4,'shushant','aggarwal',23,'shushant@yahoo.com',45454,'hyderabad',5),
(5,'pratap','singh',36,'p@xyz.com',77767,'mumbai',2)
''')
cursor.execute("select * from client")
for i in cursor:print(i)
print("***************************************************************************************************************************************************")


cursor.execute('''insert ignore into  project(id,employeeId,projectName,startdate,clientId) 
values
(1,1,'a','2021-04-21',3),
(2,2,'b','2021-03-12',1),
(3,3,'c','2021-01-16',5),
(4,3,'d','2021-04-27',2),
(5,5,'e','2021-05-01',4)
''')
cursor.execute("select * from project")
for i in cursor:print(i)
print("***************************************************************************************************************************************************")

# from hereonwards we are going to write codes for join
# before below lines we were creating requisite tables to run join operations

# inner join gives a table representing all common values of (both or all the tables) OR I CAN SAY (IT GIVES INTERSECTION OF TABLES)
# OUTER JOIN IS DIVIDED IN 3 SUB PARTS THAT IS 
# LEFT JOIN IT GIVES ALL DATA OF LEFT TABLE IN ADDITION TO THAT MATCHING DATA OF RIGHT TABLE
# RIGHT JOIN IT GIVES ALL DATA OF RIGHT TABLE IN ADDITION TO THAT MATCHING DATA OF LEFT TABLE
# FULL JOIN  IT GIVES UNION OF ALL TABLES 


# enlist employee id name along with project allocated them
cursor.execute("select e.id ,e.firstName,e.lastName, p.projectName from employee as e inner join project as p on e.id=p.employeeId")
for i in cursor:print(i)
print("***************************************************************************************************************************************************")

# find employee id and their contact details who is from jaipur working with client from heyderabad along with client name

cursor.execute("select e.id ,e.emailId,e.phoneNumber, c.firstName,c.lastName from employee as e inner join client as c on e.id=c.employeeId where e.city='jaipur' and c.city='hyderabad'")
for i in cursor:print(i)
print("***************************************************************************************************************************************************")

# fetch out all data of each project allocated to each employee 

cursor.execute("select e.* ,p.*   from employee as e left join project as p on e.id=p.employeeId ")
for i in cursor:print(i)
print("***************************************************************************************************************************************************")

# list out all the project along with employees name and emailid

cursor.execute("select p.* , e.firstName,e.lastName from employee as e right join project as p on e.id=p.employeeId ")
for i in cursor:print(i)
print("***************************************************************************************************************************************************")


conn.commit()




cursor.execute("show tables")
for i in cursor:print(i)
cursor.execute("select * from  employee")
for i in cursor:print(i)

cursor.execute("select * from  client")
for i in cursor:print(i)

cursor.execute("select * from  project")
for i in cursor:print(i)






