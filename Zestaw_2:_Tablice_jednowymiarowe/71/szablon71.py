# ====================================================================================================>
# Zadanie 71
# Proszę napisać program, który wypełnia N-elementową tablicę T pseudolosowymi liczbami
# nieparzystymi z zakresu [1..99], a następnie wyznacza i wypisuje różnicę pomiędzy długością najdłuższego
# znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy, a długością najdłuższego ciągu arytme-
# tycznego o ujemnej różnicy, przy założeniu, że kolejnymi wyrazami ciągu są elementy tablicy o kolejnych
# indeksach.
# ====================================================================================================>
# return max_leng_incr, max_leng_decr


def Zadanie_71(sequence): ...


if __name__ == "__main__":
    from testy71 import odpal_testy

    Zadanie_71(int(input('Podaj sequence: ')))

    # odpal_testy()