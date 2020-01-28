the_count = [1, 2, 3, 4, 5]
lists=[]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list

for i in the_count:
    lists.append(i)
for j in change:
    lists.append(j)
    print(lists)
for k in lists:
    print("K ==> ", k)

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
# append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")

twodim=[[1,2],[4,5]]

for li in twodim:
    li.insert(3,7)   #How can i add two dimentional list value in existing list.

for l in twodim:
    print(l)
