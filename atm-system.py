print("======ATM SYSTEM======")
balance=int(input("Enter total balance amount:"))

pin=1234                                #AUTH SYSTEM
attempts=3
while attempts>0:
    entered_pin=int(input("Enter your pin:"))
    if entered_pin==pin:
        print("Access Granted. Welcome to ATM System.")
        break
    else:
        attempts -= 1
        print("Invalid PIN. Please try again.")
        print("Attempts left:",attempts)
if attempts==0:
    print("Account locked due to multiple failed attempts.")
    exit()

def check_balance(balance):                 #FUNCTIONS
    return balance

def deposit_money(balance):
    deposit_amount=int(input("Enter total deposit amount:"))
    if deposit_amount<=0:
        print("Invalid amount")
        return balance,0
    else:
        print("Deposit accepted")
        return balance+deposit_amount,deposit_amount

def withdrawal_money(balance):
    withdrawal_amount=int(input("Enter total withdrawal amount:"))
    if withdrawal_amount<=0:
        print("Invalid amount")
        return balance,0
    elif withdrawal_amount>balance:
        print("Insufficient balance")
        return balance,0
    else:
        return balance-withdrawal_amount,withdrawal_amount 

def transfer_money(balance):
    account_number=int(input("Enter account number:"))
    transfer_amount=int(input("Enter total transfer amount:"))
    if transfer_amount<=0:
        print("Invalid")
        return balance,0
    elif transfer_amount>balance:
        print("insufficient balance")
        return balance,0
    else:
        return balance-transfer_amount,transfer_amount,account_number

transactions=0                                    
history=[] 
while True:                                     #MAIN MENU LOOP
    print("=========================")
    print("======ATM MAIN MENU======")
    print("=========================")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. View Transaction history")
    print("6. Exit ")
    print("=========================")
    choice=int(input("Enter your choice(1-6):"))
    
    if choice==1:
        print("Total balance amount",check_balance(balance))
        
    elif choice==2:
        balance,amount=deposit_money(balance)
        history.append("Deposit | +" + str(amount))
        print("Total deposit amount is:",balance)
        transactions+=1
        print("Transaction successful")
        
        print("====== RECEIPT ======")
        print("Transaction: Deposit")
        print("Amount:", amount)
        print("Balance:", balance)
        print("=====================")
        
    elif choice==3:
        balance,amount=withdrawal_money(balance)
        history.append("Withdraw | -" + str(amount))
        print("The updated balance is:",balance)
        transactions+=1
        print("Transaction successful")
        
        print("====== RECEIPT ======")
        print("Transaction: Withdrawal")
        print("Amount:", amount)
        print("Balance:", balance)
        print("====================")

    elif choice==4:
        balance,amount,acc=transfer_money(balance)
        history.append("Transfer to " + str(acc) + " | -" + str(amount))
        print("The new balance amount is:",balance)
        transactions+=1
        print("Transaction successful")

        print("========RECEIPT=========")
        print("Transaction: Transfer")
        print("Transferred to account:",acc)
        print("Amount:",amount)
        print("Balance:",balance)
        print("========================")
        
    elif choice==5:
        print("Total transactions completed:",transactions)
        print(history)
        
    elif choice==6:
        print("Thank you for using ATM SYSTEM ")
        break
    else:
        print("Invalid choice")
        
    
