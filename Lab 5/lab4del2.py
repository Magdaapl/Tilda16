from BintreeFilen import Bintree
from linkedQFile import LinkedQ
from ParentNode import ParentNode

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

                
def makeChildren(startord):
    alfabet = 'abcdefghijklmnoprstuvwxyzåäö'
    gamla.put(startord.word)
    for letter in range(len(startord.word)):
        for bokstav in alfabet:
            nyttord =list(startord.word)
            nyttord[letter]= bokstav
            nyttord = "".join(nyttord)
            if svenska.__contains__(nyttord) and not gamla.__contains__(nyttord):
                gamla.put(nyttord)
                nynod = ParentNode(nyttord)
                nynod.parent= startord
                q.enqueue(nynod)

            
def main():
    readfile()
    startord = input("Ange startord: ")
    slutord = input("Ange slutord: ")
    noden = ParentNode(startord)
    q.enqueue(noden)
    try:
        while not q.isEmpty():
            nod = q.dequeue()
            makeChildren(nod)
            if nod.word == slutord:
                print("Vägen från", startord, "till", slutord, "är: ")
                nod.writechain(nod)  #alla slutord
                raise SolutionFound(nod)
        print("Det finns ingen väg till", slutord)
    except SolutionFound as nod:
        print()

if __name__ == '__main__':
    main()
