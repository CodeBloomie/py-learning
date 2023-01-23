

# Instrukcje warunkowe
# Conditional Statements

# w zależności czy jakiś warunek został spełniony, czy nie

light = input("Jakie jest światło? (red, green, yellow) ")

if light == 'red': # jeżeli światło jest czerwone
    print("Czekaj!")

elif light == 'green':
    print("Jedź!")

elif light == 'yellow': # czy może jest żółte?
    print("Przygotuj się!")

else: # jeżeli jest inne niż czerwone 
    print("Niewłaściwa wartość!")