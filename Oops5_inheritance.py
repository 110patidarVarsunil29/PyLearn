class Car:
    def __init__(self):
        print("Constructor called once object creation. ")

    def speed(self):
        print("speed of car depends on roads.")

    def config(self):
        print("Car has some configration.")


class BMW:
    def __init__(self):
        # super().__init__()
        print("Child class constructor")

    def security(self):
        # super().speed()

        print("BMW car also provide security features.")

        #super().config()


class Tesla(Car,BMW):
    def __init__(self):
        super().__init__()
        print("Tesla class constructor")

    def types(self):
        print("Tesla is a electrical car")
        super().config()
        super().security()


t1 = Tesla()
t1.types()
# Types of inheritance:
# 1 A single Python inheritance is when a single class inherits from a class.   [Car==>BMW]
# 2  Multiple Python inheritance are when a class inherits from multiple base classes. [Car,BMW==>Tesla]
# 3 When one class inherits from another, which in turn inherits from another, it is multilevel python inheritance.   [Car==> BMW==>Tesla]
# 4 When more than one class inherits from a class, it is hierarchical Python inheritance. [Car==>BMW,Tesla]
# 5 Hybrid Python inheritance is a combination of any two kinds of inheritance.