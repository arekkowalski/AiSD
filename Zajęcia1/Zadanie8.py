lista = []
while True:
    liczba = input('Podaj liczbe: ')
    lista.append(liczba)
    wybor = input('Jesli chcesz zakończyć działanie programu wpisz "n", w przeciwnym wypadku wpisz dowolny znak: ')
    if wybor == 'n':
        break

tuple(lista)
print(lista)