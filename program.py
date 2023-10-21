def main():
    x = input("Podaj wiek: ")
    try:
        if(int(x)>=18 and int(x)<=120):
            print("Użytkownik jest pełnoletni.")
        else:
            exit("Użytkownik jest niepełnoletni i/lub zbyt stary")
    except ValueError:
        print("Błedna wartość.")


def sprawdz_czy_30(plec, wiek):
    try:
        if plec == 'F' and int(wiek)>=30:
            print("Pierwszy aperol za darmo!")
        else:
            pass
    except:
        print("wystąpił błąd")

main()