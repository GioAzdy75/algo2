class Trie:
    root = None

class TrieNode:
    def __init__(self,key,isEndOfWord=False,parent=None,children=None) -> None:
        self.parent = parent
        self.children = children
        self.key = key
        self.isEndOfWord = isEndOfWord


import linkedlist as link


"""Hola"""

#Ejercicio 1

def searchTrieNode(linkedlist:link.LinkedList,element):
    """Busca en una linkedlist el elemento dentro de un TrieNode elemento == key , en caso contrario retorna None"""
    if linkedlist == None:
        return None
    if linkedlist.head == None:
        return None
    
    currentNode = linkedlist.head
    while currentNode != None:
        if currentNode.value.key == element:
            return currentNode.value
        currentNode = currentNode.nextNode

    return None


def insertWrapper(linked_list,father,element):
    if linked_list is None:
        L = link.LinkedList()
        newTrieNode = TrieNode(element)
        link.add(L,newTrieNode)
        father.children = L
    
    #Caso que exista la LinkedList lo buscamos dentro
    searchNode = searchTrieNode(linked_list,element)
    
    #si no se encuentra en la lista
    if searchNode == None:
        newTrieNode = TrieNode(element)
        link.add(linked_list,newTrieNode)
    else:
        insert(searchNode.children,linked_list,element)

def insert(T:Trie,word):
    
    if T.root is None:
        element = w
        L = link.LinkedList()
        newTrieNode = TrieNode(element)
        link.add(L,newTrieNode)
        T.root = L
    else:
        for w in word:
        #Caso que no Exista LinkedList
            insertWrapper(T.root,T.root,w)
        