def main():
    x = input("Podaj wiek: ")
    try:
        if(int(x)>=18 and int(x)<=120):
            print("Użytkownik jest pełnoletni.")
        else:
            exit("Użytkownik jest niepełnoletni i/lub zbyt stary")
    except ValueError:
        print("Błedna wartość.")

def podaj_wiek():
    while True:
        wiek=input("Podaj wiek: ")
        if wiek.isdigit():
            return wiek
podaj_wiek()

main()