

# class Table:
#
#     def __init__(self, nbr_pattes:int=4):
#         self.couleur = "bleu"
#         self.nbr_pattes = nbr_pattes
#         self.largeur = 10
#         self.longueur = 15
#
#     def aire_table(self):
#         aire = self.largeur * self.longueur
#         return aire
#
#     def longueur_getter(self):
#         return self.longueur
#
#     def longueur_setter(self, valeur):
#         self.longueur = valeur
#
#
# class TableHuitPattes(Table):
#
#     def __init__(self):
#         super().__init__(8)
#         self.largeur = 20
#         self.longueur = 30
#
# table_bleue_1 = Table(6)
# # print(table_bleue_1.nbr_pattes)
# # aire_table_1 = table_bleue_1.aire_table()
# # print(aire_table_1)
# # table_bleue_1.longueur_setter(18)
# # print(table_bleue_1.longueur_getter())
# table_huit_pattes = TableHuitPattes()
# print(table_huit_pattes.aire_table())

import random as rd


class BaseDonnees:

    def __init__(self, nom, nom_famille, couleur, cegep):
        self.nom_1 = nom
        self.nom_famille_1 = nom_famille
        self.couleur_1 = couleur
        self.cegep_1 = cegep
        self.liste_personnes = [[nom, nom_famille, couleur, cegep]]

    def personne_getter(self):
        return rd.choice(self.liste_personnes)

    def ajout_personne(self, nom, nom_famille, couleur, cegep):
        self.liste_personnes.append([nom, nom_famille, couleur, cegep])

base_donnees = BaseDonnees("Éloïse", "Dupont", "rose", "cegep st hya")
base_donnees.ajout_personne("Hugo", "Barrette", "rouge", "cegep st hya")
choix_personne = base_donnees.personne_getter()
print(choix_personne)



