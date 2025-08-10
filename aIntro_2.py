import mysql.connector
from config import MYSQL_USER, MYSQL_PASSWORD


conn = mysql.connector.connect(
    host="localhost",
    user=MYSQL_USER,
    password=MYSQL_PASSWORD
)

cursor = conn.cursor()
cursor.execute("USE org")
cursor.execute("CREATE TABLE IF NOT EXISTS worker(workerId int NOT NULL PRIMARY KEY AUTO_INCREMENT,firstName CHAR(25),lastName CHAR(25),salary INT(15),joiningDate DATETIME,department CHAR (25) )")
cursor.execute("""INSERT IGNORE INTO  worker (workerId,firstName,lastName,salary,joiningDate,department) VALUES
(001,"monika","arora",100000,'14-02-20 09.00.00','HR'),
(002,"niharika","verma",80000,'14-06-11 09.00.00','admin'),
(003,"vishal","singhal",300000,'14-02-20 09.00.00','HR'),
(004,"amitabh","singh",500000,'14-02-20 09.00.00','admin'),
(005,"vivek","bhait",500000,'14-06-11 09.00.00','admin'),
(006,"vipul","diwan",200000,'14-06-11 09.00.00','accountant'),
(007,"satish","kumar",75000,'14-01-20 09.00.00','accountant'),
(008,"geetika","chauhan",90000,'14-04-11 09.00.00','HR')



""")
conn.commit()



cursor.execute("CREATE TABLE IF NOT EXISTS bonus(workerRefId INT,bonusAmt INT(10),bonusDate DATETIME ,FOREIGN KEY (workerRefID) REFERENCES worker (workerId) ON DELETE CASCADE)")
cursor.execute("""INSERT IGNORE  INTO bonus (workerRefId,bonusAmt,bonusDate) VALUES 
(001,5000,'16-02-20'),
(002,3000,'16-06-11'),
(003,4000,'16-02-20'),
(001,4500,'16-02-20'),
(002,3500,'16-06-11')
""")

conn.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS title(workerRefId INT,workerTitle CHAR(25), effectiveFrom DATETIME,FOREIGN KEY (workerRefId) REFERENCES worker(workerId) ON DELETE CASCADE)")
cursor.execute("""
INSERT IGNORE INTO title (workerRefId, workerTitle, effectiveFrom) VALUES
(001, 'Manager', '2016-02-20 00:00:00'),
(002, 'Executive', '2016-06-11 00:00:00'),
(008, 'Executive', '2016-06-11 00:00:00'),
(005, 'Manager', '2016-06-11 00:00:00'),
(004, 'Asst.Manager','2016-06-11 00:00:00'),
(007, 'Executive', '2016-06-11 00:00:00'),
(006, 'Lead', '2016-06-11 00:00:00'),
(003, 'Lead', '2016-06-11 00:00:00')
""")

conn.commit()



