class Bintree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return "bintree Class"

    def put(self, newvalue):
        # som sorterar in newvalue i trädet
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
        return "NodeClass" + str(self.value)


def putta(root, newvalue):
    if root is None:
        root = Node(newvalue)
    else:
        if newvalue < root.value:
            if root.left is None:
                root.left = Node(newvalue)
            else:
                putta(root.left, newvalue)
        elif newvalue > root.value:
            if root.right is None:
                root.right = Node(newvalue)
            else:
                putta(root.righ, newvalue)
        elif newvalue == root.value:
            pass
    return root

def __contiains__(root, value):
    if root is None:
        return False
    elif value == root.value:
        return True
    elif root.left and value < root.value:
        return __contiains__(root.left, value)
    elif root.right and value > root.value:
        return __contiains__(root.right, value)
    else:
        return False