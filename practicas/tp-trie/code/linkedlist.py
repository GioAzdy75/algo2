class LinkedList():
    head = None


class Node():
    value = None
    nextNode = None


def add(L, element):  #O(1)
    """Descripción: Agrega un elemento al comienzo de L, siendo L una LinkedList
que representa el TAD secuencia."""
    nodo = Node()
    nodo.value = element

    if L.head == None:
        L.head = nodo
    else:
        nodo.nextNode = L.head
        L.head = nodo


def search(L, element):  #O(n)
    """Descripción: Busca un elemento de la lista que representa el TAD
secuencia."""
    index = 0
    currentNode = L.head
    while currentNode != None:
        if currentNode.value == element:
            return index
        else:
            index += 1
            currentNode = currentNode.nextNode

    return None


def insert(L, element, position):  #O(n)
    """Descripción: Inserta un elemento en una posición determinada de la
lista que representa el TAD secuencia."""
    nodo = Node()
    nodo.value = element
    index = 0
    currentNode = L.head

    if position == index:
        add(L, element)
        return position
    else:
        while currentNode != None:
            index += 1
            previousNode = currentNode
            currentNode = currentNode.nextNode
            if index == position:
                nodo.nextNode = currentNode
                previousNode.nextNode = nodo
                return index

        return None


def delete(L, element):  #O(n)
    """Descripción: Elimina un elemento de la lista que representa el TAD
secuencia."""
    index = 0
    currentNode = L.head

    if currentNode == None:
        return None
    else:
      if currentNode.value == element:
          L.head = currentNode.nextNode
          return index
      else:
          index += 1
          previousNode = currentNode
          currentNode = currentNode.nextNode
          while currentNode != None:
              if currentNode.value == element:
                  previousNode.nextNode = currentNode.nextNode
                  return index
              index += 1
              previousNode = currentNode
              currentNode = currentNode.nextNode
    return None

def length(L):  #O(n)
    """Descripción: Calcula el número de elementos de la lista que representa
el TAD secuencia."""
    index = 0
    currentNode = L.head
    while currentNode != None:
        index += 1
        currentNode = currentNode.nextNode
    return index


def access(L, position):  #O(n)
    """Descripción: Permite acceder a un elemento de la lista en una posición
determinada."""
    currentnode = L.head
    index = 0
    while currentnode != None:
        if position == index:
            return currentnode.value
        else:
            index += 1
            currentnode = currentnode.nextNode
    return None


def update(L, element, position):  #O(n)
    """Descripción: Permite cambiar el valor de un elemento de la lista en
una posición determinada"""
    currentnode = L.head
    index = 0
    while currentnode != None:
        if position == index:
            currentnode.value = element
            return index
        else:
            index += 1
            currentnode = currentnode.nextNode
    return None


def imprimir_linklist(L):
    """imprime la lista de forma amigable"""
    currentNode = L.head
    print("|head| -->", end=" ")
    while currentNode != None:
        print("|" + str(currentNode.value) + "|", " --> ", end="")
        currentNode = currentNode.nextNode

    print("|None|")

def orden_inverso(L):
  """retorna una Lista enlazada con sus valores dados vuelta"""
  currentNode = L.head
  new_list = LinkedList()
  while currentNode != None:
    add(new_list,currentNode.value)
    currentNode = currentNode.nextNode

  return new_list