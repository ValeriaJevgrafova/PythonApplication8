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


#töötamine nimekirjade ja stringidega

from random import *

# Algselt on meil nimekiri, millega töötame
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    print("\nMenüü:")
    print("1. Lisa element lõppu nimekirja (append)")
    print("2. Laienda nimekirja teise nimekirjaga (extend)")
    print("3. Sisesta element nimekirja kindlasse kohta (insert)")
    print("4. Eemalda esimene element, mille väärtus on määratud (remove)")
    print("5. Eemalda element kindla indeksiga (pop)")
    print("6. Leia esimene element kindla väärtusega (index)")
    print("7. Arvuta, mitu korda element nimekirjas esineb (count)")
    print("8. Sorteeri nimekiri (sort)")
    print("9. Pööra nimekiri ümber (reverse)")
    print("10. Tee nimekirja koopia (copy)")
    print("11. Kustuta kõik elemendid nimekirjast (clear)")
    print("0. Välju programmist")
    
    # Küsi kasutajalt, millist tegevust ta soovib teha
    choice = input("Vali tegevuse number: ")

    if choice == "1":
        # Lisa element lõppu nimekirja
        element = int(input("Sisesta element, mis tuleb lisada: "))
        my_list.append(element)
        print("Nimekiri pärast lisamist:", my_list)

    elif choice == "2":
        # Laienda nimekirja teise nimekirjaga
        extension_list = list(map(int, input("Sisesta elemendid, mis laiendavad nimekirja (lahutada tühikutega): ").split()))
        my_list.extend(extension_list)
        print("Nimekiri pärast laiendamist:", my_list)

    elif choice == "3":
        # Sisesta element kindlasse kohta nimekirjas
        index = int(input("Sisesta indeks, kuhu element tuleb sisestada: "))
        element = int(input("Sisesta element, mis tuleb sisestada: "))
        my_list.insert(index, element)
        print("Nimekiri pärast sisestamist:", my_list)

    elif choice == "4":
        # Eemalda esimene element, mille väärtus on määratud
        element = int(input("Sisesta element, mis tuleb eemaldada: "))
        if element in my_list:
            my_list.remove(element)
            print("Nimekiri pärast eemaldamist:", my_list)
        else:
            print(f"Element {element} ei ole nimekirjas.")

    elif choice == "5":
        # Eemalda element kindla indeksiga
        index = int(input("Sisesta indeks, mille järgi element eemaldada: "))
        if 0 <= index < len(my_list):
            removed_element = my_list.pop(index)
            print(f"Eemaldatud element {removed_element}, nimekiri pärast eemaldamist:", my_list)
        else:
            print("Vale indeks.")

    elif choice == "6":
        # Leia esimene element kindla väärtusega
        element = int(input("Sisesta element, mille asukohta otsida: "))
        if element in my_list:
            index = my_list.index(element)
            print(f"Element {element} asub indeksil: {index}")
        else:
            print(f"Element {element} ei ole nimekirjas.")

    elif choice == "7":
        # Arvuta, mitu korda element nimekirjas esineb
        element = int(input("Sisesta element, mille esinemiste arvu otsida: "))
        count = my_list.count(element)
        print(f"Element {element} esineb nimekirjas {count} korda.")

    elif choice == "8":
        # Sorteeri nimekiri
        my_list.sort()
        print("Nimekiri pärast sorteerimist:", my_list)

    elif choice == "9":
        # Pööra nimekiri ümber
        my_list.reverse()
        print("Nimekiri pärast pööramist:", my_list)

    elif choice == "10":
        # Tee nimekirja koopia
        copied_list = my_list.copy()
        print("Koopia nimekirjast:", copied_list)

    elif choice == "11":
        # Kustuta kõik elemendid nimekirjast
        my_list.clear()
        print("Nimekiri on tühjendatud:", my_list)

    elif choice == "0":
        print("Programmist väljumine.")
        break

    else:
        print("Vale valik. Proovi uuesti.")
