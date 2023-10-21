def main():
    x = input("Podaj wiek: ")
    try:
        if(int(x)>=18 and int(x)<=120):
            print("Użytkownik jest pełnoletni.")
        else:
            exit("Użytkownik jest niepełnoletni i/lub zbyt stary")
    except ValueError:
        print("Błedna wartość.")


def sprawdzRegion(region,wiek,plec):
    try:
        if(region == 'USA' and int(wiek)>=40 and plec == 'M'):
            print("Darmowe marlboraski!")
        else:
            pass
    except:
        print("Wystapił błąd podczas sprawdzania regionu")
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