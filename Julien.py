import random as rd


# def ajout_liste(liste: list):
#     nouv_liste = [input("Nom d'un item : ") for i in range(3)]
#     liste.extend(nouv_liste)
#
# liste_1: list = [13, 14, 15]
# ajout_liste(liste_1)
# print(liste_1)

def creer_jeu():
    jeu_temp = []
    for rangee in range(3):
        if rangee == 2:
            plancher_temp = "o"
            for i in range(9):
                nbr_aleatoire = rd.randint(0, 7)
                if nbr_aleatoire == 0:
                    plancher_temp += "-"
                else:
                    plancher_temp += "_"
            jeu_temp.append(plancher_temp)
            continue
        jeu_temp.append("          ")
    return jeu_temp

def afficher_jeu(jeu_fc):
    for rangee in jeu_fc:
        print(rangee)
    # for rangee in range(len(jeu_fc)):
    #     print(jeu_fc[rangee])

def avancer_joueur(jeu_fc):
    plancher = jeu_fc[-1]

    plancher_temp = ""
    positions_tiret = []
    for i in range(len(plancher)):
        if plancher[i] == "-":
            positions_tiret.append(i)

    position_joueur = plancher.find("o")
    for i in range(len(plancher)):
        if i == position_joueur + 1:
            plancher_temp += "o"
        elif i in positions_tiret:
            plancher_temp += "-"
        else:
            plancher_temp += "_"

    jeu_fc[-1] = plancher_temp
    return jeu_fc

def boucle_jeu(jeu_fc):
    afficher_jeu(jeu_fc)
    while True:
        input()
        avancer_joueur(jeu_fc)
        afficher_jeu(jeu_fc)

jeu = creer_jeu()
boucle_jeu(jeu)


