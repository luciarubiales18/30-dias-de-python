# Day 2 : 30DaysOfPython Programming
# Variables in Python 
first_name = 'Lucia'
last_name = 'Rubiales'
full_name = 'Lucia Rubiales'
country = 'España'
city = 'Jerez'
age = 16
year = 2006
is_married = True 
is_true = 'Live in Jerez'
is_light_on = True
num_one = 5 
num_two = 4
total_sum = num_one + num_two
diif = num_one - num_two
product = num_one * num_two
divide = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two 

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
alias='Lucia'
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
print('is True?', is_true)
print(type, first_name)
print(type, last_name)
print(type, full_name)
print(type, country)
print(type, city)
print(type, age)
print(type, year)
print(type, is_married)
print(type, is_true)
print(type, is_light_on)
print('la longitud de mi nombre es', len(first_name))
print(len('lucia')==len('lucia Rubiale'))
print("Suma: ", total_sum)
print("Resta: ", diif) 
print("multiplicación: ", product)
print("División: ", divide)
print("División de módulo: ", remainder)
print("Multiplicación doble: ", exp)
print("División doble: ", floor_division)

#Calculating the area and circumference of a circle
radius = int(input("Give me radius os a circle: "))
square_of_radius = radius * radius
pi = 3.14
area_of_circle = pi * square_of_radius
print(area_of_circle)

circum_of_circle = 2 * pi * radius
print(circum_of_circle)

#Getting input from users
firstName = input("what ir your first name? ")
lastName = input("what is your last name? ")
your_country = input("What country are you from? ")
your_age = input("how old are you? ")

print("Hello , my name is", first_name, last_name, "I am from", your_country, "and I am", your_age, "years old,")

