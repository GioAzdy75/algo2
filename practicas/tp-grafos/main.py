
import stack
import myqueue
#LinkedList Implementation
""""
Vertices = 5
Lista Aristas = [[1,2],[3,2],[5,4],[2,4],[1,5]]
"""
#Ejercicio 1
def createGraph(vertices:list, aristas:list):
    """Implementa la operación crear grafo"""
    graph_list = []

    for i in range(len(vertices)):
        graph_list.append([])

    for a in aristas:
        index = a[0]
        node = a[1]
        graph_list[index].append(node)
        index = a[1]
        node = a[0]
        graph_list[index].append(node)
    
    return graph_list

def remove(lista,element):
    for i in range(len(lista)):
        if lista[i] == element:
            lista.remove(element)
            break
    return

#Ejercicio 2
def existPath(Grafo, v1, v2):
    def dfs(v,v2,visit):
        if v == v2:
            return True
        visit.append(v)
        for vecino in Grafo[v]:
            if vecino not in visit:
                if dfs(vecino,v2,visit):
                    return True
        return False
    #Inicio
    visit = []
    return dfs(v1,v2,visit)

#Ejercicio 3
def isConnected(graph):
    conexo = []
    for i in range(len(graph)):
        conexo.append(existPath(graph,i,len(graph)-1))

    for c in conexo:
        if c != True:
            return False
    return True

"""
#Ejercicio 4


def isTreeWrapper(graph,lista_recorridos,v):
    if lista_recorridos[v] == True:
        return False
    lista_recorridos[v] = True
    for g in graph[v]:
        delete_element(graph[g],v)
        print(g, graph[g])
        salida = isTreeWrapper(graph,lista_recorridos,g)
        if salida == False:
            return False
    return True

def isTree(graph):
    #Recorremos el grafo y vemos si hay un bucle si lo hay no es un arbol  verificar si es conexo
    marked = [False] * len(graph)
    return isTreeWrapper(graph,marked,0)
"""

#Ejercicio 4
def isTree(graph):
    marked = [False] * len(graph)
    padres = [-1] * len(graph)
    aristas_bucle = []
    def dfs(v,marked,padres):
        if marked[v] == True:
            return False
        marked[v] = True
        for g in graph[v]:
            if not marked[g]:
                padres[g] = v
                dfs(g,marked,padres)
            elif g != padres[v]:
                aristas_bucle.append([g,v])
    dfs(0,marked,padres)
    return all(marked) and not aristas_bucle

#Ejercicio 5
def isComplete(graph):
    #El grado de todos los vertice va hacer igual al total de los vertices - 1
    grado = len(graph) - 1 
    for g in graph:
        if grado != len(graph):
            return False
    return True

#Ejercicio 6
def convertTree(graph):
    marked = [False] * len(graph)
    padres = [-1] * len(graph)
    aristas_eliminadas = []
    def dfs(v,marked,aristas):
        marked[v] = True
        for g in graph[v]:
            if not marked[g]:
                padres[g] = v
                dfs(g,marked,aristas)
            elif padres[v] != g:
                aristas_eliminadas.append([g,v])

    dfs(0,marked,aristas_eliminadas)

    return aristas_eliminadas


#Ejercicio 7

def countConnection(graph):
    def dfs(graph,v,path):
        path.append(v)
        for g in graph[v]:
            if not g in (path):
                dfs(graph,g,path)

    list_return = []
    for v in range(len(graph)):
        path = []
        dfs(graph,v,path)
        list_return.append(path)

    print(list_return)


#Ejercicio 7
def countConnection(Grafo):
    n = len(Grafo)
    visitados = [False] * n
    cant_cc = 0
    
    def dfs(v):
        visitados[v] = True
        for vecino in Grafo[v]:
            if not visitados[vecino]:
                dfs(vecino)
    
    for i in range(n):
        if not visitados[i]:
            dfs(i)
            cant_cc += 1
    
    return cant_cc



"""
def delete_element(list,element):
    if element in list:
        list.remove(element)

def converTreeWrapper(graph,lista_recorridos,v,p,aristas_eliminadas):
    if lista_recorridos[v] == True:
        aristas_eliminadas.append([v,p])
        return 
    lista_recorridos[v] = True
    for g in graph[v]:
        delete_element(graph[g],v)
        print(g, graph[g])
        converTreeWrapper(graph,lista_recorridos,g,v,aristas_eliminadas)

def convertTree(graph):
    #Ver si el grafo tiene ciclos si tiene ciclos eliminar el ciclo para convertirlo en arbol y verificar si es conexo
    marked = [False] * len(graph)
    aristas_eliminadas = []
    converTreeWrapper(graph,marked,0,0,aristas_eliminadas)
    print(aristas_eliminadas,"eliminada")
    return 
"""





def bearthfirstsearch(graph,vertices):
    queue = myqueue.Queue()
    marked = [False] * len(vertices)
    queue.enqueue(vertices[0])
    bfs_list = []
    
    new_graph = [[] for _ in range(len(vertices))]
    m = vertices[0]

    while not queue.is_empty():
        v = queue.dequeue().value
        if not marked[v]:
            if m != v:
                new_graph[m].append(v)
            marked[v] = True
            bfs_list.append(v)
            for g in graph[v]:
                if not marked[g]:
                    queue.enqueue(g)
                    m = v

    return new_graph


def depthfirstsearch(graph,vertices):
    marked = [False] * len(vertices)
    pila = stack.Stack()
    pila.push(vertices[0])
    new_list = []
    n = 0
    while not pila.is_empty():
        v = pila.pop().value
        if not marked[v]:
            marked[v] = True
            new_list.append(v)
            for g in graph[v]:
                if not marked[g]:
                    pila.push(g)
    return new_list

def convertToDFSTree(dfs_list):
    new_graph = [[] for _ in range(len(vertices))]
    m = dfs_list[0]
    for v in range(1,len(dfs_list)):
        new_graph[m].append(dfs_list[v])
        m = dfs_list[v]       
    return new_graph



def bestRoad(graph,v1,v2):
    n = len(graph)
    dist = [float('inf')] * n
    pred = [None] * n
    dist[v1] = 0
    
    # Iniciar BFS
    queue = [v1]
    while queue:
        u = queue.pop(0)
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                pred[v] = u
                queue.append(v)
    
    # Reconstruir camino más corto
    path = [v2]
    while path[-1] != v1:
        path.append(pred[path[-1]])
    return list(reversed(path))

def isBipartite(graph):
    pass

Vertices = [0,1,2,3,4,5]

Lista_Aristas = [[1,2],[3,2],[5,4],[2,4],[1,5],[0,1]]


grafo = createGraph(Vertices,Lista_Aristas)
print(grafo)
print(existPath(grafo,0,4),"path")
print(isConnected(grafo))

print(isTree(grafo),"Es Arbol")
print(convertTree(grafo),"Arista eliminar")
print(countConnection(grafo))
#depthfirstsearch(grafo,Vertices)


print(bestRoad(grafo,1,3))
#bearthfirstsearch(grafo,Vertices)