class A:
    def __init__(self):
        self.roll = "A class"
    def m1(self):
        self.a = "A class"


class B(A):
    def __init__(self):
        self.roll = "B class "



object = B()
object.m1()
print(object.roll,"\n",object.a)