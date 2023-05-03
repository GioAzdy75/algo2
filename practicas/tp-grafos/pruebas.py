

def lista_de_adyacencia(conexiones):
    grafo = {}
    for conexion in conexiones:
        nodo1, nodo2 = conexion
        if nodo1 not in grafo:
            grafo[nodo1] = []
        if nodo2 not in grafo:
            grafo[nodo2] = []
        grafo[nodo1].append(nodo2)
        grafo[nodo2].append(nodo1)
    return grafo

def lista_de_adyacencia_listas(conexiones):
    grafo = [[] for _ in range(max(max(conexiones), default=0)+1)]
    for conexion in conexiones:
        nodo1, nodo2 = conexion
        grafo[nodo1].append(nodo2)
        grafo[nodo2].append(nodo1)
    return grafo

def imprimir_lista_de_adyacencia(grafo):
    for nodo in grafo:
        adyacentes = grafo[nodo]
        print(str(nodo) + ": " + ", ".join(str(n) for n in adyacentes))

def imprimir(grafo):
    for i in range(len(grafo)):
        print("Nodo ", i, ": ", end="")
        for j in range(len(grafo[i])):
            print(grafo[i][j], end=" ")
        print()


Vertices = [0,1,2,3,4,5]

Lista_Aristas = [[1,2],[3,2],[5,4],[2,4],[1,5],[0,1]]

lista_adyacencia = lista_de_adyacencia(Lista_Aristas)
listas_linkes = lista_de_adyacencia_listas(Lista_Aristas)
print(lista_adyacencia)
print(listas_linkes)
imprimir_lista_de_adyacencia(lista_adyacencia)
imprimir(listas_linkes)