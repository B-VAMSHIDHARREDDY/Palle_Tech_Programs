class A:
    def __init__(self):
        self.x = 10
class B(A):
    def __init__(self):
        self.y = 20
b = B()
print(b.x)
print(b.y)
