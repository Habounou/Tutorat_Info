# 0
liste_etu, liste_tp1, liste_tp2, liste_exam = [], [], [], [] # Le faire sur plusieurs lignes fonctionne aussi

for i in range(3): # Range(0,5) fonctionne aussi
    liste_etu.append(input("Prénom de l'étudiant : "))
    liste_etu[i] += ", " + input("Nom de l'étudiant : ")

    while True:
        liste_tp1.append(int(input("Note au tp1 : ")))
        if 0 <= liste_tp1[i] <= 100:
            break
        else:
            del(liste_tp1[i])
    while True:
        liste_tp2.append(int(input("Note au tp2 : ")))
        if 0 <= liste_tp2[i] <= 100:
            break
        else:
            del(liste_tp2[i])
    while True:
        liste_exam.append(int(input("Note à l'examen final : ")))
        if 0 <= liste_exam[i] <= 100:
            break
        else:
            del(liste_exam[i])


# 1
def calcul_moyenne(tp1, tp2, exam):
    liste_moy = []
    for j in range(len(tp1)):
        moyenne = tp1[j] * 0.25 + tp2[j] * 0.25 + exam[j] * 0.5
        liste_moy.append(moyenne)
    return liste_moy


# 2
def affichage(etu, tp1, tp2, exam, moyenne):
    for k in range(len(etu)):
        print(f"L'étudiant {etu[k]} a eu {tp1[k]} % dans le tp1, {tp2[k]} % dans le tp2 et {exam[k]} % dans son examen, "
              f"ce qui lui donne une moyenne de {moyenne[k]} %.")


# 3
print("\nVoici la liste des informations des élèves non-triée :\n")

liste_moyennes = calcul_moyenne(liste_tp1, liste_tp2, liste_exam)
affichage(liste_etu, liste_tp1, liste_tp2, liste_exam, liste_moyennes)


temp_moy, temp_etu, temp_tp1, temp_tp2, temp_exam = [], [], [], [], []

for i in range(len(liste_moyennes)):
    l = liste_moyennes.index(max(liste_moyennes))
    temp_moy.append(liste_moyennes.pop(l))
    temp_etu.append(liste_etu.pop(l))
    temp_tp1.append(liste_tp1.pop(l))
    temp_tp2.append(liste_tp2.pop(l))
    temp_exam.append(liste_exam.pop(l))

liste_moyennes, liste_etu, liste_tp1, liste_tp2, liste_exam = (temp_moy, temp_etu, temp_tp1, temp_tp2, temp_exam)


print("\nVoici la liste des informations des élèves triée :\n")
affichage(liste_etu, liste_tp1, liste_tp2, liste_exam, liste_moyennes)


# 4
print("\nVoici les élèves ayant une moyenne supérieure à la moyenne de leur groupe :\n")

def moyenne_groupe(moyenne):
    moy_groupe = 0
    for elem in moyenne:
        moy_groupe += elem
    return moy_groupe


moyenne_g = moyenne_groupe(liste_moyennes)
etu_sup_index = []

for note in liste_moyennes:
    if note > moyenne_g:
        etu_sup_index.append(liste_moyennes.index(note))


temp_moy, temp_etu, temp_tp1, temp_tp2, temp_exam = [], [], [], [], []

if etu_sup_index:
    for index in etu_sup_index:
        temp_moy.append(liste_moyennes[index])
        temp_etu.append(liste_etu[index])
        temp_tp1.append(liste_tp1[index])
        temp_tp2.append(liste_tp2[index])
        temp_exam.append(liste_exam[index])
else:
    print("Tout le monde est exactement sur la moyenne.")

affichage(temp_etu, temp_tp1, temp_tp2, temp_exam, temp_moy)

