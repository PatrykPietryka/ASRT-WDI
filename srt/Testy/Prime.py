import inspect
import io
from contextlib import redirect_stdout
from Bazowa import Bazowa
from typing import Callable, Tuple, Any

from _utils_T import (
    IMPORTY,
    KOMENDA,
    NAGLOWEK,
    ODPAL_TESTY,
    metoda_nasluchujaca_testow,
    metoda_zwracajaca_testow,
    dynamiczny_import_funkcji,
    RAMKA,
)


class Prime(Bazowa):
    def __str__(self) -> str:
        """
        Generuje testy dla zadania, wywołując odpowiednie metody w celu utworzenia
        struktury testów i ich wyników.
        """
        print(f"\nPisanie testów dla zadania nr: {self.nr_zadania}\n{RAMKA}")

        self.res = IMPORTY
        self.res += "\n"
        self.res += dynamiczny_import_funkcji(self.nr_zadania, self.funkcje)
        self.res += "\n\n"
        self.res += ODPAL_TESTY
        self.res += "\n"
        self.res += KOMENDA
        self.res += "\n\n"
        self.res += NAGLOWEK
        self.res += "\n"
        for funkcja in self.funkcje:
            self.generuj_testy_dla_funkcji(funkcja)
        self.finalizuj_testy()
        return self.res

    def generuj_testy_dla_funkcji(self, funkcja: Callable):
        """
        Generuje testy dla konkretnej funkcji.

        Args:
            funkcja (Callable): Funkcja, dla której mają być generowane testy.
        """
        if len(self.funkcje) > 1:
            print(f"\ttesty dla funkcji {funkcja.__name__}\n")

        liczba_argumentow = len(inspect.signature(funkcja).parameters)

        nr_testu = 1
        while True:
            try:
                parametry = self.pobierz_parametry(nr_testu, liczba_argumentow)
                if parametry == tuple("stop"):
                    break
                wynik_funkcji = self.wynik_funkcje(funkcja, parametry)
            except Exception as e:
                print(f"{str(e)} Wprowadz Ponownie!")
                continue

            if isinstance(wynik_funkcji, str):
                self.res += metoda_nasluchujaca_testow(
                    funkcja.__name__, nr_testu, parametry, wynik_funkcji
                )
            else:
                self.res += metoda_zwracajaca_testow(
                    funkcja.__name__, nr_testu, parametry, wynik_funkcji
                )

            if liczba_argumentow == 0:
                print(f"Wynik to {wynik_funkcji}")
                break

            print(f"Dla {', '.join(map(str, parametry))} wynik to {wynik_funkcji}")
            nr_testu += 1

        print("\n")

    def pobierz_parametry(self, test_index: int, param_count: int) -> Tuple:
        """
        Pobiera parametry testowe od użytkownika.

        Args:
            test_index (int): Indeks aktualnego testu.
            param_count (int): Liczba argumentów, które mają być pobrane.

        Returns:
            Tuple: Krotka z parametrami podanymi przez użytkownika.
        """
        if param_count == 0:
            return ()
        else:
            koncowka_argumetnow = "" if 1 == param_count else "y"
            wyjscie = ", lub 'stop' by zakonczyc testy" if test_index > 3 else ""
            wejscie = input(
                f"\nTest nr {test_index}\nPodaj {param_count} argument{koncowka_argumetnow} testowe{wyjscie}: "
            )
            if wejscie == "stop":
                return tuple("stop")
        print(f"\033[F\033[K\033[F\033[K\033[F\033[K", end="")
        return tuple(self.przetwarzaj_wejscie(wejscie))

    def konwertuj_argument(self, arg):
        """Konwertuje argument na odpowiedni typ: int, float lub pozostaje str bez apostrofów."""
        for typ in (int, float):
            try:
                return typ(arg)
            except ValueError:
                continue
        return arg.replace('"', "")  # Zwraca jako str, jeśli konwersje się nie powiodą

    def przetwarzaj_tablice(self, argumenty, i):
        wynik = []
        i += 1

        while argumenty[i] != "]":
            if argumenty[i] == "[":  # znaleziono nową tablicę
                tablica, i = self.przetwarzaj_tablice(argumenty, i)
                wynik.append(tablica)
            else:
                wynik.append(self.konwertuj_argument(argumenty[i]))
            i += 1

        return wynik, i

    def przetwarzaj_wejscie(self, wejscie):
        wejscie = (
            wejscie.replace(",", " ")
            .replace("]", " ] ")
            .replace("[", " [ ")
            .replace("\n", "")
        )
        argumenty = wejscie.split()

        wyniki = []
        i = 0
        while i < len(argumenty):
            if argumenty[i] == "[":
                tablica, i = self.przetwarzaj_tablice(argumenty, i)
                wyniki.append(tablica)
            else:
                wyniki.append(self.konwertuj_argument(argumenty[i]))
            i += 1

        return wyniki

    def wynik_funkcje(self, funkcja: Callable, parametry: Tuple) -> Any:
        """
        Uruchamia podaną funkcję z przekazanymi parametrami i przechwycuje jej wynik.

        Args:
            funkcja (Callable): Funkcja do uruchomienia.
            parametry (Tuple): Argumenty przekazywane do funkcji.

        Returns:
            Any: Zwraca wynik funkcji
        """
        f = io.StringIO()
        with redirect_stdout(f):
            wynik = funkcja(*parametry)
        if wynik == None:
            return repr(f.getvalue().strip())
        return wynik

    def finalizuj_testy(self):
        """
        Finalizuje proces generacji testów, wyświetla podsumowanie oraz zapisuje
        wyniki do atrybutu `res`.
        """
        print(RAMKA, end="")
        print(f"🥳 Testy dla zadania {self.nr_zadania} zostały pomyślnie wygenerowane!")
        print(RAMKA)
        self.res += "\n"
