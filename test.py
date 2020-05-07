print("Choose either admin or user")
b = input()

Admin1 = ["Hi Uddesh, your Bank Account Number = 765749097 contains Funds Rs. 3,12,000"]
Admin2 = ["Hi  Anany, your Bank Account Number = 765749098 contains Funds Rs. 1,42,000"]
Admin3 = ["Hi Priyam, your Bank Account Number = 765749099 contains Funds Rs. 2,32,000"]

#Admin1 Password is 1234
#Admin2 Password is 1235
#Admin3 Password is 1236

if(b == "admin"):
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    if(password == "1234"):
        print('\n')
        print(Admin1)
        print('\n')
    elif(password == "1235"):
        print('\n')
        print(Admin2)
        print('\n')
    else: print(Admin3)
    print("Enter the account and name of the user you want to transfer funds to: ")
    ifsc = input("Enter the IFSC Code: ")
    account = int(input("Enter the Account Number: "))
    funds = int(input("Enter the amount of funds you want to transfer in Rs.: "))
    print("Your Entered details are as follows: ")
    print("IFSC code: " +ifsc)
    print("Account Number: " +str(account))
    print("Fund: " +str(funds))    
    print("For Final Fund Transfer enter the OTP sent to your registered mobile number: ")
#Assuming OTP is sent and it is input in the registered place
else: print("You are not authorised to use this function!!!")
