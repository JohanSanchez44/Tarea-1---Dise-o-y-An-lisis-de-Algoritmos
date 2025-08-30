#Resolver el ejercicio (Metodo 1)

# * Dado un arreglo de n numeros enteros y un entero K.
# * Determinar si en el arreglo existe un par que de como suma K.
# * A[x] + A[x'] = K
import time

inicio = time.time()
arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
existe = False
K = 30

for i in range (0, len(arreglo)):
    for j in range(i, len(arreglo)):
        if arreglo[i] + arreglo[j] == K:
            print("Par encontrado :) \n", "Los numeros son: ",  arreglo[i], " + ", arreglo[j])
            existe = True
            break
    if arreglo[i] + arreglo[j] == K:
        break

if existe == False:
    print("Par no encontrado :( ")

fin = time.time()
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución: {tiempo_ejecucion:.7f} segundos")