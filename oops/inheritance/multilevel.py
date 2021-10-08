class A:
    def __init__(self):
        self.roll = "A class"
    def m1(self):
        print("A class Method")


class B(A):
    def __init__(self):
        self.roll = "B class "
    def m2(self):
        print("B class method")
class C(B):
    def __init__(self):
        self.roll = "C class"
    def m3(self):
        print("C class method ")


object = C()
object.m1()
object.m2()
object.m3()



print(object.roll)
