from random import *
print("Loendite t��tamine:")

list1 = [1, 2, 3, 4, 5]
print(f"Algne loend: {list1}")

list1.append(6)
print(f"P�rast append(6): {list1}")

list1.insert(2, 99)
print(f"P�rast insert(2, 99): {list1}")

list1.remove(99)
print(f"P�rast remove(99): {list1}")

popped_element = list1.pop(3)
print(f"P�rast pop(3) - eemaldatud element {popped_element}: {list1}")

index_of_3 = list1.index(3)
print(f"Esimese 3 esinemise indeks: {index_of_3}")

count_of_2 = list1.count(2)
print(f"2 esinemiste arv: {count_of_2}")

list1.sort()
print(f"P�rast sort(): {list1}")

list1.reverse()
print(f"P�rast reverse(): {list1}")

list2 = list1.copy()
print(f"Loendi list2 koopia: {list2}")

list1.clear()
print(f"P�rast clear(): {list1}")

print("\nStringidega t��tamine:")

string = "hello, world!"
print(f"Algne string: {string}")

list_from_string = string.split(", ")
print(f"P�rast split(', '): {list_from_string}")

joined_string = ", ".join(list_from_string)
print(f"P�rast join(', '): {joined_string}")

new_string = string.replace("world", "Python")
print(f"P�rast replace('world', 'Python'): {new_string}")

upper_string = string.upper()
print(f"P�rast upper(): {upper_string}")

lower_string = string.lower()
print(f"P�rast lower(): {lower_string}")

substring = string[7:12]
print(f"Alamstring alates 7. kuni 12. t�heni: {substring}")

