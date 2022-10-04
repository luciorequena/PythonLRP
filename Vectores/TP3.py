vec = []

print("Ingrese la cantidad de elementos del vector")
cant = int(input())

if 1 <= cant and cant <= 200:
    for i in range(1,cant+1):
        elemento = int( input("Ingrese Entero {0}: ".format(i)))
        vec.append(elemento)

    i = 0

vec2 = []

for elemento in vec :
    if elemento not in vec2:
        vec2.append(elemento)

vec2.sort()

print(vec2)