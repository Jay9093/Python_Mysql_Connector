#Deleting a record
import mysql.connector as mys
mycon = mys.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'supermarket')
mycursor = mycon.cursor()
eno = int(input("Enter employee number"))
query = "select * from stock where Product_ID = {}".format(eno)
mycursor.execute(query)
data = mycursor.fetchone()
if data!= None:
    print(data) #Result set
    ans = input("Are you sure you wish to delete this record? (y/n)")
    if ans == 'y':
        query = "delete from stock where Product_ID = {}".format(eno)
        mycursor.execute(query)
        mycon.commit()
        print("Record deleted")

else:
    print("Sorry, no such employee number exists")
mycon.close()
    
