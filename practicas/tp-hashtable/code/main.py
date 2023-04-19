

#Ejercicio 1
keys = [5,28,19,15,20,33,12,17,10]

def hashing(key):
    return key % 9

keys_hash = []
for k in keys:
    keys_hash.append(hashing(k))

#print(keys)
#print(keys_hash)
"""
Resulta que hay coliciones y estas son encadenadas, desperdiciando mas espacio ya que habian espacios nulos para ocupar
"""

#Ejercicio 2
import algo1
import linkedlist


def crear_diccionario(size):
    dictionary = []
    i = 0
    while i < size:
        dictionary.append(None)
        i += 1
    return dictionary
    
def insert(D,key,value):
    """Inserta un key en una posición determinada por la función de hash (1) en el diccionario (dictionary). 
    Resolver colisiones por encadenamiento. En caso de keys duplicados se anexan a la lista."""
    if len(D) < key:
        return "Failed"

    if D[key] == None:
        L = linkedlist.LinkedList()
        linkedlist.add(L,value)
        D[key] = L
    else:
        L = D[key]
        linkedlist.add(L,value)
    return D

def search(D,key):
    """Busca un key en el diccionario"""
    if len(D) < key:
        return None
    return D[key]

def delete(D,key):
    """Elimina un key en la posición determinada por la función de hash (1) del diccionario (dictionary)"""
    if len(D) < key:
        return None
    D[key] = None
    return D


##Parte 2
#Ejercicio 3
from math import sqrt
tamano = 1000
dictionary = crear_diccionario(tamano)

def hashing(m,key):
    A = (sqrt(5)-1)/2
    return round(m*(key * A %1))

#for i in range(61,66):
    #print(hashing(tamano,i))


#Ejercicio 4

def search_element(D,element):
    key = hashing(len(D)-1,ord(element))
    linklist = search(D,key)
    if linklist == None:
        return
    index = linkedlist.search(linklist,element)
    result = linkedlist.access(linklist,index)
    return result

def ispermutation(string_s,string_p):
    largo_caracteres = 128
    list_abecedario = crear_diccionario(largo_caracteres)

    for s in string_s:
        key = hashing(largo_caracteres-1,ord(s))
        insert(list_abecedario,key,s)

    count = 0
    for p in string_p:
        element = search_element(list_abecedario,p)
        if element == p:
            count += 1
    
    return (count == len(string_s))



#Ejercicio 5
"""
Implemente un algoritmo que devuelva True si la lista que recibe de entrada tiene todos sus
elementos únicos, y Falso en caso contrario. Justificar el coste en tiempo de la solución
propuesta.
"""
#hash

def lista_unica(lista):
    dictionary = crear_diccionario(len(lista))
    for i in range(lista):
        index = search_element(dictionary,lista[i])
        if linkedlist.access(lista[i],index) == i:
            return False
        insert(dictionary,hashing(i),lista[i])
    
    return True

#Ejercicio 6


#Ejercicio 7
"""
Implemente un algoritmo para realizar la compresión básica de cadenas utilizando el
recuento de caracteres repetidos. Por ejemplo, la cadena aabcccccaaa se convertiría en a2blc5a3. 
Si la cadena "comprimida" no se vuelve más pequeña que la cadena original, su
método debería devolver la cadena original. Puedes asumir que la cadena sólo tiene letras
mayúsculas y minúsculas (a - z, A - Z). Justificar el coste en tiempo de la solución propuesta.
"""

def compresion_cadena(cadena):
    count = 1
    nueva_cadena = ""
    if len(cadena) == 1:
        return cadena
    for i in range(1,len(cadena)):
        if len(cadena)-1 == i:
            nueva_cadena += f"{cadena[i-1]}{count+1}"
        elif cadena[i-1] != cadena[i]:
            nueva_cadena += f"{cadena[i-1]}{count}"
            count = 0
        count += 1
    if len(nueva_cadena) < len(cadena):
        return nueva_cadena
    return cadena

#Ejercicio 8
"""
Se requiere encontrar la primera ocurrencia de un string p1...pk en uno más largo a1...aL.
Implementar esta estrategia de la forma más eficiente posible con un costo computacional
menor a O(K*L) (solución por fuerza bruta). Justificar el coste en tiempo de la solución
propuesta.
"""
def primera_ocurrencia(cadena_p , cadena_a):
    length_a = len(cadena_a)
    for i in range(len(cadena_p)):
        if cadena_p[i:i+length_a] == cadena_a:
            return i

#Ejercicio 9
"""
Considerar los conjuntos de enteros S = {s1, . . . , sn} y T = {t1, . . . , tm}. Implemente un
algoritmo que utilice una tabla de hash para determinar si S ⊆ T (S subconjunto de T). ¿Cuál
es la complejidad temporal del caso promedio del algoritmo propuesto?
"""

def search_element_9(D,element):
    key = hashing(len(D)-1,element)
    linklist = search(D,key)
    if linklist == None:
        return
    index = linkedlist.search(linklist,element)
    result = linkedlist.access(linklist,index)
    return result

def subconjunto(S,T):
    largo_T = len(T)
    hashtable = crear_diccionario(largo_T)

    for t in range(largo_T):
        key = hashing(largo_T-1,T[t])
        insert(hashtable,key,T[t])
    for s in range(len(S)):
        search = search_element_9(hashtable,S[s])
        if search != S[s]:
            return False

    return True

p =[3,4,5,6,7]
q = [2,3,4,5,6,8,9]

print("Subconjunto : ",subconjunto(p,q))



print("Ocurrencia indice: ",primera_ocurrencia("abracadabra","dabra"))

print(compresion_cadena("aabcccccaaa"))
#Pruebas
"""
dictionary = crear_diccionario(5)
insert(dictionary,2,"Queso")
insert(dictionary,4,"Perro")
insert(dictionary,2,"Bondiola")
print(dictionary)
linkedlist.imprimir_linklist(search(dictionary,2))
"""