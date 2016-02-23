class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

    def writechain(self, barn):
        if barn.parent == None:
            print(barn.word)
        else:
            self.writechain(barn.parent)
            print(barn.word)
