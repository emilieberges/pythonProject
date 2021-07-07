# -*-coding:Utf-8 -*
# print("hello")
# En utilisant des boucles while lorsque le nombre d'itérations n'est pas connu et des boucles for lorsque le nombre d'itérations est connu :
#
# 1. Écrire un algorithme qui demande un entier positif, et le rejette tant que le nombre saisi n’est pas conforme.
#
# i = -1
# while (i < 0):
#     i = int(float(input("veuillez saisir un entier positif: \n")))
#     if i < 0:
#         print("le nombre", i, "saisi est non conforme")
# print("le nb", i, "saisi est positif, donc conforme")

#

# 2. Écrire un algorithme qui demande 10 entiers, compte le nombre d’entiers positifs saisis, et affiche ce résultat.
# cpt = 0
# for i in range(10):
#     a = int(float(input("veuillez saisir un entier positif ou negatif: \n")))
#     if a>= 0:
#         cpt = cpt + 1
# print("le nom d'entier positif saisi est", cpt)


#

# # 3. Écrire un algorithme qui demande des entiers positifs à l’utilisateur, les additionne, et qui s’arrête en affichant le
# # résultat dès qu’un entier négatif est saisi.
# # i est un entier positif
# i = 1
# somme = 0
# while (i >= 0):
#     i = int(float(input("veuillez entrez un entier positif: \n")))
#     if i >= 0:
#         somme += i
# print("La somme des entiers positifs saisis est égale à", somme)



# # 4. Modifier ce dernier algorithme pour afficher la moyenne de la série d’entiers positifs saisis.
# i = 1
# nombre = 0
# somme = 0
# moyenne = 0
#
# while (i >= 0):
#     i = int(float(input("veuillez entrez un entier positif: \n")))
#     if i >= 0:
#         somme += 1
#         nombre = nombre + 1
#     if i < 0:
#         break
# moyenne = somme /nombre
# print("La moyenne des entiers positifs est ", moyenne)


#Exercices sur les Listes
# jour = ["lundi", "mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
# print(jour)

# fruits et légumes
# fruits = ['orange','fraises']
# # legumes = ['carottes', 'brocolis']
# # print(fruits + legumes)
# fruits[2:2]=['miel']
# print(fruits)
# #suppression
# fruits[2:3]= ['pommes']
# print(fruits)
# fruits[2:3]= []
# print(fruits)
# fruits[1:]= ['poires','ananas','kiwis']
# print(fruits)
#
# #fable
# fable = ["je","plie","mais","ne","romps","pas"]
# print(" ".join(fable))

#
# sept_zeros = [0]*7 ; sept_zeros
# print(sept_zeros)
#
# L = ['Dans', 'Python', 'tout', 'est', 'objet']
# len(L)

s = [0]*tailleListe
for i in range(tailleListe):
    s[i] = random()
print(s)






