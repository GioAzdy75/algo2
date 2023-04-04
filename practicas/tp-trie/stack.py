import linkedlist

class Stack():
    head = None

class Node():
    value = None
    nextNode = None

def push(S,element):
  """Descripción: Agrega un elemento al comienzo de S, siendo S una estructura de tipo LinkedList"""
  linkedlist.add(S,element)

def pop(S):
    if S != None:
        if S.head != None:
            head = S.head
            S.head = S.head.nextNode
            return head.value
