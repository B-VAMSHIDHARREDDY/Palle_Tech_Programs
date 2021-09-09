# Syntax
# if(condition):
#     if block
# else:
#     else block

print("-------------------------Example 1 ------------------------------")
x = 20
y = 10
if(y > x):
    print('y is greater than x')
else:
    print('y is not greater than x')

print("-------------------------Example 2 ------------------------------")

Age = 20
if(x >= 18):
    print('Eligible for vote')
else:
    print('Not Eligible for vote')

print("-------------------------Example 3 ------------------------------")
# Given string palindrome or not

string = "lalalalal"
string2 = ""
for i in string:
    string2 = i + string2
if (string == string2):
    print("is palindrome ")
else:
    print("is not palindrome")