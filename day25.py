import pandas as pd
import numpy  as np

fruits = ["Orange", "Banana", "Mango"]
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)


dct = {"name": "David", "country": "Spain", "city": "Madrid"}
s = pd.Series(dct)
print(s)


dct = ["David", "Spain", "Madrid"]
s = pd.Series(dct, index=["name", "country", "city"])
print(s)


data = [
["David", "España", "Madrid"],
["John", "Inglaterra", "Londres"],
["María", "Francia", "París"]
]

df = pd.DataFrame(data, columns=["Nombre", "Paín", "Ciudad"])
print(df)


data = {"Name": ["David", "John", "María"], "Country": ["Spain", "Inglaterra", "Francia"], "Ciudad": ["Madrid", "Londres", "París"]}
df = pd.DataFrame(data)
print(df)

weights = [74, 78, 69]
df["Weight"] = weights
print(df)

heights = [173, 175, 169]
df['Height'] = heights
print(df)


# Read the hacker_news.csv file from data directory
df = pd.read_csv('weight-height.csv')

# Get the first five rows
print(df.head())


# Get the last five rows
print(df.tail())

# Get the title column as pandas series
print(df.columns)

# Count the number of rows and columns
# Explore the data and make sense of it

num_filas = len(df)
num_columnas = len(df.columns)
print("Número de filas:", num_filas)
print("Número de columnas:", num_columnas)

# Filter the titles which contain python
count_python = df.apply(lambda x: x.astype(str).str.contains('python', case=False)).sum().sum()
print("Número de veces que aparece la palabra 'python' en todo el DataFrame:", count_python)

# Filter the titles which contain JavaScript
count_javascript = df.apply(lambda x: x.astype(str).str.contains('JavaScript', case=False)).sum().sum()
print("Número de veces que aparece la palabra 'python' en todo el DataFrame:", count_javascript)