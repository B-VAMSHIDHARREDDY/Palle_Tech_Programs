class A:
    def m1(self):
        print("Hai")
    def m2(self):
        print("Hello")
class B(A):
    def m2(self):
        print("bye")
b = B()
b.m1()
b.m2()