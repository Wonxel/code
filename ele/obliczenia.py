from belka import Belka
from podpory import *
from sily import Sila

class Obliczenia:
    """ Klasa odpowiadająca za obliczanie reakcji podpór i strzałki ugięcia belki """
    
    def __init__(self, belka: Belka, sily: list[Sila], podpory: list[Podpora]):
        """ Zarówno siły jak i podpory należy podać jako listy (w kwadratowych nawiasach: []), nawet jeśli jest tylko jedna siła. Podpory zawsze muszą być dwie."""
        self.belka = belka
        self.sily = sily
        self.podpory = podpory

    def oblicz_reakcje(self):
        # Ustalanie, czy podpora moze przenosic sily poziome (przyjmuje, ze tylko PodporaStala moze)
        podpora_stala = [podpora for podpora in self.podpory if isinstance(podpora, PodporaStala)]
        podpora_przesuwna = [podpora for podpora in self.podpory if isinstance(podpora, PodporaPrzesuwna)]
        
        if len(podpora_stala) != 1 or len(podpora_przesuwna) != 1:
            raise ValueError("Musisz miec dokladnie jedna podpore stala i jedna przesuwna!")

        podpora_A = podpora_stala[0]
        podpora_B = podpora_przesuwna[0]

        # Reakcje pionowe
        suma_sil_pionowych = sum(sila.skladowa_pionowa() for sila in self.sily)

        # Moment wokol podpory A (stalej)
        moment_A = sum(sila.skladowa_pionowa() * (sila.pozycja - podpora_A.pozycja) for sila in self.sily)

        # Reakcja pionowa w podporze B
        reakcja_B_pionowa = moment_A / (podpora_B.pozycja - podpora_A.pozycja)

        # Reakcja pionowa w podporze A
        reakcja_A_pionowa = suma_sil_pionowych - reakcja_B_pionowa

        # Reakcje poziome (tylko w podporze stalej)
        suma_sil_poziomych = sum(sila.skladowa_pozioma() for sila in self.sily)
        reakcja_A_pozioma = suma_sil_poziomych  # Zalozenie, ze tylko podpora stala przenosi sily poziome

        return {
            "reakcja_A_pionowa": reakcja_A_pionowa,
            "reakcja_A_pozioma": reakcja_A_pozioma,
            "reakcja_B_pionowa": reakcja_B_pionowa
        }

    def oblicz_strzalke_ugiecia(self, x):
        """ Wyznaczanie strzalki ugiecia w dowolnym punkcie belki na podstawie superpozycji.
            Parametr x wskazuje, w którym miejscu belki sprawdzamy jej ugięcie """
        
        F = sum(sila.skladowa_pionowa() for sila in self.sily)
        h = self.belka.wysokosc
        L = self.belka.szerokosc
        E = self.belka.modul_younga
        I = self.belka.oblicz_moment_bezwladnosci(L,h)

        # matematyka

        a = F * h * (L - x)
        b = 6 * E * I[0] + I[1] * L
        c = L**2 - h**2 - (L - x)**2

        # koniec matmy matematyka

        return (a / b) * c


        # TODO
        #
        # Klasy obiektów zaimportowanych w __init__ zawierają wszystkie potrzebne informacje
        # 1. Wyznacz składową pionową dla każdej siły
        # 2. Oblicz ugięcie belki wywołane daną siłą
        # 2a. Jeżeli miejsce, w którym mierzymy ugięcie jest bliżej początku belki (lewej strony), niż miejsce działania siły, to zastosuj odpowiedni wzór do takiego przypadku
        # 2b. Jeżeli miejsce pomiaru ugięcia jest dalej od początku belki, to zastosuj odpowiedni wzór do takiej sytacji
        # 3. Zgodnie z zasadą superpozycji, zsumuj ugięcia spowodowane każdą z sił
        # 4. Zwróc zsumowane ugięcia w postaci jednej ZMIENNEJ (!!! NIE LISTY !!!)
        