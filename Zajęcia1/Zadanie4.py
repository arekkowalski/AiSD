def zadanie2(imie, nazwisko):
    return imie[0].capitalize() + ". " + nazwisko.capitalize()

def zadanie4(imie, nazwisko, funkcja):
    return  funkcja(imie, nazwisko)

print(zadanie4("arek", "kowalski",zadanie2))