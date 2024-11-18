import math

class Belka:
    def __init__(self, szerokosc: float, wysokosc: float, dlugosc: float, modul_younga: float):
        self.moment_bezwladnosci = self.oblicz_moment_bezwladnosci(szerokosc, wysokosc)
        self.dlugosc = dlugosc  # [m]
        self.szerokosc = szerokosc  
        self.wysokosc = wysokosc
        self.modul_younga = modul_younga # [Pa]

    def oblicz_moment_bezwladnosci(self, szerokosc, wysokosc):
        # Zwroc wartosc momentu bezwladnosci dla danych wejsciowych szerokosc, wysokosc
        # Znajdz wzór na wartość momentu bezwładnosci dla belki o przekroju prostokata. Sila przykladana jest wzdluz wymiaru wysokosc

        # sprawdz czy wartość nie jest mniejsza lub równa 0
        if not szerokosc <= 0 or not wysokosc <= 0 :
            # podstawianie do wzoró b*h^3/12
            jx0 = szerokosc * wysokosc ** 3 / 12

            # podstawianie do wzoró h*b^3/12
            jy0 = wysokosc * szerokosc ** 3 / 12

            # print wartości a czemu by nie 
            print("jx0: " + str(jx0) + "jy0: " + str(jy0))

            # zwracamy wartości jx0, jy0
            return [jx0,jy0]
        else:
            # zwraca wartość None jeśli podano cyfrę mniejszą lub równą 0
            print("Funkcja: oblicz_moment_bezwladnosci wprowadzono liczbę 0")
            return None
        
        
