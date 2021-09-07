# Syntax :
#     def function_name(parameters)
#         --------------------------
#         ---------code-------------
#         --------------------------
#         return results_of_function_output

print("---------------------------Example 1 ------------------------------")
# Addition of two numbers using function
def addition(x,y):
    return x + y
result = addition(10,20)
print(result)

print("---------------------------Example 2 ------------------------------")
# print is vowel or not using funtion
def vowels(x):
    if x in "aeiouAEIOU":
        return "is vowel"
    else:
        return "is not vowel"
x = vowels('a')
print(x)

print("---------------------------Example 3 -------------------------------")
# print is even or not using function
def even_odd(number):
    if number%2 == 0:
        return  "is even"
    else:
        return "is odd"
result = even_odd(10)
print(result)

print("---------------------------Example 4 -------------------------------")
# print last list value using
def list(x):
    return x[-1]
re = list([1,2,3,4,5,6,2,3,4,5,10])
print(re)
print("---------------------------Example 5 -------------------------------")
# write a function to find factorial of given number
def fact(num):
    result = 1
    while num >= 1:
        result = result * num
        num = num - 1
    print(result)

for i in range(1,10):
    fact(i)
print("---------------------------Example 6 --------------------------------")

# Find Prime Number or Not
def prime_number(num):
    prime = True
    for i in range(2,num):
        if num%i == 0:
            prime = False
            break
    return prime
result = prime_number(-5)
print(result)

print("---------------------------Example 7 ---------------------------------")
def fibonacci_ser(m):
    n1, n2 = 0, 1
    for i in range(m):
        print(n1,end=' ')
        sum = n1 + n2
        n1 = n2
        n2 = sum
fibonacci_ser(5)