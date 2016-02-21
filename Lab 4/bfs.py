from BintreeFilen import Bintree
svenska = Bintree()
gamla = Bintree()


def readfile():
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            svenska.put(ordet)


def makechildren(startord):
    barn = []
    gamla.put(startord)
    alfabet = "abcdefghijklmnoprstuvwxyzåäö"
    for letter in range(len(startord)):
        for bokstav in alfabet:
            nyttord = list(startord)
            nyttord[letter] = bokstav
            nyttord = "".join(nyttord)  # Startord = "maj" nyttord = maö
            if nyttord in svenska and nyttord not in gamla:
                gamla.put(nyttord)
                barn.append(nyttord)
    print(barn)


def main():
    readfile()
    startord = input("Välj startord: ")
    slutord = input("Välj slutord: ")
    makechildren(startord)


if __name__ == '__main__':
    main()
