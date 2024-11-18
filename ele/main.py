from belka import Belka
from sily import Sila
from podpory import PodporaStala, PodporaPrzesuwna
from obliczenia import Obliczenia
import obliczenia 
import sily
import json



b1 = Belka(12,8,0,0)

ps1 = PodporaStala(0)

pp1 = PodporaPrzesuwna(30)

s1 = Sila(10,10,90)
print(s1.skladowa_pionowa())

s2 = Sila(10,20,90)
print(s2.skladowa_pionowa())

o = Obliczenia(b1,[s1,s2],[ps1,pp1])

print(o.oblicz_reakcje())

print(o.oblicz_strzalke_ugiecia(10))




#TODO
#
# Wykorzystać pozostałe pliki do wyświetlenia komunikatu w konsoli zwracającego:
# - Reakcję w podporach
# - Strzałkę ugięcia w wybranym punkcie belki


        #
        # Klasy obiektów zaimportowanych w __init__ zawierają wszystkie potrzebne informacje
        # 1. Wyznacz składową pionową dla każdej siły
        # 2. Oblicz ugięcie belki wywołane daną siłą
        # 2a. Jeżeli miejsce, w którym mierzymy ugięcie jest bliżej początku belki (lewej strony), niż miejsce działania siły, to zastosuj odpowiedni wzór do takiego przypadku
        # 2b. Jeżeli miejsce pomiaru ugięcia jest dalej od początku belki, to zastosuj odpowiedni wzór do takiej sytacji
        # 3. Zgodnie z zasadą superpozycji, zsumuj ugięcia spowodowane każdą z sił
        # 4. Zwróc zsumowane ugięcia w postaci jednej ZMIENNEJ (!!! NIE LISTY !!!)