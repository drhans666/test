#-*- coding: utf-8 -*-
import os
import sys
os.system('cls')

tekst = raw_input('Wprowadz text o dlugosci od 20 do 30 znakow:')
ilosc = len(tekst)

# sprawdza czy została wpisana odpowiednia ilosc znakow
if ilosc not in range (20, 30):
  print 'Mialo byc 20-30 znakow'
  sys.exit(0)

# wyznacza srodkowa wartosc sumy liter zmiennej "tekst"
litera = ilosc / 2

# wyświetla przypisany srodkowej wartosci liter znak, nastpenie mnozy go 10 krotnie
print 'Dziesieciokrotnosc srodkowej litery Twojego wyrazu to:', tekst[litera] * 10

