class Trie:
    root = None

class TrieNode:
    def __init__(self,key,isEndOfWord=False,parent=None,children=None) -> None:
        self.parent = parent
        self.children = children
        self.key = key
        self.isEndOfWord = isEndOfWord


import linkedlist as link
import stack

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
        
        return newTrieNode 
    else:
        #Caso que exista la LinkedList lo buscamos dentro
        searchNode = searchTrieNode(linked_list,element)
        
        if searchNode == None:
            newTrieNode = TrieNode(element)
            link.add(linked_list,newTrieNode)
            return newTrieNode
        else:
            return searchNode

def insert(T:Trie,word):
    
    #Si no existe la Primer Letra
    if T.root is None:
        element = word[0]
        L = link.LinkedList()
        newTrieNode = TrieNode(element)
        link.add(L,newTrieNode)
        T.root = L
        currentNode = newTrieNode
        length_word = len(word)

        for i in range(1,length_word):
            currentNode = insertWrapper(currentNode.children,currentNode,word[i])
            if i == length_word -1:
                currentNode.isEndOfWord = True
    else:
        currentNode = T
        currentChildren = T.root

        length_word = len(word)
        for i in range(length_word):
            currentNode = insertWrapper(currentChildren,currentNode,word[i])
            
            print(currentNode.key)#
            if i == length_word -1:
                currentNode.isEndOfWord = True
            else:
                currentChildren = currentNode.children
            
        


def delete(trie,word):
    pila = stack.Stack()
    
    currentNode = trie
    currentChildren = currentNode.root
    for i in range(len(word)):
        currentNode = searchTrieNode(currentChildren,word[i])
        if currentNode == None:
            return -1
        else:
            stack.push(pila,currentNode)
            currentChildren = currentNode.children
    
    endNode = stack.pop(pila)
    
    if endNode.isEndOfWord == True:
        if endNode.children == None:
            currentNode = stack.pop(pila)
            while currentNode != None:
                link.delete(currentNode.children,endNode)
                if currentNode.isEndOfWord == True:
                    break
                endNode = currentNode
                currentNode = stack.pop(pila)
                if currentNode == None:
                    link.delete(trie.root,endNode)
                
                    
        else:
            endNode.isEndOfWord = False
    else:
        return -1

    return 1


def search(trie,palabra):
    if trie == None:
        return
    currentNode = trie.root
    for i in range(len(palabra)):
        searchNode = searchTrieNode(currentNode,palabra[i])
        if i == len(palabra)-1:
            if searchNode.isEndOfWord == False:
                return False
        if searchNode == None:
            return False
        currentNode = searchNode.children

    return True
    



palabra = "Queso"
palabra2 = "Que"
palabra3 = "Pala"
ArbolTrie = Trie()
print(ArbolTrie.root)
insert(ArbolTrie,palabra)

q = ArbolTrie.root.head.value
print(q.key)
u = q.children.head.value
print(u.key)
e = u.children.head.value
print(e.key)
s = e.children.head.value
print(s.key)
o = s.children.head.value
print(o.isEndOfWord)

insert(ArbolTrie,palabra2)
print(e.isEndOfWord)


insert(ArbolTrie,palabra3)



print("La palabra encontrada: ",search(ArbolTrie,"Pala"))
"""
print(ArbolTrie.root.head.nextNode.value.key)

print("Empieza")
print(delete(ArbolTrie,palabra))

print(delete(ArbolTrie,"quevedo"))

print(delete(ArbolTrie,"Qu"))

print(delete(ArbolTrie,palabra3))

#print(u.children.head.value.children.head)

link.imprimir_linklist(ArbolTrie.root)
print(ArbolTrie.root.head.value.key)

"""
