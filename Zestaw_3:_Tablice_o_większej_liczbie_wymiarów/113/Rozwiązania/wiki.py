# ====================================================================================================>
# Zadanie 113
# Dana jest tablica T[N][N] wypełniona wartościami 0,1. Każdy wiersz tablicy traktujemy
# jako liczbę zapisaną w systemie dwójkowy m o długości N bitów. Stała N jest rzędu 1000.
# Proszę zaimplementować funkcję distance(T), która dla takiej tablicy wyznaczy dwa wiersze, dla których różnica zawartych
# w wierszach liczb jest największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić odległość
# pomiędzy znalezionymi wierszami. Można założyć, że żadne dwa wierze nie zawierają identycznego ciągu
# cyfr.
# ====================================================================================================>

# https://github.com/MarcinSerafin03/bit-algo-start-24-25-WDI/tree/main


def bin_to_deci(row):
    res = 0
    exp = 0
    for i in range(len(row) - 1, -1, -1):
        res += 2**exp * row[i]
        exp += 1
    return res


def bigger(row1, row2):
    l = len(row1)
    for i in range(l):
        if row1[i] > row2[i]:
            return True
        elif row1[i] < row2[i]:
            return False
    return True


def distance(T):
    mini_ind = 0
    maxi_ind = 0
    for i in range(len(T)):
        if bigger(T[i], T[maxi_ind]):
            maxi_ind = i
        if bigger(T[mini_ind], T[i]):
            mini_ind = i

    return bin_to_deci(T[maxi_ind]) - bin_to_deci(T[mini_ind])
