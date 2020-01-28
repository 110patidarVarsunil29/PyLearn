# Method overridding
class A:
    aa = 10

    def functionality(self):
        print("This is A class of functionality.")


class B(A):

    def functionality(self):
        super().functionality()
        bb = super().aa
        print("This is B class of functionality.", bb)


b1 = B()
b1.functionality()


# Method overloading
class C:
    def sum(self, a, b):
        return a + b

    def sum(self, a=None, b=None, c=None):
        s = 0
        if a is not None and b is not None and c is not None:

            s = a + b + c
            return s
        elif a is not None and b is not None and c is None:
            s = a + b
            return s
        else:
            s = a
            return s


c1 = C()
print(c1.sum(3, 5, 3))
print(c1.sum(10, 24))
print(c1.sum(10))
