#acceder au element d'une liste
maliste= [10,20,30,40,50,60,70]
print(maliste[0])
print(maliste[-1])
print(maliste[-2])
#acceder aux element par slice
#maliste= liste1[debut:fin:step]
liste1= maliste[2:5]
liste1= maliste[: :-1]
print(liste1)
#PARCOURIRE UNE LISTE
maliste=[1,2,3,4,5]
#BOUCLE FOR
for i in maliste
    print(i, end=" ")
#boucle while
i=0
while(i< len(maliste)):
    print(maliste[i], end=" ")
    i=i+1
 #impaire
maliste= [0,1,2,3,4,5,6,7,8,9,10,11]
for i in maliste:
    if(i % 2 != 0):
        print(i, end=" ")
# #parcourir une liste
# maliste= [0,1,2,3,4,5,6,7,8,9,10]
#
# #boucle for
# for i in maliste:
#     print(i, end="**")
#
# #boucle while
# print()
# i = 0
# while(i < len(maliste)):
#     print(maliste[i], end="--")
#     i =i+1

#exercice01: afficher uniquement les nombres pairs entre 0 et 11
#exercice02: afficher uniquement les nombres impairs entre 0 et 11

# maliste= [0,1,2,3,4,5,6,7,8,9,10,11]
# for i in maliste:
#     if(i % 2 != 0):
#         print(i, end=" ")

#exercice 03: ecrire un programme qui affiche une element d'une liste
#ainsi que ses indices positif et negatif
#maliste= ["Mohessen", "Mohammed", "Iurie"]
maliste= [0,1,2,3,4,5,6,7,8,9,10]
n= len(maliste)
# print(n)
for i in range(n):
   print(maliste[i], "est disponible a l'indice positif: ", i, " et a l'indice negatif: ", i-n)
# Exercice 05: 1-creer une liste vide
#             2-Ajouter tous les nombres divisibles par 10 dans cette liste jusqu'100
# Exercice 05:
# 1-creer une liste vide
ma_liste = []

# 2-Ajouter tous les nombres divisibles par 10 dans cette liste jusqu'100
for i in range(101):
    if i % 10 == 0:
        ma_liste.append(i)

print(ma_liste)
# print(x.count(10))

#index() retourne l'indice de la premiere apparution d'un element
# maliste= [1,2,3,3,3,3,5]
# print( 0 in maliste)
# print( 1 in maliste)
# print(maliste.index(10))

#append() ajoute un element a la fin de notre liste
# maliste= []
# maliste.append(9)
# maliste.append(90)
# maliste.append("test")
# print(maliste)

#Exercice 05: 1-creer une liste vide
#             2-Ajouter tous les nombres divisibles par 10 dans cette liste jusqu'100


#insert() ajouter un element dans une liste a un indice specifique

# maliste= [1, 2, 3, 4]
# maliste.insert(1, 'test')
# print(maliste)
#
# maliste.insert(0, 'python')
# print(maliste)
#
# maliste.insert(11, 'java')
# print(maliste)
#
# maliste.insert(-10, 'javascript')
# print(maliste)

#extend() elle ajoute un ensemble d'elements (d'un coup) a la fin d'une liste
list01= ['java', 'C#', "python"]
list02= ['PHP', 'C++', "Javascript"]
print(list01 + list02)
list01.extend(list02)
# list02.extend(list01)
print(list01)
# print(list02)
