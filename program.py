def main():
    x = input("Podaj wiek: ")
    try:
        if(int(x)>=18 and int(x)<=120):
            print("Użytkownik jest pełnoletni.")
        else:
            exit("Użytkownik jest niepełnoletni i/lub zbyt stary")
    except ValueError:
        print("Błedna wartość.")


def sprawdzRegion(region,wiek):
    try:
        if(region == 'USA' and int(wiek)>=40):
            print("Darmowe marlboraski!")
        else:
            pass
    except:
        print("Wystapił błąd podczas sprawdzania regionu")

main()