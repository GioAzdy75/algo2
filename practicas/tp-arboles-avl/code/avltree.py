class AVLTree:
    root = None

class AVLNode:
    def __init__(self,parent = None,leftnode = None,rightnode = None,key=None,value=None,bf = None) -> None:
        self.parent = parent
        self.leftnode = leftnode
        self.rightnode = rightnode
        self.key = key
        self.value = value
        self.bf = bf
    def __str__(self):
        return f"{self.key} --> {self.value} , bf {self.bf}"

#Ejercicio 1
def rotateLeft(tree,avlnode):
    """Realiza la rotacion a la izquierda"""
    if tree.root == avlnode:
          nodeA = avlnode
          nodeB = nodeA.rightnode

          tree.root = nodeB
          nodeA.rightnode = nodeB.leftnode
          nodeB.leftnode = nodeA
          nodeA.parent = nodeB
          nodeB.parent = None
    else:
          nodeA = avlnode
          nodeB = nodeA.rightnode
          parentNode = nodeA.parent

          if parentNode.leftnode == nodeA:
               parentNode.leftnode = nodeB
          else:
               parentNode.rightnode = nodeB
          nodeA.rightnode = nodeB.leftnode
          nodeB.leftnode = nodeA
          nodeA.parent = nodeB
          nodeB.parent = None
         
    return tree

def rotateRight(tree,avlnode):
    "Realiza la rotacion a la derecha"
    if tree.root == avlnode:
        nodeA = avlnode
        nodeB = nodeA.leftnode

        tree.root = nodeB
        nodeA.leftnode = nodeB.rightnode
        nodeB.rightnode = nodeA
        nodeB.parent = None
        nodeA.parent = nodeB

    else:
        nodeA = avlnode
        nodeB = nodeA.leftnode
        parentNode = nodeA.parent
        
        if parentNode.leftnode == nodeA:
            parentNode.leftnode = nodeB
        elif parentNode == nodeB:
            parentNode.rightnode = nodeB
        nodeA.leftnode = nodeB.rightnode
        nodeB.rightnode = nodeA
        nodeB.parent = parentNode
        nodeA.parent = nodeB

    return tree


def heightTree(root):
    if root == None:
        return -1
    if isinstance(root,AVLTree):
        root = root.root
    

    leftheight = heightTree(root.leftnode)

    rightheight = heightTree(root.rightnode)
    
    if leftheight > rightheight:
         return leftheight + 1
    else:
         return rightheight + 1


#Ejercicio 2
def calculateBalance(root):
    """calcula el balance factor de un arbol binario de busqueda"""
    if root == None:
         return None
    if isinstance(root,AVLTree):
        root = root.root

    calculateBalance(root.leftnode)
    calculateBalance(root.rightnode)

    leftvalue = heightTree(root.leftnode)
    rightvalue = heightTree(root.rightnode)

    diffvalue = (leftvalue - rightvalue)
    
    root.bf = diffvalue
    

#Ejercicio 3
def Wrapper_reBalance(tree,root):
    if root == None:
        return None
    
    if isinstance(root,AVLTree):
        root = root.root
    

    Wrapper_reBalance(tree,root.leftnode)
    Wrapper_reBalance(tree,root.rightnode)

    while True:
        calculateBalance(tree)
        if root.bf < -1:
            if root.rightnode.bf <= 0:
                rotateLeft(tree, root)
            else:
                rotateRight(root, root.rightnode)
                rotateLeft(tree, root)
        elif root.bf > 1:
            if root.leftnode.bf >= 0:
                rotateRight(tree,root)
            else:
                rotateLeft(tree, root.leftnode)
                rotateRight(tree, root)
        else:
            break
    
    return tree
def reBalance(tree):
    return Wrapper_reBalance(tree,tree.root)

#Ejercicio 4
def wrapperInsert(node,currentNode):
    if node.value < currentNode.value:
        if currentNode.leftnode == None:
            currentNode.leftnode = node
            node.parent = currentNode
        else:
            wrapperInsert(node, currentNode.leftnode)
    else:
        if currentNode.rightnode == None:
            currentNode.rightnode = node
            node.parent = currentNode
        else:
            wrapperInsert(node, currentNode.rightnode)
    

def insert(tree,value,key):
    newNode = AVLNode(key=key,value=value)
    if tree.root == None:
        tree.root = newNode
        return tree
    
    wrapperInsert(newNode,tree.root)
    reBalance(root)

#Ejercicio 5
def findMinNode(B):
  if B.leftnode == None:
    return B
  return findMinNode(B.leftnode)


def findMaxNode(B):
  if B.rightnode == None:
    return B
  return findMaxNode(B.rightnode)

def deleteNode(currentNode,key):

  if currentNode == None:
    return

  if currentNode.key == key:
    #si es un leaftnode
    if currentNode.leftnode == None and currentNode.rightnode == None:
      parentNode = currentNode.parent
      if parentNode.leftnode != None and parentNode.leftnode.key == key:
        parentNode.leftnode = None
      elif parentNode.rightnode != None and parentNode.rightnode.key == key:
        parentNode.rightnode = None

    #si es un nodo con un solo hijo
    elif currentNode.leftnode == None:
      currentNode.key = currentNode.rightnode.key
      currentNode.value = currentNode.rightnode.value
      currentNode.parent = currentNode.rightnode.parent
        
    elif currentNode.rightnode == None:
      currentNode.key = currentNode.leftnode.key
      currentNode.value = currentNode.leftnode.value
      currentNode.parent = currentNode.leftnode.parent

    #si tiene dos hijos
    else:
      tempNode = findMinNode(currentNode.rightnode)
      currentNode.key = tempNode.key
      currentNode.value = tempNode.value
      currentNode.parent = tempNode.parent
      deleteNode(currentNode.rightnode,currentNode.key)
      

  if currentNode.key < key:
    deleteNode(currentNode.rightnode,key)
  else:
    deleteNode(currentNode.leftnode,key)

"""DeleteKey"""

def deleteKey(B,key):

  if B == None:
    return None
  deleteNode(B.root,key)
  reBalance(B)
  return 

#Funcion Adicional
def display(root):
        if isinstance(root,AVLTree):
            root = root.root
        lines, *_ = _display_aux(root)
        for line in lines:
            print(line)

def _display_aux(root):
        # No child.
        if root.rightnode is None and root.leftnode is None:
            line = '%s' % root.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if root.rightnode is None:
            lines, n, p, x = _display_aux(root.leftnode)
            s = '%s' % root.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if root.leftnode is None:
            lines, n, p, x = _display_aux(root.rightnode)
            s = '%s' % root.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = _display_aux(root.leftnode)
        right, m, q, y = _display_aux(root.rightnode)
        s = '%s' % root.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

