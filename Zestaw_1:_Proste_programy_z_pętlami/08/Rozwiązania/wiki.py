# ====================================================================================================>
# Zadanie 8
# Proszę napisać program rozwiązujący równanie xx =2024 metodą bisekcji.
# ====================================================================================================>


def Zadanie_8():
    eps = 10**-6
    a = 4
    b = 5
    while b - a > eps:
        if ((a + b) / 2) ** ((a + b) / 2) > 2024:
            b = (a + b) / 2
        else:
            a = (a + b) / 2
    print(a, b)


