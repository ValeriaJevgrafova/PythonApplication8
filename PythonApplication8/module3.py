#"kivi, k��rid, paber!"

from random import *

# Loob valikute loetelu
valikud = ["kivi", "k��rid", "paber"]

# K�ivitab l�pmatu ts�kli, nii et m�ng j�tkub, kuni m�ngija �tleb 'l�peta'
while True:
    # palub m�ngijal sisestada oma valik
    m�ngija_valik = input("Vali: kivi, k��rid v�i paber (v�i 'l�peta' m�ngu l�petamiseks): ")

    # Kontrollib, kas m�ngija soovib m�ngu l�petada
    if m�ngija_valik == "l�peta":
        print("M�ng l�ppenud")  # Kui jah, v�ljastab l�pliku l�ppseisundi  ja l�petab ts�kli
        break

    # Kui m�ngija valik on kehtetu, palub ta m�ngijal uuesti valida.
    if m�ngija_valik not in valikud:
        print("Vale sisend. Proovi uuesti")  # Vead toovad m�ngija tagasi sisestuse valikusse
        continue

    # Arvuti valib juhuslikult �he valiku
    arvuti_valik = random.choice(valikud)
    print(f"Arvuti valis: {arvuti_valik}")

    # Kontrollib tulemusi ja annab tagasisidet
    if m�ngija_valik == arvuti_valik:
        print("Viik!")
    elif (m�ngija_valik == "kivi" and arvuti_valik == "k��rid") or \
         (m�ngija_valik == "k��rid" and arvuti_valik == "paber") or \
         (m�ngija_valik == "paber" and arvuti_valik == "kivi"):
        print("Sa v�itsid!")
    else:
        print("Sa kaotasid!")


#t��tamine nimekirjade ja stringidega

from random import *

# Algselt on meil nimekiri, millega t��tame
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    print("\nMen��:")
    print("1. Lisa element l�ppu nimekirja (append)")
    print("2. Laienda nimekirja teise nimekirjaga (extend)")
    print("3. Sisesta element nimekirja kindlasse kohta (insert)")
    print("4. Eemalda esimene element, mille v��rtus on m��ratud (remove)")
    print("5. Eemalda element kindla indeksiga (pop)")
    print("6. Leia esimene element kindla v��rtusega (index)")
    print("7. Arvuta, mitu korda element nimekirjas esineb (count)")
    print("8. Sorteeri nimekiri (sort)")
    print("9. P��ra nimekiri �mber (reverse)")
    print("10. Tee nimekirja koopia (copy)")
    print("11. Kustuta k�ik elemendid nimekirjast (clear)")
    print("0. V�lju programmist")
    
    # K�si kasutajalt, millist tegevust ta soovib teha
    choice = input("Vali tegevuse number: ")

    if choice == "1":
        # Lisa element l�ppu nimekirja
        element = int(input("Sisesta element, mis tuleb lisada: "))
        my_list.append(element)
        print("Nimekiri p�rast lisamist:", my_list)

    elif choice == "2":
        # Laienda nimekirja teise nimekirjaga
        extension_list = list(map(int, input("Sisesta elemendid, mis laiendavad nimekirja (lahutada t�hikutega): ").split()))
        my_list.extend(extension_list)
        print("Nimekiri p�rast laiendamist:", my_list)

    elif choice == "3":
        # Sisesta element kindlasse kohta nimekirjas
        index = int(input("Sisesta indeks, kuhu element tuleb sisestada: "))
        element = int(input("Sisesta element, mis tuleb sisestada: "))
        my_list.insert(index, element)
        print("Nimekiri p�rast sisestamist:", my_list)

    elif choice == "4":
        # Eemalda esimene element, mille v��rtus on m��ratud
        element = int(input("Sisesta element, mis tuleb eemaldada: "))
        if element in my_list:
            my_list.remove(element)
            print("Nimekiri p�rast eemaldamist:", my_list)
        else:
            print(f"Element {element} ei ole nimekirjas.")

    elif choice == "5":
        # Eemalda element kindla indeksiga
        index = int(input("Sisesta indeks, mille j�rgi element eemaldada: "))
        if 0 <= index < len(my_list):
            removed_element = my_list.pop(index)
            print(f"Eemaldatud element {removed_element}, nimekiri p�rast eemaldamist:", my_list)
        else:
            print("Vale indeks.")

    elif choice == "6":
        # Leia esimene element kindla v��rtusega
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
        print("Nimekiri p�rast sorteerimist:", my_list)

    elif choice == "9":
        # P��ra nimekiri �mber
        my_list.reverse()
        print("Nimekiri p�rast p��ramist:", my_list)

    elif choice == "10":
        # Tee nimekirja koopia
        copied_list = my_list.copy()
        print("Koopia nimekirjast:", copied_list)

    elif choice == "11":
        # Kustuta k�ik elemendid nimekirjast
        my_list.clear()
        print("Nimekiri on t�hjendatud:", my_list)

    elif choice == "0":
        print("Programmist v�ljumine.")
        break

    else:
        print("Vale valik. Proovi uuesti.")