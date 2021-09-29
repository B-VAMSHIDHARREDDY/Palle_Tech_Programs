class A:
    def __init__(self):
        self.x = 10       # self.x is instance variable
    def m(self):
        self.y = 20       # self.y is instance variable
a = A()
a.m()
print(a.x)
print(a.y)

