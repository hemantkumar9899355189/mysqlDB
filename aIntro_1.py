import mysql.connector
from config import MYSQL_USER, MYSQL_PASSWORD


conn = mysql.connector.connect(
    host="localhost",
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database="org" 
)

print(conn)

cursor = conn.cursor()
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)
print("describing worker table")
cursor.execute("DESCRIBE worker")
for i in cursor:
  print(i)
cursor.execute("SELECT* FROM worker")
for i in cursor:
  print(i)


print("="*99)

print("describing bonus table")
cursor.execute("DESCRIBE bonus")
for i in cursor:
  print(i)
cursor.execute("SELECT* FROM bonus")
for i in cursor:
  print(i)


print("="*99)
print("describing title table")
cursor.execute("DESCRIBE title")
for i in cursor:
  print(i)
cursor.execute("SELECT* FROM title")
for i in cursor:
  print(i)


