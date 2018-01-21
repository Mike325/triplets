""" Escriba un programa que genere un millon de numeros enteros aleatorios
entre -100 y 100.
1.- Escriba los primero 1,000 en un archivo 1Knums.txt
2.- Escriba los primero 2,000 en un archivo 2Knums.txt
3.- Escriba los primero 5,000 en un archivo 5Knums.txt
4.- Escriba los primero 10,000 en un archivo 10Knums.txt
5.- Escriba los primero 100,000 en un archivo 100Knums.txt
6.- Escriba el millon de numeros en un archivo 1Mnums.txt """

import random
import time

start_time = time.time()
file_1k = open ('1Knums.txt', 'w')
file_2k = open ('2Knums.txt', 'w')
file_5k = open ('5Knums.txt', 'w')
file_10k = open ('10Knums.txt', 'w')
file_100k = open ('100Knums.txt', 'w')
file_1m = open ('1Mnums.txt', 'w')

for x in range(1000000):
    number = str(random.randint(-100,100))
    if x <= 999 :
        file_1k.write(number + ',')
        file_2k.write(number + ',')
        file_5k.write(number + ',')
        file_10k.write(number + ',')
        file_100k.write(number + ',')
        file_1m.write(number + ',')

    elif x <= 1999:
        file_2k.write(number + ',')
        file_5k.write(number + ',')
        file_10k.write(number + ',')
        file_100k.write(number + ',')
        file_1m.write(number + ',')

    elif x <= 4999:
        file_5k.write(number + ',')
        file_10k.write(number + ',')
        file_100k.write(number + ',')
        file_1m.write(number + ',')

    elif x <= 9999:
        file_10k.write(number + ',')
        file_100k.write(number + ',')
        file_1m.write(number + ',')

    elif x <= 99999:
        file_100k.write(number + ',')
        file_1m.write(number + ',')

    elif x <= 999999:
        file_1m.write(number + ',')      

print(x)
print("EXE TIME: " + str(time.time() - start_time))

file_1k.close()
file_2k.close()
file_5k.close()
file_10k.close()
file_100k.close()
file_1m.close()  



    
