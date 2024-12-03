# nie refaktoryzowalme to tylko napisalem w 15 m prosze nie oceniac plz


def dodaj_readme():
    """skrypt tworzacy zdjecia zadan w folderach o tych samych nazwach"""
    import os

    FOLDERY_ZADAN = [
        "",
        "Kolokwia/Kolokwium_1",
        "Kolokwia/Kolokwium_2",
        "Kolokwia/Kolokwium_3",
        "Kolokwia/Kolokwium_3",
        "Zestaw_1:_Proste_programy_z_pętlami",
        "Zestaw_2:_Tablice_jednowymiarowe",
        "Zestaw_3:_Tablice_o_większej_liczbie_wymiarów",
        "Zestaw_4:_Struktury_danych",
        "Zestaw_5:_Rekurencja",
        "Zestaw_6:_Struktury_odsyłaczowe_liniowe",
        "Zestaw_7:_Struktury_drzewiaste",
        "Zestaw_8:_Wyszukiwanie_i_sortowanie",
    ]

    sciezki = [f"../../{folder}" for folder in FOLDERY_ZADAN]

    zadania = []
    for folder_zadania in sciezki:
        zadania_folderu = [
            z
            for z in os.listdir(folder_zadania)
            if os.path.isdir(os.path.join(folder_zadania, z))
        ]
        zadania.append(zadania_folderu)

    sciezka_zdjec = "../zbior_zadan/"
    elements = os.listdir(sciezka_zdjec)
    for element in elements:
        nazwa_zdjecia, _ = element.split(".")
        for i, z in enumerate(zadania):
            if nazwa_zdjecia in z:
                if "README.md" not in os.listdir(
                    os.path.join(sciezki[i], nazwa_zdjecia)
                ):
                    with open(
                        os.path.join(sciezki[i], nazwa_zdjecia, "README.md"), "w"
                    ) as file:
                        file.write(
                            f"![Zadanie {nazwa_zdjecia}](../../srt/zbior_zadan/{nazwa_zdjecia}.png)"
                        )

                    print("dodano readme do ", nazwa_zdjecia)


dodaj_readme()
