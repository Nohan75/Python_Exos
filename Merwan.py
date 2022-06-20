import sys

while True :

    Annee = int(input("Entre ton annee : "))

    if Annee % 4 == 0 and Annee % 100 != 0 or Annee % 400 == 0 :
        print("Votre annee ", Annee ," est bisextilte")
    else:
        print("Votre annee ", Annee ," est  pas bisextilte")

    if input("Voulez-vous continuer ? (o/n) ") == "n":
        sys.exit()
    else:
        continue