# class A:
#     x = 10
# class B(A):
#     y = 20
# class C(A):
#     z = 30
# print(A.x)
# print(B.x, B.y)
# print(C.x, C.z)

class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class1
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")


class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")


object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()