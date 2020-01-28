# In this section we are talking about class, how we can create a class and 
# how we can create method and class object, also how can we call method.
class Oops_classes:
    # what is __INT__() method in python.    
    def __init__(self):
        self.CPU="i3"
        self.RAM=8

    def config(self):
        print("Config is a ",self.CPU, self.RAM)
    def update(self):
        self.RAM=24
    
    def compare(self,others):
        if self.RAM==others.RAM:
            return True
        else:
            return False
obj1=Oops_classes()
obj2=Oops_classes()
# Oops_classes.config(obj1)   # In this way we can call method but second way also more familiar.
obj1.config()
obj2.config()
#obj2.update()
obj2.config()
if obj2.compare(obj1):
    print("They are same")
else:
    print("They are different")