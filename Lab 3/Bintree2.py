from BintreeFilen import Bintree
def main():
    svenska = Bintree()
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet in svenska:
                print(ordet, end = " ")
            else:
                svenska.put(ordet)             # in i sökträdet
    print("\n")
main()