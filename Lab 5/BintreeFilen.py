class Bintree():
    def __init__(self):
        self.root = None

    def __str__(self):
        return "bintree Class"

    def put(self, newvalue):
        if self.root is None:
            self.root = Node(newvalue)
        # som sorterar in newvalue i trädet
        else:
            self.root = putta(self.root, newvalue)

    def __contains__(self, value):
        # som kollar om value finns i trädet
        return finns(self.root, value)

    def write(self):
        # som skriver ut trädet
        skriv(self.root)
        print("\n")


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)



def putta(root, newvalue):
    
    i=0
    if newvalue < root.value:
        if root.left is not None:
            putta(root.left, newvalue)
                
        else:
                
            root.left = Node(newvalue)
    elif newvalue > root.value:
        if root.right is not None:
                
            putta(root.right, newvalue) 
        else:
                
            root.right = Node(newvalue)

    return root

def finns(root, value):
    if root is None:
        return False
    elif value == root.value:
        return True
    elif root.left and value < root.value:
        return finns(root.left, value)
    elif root.right and value > root.value:
        return finns(root.right, value)
    else:
        return False


def skriv(root):
    if root is None:
        skriv(root.left)
        print(root.value)
        skriv(root.right)
