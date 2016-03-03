from Låtar import Låtar

def readfile(filen):
    list = []
    dictionary = {}

    with open(filen, encoding="utf8") as fil:
        rader = fil.readlines()

        for rad in rader:
            objekt = rad.strip().split("<SEP>")
            list.append(Låtar(objekt[0], objekt[1], objekt[2], objekt[3]))
            dictionary[objekt[2]] = list[len(list)-1]
    return list, dictionary


def linsok(lista, artistnamn):   #linjärsökning i osorterad lista
    found = False

    for i in lista:
        if i.artistnamn == artistnamn:
            found = True

    return found


def sortera(lista):
    if len(lista) > 1:
        mitten = len(lista)//2
        vensterHalva = lista[:mitten]
        hogerHalva = lista[mitten:]

        sortera(vensterHalva)
        sortera(hogerHalva)

        i, j, k = 0, 0, 0

        while i < len(vensterHalva) and j < len(hogerHalva):
            if vensterHalva[i] < hogerHalva[j]:
                lista[k] = vensterHalva[i]
                i = i + 1
            else:
                lista[k] = hogerHalva[j]
                j = j + 1
            k = k + 1

        while i < len(vensterHalva):
            lista[k] = vensterHalva[i]
            i = i + 1
            k = k + 1

        while j < len(hogerHalva):
            lista[k] = hogerHalva[j]
            j = j + 1
            k = k + 1

    return lista


def binsok(lista, artistnamn):
    first = 0
    last = len(lista)-1
    found = False

    while first <= last and not found:
        mid = (first + last)//2

        if lista[mid] == artistnamn:
            found = True
        else:
            if artistnamn < lista[mid].get_artist():
                last = mid-1
            else:
                first = mid+1
    return found
