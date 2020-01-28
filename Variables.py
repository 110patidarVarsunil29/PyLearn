print("Variables and Names")
Cars='Tesla'
Model='T30'
Price=35000
#print(type(Price))
Model_type='Automative'
Car_pool_capacity=3
Passengers=100

print("There are", Cars, "cars available.")
print("There are only", Model, "Model available.")
print("There will be $",Price, "per cars today in black friday offer.")
print("We can sit", Car_pool_capacity, "people in one ", Cars, Model)
print("We have", Passengers, "to carpool today.")

#String Format

my_name = 'Sunil Patidar'
my_age = 24 # not a lie
my_height = 74 # inches
my_weight = 120 # lbs
my_eyes = 'May be black'
my_teeth = 'White'
my_hair = 'Black'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")