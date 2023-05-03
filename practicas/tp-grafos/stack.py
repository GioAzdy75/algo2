class Node():
    def __init__(self,value) -> None:
        self.value = value
        self.nextNode = None

class Stack():
    def __init__(self) -> None:
        self.head = None

    def push(self,element):
        """Descripción: Agrega un elemento a la pila"""
        new_node = Node(element)
        if self.head == None:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    def pop(self):
        """Retorna el ultimo elemento de la Pila en forma de nodo"""
        if self.head != None:
            head = self.head
            self.head = self.head.nextNode
            return head

    def is_empty(self):
        if self.head == None:
            return True
        
        return False
        
    def imprimir_stack(self):
        """imprime la lista de forma amigable"""
        currentNode = self.head
        print("|head| -->", end=" ")
        while currentNode != None:
            print("|" + str(currentNode.value) + "|", " --> ", end="")
            currentNode = currentNode.nextNode
        print("|None|")
