class Plats1():
    def __init__(self, namn, beskrivning, latitud, longitud, datum):
        self.namn = namn
        self.beskrivning = beskrivning
        self.latitud = latitud
        self.longitud = longitud
        self.datum = datum

    def visa_namn(self):
        return self.namn

    def visa_beskrivning(self):
        return self.beskrivning

    def visa_latitud(self):
        return self.latitud

    def visa_datum(self):
        return self.datum

    def __str__(self):
        return str(self.namn) + " " + str(self.beskrivning) + " " + str(self.latitud) + " " + str(
            self.longitud) + " " + str(self.datum)


def läsa_filen(lista):
    with open(lista, encoding="utf8") as f:
        lista = [row.strip() for row in f]
    return lista


def skapa_objekt(lista):
    objekt_lista = []
    for i in range(6, len(lista) - 4, 6):
        objekt_lista.append(Plats1(lista[i], lista[i + 1], lista[i + 2],
                                   lista[i + 3], lista[i + 4]))
    return objekt_lista


def leta(objekt_lista):
    user_input = input("Leta efter plats: ")
    for i in range(0, len(objekt_lista)):
        if str(objekt_lista[i].visa_namn()) == user_input:
            print(objekt_lista[i])

def leta3(objekt_lista):
    user_input3 = input("Du kan också söka genom beskrivning: ")
    for i in range(0, len(objekt_lista)):
        if str(objekt_lista[i].visa_beskrivning()) == user_input3:
            print(objekt_lista[i])

def main():
    lista = läsa_filen("geodataSW.txt")
    objekt_lista = skapa_objekt(lista)
    leta(objekt_lista)
    leta3(objekt_lista)

if __name__ == '__main__':
    main()
