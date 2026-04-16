import pandas as pd
import random as rd

collection = {"a": 1, "b": 2, "c": 3}

for cle, valeur in collection.items():
    if cle == "b":
        print(valeur)

imbriquee = [
    [{1}, (2, 4), {"a": 3}],
    [4, 5, 6],
    [7, 8, 9, 10, 11, 12]
]

print(imbriquee[2][1])

notes = [rd.randint(0, 100) for i in range(100)]
print(notes)

df = pd.read_excel("./Doc_excel.xlsx", sheet_name="Tableaux et calculs", usecols="B:G")
print(df)

