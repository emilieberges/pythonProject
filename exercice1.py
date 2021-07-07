# -*-coding:Utf-8 -*
# print("hello")

#1. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est positif (>= 0) ou non, et affiche
#“positif” ou “négatif”.
#1.1 saisie du nb entier
# i_entier = int(input("Veuillez saisir un nb entier: \n"))
# #1.2 tester si ce nb est positif
# if i_entier >=0:
#     #1.3 afficher positif
#     print("la valeur saisie est positive")
# else:
#     #1.4 afficher négatif
#     print("la valeur saisie est négative")


#2. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est strictement positif, nul ou strictement
#négatif, et affiche ce résultat.
#2.1 saisie du nb entier
# i_entier = int(float(input("Veuillez saisir un nb entier: \n")))
# #2.2 tester si le nombre est strictement positif
# if i_entier > 0:
#     print("la valeur est strictement positive")
#     #2.3 affiche si nul
# elif i_entier == 0:
#     print("la valeur est nulle")
# #2.3 afficher negatif
# else:
#     print("la valeur est strictement négative")





#3. Écrire un algorithme qui demande un réel à l’utilisateur et affiche sa valeur absolue (sans utiliser de fonction
#prédéfinie évidemment).
#3.1 Saisir un nombre réel
# i_reel = float(input("Veuillez écrire un réel"))
# # 3.2 afficher sa valeur absolue
# if i_reel < 0:
#     i_reel = -i_reel
#
# print("la valeur absolue de i_reel est ", (i_reel))


#4. Écrire un algorithme qui demande un réel à l’utilisateur et l’arrondit à l’entier le plus proche (les x,5 seront arrondis
#à l’entier supérieur).
# i_reel = float(input("Veuillez écrire un réel: \n"))
# i_tronque = int(i_reel) #-4
# delta = i_reel - i_tronque #0.5
#
# i_arrondi = i_tronque
# if delta >= 0.5 and i_reel >= 0:
#     i_arrondi = i_tronque + 1
# elif delta <= -0.5 and i_reel < 0:
#     i_arrondi = i_tronque - 1
#
# print("l'arrondi de", i_reel, "est", i_arrondi)

#5. Écrire un algorithme qui demande le numéro d’un mois et affiche le nombre jours que comporte ce mois (sans tenir
#compte des années bissextiles).
#Saisir le numéro d'un mois
# #
# mois = input("Partie 5: Tapez un numéro de mois (entre 0 et 12) svp => ")
# if int(mois) < 0:
#     print("Le numéro de mois doit être supérieur ou égal à 1")
# elif int(mois) > 12:
#     print("Le numéro de mois doit être inférieur ou égal à 12")
# else:
#     if int(mois) == 2:
#         print("Le mois", mois, "comporte 28 jours")
#     elif (int(mois) == 4) or (int(mois) == 6) or (int(mois) == 9) or (int(mois) == 11):
#         print("Le mois", mois, "comporte 30 jours")
#     else:
#         print("Le mois", mois, "comporte 31 jours")


#6. Écrire un algorithme qui vérifie si une année est bissextile. On rappelle qu’il y a des années bissextiles tous les
#4 ans, mais la première année d’un siècle ne l’est pas (1800, 1900 n’étaient pas bissextiles) sauf tous les 400 ans
#(2000 était une année bissextile).
#nota: l'opérateur %n (modulo n) permet de détecter les cycles et renvoie 0 si on ne se trouve pas en début/fin de cycle
#exemple %4 sur un nombre i incrémenté à partir de 0, i%4 va donner la suite 0 1 2 3 0 1 2 3 0 etc..
#i=0
#while i< 10
#   print(i, "%4 vaut", i%4)
#i = i+1
#si (annéee%4 == 0 et annee%100 != 0) ou année%400 == 0 alors année bissextile
# annee = int(input("exercice 1.6: veuillez saisir une année: \n"))
# if (annee%4 == 0 and annee%100 != 0) or annee%400 == 0:
#     print("L'année", annee, "est bissextile")
# else:
#     print("l'année", annee, "est pas bissextile")

# 7. Écrire un algorithme qui demande une date sous la forme de 2 nombres entiers (numéro du jour et numéro du mois)
# et affiche la saison (ex : 12/02; hiver). On supposera que le premier jour de la saison est toujours le 21.
# jour = int(input("Partie 7: Ecrire un numéro du jour svp: \n"))
# mois = int(input("Partie 7: Ecrire un numéro du mois svp: \n"))
# if (jour >= 21 and mois == 12) or mois == 1 or mois == 2 or (jour< 21 and mois == 03):
#     print("c'est l'hiver")
# elif (jour >= 21 and mois == 03) or mois == 4 or mois == 5 or (jour<21 and mois == 06):
#     print("vive le printemps")
# elif(jour >= 21 and mois == 06) or mois == 7 or mois == 8 or (jour <21 and mois== 9):
#     print("vive l'été")
# else:
#     print("c'est l'automne")