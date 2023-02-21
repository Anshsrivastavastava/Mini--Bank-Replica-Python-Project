from Acounts import *
x = Bank()

while True:
    print(f"--------------------------------------------->>>>   Welcome To {Bank.Bank_Name}   <<<-------------------------------------------------\n")
    print()
    print("+="*15)
    print("1.   For Login")
    print("2.   Deposite From Bank")
    print("3.   Withdraw From Account")
    print("4.   For Mini Statement ")
    print("5    For Interest Rate")
    print("6.   For Exit")
    print("+="*15)

    choice = input("Select Your Choice :")
    if choice =="1":
        print(x.login())

    if choice =="2":
        amount = int(input("Enter Your Amount :"))
        print(x.Deposite(amount))
    
    if choice =="3":
        amount = int(input("Enter Your Withdraw Amount :"))
        print(x.withdraw(amount))
    
    if choice =="4":
        print("*"*50)
        print(x.mini_statement())
        print("*"*50)
    
    if choice =="5":
        print(x.interest_rate())
    
    if choice =="6":
        print("           Thanks For Visiting          ")
        break
        

