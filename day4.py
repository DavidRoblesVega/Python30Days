# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
concatenate = "Thirty " "Days " "Of " "Python"
print(concatenate)

# Declare a variable named company and assign it to an initial value "Coding For All".
# Print the variable company using print().
# Print the length of the company string using len() method and print().
# Change all the characters to uppercase letters using upper() method.
# Change all the characters to lowercase letters using lower() method
company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())

cadena = "Coding For All"
# Usar el método capitalize() para capitalizar la primera letra de la cadena
print(cadena.capitalize())

# Usar el método title() para capitalizar la primera letra de cada palabra en la cadena
print(cadena.title())

# Usar el método swapcase() para intercambiar entre minúsculas y mayúsculas
print(cadena.swapcase())


palabras = cadena.split()
primera_palabra = palabras[0]
print(primera_palabra)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
palabra = "Coding"

try:
    indice = cadena.index(palabra)
    print(f"La palabra '{palabra}' se encuentra en la posición {indice} en la cadena.")
except ValueError:
    print(f"La palabra '{palabra}' no se encuentra en la cadena.")

# Replace the word coding in the string 'Coding For All' to Python.
python = "Python"
replace = cadena.replace("Coding", python)
print(replace)

# Split the string 'Coding For All' using space as the separator (split()) .
cadena = "Coding For All"
palabras = cadena.split()
print(palabras)

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
cadena = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
empresas = cadena.split(", ")
print(empresas)

# What is the character at index 0 in the string Coding For All.
cadena = "Coding For All"
primer_caracter = cadena[0]
print(primer_caracter)


# What is the last index of the string Coding For All.
cadena = "Coding For All"
longitud = len(cadena)
ultimo_caracter = cadena[longitud-1]
print(ultimo_caracter)

# What character is at index 10 in "Coding For All" string.
cadena = "Coding For All"
caracter_indice_10 = cadena[10]
print(caracter_indice_10)

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
nombre = "Python For Everyone"
palabras = nombre.split()  # Dividir el nombre en palabras
acrónimo = "".join(word[0] for word in palabras)
print(acrónimo)


# Use index to determine the position of the first occurrence of C in Coding For All.
# Use index to determine the position of the first occurrence of F in Coding For All.
cadena = "Coding For All"
letra = cadena.index("C")
print(letra)

cadena = "Coding For All"
letra = cadena.index("F")
print(letra)


# Use rfind to determine the position of the last occurrence of l in Coding For All People.
letra = cadena.rfind("l")
print(letra)


# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'

# Usando el método index()
index = sentence.index('because')
print("La posición de la primera ocurrencia de 'because' es:", index)

# Usando el método find()
index = sentence.find('because')
print("La posición de la primera ocurrencia de 'because' es:", index)


# Does ''Coding For All' start with a substring Coding?
cadena = 'Coding For All'
substring = 'Coding'

if cadena.startswith(substring):
    print("Sí, 'Coding For All' comienza con 'Coding'.")
else:
    print("No, 'Coding For All' no comienza con 'Coding'.")


# Which one of the following variables return True when we use the method isidentifier():
cadena1 = "30DaysOfPython"
cadena2 = "thirty_days_of_python"

print(cadena1.isidentifier())
print(cadena2.isidentifier())

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_string = " ".join(libraries)
print(joined_string)