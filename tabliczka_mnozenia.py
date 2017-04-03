# wypisz pustą komórkę w lewym górnym rogu, nagłówek kolumny z numerem wiersza
print('\t ', end='')

# wypisz nagłówki kolumn
for nr_kolumny in range(1, 11):
    print('\t' + str(nr_kolumny) + ' ', end='')
print()

for nr_wiersza in range(1, 11):
    # wypisz nagłówek wiersza
    print('\t' + str(nr_wiersza) + ': ', end='')
    # wypisz kolejne komórki tabliczki mnożenia
    for nr_kolumny in range(1, 11):
        print('\t' + str(nr_wiersza * nr_kolumny) + ' ', end='')
    print()

a = 5
b = 10
c = 0.581234
# %d to liczba całkowita, %f to float
print('Wartość zmiennej a: %d a potem wartość zmiennej b: %d i c: %.8f' % (a, b, c))
print('Wartość zmiennej a: {} a potem wartość zmiennej b: {: 2d} i c: {: 3.2f}'.format(a, b, c))