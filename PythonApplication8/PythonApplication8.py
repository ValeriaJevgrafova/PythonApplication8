from random import *
sõne="Programmeerimine"
print(sõne)
sõne_list=list(sõne)
print(sõne_list)
sõne_list.reverse()
print(sõne_list)
print(sõne_list.index("P"))
print(len(sõne_list))
print(len(sõne))
kogus_m=sõne_list.count("m")
for m in range(kogus_m):
    sõne_list.remove("m")
tähed=randint(1,6)
for i in range(tähed):
    while 1:
        try:
            t=input("Sisesta täht: ")
            if t.isalpha(): break
        except:
            print("On vaja täht!")
    while 1:
        try:
            ind=input("Sisesta index: ")
            if ind.insumeric() & int(ind)<len(sõne_list): break
        except:
            print("Om vaja index!")
    sõne_list.insert(int(ind),t)
print(sõne_list)
def fuktion(e):
    return len(e)
sõne_list.sort(reverse=True, ke=function)
print(sõne_list)