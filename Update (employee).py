#Updating a record
import mysql.connector as mys
mycon = mys.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'supermarket')
mycursor = mycon.cursor()
eno = int(input("Enter employee number"))
query = "select * from customer where Customer_ID = {}".format(eno)
mycursor.execute(query)
data = mycursor.fetchone()
if data!= None:
    print(data) #Result set
    ans = input("Are you sure to update salary? (y/n)")
    if ans == 'y':
        s = int(input("Enter new salary"))
        query = "update customer set Half_Yearly_Sales = {} where Customer_ID = {}".format(s,eno)
        mycursor.execute(query)
        mycon.commit()
        print("Record updated")

else:
    print("Sorry, no such employee number exists")
mycon.close()
    


