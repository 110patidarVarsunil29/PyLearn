class PyCharm:
    def execute(self):
        print("Compiling Python code in PyCharm!!!")
        print("Running Python code in PyCharm")


class MSCode:
    def execute(self):
        print("Compiling Python code in MSCode!!!")
        print("Running Python code in MSCode")


class Laptop:
    def code(self, ide):
        ide.execute()


ide = PyCharm()
lp = Laptop()
lp.code(ide)
