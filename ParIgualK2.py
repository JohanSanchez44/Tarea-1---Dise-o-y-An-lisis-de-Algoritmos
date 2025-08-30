#Resolver el ejercicio (Metodo 2) HASH

# * Dado un arreglo de n numeros enteros y un entero K.
# * Determinar si en el arreglo existe un par que de como suma K.
# * A[x] + A[x'] = K
import time 

def encontrarSuma(lista, K):
    numGuardados = set()
    for num in lista:
        if num == K/2:
            return True, (num, num)
        complemento = K - num
        if complemento in numGuardados:
            return True, (num, complemento)
        numGuardados.add(num)
    return False, None

inicio = time.time()
arreglo = [6, 9, 1, 4, 13, 15, 8, 10, 11, 2, 5, 7, 3, 14, 12]
K = 2
existe, par = encontrarSuma(arreglo, K)

if existe:
    print("Par encontrado :)\n", "Los numeros son: ", par[1], " + ", par[0])
else: 
    print("Par no encontrado :( ")

fin = time.time()
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución: {tiempo_ejecucion:.7f} segundos")
