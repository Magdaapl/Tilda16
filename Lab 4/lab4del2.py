from BintreeFilen import *
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
            if svenska.exists(ordet):             
                gamla.put(ordet) 
            else:
                svenska.put(ordet)

                
def makeChildren(start):
    
    alfabet = 'abcdefghijklmnoprstuvwxyzåäö'
    for bokstav in alfabet:
        for i in range(len(start)):
            barn = start[:i]+bokstav+start[i+1:]
            
            if svenska.exists(barn) and not gamla.exists(barn):
                gamla.put(barn)
                q.enqueue(barn)
            
            
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
