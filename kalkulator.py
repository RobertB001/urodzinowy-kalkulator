import datetime

print("Podaj datę swoich urodzin:")
rok = int(input("Rok urodzenia (np. 2013): "))
miesiac = int(input("Miesiąc (1-12, np. 4): "))
dzien = int(input("Dzień (np. 7): "))
ile_lat = int(input("Do ilu lat w przód sprawdzić (np. 30): "))

dzis = datetime.date.today()
biezacy_rok = dzis.year


print(f"\nTwoje urodziny wypadają w weekend w tych latach:")
znaleziono = False
for pszyszly_rok in range(biezacy_rok, biezacy_rok + ile_lat +1):
    try:
        data = datetime.date(przyszly_rok, miesiac, dzien)
    except ValueError:
            continue
    dzien_tygodnia = data.weekday()
    if dzien_tygodnia == 5:
        print(f" {przyszly_rok} - sobota") 
        znaleziono = True
    elif dzien_tygodnia == 6:
        print(f" {przyszly_rok} - niedziela")
        znaleziono = True

if not znaleziono:
    print(" Brak - w tym przedziale lat urodziny nie wypadaja w weekend.")
