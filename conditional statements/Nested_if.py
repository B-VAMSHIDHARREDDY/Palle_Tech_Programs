# if (condition1):
#     Executes when condition1 is true
#    if (condition2):
#        Executes when condition2 is true
#    if Block is end here
#  if Block is end here

# Example 1
x = 15
if x <= 15:
    print("welcome")
    if x == 10:
        print('python')
    else:
        print('Pycharm')
else:
    print("Good bye")
#############################################################################
# Example 2 Withdraw amount and deposit and view balance in atm system

pin = 1234
account_bal = 20000
d = True
while d:
    transaction = input("you have withdraw or deposit or view balance ")
    if transaction == 'withdraw':
        wid_amount = int(input("Enter Withdraw amount: "))
        if wid_amount <= account_bal:
            pin_con = int(input("Enter PIN: "))
            if pin_con == pin:
                print("collect the cash")
                account_bal -= wid_amount
            else:
                print("You enter wrong pin")
        else:
            print("Insufficient Balance")
    elif transaction == 'deposit':
        amount = int(input("enter the amount you have deposit: "))
        account_bal += amount
        print("Successfully Deposit")
    elif transaction == 'view balance':
        print("account_bal= ", account_bal)
    else:
        d = False

