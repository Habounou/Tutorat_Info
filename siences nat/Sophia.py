tp1 = [1, 2, 3, 4, 5]
tp2 = [4, 5, 6, 7, 8]
tp3 = [7, 8, 9, 10, 11]
notes_add = []

for i in range(len(tp1)):
    note1 = tp1[i]
    note2 = tp2[i]
    note3 = tp3[i]
    addition = note1 + note2 + note3
    notes_add.append(addition)

# print(notes_add)

# On veut une suite de Fib. (0, 1, 1, 2, 3, 5...) jusqu'à un entier limite k.
k = 22
suite_fib = [0, 1]
suivant = 1

while suivant < k:
    suite_fib.append(suivant)
    # [0, 1, 1, 2...]
    suivant = suite_fib[-1] + suite_fib[-2]

# print(suite_fib)

# Dernier passage comète : 1986, à chaque 76. Dans les prochaines 1000 années, les passages (à partir de 2026).
annees_passages = []
decalage = 2026 - 1986

for i in range(0, decalage + 1000, 76):
    passage = 2026 + i
    annees_passages.append(passage)

print(annees_passages)

