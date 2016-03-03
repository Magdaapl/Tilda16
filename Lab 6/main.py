import timeit
from sök_sort import *
from Låtar import Låtar

def main():
    filename = "unique_tracks.txt"

    lista, dictionary = readfile(filename)
    n = len(lista)
    print("Antal element =", n)

    sista = lista[n - 1]
    testartist = sista.artistnamn

    linjtid = timeit.timeit(stmt=lambda: linsok(lista, testartist), number=10000)
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")

    sorttid = timeit.timeit(stmt=lambda: sortera(lista), number=1)
    print("Sorteringen tog", round(sorttid, 4), "sekunder")

    bintid = timeit.timeit(stmt=lambda: binsok(lista, testartist), number=10000)
    print("Binärsökningen tog", round(bintid, 4), "sekunder")

    dictionarytid = timeit.timeit(stmt=lambda: dictionary[testartist], number=10000)
    print("Slå upp i dictionary tog", round(dictionarytid, 4), "sekunder")


if __name__ == '__main__':
    main()
