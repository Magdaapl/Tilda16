#from ArrayQfile import ArrayQ
from linkedQFile import LinkedQ

def läser_input():
    """
    Läser in hela raden som ges av användaren och
    skapar en lista med sub-strängar
    """
    ordning = input("Ange ordning på kortleken?: ")
    return ordning.split() #delar upp raden i strängar som lagras i en lista


def fyll_kortlek(ordning, kortlek):
    
    for k in ordning:
        k = int(k) # konverterar k till heltal
        kortlek.enqueue(k)# sätter varje kort i kö kortlek


def visa_kortlek(kortlek):
    
    while kortlek.isEmpty() == False: #körs medans kortleken inte är tom
        köad_kort = kortlek.enqueue(kortlek.dequeue()) #köar kortet 
        ta_bort_kortleken = kortlek.dequeue()
        print(ta_bort_kortleken, end=" ") #visar alla kort som ligger först i kön
        

def main():
    
#    q = ArrayQ()
    q = LinkedQ()
    ordning = läser_input()
    osorterad_array = fyll_kortlek(ordning, q)
    visa_kortlek(q)
        
# 7 1 12 2 8 3 11 4 9 5 13 6 10

if __name__ == '__main__':
    main()
