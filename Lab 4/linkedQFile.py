'''
skapad av : moku@kth.se och ammp@kth.se
hjälp av http://alextrle.blogspot.se/2011/05/write-linked-list-in-python.html
'''
class Node:
    """
    ändra:Hjälpklass till LinkedQ som sparar nuvarande värde och nästa med privata argument
    """

    def __init__(self, value, next=None):
        self._value = value #privat atribut som innehåller ett värde (value)
        self._next = next #privat atribut som innehåller en referens till nästa Node (next)

    def geValue(self):
        return self._value

    def geNext(self):
        return self._next
    
    def fixNext(self, pekare):  #sätter in next till inskriven pekare
        self._next = pekare     
        
class LinkedQ:
    """
    äändra:Kö som använder klassen Node för att skapa en länkad lista som används som en kö
    """
    
    def __init__( self ):
       
        self.first = None # atribut som håller reda på den första noden i kön
        self.last = None # atribut som håller reda på den sista noden i kön
        self.n = 0 #antalet element i listan
        
    def enqueue(self, data):
        
        ny_node = Node(data) #instansiera new node

        if self.first == None: #om det är första node, lägg in här
            self.first = ny_node

        if self.last != None: #om det inte är första node, länka in på slutet
            self.last.fixNext(ny_node)

        self.last = ny_node #lagra elementet
        self.n += 1 #höj antalet element med 1
    
    def dequeue(self):
        if self.n == 0:
            return None
        
        rValue = self.first.geValue()
        self.n -= 1
        self.first = self.first.geNext()
        return rValue
    
            
    def isEmpty(self):
        if self.first == None:
            return True
        else:
            return False
