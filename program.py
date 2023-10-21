# program.py adult checking !
wiek = input('Podaj wiek użytkownika jako liczbę: ')
wiek = int(wiek)

if wiek >= 18:
    print('Witaj w apce. Możesz kupować')
else:
    exit('jeśteś za młody')

def sprawdzamy_wiek():
    wiek = input('Podaj wiek: ')
    if wiek> 18:
        print('zapraszamy!')
    else:
        print('spadaj młody!')
