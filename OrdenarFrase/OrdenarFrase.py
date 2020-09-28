from numpy import array
from collections import Counter
frase = 'es parte de crecer timmy'#Aqui cambia la frase
fra = frase.split()

archivo = open('frase.txt', 'r')#Aqui lee el txt
oracion = archivo.read()
ora = oracion.split()
archivo.close()
a = len(fra)

aux = [None]*a
ordenada = ""

for i in range(0, len(ora)):
    for j in range(0, len(ora)):
        if Counter(ora[i]) == Counter(fra[j]):
            aux[j] = ora[i]

for i in range(0, len(aux)):
    ordenada += aux[i]+" "
    print(ordenada)
