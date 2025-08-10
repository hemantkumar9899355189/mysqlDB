# data manipulation language
import mysql.connector
from config import MYSQL_USER, MYSQL_PASSWORD


conn = mysql.connector.connect(
    host="localhost",
    user=MYSQL_USER,
    password=MYSQL_PASSWORD
)
cursor = conn.cursor()
cursor.execute("USE my_new_database")


t="customer"
a="pinCode"
cursor.execute(f"SHOW COLUMNS FROM {t} LIKE '{a}'")
result = cursor.fetchone()
if result is None:
    cursor.execute(f"ALTER TABLE {t} ADD {a} VARCHAR(25) ")
    conn.commit()
else:
    print(f"✅ Column '{a}' already exists.")
cursor.execute("DESC customer")
print(cursor)
for i in cursor:
    print(i)

# inserting new entery in the table 
cursor.execute(f'''
INSERT IGNORE INTO {t}(customerId,name,gender,city,address,pinCode)
values(1,"mukesh","m","delhi","rohini sector 24",110085)
''')
# adding multiple values at a time

cursor.execute(f'''
INSERT IGNORE INTO {t}(customerId,name,gender,city,address,pinCode)
values 
(2,"muskan","g","delhi","rohini sector 4",110086),
(3,"meena","g","lucknow","charbag gali no. 4 ",110088),
(4,"mayank","m","mumbai","khedewala",110087)

''')
# ALTERNATIVE way to pass values ,but you will have to follow order of columns defined
cursor.execute(f"INSERT IGNORE INTO {t} values(5,'monu','m','delhi','kanjhawla','110089')")
# when we dont have all data of a customer then we need to pass partial enteries while other columns either get null value or default value if any set
cursor.execute(f"INSERT IGNORE INTO {t} (customerId,name,gender) values(6,'meera','g')")

# updating 
cursor.execute("update customer set address='canought place' where customerId=6 ")

# UPDATING ALL ENTERIES OF A COLUMN
cursor.execute("update customer set pinCode=110099 ")
cursor.execute("SET SQL_SAFE_UPDATES=0 ")# SOME TIME WE MIGHT GET ERROR WHEN UPDATING ALL ENTERIES OF THE COLUMN IN THAT CASE WE NEED TO SET SQL_SAFE_UPDATE=0 THEN THERE WILL NOT BE ANY ERROR


cursor.execute(f"select*  from {t}")
for i in cursor:
    print(i)  
print()  
# deleting a row from the table
cursor.execute("delete from customer where name='monu'")

cursor.execute(f"select*  from {t}")
for i in cursor:
    print(i) 

# cursor.execute("delete from customer") # this command is used to delete all rows of a table
cursor.execute("show tables") 
for i in cursor:
    print(i)

# now lets learn delete constraints but before that we need to create another table that is orderDetails with a foreign key cutomerId of customer table  

cursor.execute('''create table IF NOT EXISTS orderDetails(

orderId integer primary key,
deliveryDate date,
custId int,
foreign key(custId) references customer(customerId))
   ''')

cursor.execute("insert ignore into orderDetails values(3,'2019-03-11',1)")
cursor.execute("insert ignore into orderDetails values (4,'2019-03-15',2)")
cursor.execute("select* from orderDetails")
for i in cursor:
    print(i)
   
# now suppose i am gonna delete the customer id from parent table what effect shall we see in child table
# there are three things that can happen 
# 1st it will give an error 
# 2nd is that when we delete foreign element from parent table then corresponding enteries will also get deleted from chiled table
# 3rd is that when we delete foreign element from parent table then in child table we will set nill value for those deleted foreign key 


# now lets see the 1st case
print("CASE 1  ****************************************************************************************************************")




try :
    cursor.execute("delete from customer where customerId=1")
    print("there was no error")
except :
    print("There was an error ")


# 2nd case
## to see this case first we need to delete our already created order detail table and then recreate it 


## deleting table using drop command
print("CASE 2  ****************************************************************************************************************")

cursor.execute("delete from orderdetails")
cursor.execute("drop table orderdetails")

print("we have only 3 tables ")

cursor.execute("show tables")
for i in cursor:
    print(i)


## recreating table with a command ON DELETE CASCADE

cursor.execute('''create table IF NOT EXISTS orderDetails(

orderId integer primary key,
deliveryDate date,
custId int,
foreign key(custId) references customer(customerId) ON DELETE CASCADE) 
   ''')

cursor.execute("insert ignore into orderDetails values (3,'2019-03-11',1)")
cursor.execute("insert ignore into orderDetails values (4,'2019-03-15',2)")

print("now after recreation we have total 4 tables")

cursor.execute("show tables")
for i in cursor:
    print(i)
cursor.execute("SELECT * FROM orderDetails")
for row in cursor:
    print(row)

#  now lets see effect of deleting parent foreign element in second case

try:
    cursor.execute("delete from customer where customerId=1")
    print("there was no error")
except:
    print("there was an error")

cursor.execute("select * from customer")
for i in cursor:
    print(i)

cursor.execute("select * from orderdetails")
for i in cursor:
    print(i)




# to 3rd case we will have to delete the table using drop command and 
# will reacreat with comman ON DELETE SET NULL

# deleteing table 


print("CASE 3  ****************************************************************************************************************")

cursor.execute("delete from orderdetails")
cursor.execute("drop table orderdetails")
print("after delete we have 3 table")
cursor.execute("show tables")
for i in cursor:
    print(i)
    

# creating table with command ON DELETE SET NULL

cursor.execute('''create table IF NOT EXISTS orderDetails(

orderId integer primary key,
deliveryDate date,
custId int,
foreign key(custId) references customer(customerId) ON DELETE SET NULL) 
   ''')
   
print("now we have 4 tables")

cursor.execute("show tables")
for i in cursor:
    print(i)

#  before we add enteries in table orderDetails let 1st we create the entery in customer table with customerId 1 because we had deleted it in case 2

cursor.execute(f'''
INSERT IGNORE INTO {t}(customerId,name,gender,city,address,pinCode)
values(1,"mukesh","m","delhi","rohini sector 24",110085)
''')

# adding enteries


cursor.execute("insert ignore into orderDetails values (3,'2019-03-11',1)")
cursor.execute("insert ignore into orderDetails values (4,'2019-03-15',2)")





cursor.execute("SELECT * FROM orderdetails")
for i in cursor:
    print(i)

cursor.execute("delete from customer where customerId=1")

print("enteries after deleting row from orderdetails table")

cursor.execute("SELECT * FROM orderdetails")
for i in cursor:
    print(i)

print("after drop we have 3 tables")
cursor.execute("delete from orderdetails")
cursor.execute("drop table orderdetails")




cursor.execute("show tables")
for i in cursor:
    print(i)


cursor.execute(f'''
INSERT IGNORE INTO {t}(customerId,name,gender,city,address,pinCode)
values(1,"mukesh","m","delhi","rohini sector 24",110085)
''')

cursor.execute("select * from customer")
for i in cursor:
    print(i)
conn.commit()
cursor.close()
conn.close()




