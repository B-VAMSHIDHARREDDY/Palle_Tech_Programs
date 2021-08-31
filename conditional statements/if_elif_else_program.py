# Syntax
# if(condition):
#     #statement to execute if condition is true
# elif(condition):
#     #statement to be executed if condition is false and elif is true
# elif(condition):
#     #statement to be executed if both condition are false and this elif condition is true
# .
# .
# .
# .
# else:
#     #statement to executed when all conditions are false



# you will tack two fruits apple,mango
# apple kg for 250rs
# mango kg for 120rs
# you print the total amount
#

fruit = input("Enter fruit name:-")
quantity = float(input("enter quantity:-"))

if 'apple' == fruit:
    bill = quantity * 250
    print("Total amount:- ",bill)
elif 'mango' == fruit:
    bill = quantity * 120
    print("Amount:- ", bill)
else:
    print("Enter correct fruit Name")

# Discount the 5% in range 500rs to 1000r
# Discount the 10% in range 1000rs above
dis_bill = 0
if bill > 1 and bill < 500:
    print("You have No discount")
elif bill < 1000 and bill >= 500:
    print("you have 5% Discount")
    dis_bill = bill * (5/100)
elif bill >= 1000:
    print("you have 10% Discount")
    dis_bill = bill * (10/100)
else:
    print("you not buy any product")

print("Total amount = ", bill - dis_bill)