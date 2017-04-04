# -*- coding: utf-8 -*-
import os
import sys
import random


def daj_litere():
    while True:
        litera = raw_input("Wpisz pojedyncza litere: ")

        if len(litera) != 1:
            print
            'miala byc jedna litera'
            continue
        return litera


def sprawdz(litera, slowo, trafione):
    if litera not in slowo:
        print
        'BRAK WYSTAPIEN.'
        return False
    elif litera in trafione:
        print
        'BYLO. NIE MA CWANIAKOWANIA.'
        return False
    return True


def main():
    os.system('cls')
    print
    'WITAJ W MOJEJ WERSJI HANGMAN. UWAGA PRODUKT RAKOTWORCZY!'

    slowa = ['samolot', 'kelnerka', 'komputer', 'makaron', 'motor', 'transport']
    slowo = random.choice(slowa)

    zycia = 11
    # odpowiedzialne za zliczanie trafien
    do_odgadniecia = len(set(slowo))
    # odpowiedzialna za wyswietlanie trafien
    trafione = []

    while True:
        # pobranie danych i weryfikacja
        litera = daj_litere()

        if not sprawdz(litera, slowo, trafione):
            zycia -= 1
            print
            'POZOSTALO {} ZYC'.format(zycia)
            if len(zycia) == 1:
                print
                'przegrales zycie'
                sys.exit()
            continue

        # policzenie wyników
        trafione.append(litera)

        # wypisywanie zgadnietych liter
        print
        '{} wystapienia'.format(slowo.count(litera))
        for char in slowo:
            print
            char if char in trafione else '.'

        do_odgadniecia -= 1
        if do_odgadniecia == 0:
            print
            'ODGADLES. GRATULUJE'
            sys.exit()


if __name__ == '__main__':
# uruchom glowny program tylko jak ten skrypt jest odpalony z python a nie importowany z innego pliku
main()