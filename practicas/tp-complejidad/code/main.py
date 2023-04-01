


"""5 - Implementar un algoritmo Contiene-Suma(A,n) que recibe una lista de enteros A y un entero n
y devuelve True si existen en A un par de elementos que sumados den n. Analice el costo
computacional."""
def contienesuma(A,n):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if (A[i] + A[j]) == n:
                return True
    return False

