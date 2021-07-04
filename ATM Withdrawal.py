print ("Welcome to ABC Bank")

def ATM_Balance_Check ():
    Current_Balanace  = 1000
    ATM_Balance = 4000
    Entered_Amount = int(input("Enter Amount you need withdraw = "))
    if (Entered_Amount <= Current_Balanace and Entered_Amount <=ATM_Balance ):
        print ("You can withdraw funds")
        Current_Balanace = Current_Balanace - Entered_Amount
        ATM_Balance = ATM_Balance - Entered_Amount
    else:
        print ("Funds not sufficient")
    print (Current_Balanace)
    print (ATM_Balance)

ATM_Balance_Check ()
