import unittest
import io
from contextlib import redirect_stdout

from exercise143 import Zadanie_143

TESTY = False  # po napisaniu testow zmienic na true


# testy pisze sie kopiujac jedna z tych funkcji i zmieniajac nazwe. trzeba zostawic przedrostek test_<tutaj dowolnosci>
# jesli funkcja przyjmuje wartosci trzeba dodac do wywolan aby testy dzialaly
# oczekiwne wyniki sa w tablicy zeby moc akceptowac kilka mozliwych dobrych wynikow w roznej kolejnosci/formacie np ["(1,2)","1 2","1\n2\n"]
# print(f"{repr(wynik)}") # Przydaje sie, wyświetla wynik wraz z niewidocznymi znakami (np"\t1\n2\n3\n") gotowe do wklejenia do oczekiwanego_wyniku
class Test143(unittest.TestCase):

    def test_wypisywania(self):
        f = io.StringIO()
        with redirect_stdout(f):
            Zadanie_143()
        wynik = f.getvalue().strip()

        oczekiwany_wynik = [""]
        self.assertIn(wynik, oczekiwany_wynik)

    def test_zwracania(self):
        wynik = Zadanie_143()

        oczekiwany_wynik = [None]
        self.assertIn(wynik, oczekiwany_wynik)


def odpalTesty():
    assert TESTY, "Testy do tego zadania nie zostaly jeszcze napisane"
    suite = unittest.TestLoader().loadTestsFromTestCase(Test143)
    unittest.TextTestRunner(verbosity=2).run(suite)
