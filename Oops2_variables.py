class Oops_variables:
    #In this section we are talking about car as a class.

    wheels=4  #Global variable
    def __init__(self):
    # If you are create variable inside __init__ method, these are variables called Instance variables. 
        self.mil=10         #Instance variable
        self.name="BMW"     #Instance variable
    def speeds(self):
        speed=85     #Local variable
        print("BMW car avearge speed is ",speed)
c1=Oops_variables()
c2=Oops_variables()
print(c1.mil, c1.name,c1.wheels)
c2.mil=8
c2.wheels=8  #how was that possible, we can't change Class level variables by object or instance.
print(c2.mil, c2.name,c2.wheels)
c2.speeds()