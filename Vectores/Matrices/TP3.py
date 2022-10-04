MONTO = []

print("Ingrese número de sucursales y años: ")
N = int( input("Número de Sucursales: "))
M = int( input("Número de Años: "))

for i in range(M):
    MONTO.append([])

    for j in range(N):
        print("Ingrese ventas de la sucursal", j+1 , "en el año", i+1 )
        venta = int(input())
        MONTO[i].append(venta)


print("SUCURSAL CON MAS VENTAS:")

MAX = 0

for j in range(N):
    SUMA = 0

    for i in range(M):
        SUMA = SUMA + MONTO[i][j]

    print ("Número de ventas de la Sucursal" , j+1, "es", SUMA)

    if SUMA > MAX :
        MAX = SUMA
        SUC = j + 1

print("Sucursal que más vendió: ", SUC)


print("PROMEDIO DE VENTAS DEL AÑO:")

MAX = 0

for i in range(M):
    SUMA = 0
    
    for j in range(N):
        SUMA = SUMA + MONTO[i][j]
    
    PROM = SUMA/N
    
    print ("Promedio de ventas del año" , i+1, "es", PROM)

    if PROM > MAX :
        MAX = PROM
        ANO = i + 1

print("Año con mayor promedio", ANO)