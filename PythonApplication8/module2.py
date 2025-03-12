from random import *
print("Loendite töötamine:")

list1 = [1, 2, 3, 4, 5]
print(f"Algne loend: {list1}")

list1.append(6)
print(f"Pärast append(6): {list1}")

list1.insert(2, 99)
print(f"Pärast insert(2, 99): {list1}")

list1.remove(99)
print(f"Pärast remove(99): {list1}")

popped_element = list1.pop(3)
print(f"Pärast pop(3) - eemaldatud element {popped_element}: {list1}")

index_of_3 = list1.index(3)
print(f"Esimese 3 esinemise indeks: {index_of_3}")

count_of_2 = list1.count(2)
print(f"2 esinemiste arv: {count_of_2}")

list1.sort()
print(f"Pärast sort(): {list1}")

list1.reverse()
print(f"Pärast reverse(): {list1}")

list2 = list1.copy()
print(f"Loendi list2 koopia: {list2}")

list1.clear()
print(f"Pärast clear(): {list1}")

print("\nStringidega töötamine:")

string = "hello, world!"
print(f"Algne string: {string}")

list_from_string = string.split(", ")
print(f"Pärast split(', '): {list_from_string}")

joined_string = ", ".join(list_from_string)
print(f"Pärast join(', '): {joined_string}")

new_string = string.replace("world", "Python")
print(f"Pärast replace('world', 'Python'): {new_string}")

upper_string = string.upper()
print(f"Pärast upper(): {upper_string}")

lower_string = string.lower()
print(f"Pärast lower(): {lower_string}")

substring = string[7:12]
print(f"Alamstring alates 7. kuni 12. täheni: {substring}")

