from BintreeFilen import Bintree

def main():
    svenska = Bintree()
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet in svenska:
                pass
            else:
                svenska.put(ordet) # in i sökträdet

    engelska = Bintree()
    with open("engelska.txt", "r", encoding = "utf-8") as engelskfil:
        for row in engelskfil:
            for word in row.split():
                if word in engelska:
                    pass
                elif word in svenska:
                    engelska.put(word)
                    print(word, end = " ")

main()