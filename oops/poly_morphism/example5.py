class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y
class B(A):
    def __init__(self):
        super().__init__(10,20)
        self.m = 30
b = B()
print(b.x)
print(b.y)
print(b.m)
