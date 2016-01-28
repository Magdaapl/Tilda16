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


def read_file(the_list):
    with open(the_list, encoding="utf8") as location_file:
        the_list = [row.strip() for row in location_file]
    return the_list


def create_object(the_list):
    object_list = [Plats1(the_list[i], the_list[i + 1], the_list[i + 2],
                         the_list[i + 3], the_list[i + 4]) \
                   for i in range(6, len(the_list) - 4, 6)]
    return object_list


def search(object_list):
    userinput = input("Vilket plats vill du söka efter?: ")
    for i in range(0, len(object_list)):
        if str(object_list[i].visa_namn()) == userinput:
            print(object_list[i])


def main():
    the_list = read_file("geodataSW.txt")
    object_list = create_object(the_list)
    search(object_list)


if __name__ == '__main__':
    main()
