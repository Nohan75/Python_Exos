import sys

while True:
    year = int(input("Entrez une année : "))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("L'année", year, "est bissextile.")
    else:
        print("L'année", year, "n'est pas bissextile.")
    if input("Voulez-vous continuer ? (o/n) ") == "n":
        sys.exit()
    else:
        continue
