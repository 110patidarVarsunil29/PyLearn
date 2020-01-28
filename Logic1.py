people=20
cats=15
dogs=18

if people<cats:
    print("Too many cats! The world is doomed!")
if people>cats:
    print("Not many cats! The world is saved!")
if people<dogs:
    print("The world is drooled on!")
if people> dogs:
    print("Now worid is dry!!!!")
else:
    print("Something Else!!!!!")

dogs=dogs+10
cats=cats+10
people=people+2


if people<cats or people<dogs:
    print("Too many cats! The world is doomed!")
elif people>cats or people>dogs:
    print("Not many cats! The world is saved!")
else:
    print("We can't decide it !!!!!")

if people<dogs or people<cats:
    print("The world is drooled on!")
elif people> dogs or people>cats:
    print("Now worid is dry!!!!")
else:
    print("We can't decide it !!!!!")