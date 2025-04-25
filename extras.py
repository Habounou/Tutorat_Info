# Exemple d'un algorithme de tri rapide
fausse_liste_moy = [98.5, 87.2, 35.2, 76.4, 42.0]
while True:
    temp_moy = fausse_liste_moy.copy()
    for i in range(len(fausse_liste_moy)):
        if i != 0:
            if fausse_liste_moy[i] > fausse_liste_moy[i - 1]:
                fausse_liste_moy[i], fausse_liste_moy[i - 1] = fausse_liste_moy[i - 1], fausse_liste_moy[i]
    if fausse_liste_moy == temp_moy:
        break
print(fausse_liste_moy)


# Différence entre .append() et l'opérateur '+' (inverse de ce que j'avais dit à la première rencontre)
lettres_rand1 = ['t', 'u']
lettres_rand2 = ['j', 'z']
lettres_rand3 = []

lettres_rand4 = lettres_rand1 + lettres_rand2
print(lettres_rand4)

lettres_rand3.append(lettres_rand1)
lettres_rand3.append(lettres_rand2)
print(lettres_rand3)