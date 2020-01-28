class Oops_methods:
    school="MIT"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):  #avg() method is instance method because it's work with object.
        return self.m1+self.m2+self.m3/3

    def get_m1(self):
        return self.m1
    def set_m1(self,m1):
        self.m1=m1


#when you are working with class variable you should specific cls variable as a argument in class method
# With class method we can use @classmethod.
    
    @classmethod
    def getSchool(cls):
        cls.school="MIST"
        return cls.school


#With static method we can use @staticmethod.
    @staticmethod
    def info():
        print("This is a Static method in Python class..!!")

s1=Oops_methods(35,37,44)
s2=Oops_methods(32,25,22)
print(s2.avg())
print(Oops_methods.getSchool())
#print(Oops_methods.school)
print(Oops_methods.info())