def main():
    x = input("Podaj wiek: ")
    try:
        if(int(x)>=18 and int(x)<=120):
            print("Użytkownik jest pełnoletni.")
        else:
            exit("Użytkownik jest niepełnoletni i/lub zbyt stary")
    except ValueError:
        print("Błedna wartość.")



def okresl_region ():
    regio = ""
    while len(regio)!= 3:
        x = input("Podaj region, np. EUR -= Europa, USA - Stany")
        regio = x.upper()
    return regio
