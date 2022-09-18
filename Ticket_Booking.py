#Assignament
#Ticket_Booking
#My Name is Rilwana N.H.
#Batch 57 @ Besant Technology
#Try my project with this input -> From : Chennai To: tiruchendur Date: 2022-09-21
import mysql.connector
import sys

class Ticket:
    mydb = mysql.connector.connect(
        host ="localhost",
        user = "root",
        password ="rilshabi6",
        database="traindb"
    )
    mycursor = mydb.cursor()

    def truncate(self):
        truncate = "truncate ticket_booking"
        self.mycursor.execute(truncate)
        self.mydb.commit()

    def checkavailable(self,fromplace,toplace,available_date):
        sql ="select * from destination where fromdesig = '%s' and todesig = '%s' and date_travel = '%s'"%(fromplace,toplace,available_date)
        self.mycursor.execute(sql)
        sd = self.mycursor.fetchall()
        for i in sd:
            id = i[0]
            #print(f"{i[0]},{i[1]},{i[2]}")
            print("\n Your ticket available")
            return id
        else:
            print("\n Ticket not available")
            sys.exit(1)

    def adultchildfare(self,id,a,c):
        sql1 = f"select adult_fare,child_fare from destination where id = {id}"
        self.mycursor.execute(sql1)
        fare = self.mycursor.fetchall()
        for x in fare:
            adult_fare=x[0]
            child_fare =x[1]
            print(f"\n Adult Fare : {adult_fare}")
            print(f"\n Child Fare : {child_fare}")
        total = ((a*adult_fare)+(c*child_fare))
        sql2 =f"insert into ticket_booking values({a},{c},{adult_fare},{child_fare},{total})"
        self.mycursor.execute(sql2)
        self.mydb.commit()
        return total
         

    def adultonly(self,id,a):
        sql1 = f"select adult_fare from destination where id = {id}"
        self.mycursor.execute(sql1)
        fare = self.mycursor.fetchall()
        for x in fare:
            adult_fare=x[0]
            print(f"\n Adult Fare : {adult_fare}")
        total = ((a*adult_fare))
        sql3 = f"insert into ticket_booking values({adult},{0},{adult_fare},{0},{total}"
        self.mycursor.execute(sql3)
        self.mydb.commit()
        return total

print("**********Online Train Ticket Booking***********")
print ("Train available from and to places ")
print("\n 1.chennai to tiruchendur(up&down) \n 2.chennai to tanjavoor(up&down) \n 3.coimbataore to tiruchur")
print("\n Train available dates from 2022-09-20 to 2022-09-24")
ticket1 = Ticket()
ticket1.truncate()
try:

    fromplace = input("\n From : ").lower().strip()
    toplace = input("\n To : ").lower().strip()
    available_date = input("\n Date(YYYY-mm-dd) : ")
    id = ticket1.checkavailable(fromplace,toplace,available_date)
except Exception:
    print("\n Some error occurs.. try after sometime..") 
try:       
    adult=int(input("\n Adult count : "))
    child=int(input("\n child count : "))
    if adult > 0 and child > 0:
        total = ticket1.adultchildfare(id,adult,child)
        print(f"\n Your total ticket  amount : {total}\n")
    if adult > 0 and child == 0:
        total=ticket1.adultonly(id,adult)
        print(f"\n Your total ticket fare: {total}\n")
    if adult == 0 and child > 0:
        print("\n child can't travel alone,sorry\n")
        sys.exit(1)
except Exception:
    print("\n Some error occurs.. try after sometime..") 
finally:
    if ticket1.mydb.is_connected():
        ticket1.mydb.close()
        ticket1.mycursor.close()

        