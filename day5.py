# Declare an empty list
lista = []

# Declare a list with more than 5 items
lista2 = ["tomate", "patata", "lechuga", "cebolla", "zanahoria", "manzana"]
print(lista2)

# Find the length of your list
print(len(lista2))

# Get the first item, the middle item and the last item of the list
primer_item = lista2[0]
medio_item = lista2[len(lista2)//2]
ultimo_item = lista2[len(lista2)-1]

print(primer_item)
print(medio_item)
print(ultimo_item)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["David", 25, 1.78, "soltero", "Fuenlabrada"]
print(mixed_data_types)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
primer_item = it_companies[0]
medio_item = it_companies[len(it_companies)//2]
ultimo_item = it_companies[len(it_companies)-1]

print(primer_item)
print(medio_item)
print(ultimo_item)

# Print the list after modifying one of the companies
it_companies[1] = "Tesla"
print(it_companies)

# Add an IT company to it_companies
it_companies.append("HP")
print(it_companies)

# Insert an IT company in the middle of the companies list
medio_item = len(it_companies)//2
it_companies.insert(medio_item, "Razer")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
resultado = "#; ".join(it_companies)
print(resultado)

# Check if a certain company exists in the it_companies list.
empresa_buscada = "Microsoft"

if empresa_buscada in it_companies:
    print("La empresa", empresa_buscada, "se encuentra en la lista")
else:
    print("La empresa", empresa_buscada, "no se encuentra en la lista")

# Sort the list using sort() method
it_companies.sort()
print(it_companies)


# Reverse the list in descending order using reverse() method
it_companies.sort()
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
primeras_tres_empresas = it_companies[:3]
print(primeras_tres_empresas)

# Slice out the last 3 companies from the list
ultimas_tres_empresa = it_companies[-3:]
print(ultimas_tres_empresa)

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the last IT company from the list
eliminar_ultima_impresa = it_companies.pop()
print(it_companies)
print("La empresa eliminada es ", eliminar_ultima_impresa)

# Remove all IT companies from the list
it_companies = ['Google', 'Apple', 'Microsoft', 'Facebook', 'Amazon', 'IBM']

for empresa in it_companies[:]:
    it_companies.remove(empresa)

print(it_companies)

# Destroy the IT companies list
it_companies = ['Google', 'Apple', 'Microsoft', 'Facebook', 'Amazon', 'IBM']
it_companies = []
print(it_companies)


# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack.append("Redux")
print(full_stack)
full_stack.append("Python")
print(full_stack)
full_stack.append("SQL")
print(full_stack)


#EXERCISES: LEVEL 2
# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
# Add the min age and the max age again to the list
# Find the median age (one middle item or two middle items divided by two)
# Find the average age (sum of all items divided by their number )
# Find the range of the ages (max minus min)
# Compare the value of (min - average) and (max - average), use abs() method

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages_sorted = sorted(ages)
print(ages_sorted)
min_ages = ages_sorted[0]
max_ages = ages_sorted[-1]
ages_sorted.append(min_ages)
ages_sorted.append(max_ages)
print(ages_sorted)

n = len(ages_sorted)
if n % 2 == 0:
    median_age = (ages_sorted[n//2 - 1] + ages_sorted[n//2]) / 2
else:
    median_age = ages_sorted[n//2]
print(median_age)

average_ages = sum(ages_sorted) / len(ages_sorted)
print(average_ages)

age_ranges = max_ages - min_ages
print(age_ranges)

difference_min_average = abs(min_ages - average_ages)
difference_max_average = abs(max_ages - average_ages)
print(difference_min_average)
print(difference_max_average)















































































































































