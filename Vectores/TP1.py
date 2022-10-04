i = 1
lista = []

print("Ingrese la cantidad de elementos que se van a ingresar:")
cant = int(input())

while i <= cant:
    elemento = int(input("Ingrese elemento: "))
    lista.append(elemento)

    i = i+1

print(lista) 