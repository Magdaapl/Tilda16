from BintreeFilen import Bintree
from linkedQFile import LinkedQ

q = LinkedQ()
svenska = Bintree()
gamla = Bintree()

class SolutionFound(Exception):
    pass

def readfile():
    with open("word3.txt","r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                
            if svenska.__contains__(ordet):
                gamla.put(ordet) 
            else:
                svenska.put(ordet)

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

                
def makeChildren(startord):
    alfabet = 'abcdefghijklmnoprstuvwxyzåäö'
    for letter in range(len(startord)):
        for bokstav in alfabet:
            nyttord =list(startord)
            nyttord[letter]= bokstav
            nyttord = "".join(nyttord)
            if svenska.__contains__(nyttord) and not gamla.__contains__(nyttord):
                gamla.put(nyttord)
                q.enqueue(nyttord)

            
def main():
    readfile()
    startord = input("Ange startord: ")
    slutord = input("Ange slutord: ")
    q.enqueue(startord)
    
    try:
        while not q.isEmpty():
            
            nod = q.dequeue()
            makeChildren(nod)
            if nod == slutord:
        
                print("Det finns en väg till", slutord)
                raise SolutionFound(nod)
    
        
        print("Det finns ingen väg till", slutord)
    except SolutionFound as nod:
    
        print()
if __name__ == '__main__':
    main()
