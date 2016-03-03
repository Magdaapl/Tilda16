from Låtar import Låtar

def readfile(filen):
    lista = []
    dictionary = {}

    with open(filen, encoding="utf8") as fil:
        for rad in fil:
            objekt = rad.split("<SEP>")
            lista.append(Låtar(objekt[0], objekt[1], objekt[2], objekt[3]))
            dictionary[objekt[2]] = lista[len(lista)-1]
    return lista, dictionary


def linsok(list, artistnamn):   #linjärsökning i osorterad lista
    found = False
    counter = 0
    while counter <len(list) and not found:
        if list[counter].artistnamn == artistnamn:
            found = True
        else:
            counter = counter+1

    return found


def sortera(list):
    if len(list)>1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]

        sortera(left)
        sortera(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k]=right[j]
                j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    return list


def binsok(list, artistnamn):
    first = 0
    last = len(list)-1
    found = False

    while first <= last and not found:
        mid = (first + last)//2

        if list[mid].artistnamn == artistnamn:
            found = True
        else:
            if artistnamn < list[mid].artistnamn:
                last = mid-1
            else:
                first = mid+1
    return found
