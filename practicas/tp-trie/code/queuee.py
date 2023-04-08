import linkedlist 

class Queue():
   head = None
def enqueue(Q,element):
    """Descripción: Agrega un elemento al comienzo de Q, siendo Q una estructura de tipo LinkedList."""
    linkedlist.add(Q,element)


def dequeue(Q):#revisar
    """Descripción: extrae el último elemento de la cola Q, siendo Q una estructura de tipo LinkedList."""
    if Q != None:
      if Q.head != None:
        if Q.head.nextNode != None:
          currentNode = Q.head
          while currentNode.nextNode != None:
            previousNode = currentNode
            currentNode = currentNode.nextNode
          previousNode.nextNode = None
        else:
          if Q.head.nextNode == None:
            Q.head = None
    return None
