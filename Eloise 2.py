# def freq_lettres(liste_de_mots):
#     liste_jointe = "".join(liste_de_mots)
#     liste_jointe = liste_jointe.lower()
#     while len(liste_jointe) > 0:
#         lettre_en_cours = liste_jointe[-1]
#         nbr_de_lettres = liste_jointe.count(lettre_en_cours)
#         print(lettre_en_cours + " : " + str(nbr_de_lettres))
#         liste_jointe = liste_jointe.replace(lettre_en_cours, "")
#
# liste_bidon = ["gchgehn", "dhnege", "dwgjcg"]
# freq_lettres(liste_bidon)


def liste_triee(liste):
    liste.sort()
    return liste

def recherche_titre(liste):
    livre_donner = input("Entrer un titre: ")
    liste_temp=[]
    for livre in liste:
        if livre_donner.lower() in livre.lower():
            liste_temp.append(livre)
    return liste_temp

def transfo_titre(liste):
    liste_temp_min = []
    liste_temp_maj = []
    for livre in liste:
        liste_temp_min.append(livre.lower())
        liste_temp_maj.append(livre.upper())
    return liste_temp_min, liste_temp_maj

def comptage_caractere(liste):
    liste_temp=[]
    for livre in liste:
        liste_temp.append(len(livre))
    return liste_temp

def extraction_titre(liste):
    titre_choisi = liste[1]
    liste_temp = titre_choisi.split(" ")
    for mot in liste_temp:
        print(mot)

def modifier_liste(liste):
    pass


livres = ["Le Petit Prince", "Les Misérables", "Germinal", "L'Étranger", "Harry Potter"]
livres_tries = liste_triee(livres)
print(livres_tries)
livre_trouver = recherche_titre(livres_tries)
print(livre_trouver)
liste_changer = transfo_titre(livres_tries)
print(liste_changer)
caractere_compte = comptage_caractere(livres_tries)
print(caractere_compte)
extraction_titre(livres_tries)

