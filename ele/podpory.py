class Podpora:
    """ Klasa abstrakcyjna dla podpór """
    def __init__(self, pozycja: float):
        self.pozycja = pozycja  # Pozycja podpory na belce (odległość od początku belki)

class PodporaStala(Podpora):
    """ Podpory stałe przenoszą siły pionowe, poziome i momenty """
    def __init__(self, pozycja: float):
        super().__init__(pozycja)

class PodporaPrzesuwna(Podpora):
    """ Podpory przesuwne przenoszą tylko siły pionowe """
    def __init__(self, pozycja: float):
        super().__init__(pozycja)
