# Tutorat_Info

## Exercice

Un professeur désire gérer les notes de ses étudiants. On suppose qu’il a 5 étudiants. Pour cela, il a décidé d’utiliser les listes comme structures de données.
On vous demande de saisir les informations suivantes pour 5 étudiants en respectant l’affichage suivant :

- Étudiant i (ici j’ai donné i qu’il faut remplacer par 1, 2, …5)
- Prénom et Nom
- Note tp1
- Note tp2
- Note examen
##
-	Les noms des étudiants doivent être stockés dans une liste etudiants
-	Les notes des tp1 doivent être stockées dans une liste tp1
-	Les notes des tp2 doivent être stockées dans une liste tp2
-	Les notes des examens doivent être stockées dans une liste examen

## On vous demande de :

1-	Écrire une fonction calcul_moyenne, qui prend en argument les listes tp1, tp2 et examens puis retourne une liste moyenne qui qui représente la moyenne pondérée des notes. Sachant que les pondérations des travaux sont : tp1 : 25%, tp2 : 25% examen 50%.

2-	Écrire une fonction affichage qui prend en arguments les listes étudiants, tp1, tp2, examens et moyenne puis pour chaque étudiant on écrit :
L’étudiant X a eu X1 dans tp1, X2 dans tp2 et X3 dans son examen ce qui lui donne une moyenne de X4 (avec X, X1, X2, X3 et X4 sont le nom, la note du tp1, la note du tp2 et la note de tp3 et la moyenne respectivement)

3-	Trier la liste moyenne dans l’ordre décroissant (sans utiliser de fonction prédéfinie). De plus, faites attention de préserver l’ordre en fonctions des informations des étudiants. Pour s’assurer, faites appel à la fonction affichage avant le tri puis après le tri.

4-	Afficher les noms des étudiants ayant une moyenne qui est supérieure strictement à la moyenne du groupe

5-	Quels sont les noms des étudiants ayant réussi le cours ? Pour réussir un cours, un étudiant doit avoir au moins 60% comme moyenne dans les deux TPS et 60% dans l’examen.

6-	Le professeur a décidé d’accorder un bonus à ces étudiants pour leurs sérieux et leurs persévérances. Pour cela, il a décidé d’accorder une augmentation de 10% de la note de l’examen de tous les étudiants. Réalisez cette augmentation puis faites appel à la fonction calcul_moyenne et affichage pour vérifier s’il y a eu des changements.
