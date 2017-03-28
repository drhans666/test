# -*- coding: utf-8 -*-
import os
import sys
import random
os.system('cls')


def pobieranie_i_weryfikacja():

    slowo = 'transport'
    while True:
        litera = raw_input("Wpisz pojedyncza litere: ")

        # liczy czy faktycznie została wpisana pojedyncza litera

        # walidacja
        if len(litera) != 1:
            print 'miala byc jedna litera'
            continue
        break

    return slowo, litera,


def main():
    zycia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odganiete = 0
    while True:
        slowo, litera = pobieranie_i_weryfikacja()

        if litera not in slowo:
            del zycia[1]
            print '0 wystapien. idz umrzyj'
            if len(zycia) < 2:
                sys.exit('Przegrales')
            continue

        # wykonanie
        print 'brawo'
        print slowo.count(litera), ('wystapienia')
        odganiete = odganiete + slowo.count(litera)
        if odganiete >= len(slowo):
            print 'wygrales'
            exit()


if __name__ == '__main__':
    # uruchom glowny program tylko jak ten skrypt jest odpalony z python a nie importowany z innego pliku
    main()
