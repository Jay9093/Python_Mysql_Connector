#Fetchall 2 
import mysql.connector as mys
mycon = mys.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'company')
mycursor = mycon.cursor()
mycursor.execute("select * from employee")
mydata = mycursor.fetchall()
nrec = mycursor.rowcount
print("Total records found are",nrec)
for row in mydata:
    print(row[0], ':', row[1], ':', row[2], ':', row[3], ':')
    
