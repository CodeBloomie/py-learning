# List - Lista

list_a = [] # pusta lista
print(list_a)

#################################################################

list_b = ["Ghi", "Jkl"] # lista z dodanymi osobami
print(list_b)

#################################################################

# list_a.pop([0]) # pop - usuwanie z listy ze zwracaniem go (w argumencie - numer indeksu elementu)
# list_a.reverse() # reverse - odwracanie listy (w argumencie - nic)

# print(list_a([0])) # wyświetlenie elementu (w argumencie - numer indeksu elementu)

# list_a.append("Andrzej") # dodawanie do listy (w argumencie - str, bool, float)

# list_a.remove("Kamil") # usuwanie z listy (w argumencie - obiekt do usunięcia [pierwsze wystąpienie wartości])

# list_a.clear() # czyszczenie listy

# list_a.sort(reverse=True) - posortowanie listy w odwrotną stronę

#################################################################

names_list = ["Kamil", "Mateusz", "Rafał", "Andrzej"]
names_list2 = ["Dominik"]
names_list3 = names_list + names_list2

print(names_list3)