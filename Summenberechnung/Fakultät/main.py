"""Berechnung der Fakultät"""

i = int(input("Eingabe:"))
f = 1
for a in range(1, (i+1)):
    f = f * a

print("Die Fakultät ist:", f)
