import random as rd


def rajouter_billes(liste, couleur: str, nbr_billes_a_rajouter):
    liste.extend(couleur * nbr_billes_a_rajouter)

ma_liste_string = "bleu$$rouge$vert$$$jaune"
ma_liste = ma_liste_string.split("$")

temp_liste = []
for i in range(len(ma_liste)):
    if ma_liste[i] == "":
        temp_liste.append(i)

nbr_decalage = 0
for i in temp_liste:
    i -= nbr_decalage
    del ma_liste[i]
    nbr_decalage += 1

nbr_billes = {"bleu": 3, "rouge": 2, "vert": 6, "jaune": 4}

couleur_choisie = input("Quelle couleur voulez vous rajoutez ? ")
nbr_rajouter = int(input("Combien de billes voulez vous rajouter ? "))
rajouter_billes(ma_liste, couleur_choisie, nbr_rajouter)


nbr_billes_a_acheter = int(input("Combien de billes voulez vous acheter ? "))

for key, value in nbr_billes.items():
    for i in range(value - 1):
        ma_liste.append(key)

rd.shuffle(ma_liste)
print(ma_liste[0:nbr_billes_a_acheter])

