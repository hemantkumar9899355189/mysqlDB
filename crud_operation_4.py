import mysql.connector
from config import MYSQL_USER, MYSQL_PASSWORD


conn = mysql.connector.connect(
    host="localhost",
    user=MYSQL_USER,
    password=MYSQL_PASSWORD
)

t="customer2"
cursor = conn.cursor()
cursor.execute("USE my_new_database")

cursor.execute("""
CREATE TABLE IF NOT EXISTS customer2 (
    customerId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    gender VARCHAR(10),
    city VARCHAR(100),
    address VARCHAR(255),
    pinCode VARCHAR(10)
)
""")

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

cursor.execute("select * from customer2 ")
for i in cursor:print(i)

print("*******************************************************************************************")

# REPLACE keyword in mysql does two thing
# IF there is alredy data exists for targated row then it will replace with the data given 
# if there is no data then it will enter new entry there let see
# CASE1
cursor.execute("replace into customer2(customerId,city) values(1,'chennai')")

cursor.execute("select* from customer2")
for i in cursor:print(i)
print("****************************************************************************************************")
cursor.execute("delete from customer2 where customerId=1")


cursor.execute(f'''
INSERT IGNORE INTO {t}(customerId,name,gender,city,address,pinCode)
values(1,"mukesh","m","delhi","rohini sector 24",110085)
''')
cursor.execute("select * from customer2")
for i in cursor:print(i)
print("************************************************************************************************")

# CASE2
cursor.execute("replace into customer2(customerId,city) values(5,'karnatka')")

cursor.execute("select* from customer2")
for i in cursor:print(i)
print("****************************************************************************************************")
cursor.execute("delete from customer2 where customerId=5")

# update vs replce
# if there no targeted row then replce will add new row but update will do nothing

