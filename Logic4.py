i =1
numbers=[]
while i <1:
    print(f"The value of i is {i} .")
    numbers.append(i)
    print(numbers)
    i=i+1
    print(f"After increment the value of i is {i} !!!")

for j in numbers:
    print(j)

for k in range(5):
    numbers.append(k)
    print(numbers)

animals = ['bear', 'tiger', 'penguin', 'zebra']
animals.insert(7,'Lion')

for i in animals:
    print(i)