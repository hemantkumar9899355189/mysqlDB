import mysql.connector
from config import MYSQL_USER, MYSQL_PASSWORD


conn = mysql.connector.connect(
    host="localhost",
    user=MYSQL_USER,
    password=MYSQL_PASSWORD
)
cursor = conn.cursor()
cursor.execute("USE my_new_database")

cursor.execute("show tables")
print(cursor)
for i in cursor:
    print(i)
# DECLARING PRIMARY KEY AND ACCEPTING ONLY UNIQUE ENTERIES
cursor.execute("CREATE TABLE IF NOT EXISTS customer(customerId INT NOT NULL PRIMARY KEY AUTO_INCREMENT,name VARCHAR(25) UNIQUE )")
for i in cursor:
    print(i)
# DECLARING FOREIGN KEY AND CHECKING ENTERIS ON SOME CONDITION
cursor.execute("CREATE TABLE IF NOT EXISTS ACCOUNT(accountId INT,accountBalance INT,CONSTRAINT checkBalance CHECK(accountBalance>100) , FOREIGN KEY (accountId) REFERENCES customer(customerId) )")
for i in cursor:
    print(i)
# DECLARING FOREIGN KEY AND CHECKING ENTERIS ON SOME CONDITION alternative
cursor.execute("CREATE TABLE IF NOT EXISTS ACCOUNT(accountId INT,accountBalance INT, CHECK(accountBalance>100) , FOREIGN KEY (accountId) REFERENCES customer(customerId) )")
for i in cursor:
    print(i)
# note: CONSTRAINT word above used to give name of the contarint(i.e checkbalance)
# setting DEFAULT value
cursor.execute("CREATE TABLE IF NOT EXISTS ACCOUNT(accountId INT,accountBalance INT NOT NULL DEFAULT 100, CHECK(accountBalance>999) , FOREIGN KEY (accountId) REFERENCES customer(customerId) )")
for i in cursor:
    print(i)

# # alter operations .

# #adding new column


cursor.execute("SHOW COLUMNS FROM account LIKE 'interest'")
result = cursor.fetchone()
if result is None:
    cursor.execute("ALTER TABLE account ADD interest FLOAT NOT NULL DEFAULT 0")
    conn.commit()
else:
    print("✅ Column 'interest' already exists.")


#modifying



cursor.execute("ALTER TABLE account MODIFY interest INT NOT NULL DEFAULT 0")

#describing
cursor.execute("DESC account")
for i in cursor:
    print(i)

# renaming columns

cursor.execute("SHOW COLUMNS FROM account LIKE 'savingInterest'")
result = cursor.fetchone()
if result is None:
    cursor.execute("ALTER TABLE account CHANGE COLUMN interest savingInterest FLOAT NOT NULL DEFAULT 0")
    cursor.execute("DESC account")
    for i in cursor:
        print(i)  
else: 
     print("✅ Column already exists.")
# droping columns

   
cursor.execute("SHOW COLUMNS FROM account LIKE 'savingInterest'")
if cursor.fetchone():
    cursor.execute("ALTER TABLE account DROP COLUMN savingInterest")
    conn.commit()
    print("✅ Column 'savingInterest' dropped.")
else:
    print("ℹ️ Column 'savingInterest' does not exist.")

cursor.execute("DESC account")
for i in cursor:
    print(i)

# # renaming table
cursor.execute("SHOW TABLES LIKE 'account'")
if cursor.fetchone():
    cursor.execute("ALTER TABLE account RENAME TO account_Details")
    conn.commit()
    print("✅ Table 'account' renamed to 'account_Details'.")
else:
    print("❌ No such table 'account' exists to rename.")

cursor.execute("show tables")
print(cursor)
for i in cursor:
    print(i)

cursor.execute("SHOW TABLES LIKE 'account_Details'")
if cursor.fetchone():
    cursor.execute("ALTER TABLE account_Details RENAME TO account")
    conn.commit()
    print("✅ Table 'account_Details' renamed to 'account'.")
else:
    print("❌ No such table 'account_Details' exists to rename.")
    
cursor.execute("show tables")
print(cursor)
for i in cursor:
    print(i)


