import random
import json
import sys

class Bank:
    Bank_Name = 'State Bank Of India'
    def __init__(self):
        self.Balance = 0
        self.mini_credit_statement = {}
        self.mini_debit_statement={}
        self.ISFC_code =  "SBIN"+str(random.randint(11111,99999))+(random.choice("ADFGENIL")) 
    
    def login(self):
        name = input("Enter Your Name Here :")
        self.acount_num = random.randint(1111111111,99999999999999)
        UPI_PIN = int(input("set Your six digit UPI PIN :"))
        d = {"Account Holder Name":name,
             "Account Number":self.acount_num,
             "UPI PIN":UPI_PIN}    
        with open("Account_Details.json",'w') as f:
            json.dump(d,f,indent = 4)  
        return "Account Login Sucessfully"
    
    def Deposite(self,Amount):
        with open("Account_Details.json","r") as f:
            temp =  json.load(f)   
        pin = int(input("Enter Your UPI Pin here :"))
        if  pin== temp["UPI PIN"]:
            self.Balance = self.Balance+Amount
            self.mini_debit_statement[Amount] = self.Balance
            print()
            print(" Rs. ",Amount,"is credited in your\n",Bank.Bank_Name,"a\c XXXXXX",str(temp["Account Number"])[-1:-5:-1],
            """\n New Balance: Rs. """,self.Balance)
            return ""
        else:
            return "Invalid PIN"

    def withdraw(self,Amount):
        with open("Account_Details.json","r") as f:
            temp =  json.load(f)   
        pin = int(input("Enter Your UPI Pin here :"))
        if  pin== temp["UPI PIN"]:
            if self.Balance < 0 :
                return "Inficiant Balance You Can't Withdraw "
            self.Balance = self.Balance-Amount
            self.mini_credit_statement[Amount] = self.Balance
            print()
            print(" Rs. ",Amount,"is Debit in your\n",Bank.Bank_Name,"a\c XXXXXX",str(temp["Account Number"])[-1:-5:-1],
            """\n New Balance: Rs. """,self.Balance)
            return ""
        else:
            return "Invalid PIN"
    
    def interest_rate(self):
        interest = self.Balance*3.5//100
        print("MY Interest Rate is :",interest)
        return ""

    def mini_statement(self):
        print("Mini Debit Statement is :",self.mini_credit_statement)
        print("Mini Credit Statement is :",self.mini_debit_statement)
        return ""



