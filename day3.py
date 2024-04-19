# Declare your age as integer variable
# Declare your height as a float variable
# Declare a variable that store a complex number
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h)

age = 25
height = 1.78
complex_number = 3 + 3j


b = float(input("Introduce la base del triángulo "))
h = float(input("Introduce la altura del triángulo "))
area = 0.5 * b * h
print("El área de triángulo es: ", area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of triangle is ", perimeter)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = 20
width = 10
area_rectangle = length * width
perimeter_rectangle = 2 * (length * width)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
r = 5
area_circle = pi * r * r
circumference = 2 * pi * r


# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
if len("python") > len("dragon"):
    print(False)

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
if "on" in "python" and "on" in "dragon":
    print(True)
else:
    print(False)

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
if "jargon" in sentence:
    print(True)
else:
    print(False)

# There is no 'on' in both dragon and python
if "on" not in "python" and "on" not in "dragon":
    print(True)
else:
    print(False)

# Find the length of the text python and convert the value to float and convert it to string
longitud_python = len("python")
print(longitud_python)
print(type(longitud_python))

longitud_python_float = float(longitud_python)
print(longitud_python_float)
print(type(longitud_python_float))

longitud_python_str = str(longitud_python)
print(longitud_python_str)
print(type(longitud_python_str))


num3 = int(input("Introduce un número para comprobar si es par: "))
is_par = num3 % 2
if is_par == 0:
    print("El número ", num3, " es par")
else:
    print("El número", num3, "es impar")


# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# Check if type of '10' is equal to type of 10
# Check if int('9.8') is equal to 10

floor_division = 7 / 3
if floor_division == 2.7:
    print(True)
else:
    print(False)


if "10" == 10:
    print(True)
else:
    print(False)


if int(9.8) == 10:
    print(True)
else:
    print(False)

hours = int(input("Introduce las horas semanales "))
price = float(input("Introduce el precio por hora "))
total = hours * price
print("A la semana ganas: ", total)
