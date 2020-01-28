def add(args1,args2):
    print(f"ADDING {args1} + {args2}")
    return args1+args2
def subtract(args1, args2):
    print(f"SUBTRACTING {args1} - {args2}")
    return args1 - args2
print("Let's do some math with just functions!")
age = add(30, 5)
height = subtract(78, 4)

print(f"Age: {age}, Height: {height}")
what = add(age, subtract(height,2))
print("That becomes: ", what, "Can you do it by hand?")
b=34 / 100
print(b)
a=24 + ((b) - 1023)
print(a)