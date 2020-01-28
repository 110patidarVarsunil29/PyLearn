from sys import argv, path, modules, stdin , platform, prefix,  winver
from os import chdir
# read the WYSS section for how to run this
script, first, second, third,fourth = argv
location=path
dictionary=modules
a=input("Enter something!!")
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your fourth variable is:", fourth)
print("Your third variable is:", third)
print("Your path variable is:", path)
print("Your modules variable is:", modules)
print("Your standard input file object is:", stdin)
print("The first static variable of sys modules ",platform)
print("The prefix ststic variable of sys modules ", prefix)
print(" winver ",  winver)
print("OS module chdir ", chdir)
#python -m pydoc SPECIALMETHODS