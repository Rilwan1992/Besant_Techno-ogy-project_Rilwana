#ATM management system
#My Name is Rilwana N.H.
#Batch 57 @ Besant Technology
#This is my own project.
#Try my project with this input -> Account Number : 87657 & Pin : 3452
import mysql.connector
import sys
class Atm_machine:
    mydb = mysql.connector.connect(
        host ="localhost",
        user = "root",
        password ="rilshabi6",
        database="atm_db"
    )
    mycursor =mydb.cursor()
    def login(self,user):        
        sql = f"select Acc_no from account_info where acc_no={user}"
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        for x in myresult:
            if user in x:
                sql1 = "select Pin_no from account_info"
                self.mycursor.execute(sql1)
                result =self.mycursor.fetchall()
                return(result)
        else:
            print("Account number does not exist.Please try again")
            sys.exit(1)
        
    def pin(self,result,pin_num,user):                
        for x in result:
            if pin_num in x:
                #mycursor =self.mydb.cursor()
                sql2=f"select acc_name from account_info where acc_no={user}"
                self.mycursor.execute(sql2)
                result1 = self.mycursor.fetchone()
                return(result1)
        else:
            print("Sorry wrong pin.. try again")
            sys.exit(1)

    def view_info(self,user):
        #mycursor =self.mydb.cursor()
        sql3 = f"select acc_bal from account_info where acc_no={user}"
        self.mycursor.execute(sql3)
        view= self.mycursor.fetchone()
        for z in view:
            print(f"*********Your account balance : {z} Rs.*************")

    def withdraw(self,user):
        try:
            sql5=f"select acc_bal from account_info where acc_no={user}"
            self.mycursor.execute(sql5)
            pb=self.mycursor.fetchone()                            
            wd_amount=int(input("Enter Amount : ").strip()) 
            for f in pb:
                if f >= wd_amount:
                    print(f"Your previous amount : Rs. {f}")                           
                    sql4 = f"update account_info set acc_bal = acc_bal - {wd_amount} where acc_no = {user}"
                    self.mycursor.execute(sql4)
                #wd = self.mycursor.fetchone()
                    self.mydb.commit()
                    sql6=f"select acc_name,acc_bal from account_info where acc_no ={user}"
                    self.mycursor.execute(sql6)
                    fb = self.mycursor.fetchall()
                    for a,b in fb:
                        print(f"Name : {a}")
                        print(f"current Balance : Rs. {b}")
                else:
                    print("you balance is not sufficient")
                    print(f"Your Balance amount : Rs. {f} ")
                    print("Enter correct amount...")
        except Exception:
            print("Enter correct data..")
            sys.exit(1)


    def change_pin(self,user):
        try:
            old_pin = int(input("Enter your old pin : "))
            sql7 = f"select pin_no from account_info where pin_no={old_pin}"
            self.mycursor.execute(sql7)
            op = self.mycursor.fetchall()
            for c in op:
                if c in op:
                    new_pin = int(input("Enter your New pin(4 digits) : "))
                    sql8 = f"update account_info set pin_no = {new_pin} where acc_no={user}"
                    self.mycursor.execute(sql8)
                    #np=mycursor.fetchone()
                    self.mydb.commit()
                    print("New pin updated.. please login with new pin.. Thank you..")
                    break
            else:
                print("Old password wrong")
        except Exception:
            print("Some error occured..please try again..")
                                
#***************************Main Starts Here***************************************************
print("*******Welcome to our ATM center*********")
try:
    user = int(input("Enter your 5 Digit Account Number without space: ").strip())
    atm = Atm_machine()
    result = atm.login(user)
except Exception:
    print("Enter correct Numeric Numbers")
    print("please try again") 
    print("Bye")
    sys.exit(1)
    
try:    
    pin_num = int(input("Enter your 4 Digit ATM pin without space : ").strip()) 
    result1=atm.pin(result,pin_num,user)
except Exception:
    print("some error occured .. please try again..")
    sys.exit(1)
for y in result1:
    print(f"******welcome {y}*******")
    while True:
        print("1. VIEW BALANCE ENQUIRY")
        print("2. WITHDRAW AMOUNT ")
        print("3. TO CHANGE ATM PIN")
        print("4. EXIT ")
        try:
            user_entry = int(input("Enter the option do you want to process : ").strip())
            if user_entry == 1 :
                atm.view_info(user)
            elif user_entry == 2:
                atm.withdraw(user)                               
            elif user_entry == 3:
                atm.change_pin(user)
                break
            elif user_entry == 4:
                print("Thank you for using our ATM")
                break
        except Exception:
            print("PLEASE ENTER CORRECT NUMERIC NUMBER 1 TO 4 ")
                                    



        



