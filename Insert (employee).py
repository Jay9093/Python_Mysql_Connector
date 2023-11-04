#Inserting a record
import mysql.connector as mys
mycon = mys.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'company')
mycursor = mycon.cursor()
ans = 'y'
while ans == 'y':
    eno = int(input("Enter employee number"))
    nm = input("Enter name")
    dp = input("Enter department")
    s = int(input("Enter salary"))
    query = "insert into employee values ({0}, '{1}', '{2}', {3})".format(eno, nm, dp, s)
    mycursor.execute(query)
    mycon.commit()
    print("Record saved")
    ans = input("Add more? (y/n)")
    


