from random import *

valikud = ["kivi", "k‰‰rid", "paber"]

def m‰ngi():
    while True:
        m‰ngija_valik = input("Vali: kivi, k‰‰rid vıi paber (vıi 'lıpeta' m‰ngu lıpetamiseks): ")
        if m‰ngija_valik == "lıpeta":
            print("M‰ng lıppenud")
            break
        if m‰ngija_valik not in valikud:
            print("Vale sisend. Proovi uuesti")
            continue

        arvuti_valik == random.choice(valikud)
        print(f"Arvuti valis: {arvuti_valik}")

        if m‰ngija_valik == arvuti_valik:
            print("Viik!")
        elif (m‰ngija_valik == "kivi" and arvuti_valik == "k‰‰rid") or \
             (m‰ngija_valik == "k‰‰rid" and arvuti_valik == "paber") or \
             (m‰ngija_valik == "paber" and arvuti_valik == "kivi"):
            print("Sa vıitsid!")
        else:
            print("Sa kaotasid!")