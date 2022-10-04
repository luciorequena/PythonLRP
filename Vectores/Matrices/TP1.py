mat1 = []
mat2 = []
mat3 = []

print ("Ingrese dimensión de la matriz,máximo 100")
f = int( input("Número de Filas: "))
c = int( input("Número Columnas: "))

for i in range (f):
    mat1.append([])
    mat2.append([])
    mat3.append([])

    for j in range (c):
        mat1[i].append(int(input("mat1{}{}: ".format(i+1,j+1))))
        mat2[i].append(int( input("mat2{}{}: ".format(i+1,j+1))))
        mat3[i].append(mat1[i][j] + mat2[i][j])


print(mat1)
print(mat2)
print(mat3)