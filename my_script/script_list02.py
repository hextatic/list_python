# #fonction pop() elle supprime le dernier element dans une liste et le retourne
# list03=[10,20,30,40,50]
# print(list03)
# print(list03.pop())
# print(list03)
# print(list03.pop())
# print(list03)
# #vous pouvez specifier une indice que vous voulez supprimer
# print(list03.pop(0))
# print(list03)
#
# a= list03.pop(0)
# print(a*10)

#fonction remove cest pour supprimer un element specifique
list04=[10,20,30,40,50]
list04.remove(40)
print(list04)
list04.remove(60)
print(list04)

# tri des elements d'une liste
# inversion
list01=[10,20,30,40]
list01.reverse()
print(list01)
#sort pour trier en ordre croissant des nombres
list02=[40,30,20,15,60,70,2]
list02.sort()
print(list02)
# avec les chaines de caractere il va en ordre alphabetique
list03=["test02", "test01", "test03"]
list03.sort()
print(list03)
list04=["mohammed", "iurie", "hassan", "Rameen", "rameen", "Rameez"]
list04.sort()
print(list04)
#on ne peut pas melanger int et str
list05=[20,10,5, "test"]
list05.sort()
print(list05)

