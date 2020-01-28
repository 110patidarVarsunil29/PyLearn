class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(self.a + self.b)  # Output should be 15
        # But Behind the scence Python code is different, let's see:
        print("Behind the scene Python complier genrate special Magic add method ", int.__add__(a, b))


a = A(5, 10)


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m1
        s3 = Student(m1, m2)

        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        if r1>r2:
            return True
        else:
            return False


    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

s1 = Student(40, 74)
s2 = Student(88, 98)
s3 = s1 + s2
print(s3.m1)
print(s3.m2)

if s1 > s2:
    print("s1 has greter value")
else:
    print("s2 has greater value")

print(s1.__str__())
print(s2.__str__())