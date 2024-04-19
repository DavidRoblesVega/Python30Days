# Day 2: 30 Days of python programming

firstname = "David"
lastname = "Robles"
fullname = firstname + " " + lastname
country = "Spain"
city = "Madrid"
age = 25
year = 1999
is_married = False
is_true = True
is_light = False

print(type(firstname))
print(type(lastname))
print(type(fullname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))

print(len(firstname))

if len(firstname) > len(lastname):
    print("El nombre es más largo que el apellido.")
elif len(firstname) < len(lastname):
    print("El apellido es más largo que el nombre.")
else:
    print("El nombre y el apellido tienen la misma longitud.")
