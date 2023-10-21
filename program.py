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
          
def podajPlec():
    plec=""
    while plec != "M" and plec != "F":
        x = input("Podaj płeć: M - mężczyzna, F - kobieta: ")
        plec = x.upper()
    return plec

def okresl_region ():
    regio = ""
    while len(regio)!= 3:
        x = input("Podaj region, np. EUR -= Europa, USA - Stany")
        regio = x.upper()
    return regio

def sprawdz_czy_30(plec, wiek):
 try:
        if plec == 'F' and int(wiek)>=30:
            print("Pierwszy aperol za darmo!")
        else:
            pass
    except:
        print("wystąpił błąd")

def promocja_malboro(region,wiek,plec):
    try:
        if(region == 'USA' and int(wiek)>=40 and plec == 'M'):
            print("Darmowe marlboraski!")
        else:
            pass
    except:
        print("Wystapił błąd podczas sprawdzania regionu")