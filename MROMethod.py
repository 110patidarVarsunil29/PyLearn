#Constructor in inheritance:==
class X:
    def __init__(self):
        print("Printing init of X")
    def displayX(self):
        print("X")
class Y(X):

    def __init__(self):
        print("Printing init of Y")
    def displayY(self):
        print("Y")
y1=Y()

#MRO (Method resolution Order)
class A:
    def displayA(self):
        print("A")
class B:
    def displayB(self):
        print("B")
class C(B,A):
    def displayC(self):
        print("C")
c1=C()
print(C.mro())