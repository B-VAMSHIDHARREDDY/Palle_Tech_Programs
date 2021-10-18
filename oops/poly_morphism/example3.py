class A:
    x = 10
    def __init__(self):
        self.y = 10
    def m1(self):
        print("hello")
class B(A):
    x = 50
    def __init__(self):
        self.m = 100
    def m1(self):
        print("bye")
b = B()
print(B.x)
# print(b.y)  it is error
print(b.m)
b.m1()