#define a finction with def keyword in python

def printvariable(*sunil):  
#What does the * in *args do?
#That tells Python to take all the arguments to the function and then
#put them in args as a list. It’s like argv that you’ve been using but for functions.
    variable1, variable2,var3=sunil
    print(f"variable1 : {variable1} , variable2 : {variable2} , var3: {var3}")

printvariable("Sunil ","Patidar","Mumbai")

def printvariable2(args1,args2):
    print(f"variable1 : {args1} , variable2 : {args2}")

printvariable2("Mahesh","Pilot")

def printvariable1(args1):
    print(f"variable1 : ",args1)
printvariable1("Vijesh")

def printvariable0():
    print("This function not taken arguments!!!!")

printvariable0()
