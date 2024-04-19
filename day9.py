# Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

edad = int(input("Enter your age "))
if edad >= 18:
    print("You are old enough to learn to drive")
else:
    print("You need", (18-edad), "more years to learn to drive")


# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = 25
your_age = int(input("Enter your age "))
if my_age > your_age:
    print("I'm older than you")
elif my_age == your_age:
    print("Our age is the same")
else:
    print("You're older than me")


# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))
if num1 > num2:
    print(num1, "is greater than", num2)
elif num2>num1:
    print(num2, "is greater than", num1)
else:
    print(num1, "is equal to", num2)

# Write a code which gives grade to students according to theirs scores:
score = int(input("Enter your score "))

if 80<= score <=100:
    grade = "A"
elif 70<= score <=89:
    grade = "B"
elif 60<= score <=69:
    grade = "C"
elif 50<= score <=59:
    grade = "D"
elif 0<= score <=49:
    grade = "B"
else:
    grade = "Invalid score"

print("The student's grade is:", grade)


# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

month = input("Enter this month: ")

if month == "September" or month == "October" or month == "November":
    season = "Autumn"
elif month == "December" or month == "January" or month == "February":
    season = "Winter"
elif month == "March" or month == "April" or month == "May":
    season = "Spring"
elif month == "June" or month == "July" or month == "August":
    season = "Summer"
else:
    season = "Month is incorrect"
print("The season is", season)


# The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

new_fruit = input("Enter the fruit: ")
fruits = ['banana', 'orange', 'mango', 'lemon']

if new_fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(new_fruit)
    print("Modified list:", fruits)

# Here we have a person dictionary. Feel free to modify it!
# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
# * If the person is married and if he lives in Finland, print the information in the following format:

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills_list = person['skills']
    if len(skills_list) > 2:  # Verifica si hay al menos tres habilidades para obtener el skill medio
        middle_skill = skills_list[len(skills_list) // 2]
        print("Middle skill:", middle_skill)
    else:
        print("There are not enough skills to determine the middle one.")
else:
    print("The person dictionary does not have the 'skills' key.")


# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person:
    skills_list = person["skills"]
    if "Python" in skills_list:
        print("Python exists in the list")
    else:
        print("Python don't exists in the list")
else:
    print("The person dictionary does not have the 'skills' key.")


skills = person.get("skills", [])
is_front_end = 'JavaScript' in skills and 'React' in skills
is_back_end = 'Node' in skills and 'Python' in skills and 'MongoDB' in skills
is_fullstack = 'React' in skills and 'Node' in skills and 'MongoDB' in skills

if is_front_end:
    print("He is a front end developer")
elif is_back_end:
    print("He is a backend developer")
elif is_fullstack:
    print("He is a fullstack developer")
else:
    print("Unknown title")
