# ====================================================================================================>
# Zadanie 129
# Proszę napisać funkcję która zamienia liczby wymierne reprezentowane jako rozwinię-
# cia dziesiętne w postaci napisów na liczbę wymierną w postaci nieskracalnego ułamka jako pary licznik-
# mianownik. Na przykład: ”0.25” na (1,4), ”0.(6)” na (2,3), ”0.(142857)” na (1,7)
# ====================================================================================================>


def Zadanie_129(liczba: str): ...


if __name__ == "__main__":
    from testy129 import odpal_testy

    Zadanie_129(str(input("Podaj liczba: ")))

    # odpal_testy()