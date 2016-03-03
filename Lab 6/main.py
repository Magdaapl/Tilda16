import timeit
from sök_sort import *
from Låtar import Låtar

def main():
    filename = "unique_tracks.txt"

    list, dictionary = readfile(filename)
    n = len(list)
    print("Antal element =", n)

    sista = list[n - 1]
    testartist = sista.artistnamn

    linjtid = timeit.timeit(stmt=lambda: linsok(list, testartist), number=10000)
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")

    sorttid = timeit.timeit(stmt=lambda: sortera(list), number=1)
    print("Sorteringen tog", round(sorttid, 4), "sekunder")

    bintid = timeit.timeit(stmt=lambda: binsok(list, testartist), number=10000)
    print("Binärsökningen tog", round(bintid, 4), "sekunder")

    dictionarytid = timeit.timeit(stmt=lambda: dictionary[testartist], number=10000)
    print("Slå upp i dictionary tog", round(dictionarytid, 4), "sekunder")


if __name__ == '__main__':
    main()
