#"kivi, käärid, paber!"

from random import *

# Loob valikute loetelu
valikud = ["kivi", "käärid", "paber"]

# Käivitab lõpmatu tsükli, nii et mäng jätkub, kuni mängija ütleb 'lõpeta'
while True:
    # palub mängijal sisestada oma valik
    mängija_valik = input("Vali: kivi, käärid või paber (või 'lõpeta' mängu lõpetamiseks): ")

    # Kontrollib, kas mängija soovib mängu lõpetada
    if mängija_valik == "lõpeta":
        print("Mäng lõppenud")  # Kui jah, väljastab lõpliku lõppseisundi  ja lõpetab tsükli
        break

    # Kui mängija valik on kehtetu, palub ta mängijal uuesti valida.
    if mängija_valik not in valikud:
        print("Vale sisend. Proovi uuesti")  # Vead toovad mängija tagasi sisestuse valikusse
        continue

    # Arvuti valib juhuslikult ühe valiku
    arvuti_valik = random.choice(valikud)
    print(f"Arvuti valis: {arvuti_valik}")

    # Kontrollib tulemusi ja annab tagasisidet
    if mängija_valik == arvuti_valik:
        print("Viik!")
    elif (mängija_valik == "kivi" and arvuti_valik == "käärid") or \
         (mängija_valik == "käärid" and arvuti_valik == "paber") or \
         (mängija_valik == "paber" and arvuti_valik == "kivi"):
        print("Sa võitsid!")
    else:
        print("Sa kaotasid!")
