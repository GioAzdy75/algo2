class Node():
    def __init__(self,value) -> None:
        self.value = value
        self.nextNode = None
    
class Queue():
    def __init__(self) -> None:
        self.head = None
    
    def enqueue(self,element):
        """Descripción: Agrega un elemento al comienzo de Q, siendo Q una estructura de tipo LinkedList."""
        new_node = Node(element)
        if self.head == None:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node



    def dequeue(self):#revisar
        """Descripción: extrae el último elemento de la cola Q, siendo Q una estructura de tipo LinkedList."""
        if self.head != None:
            if self.head.nextNode == None:
                headNode = self.head
                self.head = None
                return headNode
            
            currentNode = self.head
            while currentNode.nextNode != None:
                previousNode = currentNode
                currentNode = currentNode.nextNode
            previousNode.nextNode = None
            return currentNode

    def imprimir_cola(self):
        """imprime la lista de forma amigable"""
        currentNode = self.head
        print("|head| -->", end=" ")
        while currentNode != None:
            print("|" + str(currentNode.value) + "|", " --> ", end="")
            currentNode = currentNode.nextNode
        print("|None|")


    def is_empty(self):
        if self.head == None:
            return True
        
        return False

