import mysql.connector
import time

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="pm"
)
print("THIS IS logicinfinite PASSWORD VAULT")
master = int(input("please enter MASTER KEY"))
if master == 7007:
    print("successful login")
else:
    print(" wrong master key----- exiting program ")
    time.sleep(3)
    exit(0)

n = int(input(" how many entries you want to register  "))
while n != 0:

    username = input(" enter username ")
    password = input(" enter password ")
    mycursor = mydb.cursor()
    sqlformula = "INSERT INTO studs (name,age) VALUES (%s,%s)"
    val = (username, password)
    mycursor.execute(sqlformula, val)
    mydb.commit()
    n -= 1
print("do you want to search for any password if yes then press 1 else press 0 for exiting the program")
choice = int(input("  ENTER NOW "))
if choice == 0:
    exit(0)
elif choice == 1:
    u = input(' enter username for which you need to see the password ')
    sqlformula1 = "SELECT age FROM studs WHERE name=%s"
    val1 = (u,)
    mycursor.execute(sqlformula1, val1)

    myresult = mycursor.fetchall()
    print(" password for entered username is  ")
    for i in myresult:

        print(i)

    time.sleep(5)
    i = input("press 0 to exit")
    if i == 0:
        exit(0)
