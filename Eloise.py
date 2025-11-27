def liste_mots():
    while True:
        mots_utilisateur = input("Entrez au moins 3 mots séparés par des espaces: ")
        liste_mots_utilisateur = mots_utilisateur.split(" ")
        if len(liste_mots_utilisateur) >= 3:
            return liste_mots_utilisateur
        else:
            print("Vous devez entrer au moins 3 mots.")


def longueur_mots(liste_de_mots):
    valeur_min = 999
    valeur_max = 0
    for mot in liste_de_mots:
        if len(mot) > valeur_max:
            valeur_max = len(mot)
        if len(mot) < valeur_min:
            valeur_min = len(mot)

    liste_min = []
    liste_max = []
    for mot in liste_de_mots:
        if len(mot) == valeur_min:
            liste_min.append(mot)
        if len(mot) == valeur_max:
            liste_max.append(mot)

    return {"min": liste_min, "max": liste_max}


def nouvelle_liste(liste_de_mots):
    for mot in liste_de_mots:
        i = liste_de_mots.index(mot)
        if len(mot) % 2 == 0:
            liste_de_mots[i] = mot.upper()
        else:
            liste_de_mots[i] = mot[::-1]

    return liste_de_mots


def retirer_mot(liste_de_mots):
    while True:
        mot_a_retirer = input("Entrer un mot à retirer de la liste: ")
        for mot in liste_de_mots:
            if mot == mot_a_retirer:
                liste_de_mots.remove(mot)
                return liste_de_mots
        print("Ce mot n'est pas dans la liste.")


def fusionner_liste(liste1):
    liste2 = input("Entrer une liste d'entiers: ")
    liste2 = liste2.split(" ")
    for entier in liste2:
        liste1.append(int(entier))
    return liste1


def liste_croissant(liste_pas_bon_ordre):
    liste_temp=[]
    while True:
        min_en_cours = liste_pas_bon_ordre[0]
        for i in range(len(liste_pas_bon_ordre) - 1):
            if liste_pas_bon_ordre[i + 1] < min_en_cours:
                min_en_cours = liste_pas_bon_ordre[i + 1]
        liste_temp.append(min_en_cours)
        liste_pas_bon_ordre.remove(min_en_cours)
        if len(liste_pas_bon_ordre) == 0:
            return liste_temp



# liste_input = liste_mots()
# print(liste_input)
# longueur_input = longueur_mots(liste_input)
# print(longueur_input)
# nouveaux_mots = nouvelle_liste(liste_input)
# print(nouveaux_mots)
# liste_tronquee = retirer_mot(nouveaux_mots)
# print(liste_tronquee)
liste_fusionnee = fusionner_liste([1, 2, 3])
print(liste_fusionnee)
liste_triee = liste_croissant(liste_fusionnee)
print(liste_triee)