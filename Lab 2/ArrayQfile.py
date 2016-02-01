from array import array


class ArrayQ():
    '''
    Klass med det privata attributet array med definierad numeriskt type code:i
    som säger till att vi ska lagra  data av typ integer. 
    '''
    def __init__(self, type_code="i"):
        self._array = array(type_code)

    def enqueue(self, kortleksnummer):
        '''
        lägger till given kortleksnummer sist i array
        '''
        
        return self._array.append(kortleksnummer) 

    def dequeue(self):
        '''
        Tar bort det första element vi satt in i array och returnerar det.
        '''
        return self._array.pop(0)#pop returnerar den element på plats 0

    def isEmpty(self):
        
        if len(self._array) == 0:
            return True
        else:
            return False
q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
x = q.dequeue()
y = q.dequeue()
print(x,y)   # 1 2 ska komma ut

