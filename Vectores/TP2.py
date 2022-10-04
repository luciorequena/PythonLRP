suma = 0
media = 0.0
cont = 0
temp = []

print("Ingrese cantidad de Temperaturas: ")
num = int(input())

for i in range(num):
    temperatura = float(input("Ingrese temperatura {0}:".format(i+1)))
    temp.append(temperatura)
    suma = suma + temperatura

media = suma / num

for tempElement in temp:
    if tempElement >= media:
        cont = cont + 1
        print(tempElement)

print("La media es: ",media)
print("cantidad de temperaturas mayor o igual a la media es: ",cont)