import mysql.connector
from config import MYSQL_USER, MYSQL_PASSWORD


conn = mysql.connector.connect(
    host="localhost",
    user=MYSQL_USER,
    password=MYSQL_PASSWORD
)

cursor=conn.cursor()

cursor.execute("USE org")
cursor.execute("SELECT* FROM worker ")
for i in cursor:
    print(i)
print()

cursor.execute("SELECT firstName,salary FROM worker ")
for i in cursor:
    print(i)
print()

cursor.execute("SELECT * FROM worker WHERE salary>200000")
for i in cursor:
    print(i)
print()
cursor.execute("SELECT * FROM worker WHERE salary BETWEEN 0 AND 200000")
for i in cursor:
    print(i)
print()

# logical operator AND OR NOT IN

print("# logical operator AND OR NOT IN")

cursor.execute("SELECT * FROM worker WHERE salary= 200000 OR salary =300000 OR salary=500000")
for i in cursor:
    print(i)
print()

cursor.execute("SELECT * FROM worker WHERE salary IN (200000,300000,500000)")
for i in cursor:
    print(i)
print()
cursor.execute("SELECT * FROM worker WHERE salary NOT IN (200000,300000,500000)")
for i in cursor:
    print(i)
print()
cursor.execute("SELECT * FROM worker WHERE salary=100000 AND DEPARTMENT ='HR'")
for i in cursor:
    print(i)
print()

# charactor search LIKE %% and like _

cursor.execute("SELECT * FROM worker WHERE firstName LIKE '%m%'") # it means where m apears in the name
for i in cursor:
    print(i)
print()
cursor.execute("SELECT * FROM worker WHERE firstName LIKE 'm%'") # it means where name starts with m 
for i in cursor:
    print(i)
print()
cursor.execute("SELECT * FROM worker WHERE firstName LIKE '%m'") # it means where name ends with m 
for i in cursor:
    print(i)
print()

cursor.execute("SELECT * FROM worker WHERE firstName LIKE '_m%'") # it means m at second place 
for i in cursor:
    print(i)
print()
cursor.execute("SELECT * FROM worker WHERE firstName LIKE '_m_'") # it means names with 3 charactor and m is at second place 
for i in cursor:
    print(i)
print()
cursor.execute("SELECT * FROM worker WHERE firstName LIKE 'm_'") # it means names with 2 charactor and m is at first place 
for i in cursor:
    print(i)
print()
cursor.execute("SELECT * FROM worker WHERE firstName LIKE '_m'") # it means names with 2 charactor and m is at second place 
for i in cursor:
    print(i)
print()
cursor.execute("SELECT * FROM worker WHERE firstName LIKE 'm'") # it means where names=m exact same no more charactor 
for i in cursor:
    print(i)
print()

# sorting in mysql
cursor.execute("SELECT * FROM worker ORDER BY salary ASC")#  "for descending use DESC"
for i in cursor:
    print(i)
    
# how to get distinct value  or all values with no 
cursor.execute("SELECT  DISTINCT department FROM worker ")
for i in cursor:
    print(i)
# grouping data as per title or department or etc

cursor.execute("SELECT department  FROM worker GROUP BY department")# without aggregation function , it will work similar to DISTICT function as above 
for i in cursor:
    print(i)
cursor.execute("SELECT department,COUNT(department)  FROM worker GROUP BY department")# with aggregation function COUNT
for i in cursor:
    print(i)
cursor.execute("SELECT department,AVG(salary)  FROM worker GROUP BY department")# with aggregation function AVG
for i in cursor:
    print(i)
cursor.execute("SELECT department,MIN(salary)  FROM worker GROUP BY department")# with aggregation function 
for i in cursor:
    print(i)
cursor.execute("SELECT department,MAX(salary)  FROM worker GROUP BY department")# with aggregation function 
for i in cursor:
    print(i)
cursor.execute("SELECT department,SUM(salary)  FROM worker GROUP BY department")# with aggregation function 
for i in cursor:
    print(i)
cursor.execute("SELECT department,COUNT(department)  FROM worker GROUP BY department HAVING COUNT(department) >2")# with aggregation function 
for i in cursor:
    print(i)

# having vs where

# having is used with group by while where is used with select delete update 
# having is used to filter rows of a group while where is used to filter rows of a column











