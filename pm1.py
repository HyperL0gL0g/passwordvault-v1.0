import mysql.connector
import time

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",#enter your own password here
    database="pm"# enter your database name here
)
print("THIS IS logicinfinite PASSWORD VAULT")

n = int(input("how many entries you want to register"))
while n != 0:

    username = input("enter username")
    password = input("enter password")
    mycursor = mydb.cursor()
    sqlformula = "INSERT INTO studs (name,age) VALUES (%s,%s)"
    val = (username, password)
    mycursor.execute(sqlformula, val)
    mydb.commit()
    n -= 1


u = input('enter username for which you need to see the password')
sqlformula1 = "SELECT age FROM studs WHERE name=%s"
val1 = (u,)
mycursor.execute(sqlformula1, val1)

myresult = mycursor.fetchall()
print("password for entered username is ")
for i in myresult:

    print(i)

time.sleep(5)
i = input("press 0 to exit")
if i == 0:
    exit(0)
