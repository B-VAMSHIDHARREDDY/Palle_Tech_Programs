# Syntax:
#
# for variable_name in non_primitive_datatype:
#     ----------------------------------------
#     --------------code----------------------
#     ----------------------------------------

print("----------------------------1st Example----------------------------------")
# Print list values one by one
x = [10,44,65,32]
for i in x:
    print(i)

print("----------------------------2nd Example----------------------------------")
# Print even numbers in the list
x = [10,44,65,32,50,53]
for i in x:
    if(i%2==0):
        print(i)

print("----------------------------3rd Example----------------------------------")
# Print vowels in given string using for loop
string = "Bangalore city"
for i in string:
    if i in "aeiouAEIOU":
        print(i)

print("----------------------------4th Example----------------------------------")
# Print all string whose len greater than 3
x = ["palle" , "ab" , "ram" , "krishna" , "vamshi" , "swathi"]
for i in x:
    if len(i) > 3:
        print(i)

print("----------------------------5th Example----------------------------------")
# print list value whose is divisible by 5
x = [10,44,65,73,54,55,125]
for i in x:
    if(i % 5 == 0):
        print(i)
print("----------------------------6th Example----------------------------------")
# print string specific range
string ="vamshidhar reddy"
for i in range(0,10,1):
    print(string[i], end="")
print()
print("----------------------------7th Example----------------------------------")
# print even index values is square and odd index values
x = [1,2,3,4,5,6,7,8,9,10]
for i in x:
    if i in range(0,len(x) + 1,2):
        print(i**2, end='-')
    else:
        print(i**3, end='-')
print();print("----------------------------8th Example----------------------------------")
# print string reverse using for

string = "vamshidhar"
for i in range(len(string)-1,-1 ,-1):
    print(string[i],end = '')


