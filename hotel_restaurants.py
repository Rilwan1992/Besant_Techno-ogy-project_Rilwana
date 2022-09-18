#Assignament
#Hotel Manangement
#My Name is Rilwana N.H.
#Batch 57 @ Besant Technology
#This is my own project.
import mysql.connector
import sys
class Hotel:
     mydb = mysql.connector.connect(
        host ="localhost",
        user = "root",
        password ="rilshabi6",
        database="hotel_db"
    )
     mycursor =mydb.cursor()

     def display_menu(self):
         sql="select * from menu_table"
         self.mycursor.execute(sql)
         menus=self.mycursor.fetchall()
         print("ITEM ID\tITEM NAME\tPRICE")
         for row in menus:
            print(f"{row[0]}\t{row[1]}\t\t{row[2]}")

     def check_item(self,user_menu):
        sql1 = f"select item_id,item_name from menu_table where item_id={user_menu}"
        self.mycursor.execute(sql1)
        for x in self.mycursor:
            item_received = x[1]
            print(f"Your {x[1]} is available")
            return item_received
        else:
            print("wrong entry .. try again..")
            sys.exit(1)

        
     def clear_data(self):
        comment = "truncate table bill"
        self.mycursor.execute(comment)
        self.mydb.commit()
        comment1 ="truncate table final_bill"
        self.mycursor.execute(comment1)
        self.mydb.commit()

     def get_order(self,user_menu,quantity):
        sql2 =f"select item_id from menu_table where item_id={user_menu}"
        self.mycursor.execute(sql2)
        for x in self.mycursor:
            item_id = x[0]
        sql3 = f"insert into bill values({item_id},{quantity})"
        self.mycursor.execute(sql3)
        self.mydb.commit()
        
        

     def bill(self,user_menu):
        sql4 = f"select price from menu_table where item_id = {user_menu}"
        self.mycursor.execute(sql4)
        pl = self.mycursor.fetchone()        
        for x in pl:
            price = x
        sql5 = f"select quantity from bill where item_id ={user_menu}"
        self.mycursor.execute(sql5)
        quan = self.mycursor.fetchone()
        for i in quan:
            quantity = i
            dish_amount = price * quantity
    
        sql6 =f"insert into final_bill values({dish_amount})"
        self.mycursor.execute(sql6)
        self.mydb.commit()
        
     def final_total(self):
            sql7 =f"select sum(price_quantity) as Total from final_bill"
            self.mycursor.execute(sql7)
            ft = self.mycursor.fetchone()
            for i in ft:
                total = i
            print(f"\n Your Total bill amount : {total}")
            print(" Thank you.. visit again..")
            sys.exit(1)      

#*******************MAIN STARTS HERE*************************
print("************************************BISMI HOTEL*********************************")
#Available Menu List
hotel1 = Hotel()
hotel1.clear_data()
while True:
    try:
        hotel1.display_menu()
        user_menu = int(input("\nEnter your order Id : ").strip())
        item_R = hotel1.check_item(user_menu) 
    except Exception:
        print ("Enter correct inputs...")   
    try:    
        quantity = int (input(f"How many {item_R} do you want?: ").strip())
        hotel1.get_order(user_menu,quantity)
        stop_item = input("\n To continue the order press enter \n To stop a order press z " ).lower().strip()
        hotel1.bill(user_menu)
        if stop_item == "z":
            break 
    except Exception: 
        print("Enter correct inputs..")  

hotel1.final_total()