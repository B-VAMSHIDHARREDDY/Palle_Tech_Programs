# create a parent class A in parent class create 2 methods and create a another class B in B create one method
# create object only B class and print 3 methods using class B object

class A:
    def m1(self):
        print("Method 1")
    def m2(self):
        print("Method 2")
class B(A):
    def m3(self):
        print("Method 3")
b = B()
b.m1()
b.m2()
b.m3()
