# It takes multiple arguments in single parameter and it can store the values in tuple data type

def fun(*a):
    print(a)
    print(type(a))
fun()
fun(10)
fun(100,200)
fun(100,200,300)
fun(23,23,5,67,8,8,92,5,67,8,55,7,6,56,7,5,66,65,7,656,77,6,6,7,76,6,7,7,56,7,"vamshi","reddy") # This callings are correct


