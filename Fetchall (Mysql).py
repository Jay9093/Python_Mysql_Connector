#Create your own database, update user name and password to your own!
import mysql.connector as mys
mycon = mys.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'company')
mycursor = mycon.cursor()
mycursor.execute("select * from employee")
mydata = mycursor.fetchall()
nrec = mycursor.rowcount
print("Total records found are",nrec)
for e,n,d,s in mydata:
    print(e,n,d,s)
    
