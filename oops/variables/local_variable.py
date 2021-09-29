def f1(a,b):# a and b are local variable
    x=20 # x is local variable
    print(a)
    print(b)
    print(x)
class A:
    def m1(self):
        print(self) # This line print address of object
f1(20,30)
a = A()
a.m1()
