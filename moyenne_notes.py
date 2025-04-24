# 0
liste_etu, liste_tp1, liste_tp2, liste_exam = [], [], [], [] # Le faire sur plusieurs lignes fonctionne aussi

for i in range(5): # Range(0,5) fonctionne aussi
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
        moyenne = round(tp1[j] * 0.25 + tp2[j] * 0.25 + exam[j] * 0.5, 4)
        liste_moy.append(moyenne)
    return liste_moy


# 2
def affichage(etu, tp1, tp2, exam, moyenne):
    for k in range(len(etu)):
        print("L'étudiant " + etu[k] + " a eu " + str(tp1[k]) + " % dans le tp1, " + str(tp2[k]) + " % dans le tp2 et "
              + str(exam[k]) + " % dans son examen, ce qui lui donne une moyenne de " + str(moyenne[k]) + " %.")


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
def moyenne_groupe(moyenne):
    moy_groupe = 0
    for elem in moyenne:
        moy_groupe += elem
    return round(moy_groupe/len(moyenne), 4)

moyenne_g = moyenne_groupe(liste_moyennes)
print("\nVoici les élèves ayant une moyenne supérieure à la moyenne de leur groupe (" + str(moyenne_g) + " %) :\n")
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


# 5
print("\nVoici les élèves ayant passé le cours :\n")

def passer_cours(note_tp1, note_tp2, note_exam):
    if (note_tp1 + note_tp2) / 2 >= 60 and note_exam >= 60:
        return True
    else:
        return False

temp_moy, temp_etu, temp_tp1, temp_tp2, temp_exam = [], [], [], [], []

for i in range(len(liste_etu)):
    if passer_cours(liste_tp1[i], liste_tp2[i], liste_exam[i]):
        temp_moy.append(liste_moyennes[i])
        temp_etu.append(liste_etu[i])
        temp_tp1.append(liste_tp1[i])
        temp_tp2.append(liste_tp2[i])
        temp_exam.append(liste_exam[i])

if not temp_etu:
    print("Aucun étudiant a passé le cours.")

affichage(temp_etu, temp_tp1, temp_tp2, temp_exam, temp_moy)


# 6
print("\nVoici les notes des étudiants après l'augmentation de 10 % sur l'examen :\n")

for i in range(len(liste_exam)):
    liste_exam[i] *= 1.1
    liste_exam[i] = round(liste_exam[i], 4)

liste_moyennes = calcul_moyenne(liste_tp1, liste_tp2, liste_exam)
affichage(liste_etu, liste_tp1, liste_tp2, liste_exam, liste_moyennes)


##
del(temp_moy, temp_etu, temp_tp1, temp_tp2, temp_exam)

