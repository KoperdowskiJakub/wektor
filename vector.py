import random


class Vector:
    # konstruktor
    def __init__(self, rozmiar=3, liczby=[0, 0, 0]):
        self.rozmiar = rozmiar
        self.liczby = liczby

    # dwie metody do wyciagania z wektora jego rozmiaru i elementow
    def get_rozmiar(self):
        return self.rozmiar

    def get_liczby(self):
        return self.liczby

    # wektor o losowych wspolrzednych
    def losowanie(self):
        for i in range(len(self.liczby)):
            self.liczby[i] = random.randint(-20, 20)
        return None

    # zmiana wspolrzednych wektora
    def zmiana_zmiennych(self, lista):
        if len(lista) != self.rozmiar:
            return "value ERROR"
        else:
            for i in range(self.rozmiar):
                self.liczby[i] = lista[i]
            return None

    def __add__(self, other):
        if self.rozmiar != other.rozmiar:
            return "value ERROR"
        else:
            lista = []
            for i in range(self.rozmiar):
                lista.append(self.liczby[i] + other.liczby[i])
            wynik = Vector(self.get_rozmiar(), lista)
            return wynik

    def __sub__(self, other):
        if self.rozmiar != other.rozmiar:
            return "value ERROR"
        else:
            lista = []
            for i in range(self.rozmiar):
                lista.append(self.liczby[i] - other.liczby[i])
            wynik = Vector(self.get_rozmiar(), lista)
            return wynik

    # mnozy kazdy element po kolei przez podany skalar, a potem podmienia wspolrzedne na odpowiednie wyniki
    def mnozenie_skalar(self, skalar):
        for i in range(self.rozmiar):
            self.liczby[i] = self.liczby[i] * skalar
        return None

    # liczy dlugosc wektora wg wzoru na pierwiastek z sumy kwadratow
    def dlugosc_wektora(self):
        suma = 0
        for i in range(self.rozmiar):
            suma += (self.liczby[i]) ** 2
        suma = suma ** (1 / 2)
        return suma

    # liczy iloczyn skalarny dwoch wektorow
    def iloczyn_skalarny(self, other):
        if self.rozmiar != other.rozmiar:
            return "value ERROR"
        else:
            suma = 0
            for i in range(self.rozmiar):
                tmp = self.liczby[i] * other.liczby[i]
                suma += tmp
                tmp = 0
            return suma

    # sumuje wspolrzedne
    def suma_elementow(self):
        suma = 0
        for i in range(self.liczby):
            suma += self.liczby[i]
        return suma

    # sprawdza czy mamy dany element posrod wspolrzednych wektora
    def w_srodku(self, element):
        if element in self.liczby:
            return True
        else:
            return False

    # zwraca podana wspolrzedna
    def __getitem__(self, numer):
        if numer > self.rozmiar:
            return "value ERROR"
        else:
            wynik = self.liczby[numer]
            return wynik

    # zamienia pojedyncza wspolrzedna
    def __setitem__(self, numer, wartosc):
        if numer > self.rozmiar:
            return "value ERROR"
        else:
            self.liczby[numer] = wartosc



