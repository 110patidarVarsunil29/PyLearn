class Oops4_innerclass:
# now we are assume that class name is student.

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()

    def show(self):
        print(self.name, self.rollno)

    class Laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i3'
            self.ram=8 
        def show(self):
            print(self.brand, self.cpu, self.ram)
        
    LP=Laptop()
    LP.show()
s1=Oops4_innerclass('Oracle',1223)
s1.show()
lap1=s1.lap
lap2=s1.Laptop()
# You can create object of inner class inside the outer class or
# you can create object of inner class outside the outer class provided you use outer class name to call it.
lap2.show()