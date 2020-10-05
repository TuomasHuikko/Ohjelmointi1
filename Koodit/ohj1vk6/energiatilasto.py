"""
COMP.CS.100 "energiatilasto" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873

Ohjelma muodostaa energiatilaston histogrammina käyttäjän antamista
kulutusarvoista tiettyjen kulutusluokkien mukaan luokiteltuna. Ohjelma ei
hyväksy negatiivisia arvoja ja ottaa huomioon myös tilanteen,
jossa kulutusarvoja ei ole yhtäkään.
"""

def consumption_input():
    """
    Kysyy käyttäjältä energiankulutuksen arvoja, kunnes käyttäjä syöttää tyhjän
    rivin. Funktio lisää arvot listaan. Funktio suorittaa myös arvojen
    tarkastelua ja negatiivisten arvojen kohdalla tulostaa:
    "You entered: x. Enter non-negative numbers only!", jossa x käyttäjän syöte.

    :return: Lista käyttäjän syöttämistä ei negatiivisista arvoista.
    :rtype: list
    """

    consumption_loop = True
    consumption_value_list = []

    while consumption_loop:
        consumption_value = input("Enter energy consumption (kWh): ")
        if consumption_value == "":
            consumption_loop = False
        elif int(consumption_value) < 0:
            print(f"You entered: {int(consumption_value)}."
                  f" Enter non-negative numbers only!")
        else:
            consumption_value_list.append(int(consumption_value))

    return consumption_value_list

def class_minimum_value(class_number):
    """
    Laskee kulutusluokan pienimmän arvon eli alarajan.

    :param class_number: Kyseisen kulutusluokan numero
    :type class_number: int
    :return: Palauttaa kyseisen luokan alarajan.
    :rtype: int
    """

    class_min = 10 ** class_number // 100 * 10

    return class_min

def class_maximum_value(class_number):
    """
    Laskee kulutusluokan suurimman arvon eli ylärajan.

    :param class_number: Kyseisen kulutusluokan numero
    :type class_number: int
    :return: Palauttaa kyseisen luokan ylärajan.
    :rtype: int
    """

    class_max = (10 ** class_number) - 1

    return class_max

def calc_consumption_class(consumption_values):
    """
    Laskee käyttäjän syöttämän kulutusarvon kulutusluokan ja tekee
    kulutusluokista listan.

    :param consumption_values: Lista käyttäjän syöttämistä hyväksytyistä
        kulutusarvoista.
    :type consumption_values: list
    :return: Palauttaa listan kulutusluokista kulutusarvojen lukumäärän mukaan
        kyseisessä luokassa.
    :rtype: list
    """

    max_class = calc_max_class(consumption_values)
    consumption_values = sorted(consumption_values)
    consumption_class = [0] * (max_class)
    class_number = 0
    value_counter = 0
    insert_counter = 0
    # Alustetaan muuttujat, määritetään suurin kulutusarvojen luokka sekä
    # luodaan tyhjä lista, johon kulutusluokkien arvot sijoitetaan.

    while value_counter != len(consumption_values):

        value = consumption_values[value_counter]
        class_min = class_minimum_value(class_number+1)
        class_max = class_maximum_value(class_number+1)
        value_counter += 1
        # Lasketaan arvo sekä kulutusluokan rajat.

        if value > class_max:
            class_number += 1
            value_counter = 0
            insert_counter = 0

        elif class_min <= value <= class_max:
            insert_counter += 1
            consumption_class.insert(class_number, insert_counter)
        else:
            consumption_class.insert(class_number, 0)
            # Jos luokkaan ei kuulu yhtäkään alkiota, sijoitetaan arvo 0.

    consumption_class[class_number+1:] = []
    # Poistetaan ylimääräiset alkiot listasta.

    return consumption_class

def calc_max_class(consumption_values):
    """
    Laskee suurimman kulutusluokan arvon käyttäen suurinta käyttäjän
    syöttämää arvoa.

    :param consumption_values: Käyttäjän syöttämät hyväksytyt arvot
    :type consumption_values: list
    :return: Suurimman kulutusluokan arvo
    :rtype: int
    """

    max_value = sorted(consumption_values)[-1]
    class_number = 1
    while True:
        class_min = class_minimum_value(class_number)
        class_max = class_maximum_value(class_number)

        if max_value >= class_min and max_value <= class_max:
            return class_number
        else:
            class_number += 1

def print_single_histogram_line(class_number, count, largest_class_number):
    """
    Funktio tulostaa oikean muotoisen histogrammin rivin,
    kuhan kutsut sitä oikeilla parametrien arvoilla.

    :param class_number: int,
        Mitä kulutuskatergoriaa tulostettava rivi kuvaa (1, 2, 3, ...)
        Parametria <class_number> käytetään päättämään, mikä arvoväli
        (0-9, 10-99, 100-999, ...) riville tulostuu ennen diagrammin
        "*"-merkkejä.

    :param count: int,
        Kuinka monta "*"-merkkiä riville on tarpeen tulostaa, eli
        kuinka monta käyttäjän syöttämää arvoa kuuluu <class_number>-
        parametrin kuvaamalle välillä.

    :param largest_class_number: int,
        Mikä on kaikkein suurin kategorian numero.  Riippuu
        suurimmasta käyttäjän syöttämästä kulutusarvosta.
        Esimerkiksi jos suurin käyttäjän syöttämä luku
        oli 91827364 (8 numeromerkkiä) <largest_class_number>-parametrin
        arvon tulisi myös olla 8.  Parametrin arvoa käytetään
        määriteltäessä, kuinka monta välilyöntiä muiden kuin viimeisen
        histogrammin rivin eteen pitäisi tulostaa.
    """

    min_value = class_minimum_value(class_number)
    max_value = class_maximum_value(class_number)
    range_string = f"{min_value}-{max_value}"

    largest_width = 2 * largest_class_number + 1

    print(f"{range_string:>{largest_width}}: {'*' * count}")

def print_histogram(consumption_class, consumption_values):
    """
    Tulostaa histogrammin käyttäjän syötteistä käyttäen funktiota
    "print_single_histogram_line".

    :param consumption_class: Lista kulutusluokista kulutusarvojen lukumäärän
        mukaan kyseisessä luokassa.
    :type consumption_class: list
    :param consumption_values: Lista käyttäjän syöttämistä hyväksytyistä
        arvoista.
    :type consumption_values: list
    """

    max_class = calc_max_class(consumption_values)
    class_number = 1

    while class_number <= max_class:
        count = consumption_class[class_number-1]
        # Lasketaan arvolla "class_number-1", koska listassa
        # "consumption_class" arvot alkavat indeksistä 0.
        print_single_histogram_line(class_number, count, max_class)
        class_number += 1

def main():

    print("Enter energy consumption data.")
    print("End by entering an empty line.")
    print()

    consumption_values = consumption_input()
    # Seuraavana tarkastelu siitä, onko yhtäkään kulutusarvoa syötetty.
    if consumption_values == []:
        print("Nothing to print. Done.")
    else:
        consumption_class = calc_consumption_class(consumption_values)
        print_histogram(consumption_class, consumption_values)


if __name__ == "__main__":
    main()
