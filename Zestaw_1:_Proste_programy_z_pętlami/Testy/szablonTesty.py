# ====================================================================================================>
# Zadanie 57
# Liczbę nazywamy iloczynowo-pierwszą jeżeli iloczyn jej cyfr w systemie o podstawie b jest
# liczbą pierwszą. Naprzykład: 13 jest liczbą iloczynowo-pierwszą w systemie dziesiętnym, bo1∗3=3
# 16 jest  liczbą iloczynowo-pierwszą w systemie trójkowym, bo 16=121(3) ,1∗2∗1=2 W liczbie naturalnej możemy
# dokonywać rotacji jej cyfr, np. 1428, 4281, 2814, 8142 albo 209, 092, 920. Proszę napisać funkcję, która dla
# danej liczby naturalnej N, zwróci najmniejszą podstawę systemu (z zakresu 2-16) w którym przynajmniej
# jedna z rotowanych liczb jest iloczynowo-pierwsza albo wartość None gdy taka podstawa nie istnieje.
# ====================================================================================================>


def Zadanie_57(zmiena, zmiena2) -> float: ...


if __name__ == "__main__":
    from testyTesty import odpal_testy

    Zadanie_57(int(input("Podaj zmiena: ")), int(input("Podaj zmiena2: ")))

    # odpal_testy()
