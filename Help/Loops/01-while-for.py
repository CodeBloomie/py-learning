

# Pętla WHILE to pętla która wykonuje się gdy zdefiniowany jest przez nas warunek

number1 = 1

while number1 < 2: # podczas gdy zmienna number jest mniejsza od 2, coś tam coś tam
    number1 += 1
    print(number1)


# pętla FOR wykonuje się zdefiniowaną przez nas ilość razy
for number2 in range(1, 6): # można podać KROK, jako trzeci argument, co ILE
    if number2 == 5:
        break # złamanie pętli
    print(number2)

for number2 in range(1, 6): # można podać KROK, jako trzeci argument, co ILE
    if number2 == 5:
        continue # przerywa działanie pętli przy if, i kontynuuje
    print(number2)