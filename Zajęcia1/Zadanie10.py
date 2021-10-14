napis: str = '101'
napis2: str = '1110'

def zadanie10(znaki):
    for i in range(len(znaki)):
        if znaki[i] != znaki[-1 - i]:
            return print('napis nie jest palindromem!')
    return print('napis jest palindromem!')


zadanie10(napis)
zadanie10(napis2)