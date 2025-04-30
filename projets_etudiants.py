# 1
donnees = ["Alice Dupont,15,17,18", "Bernard Poulin,12,16,19", "Raymond Genet,18,19,20", "Rose-Marie Lebas,18,19,20",
           "Loïc Astier,11,12,10"]


# 2
livrables_dict = {}

for donnee in donnees:
    donnees_split = donnee.split(",")
    print(donnees_split)
    livrables_dict[donnees_split[0]] = donnees_split[1:]

print("\n" + str(livrables_dict))


# 3
def calcul_moyennes(livrables):
    for eleve, informations in livrables.items():
        moyenne_notes = 0
        for information in informations:
            moyenne_notes += int(information)
        moyenne_notes /= len(informations)
        livrables[eleve].append(str(round(moyenne_notes, 2)))

calcul_moyennes(livrables_dict)
print("\n" + str(livrables_dict) + "\n")


# 4
def afficher_resultats(livrables):
    for eleve, informations in livrables.items():
        print(eleve + " a eu " + informations[0] + ", " + informations[1] + ", " + informations[2] +
              " pour ses livrables, soit une moyenne de " + informations[3])

afficher_resultats(livrables_dict)


# 5
liste_moyennes = []

for eleve_x, informations_x in livrables_dict.items():
    liste_moyennes.append(float(informations_x[3]))

meilleure_moyenne = max(liste_moyennes)

meilleurs_eleves = {}
for eleve_x, informations_x in livrables_dict.items():
    if float(informations_x[3]) == meilleure_moyenne:
        meilleurs_eleves[eleve_x] = livrables_dict[eleve_x]

print("\nVoici les meilleurs élèves :\n")
afficher_resultats(meilleurs_eleves)

