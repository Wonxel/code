import math

class Sila:
    """ Klasa reprezentująca siły działjące na belkę """
    
    def __init__(self, wartosc: float, pozycja: float, kat: float = 90):
        self.wartosc = wartosc  # [N]
        self.pozycja = pozycja  # Pozycja przylozenia sily na belce (odległosc od początku belki) [m]
        self.kat = kat  # Kat, pod jakim działa siła (domyślnie 90 stopni, czyli pionowo)
    
    def skladowa_pionowa(self):
        """ Oblicza składową pionową siły (sin(kat)) """
        return self.wartosc * math.sin(math.radians(self.kat))

    def skladowa_pozioma(self):
        """ Oblicza składową poziomą siły (cos(kat)) """
        return self.wartosc * math.cos(math.radians(self.kat))
