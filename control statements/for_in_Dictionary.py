print("-----------------------------Example 1-----------------------------------")
dict = {'sachin' : 'india', 'kohli' : 'india','bretlee': 'age', 'pollerd' : 'west'}
for i in dict:
    if dict[i] in 'india':
        print(i)
print("-----------------------------Example 2-----------------------------------")
dict = {'apple':30,'banana':20,'orange':10,'grapes':50 ,'apple2':300}
# you have to print the price of fruits whose name are started with vowels.
vowels = 'aeiouAEIOU'
for i in dict:
    if i[0] in vowels:
        print(dict[i])
print("-----------------------------Example 3-----------------------------------")
x = {1:'red',2:'green',3:'blue' ,4:'pink',5:'black'}
# print colors whose keys are even numbers
for i in x:
    if i%2==0:
        print(x[i])
# print("-----------------------------Example 4-----------------------------------")

