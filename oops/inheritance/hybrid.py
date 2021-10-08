class A:
    x = 20
class B(A):
    y = 30
class C(A):
    z = 40
class D(B,C):
    m = 50

print(A.x)
print(B.x,B.y)
print(C.x, C.z)
print(D.x, D.y, D.m,D.z)