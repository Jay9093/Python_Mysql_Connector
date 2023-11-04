#Fetchmany
import mysql.connector as mys
mycon = mys.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'company')
mycursor = mycon.cursor()
mycursor.execute("select * from employee")
mydata = mycursor.fetchmany(3)
nrec = mycursor.rowcount
print("Total records fetched are",nrec)
for row in mydata:
    print(row)

    
