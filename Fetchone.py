#Fetchone
import mysql.connector as mys
mycon = mys.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'company')
mycursor = mycon.cursor()
mycursor.execute("select * from employee")
mydata = mycursor.fetchone()
nrec = mycursor.rowcount
print("Total records found are",nrec)
print(mydata)
print("===========================")
mydata = mycursor.fetchone()
nrec = mycursor.rowcount
print("Total records fetched are",nrec)
print(mydata)
