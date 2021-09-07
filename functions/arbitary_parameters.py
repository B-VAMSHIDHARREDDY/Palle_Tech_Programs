# It takes multiple arguments in single parameter and it can store the values in tuple data type
print("---------------------- Example 1 ---------------------")
def fun(*a):
    print(a)
    print(type(a))
fun()
fun(10)
fun(100,200)
fun(100,200,300)
fun(23,23,5,67,8,8,92,5,67,8,55,7,6,56,7,5,66,65,7,656,77,6,6,7,76,6,7,7,56,7,"vamshi","reddy") # This callings are correct

print("---------------------- Example 2 ---------------------")
# Find the Biggest number
def fun(*n):
    a = sorted(n)
    return a[len(a)-1]
re = fun(10,20,85,7,8,56,12)
print(re)

# with out sort

def fun(*num):
    big_num = num[0]
    for i in  range(1,len(num)):
        if num[i] > big_num:
            big_num = num[i]
    return big_num
result = fun(10,20,85,7,8,56,12)
print(result)

print("---------------------- Example 3 ---------------------")
# Find the Smallest number
def fun(*num):
    big_num = num[0]
    for i in  range(1,len(num)):
        if num[i] < big_num:
            big_num = num[i]
    return big_num
result = fun(11,22,33,4,5,80)
print(result)