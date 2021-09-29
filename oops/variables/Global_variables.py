x = 10 # Global variable
z = 20 # Global variable
def f1():
    print(x)
class A:
    def __init__(self):
        self.y = x          # use global variable use any where in module
    def m1(self):
        print(z)
print(x)
f1()
a = A()
print(a.y)
a.m1()

