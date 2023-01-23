


# Data Types - typy danych
# String



# STRING - tekstowy
    # 1. 1x cudzysłów - "Zmienna"
    # 2. 1x apostrof - 'Zmienna'
    # 3. 3x cudzysłów - """Zmienna"""


# ! Nowa linia = \n
a = "Linia pierwsza a's\nLinia druga a's"
b = 'Linia pierwsza b\'s\nLinia druga b\'s'
c = """Linia pierwsza c's
linia druga c's"""

print(a)
print(b)
print(c)


name = "rafał"

# funkcja LEN = sprawdzenie długości stringa

print(len(name))

# METODA
# metody wywołujemy po podaniu jej za pomocą zmienna.metoda i ARGUMENTY
# metoda CAPITALIZE, upper, lower - NIE przyjmują argumentów

print(name.capitalize()) # zapoczatkowuje stringa dużą literą
print(name.upper()) # duże litery
print(name.lower()) # małe litery

# podawanie konkretnego znaku w stringu od jakiegoś znaku do jakiegoś znaku
# w tym przypadku podajemy od CZWARTEGO znaku do SZÓSTEGO - zero to pierwszy znak
print(name[3:5])

# w tym przypadku od czwartego znaku do końca
print(name[3:])

abc = "Jak nauczyć się programowania?"

# metoda split = podzielenie stringa na słowa

print(abc.split(" ")) # w argumencie podaliśmy znak, który ma rozdzielać słowa

łączenie_stringu = " "

print(łączenie_stringu.join(['Jak', 'nauczyć', 'się', 'programowania']))

# startswith
# zaczyna się od...

print(abc.startswith("k"))

# endswith
# kończy się na...
print(abc.endswith("?"))