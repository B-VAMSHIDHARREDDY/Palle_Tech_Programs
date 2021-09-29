class A:
    x = 10 # class variable
    y = 20 # class variable
    def __init__(self):
        self.x = 20
a = A()
print(a.x)
print(A.x) # access the class variable using class name
print(A.y)