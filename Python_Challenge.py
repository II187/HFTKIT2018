"""My Python_Challenge"""



liste = [1,2,3,4]

for eintrag in liste:
    if eintrag != 2:
        print(eintrag)
print("--------------------------------------------------------------------")

stuff = ["Asien", "Max", 1, "Monika", 2, "China", "Simbabwe", "Antarktis"]
for element in stuff:
    if element in liste:
        print(element)

print("--------------------------------------------------------------------")
count = 0

for i in stuff:
    if i in liste:
        count = count + 1
print(count)    

print("--------------------------------------------------------------------")

x = []

for i in stuff:
    if i in liste:
        x.append(i)
        
print(len(x))    


print("--------------------------------------------------------------------")

chaos =["old price: 40", "new price: 21", "old price: 29", "old price: 50", "new price: 101"]
order = []

for i in chaos:
    
    price = int((i.split(": ")[1]))
    
    if "old" in i:
        if price <= 20:
            price *= 0.8
        elif price <=50:
            price *= 0.6
        else:
            price *= 0.4

    order.append(price)
        
print(order)

print("--------------------------------------------------------------------")



"""Nimm dir Zeit, um die Aufgaben sorgfältig zu bearbeiten. Viel Erfolg! :)
Wenn du mit diesem Übungsblatt fertig bist, kannst du deine Lösung mit der Musterlösung in Textform (Datei: Abschluss Python Grundlagen (Musterloesung)) vergleichen.
Die Video-Musterlösung (in der nächsten Lektion) ist besonders ausführlich gehalten. Wenn du alles richtig gelöst hast, ist es vollkommen okay, wenn du diese Lektion dann überspringst.

1.) Ein automatisierter Trick
a.)
Eine Mathemagierin bittet dich darum, einen ihrer Tricks durch ein kleines Programm zu automatisieren. Der Trick beginnt wie folgt:
Denke dir eine Zahl aus (Variable number).
Multipliziere sie mit 2.
Addiere 10 zum Ergebnis.
Teile das Ergebnis durch 2.
Führe diese Rechnung für die Variable number durch und gebe das Ergebnis aus.
"""

number = 6

result = (number * 2 +10)/2 

print(result) # mit Nachkommastellen
print(int(result)) #ohne Nachkommastellen


""""Du hast 6 ausgewählt, das magische Ergebnis ist 11!"
aus, wobei für die Zahl 6 die Variable number und für die Zahl 11 das Ergebnis (Variable result) eingesetzt werden soll.
Hinweis: In Python darf ein print - Befehl wie folgt über mehrere Zeilen gehen. Das könnte praktisch sein, gerade wenn du viele Strings hintereinander hängen möchtest:
"""
print("Du hast " + 
      str(number) + 
      " ausgewählt, das magische Ergebnis ist " + 
      str(int(result)) + 
      "!")

# Du hast 6 ausgewählt, das magische Ergebnis ist 11!

print("------------------------------------------------------------------------------")

# Vereinfachtes Verzeichnis anlegen wenn man nur die Emailadressen kennt.

# a. ) Ziehe einen Namen aus einer Mailadresse der Form name@service.com
# Wenn die Mailadresse Max-Mustermann@gmail.com lautet, sollst du Max-Mustermann ausgeben; 
# wenn die Mailadresse KlaraKlarnamen@uni-berlin.de heisst, sollst du KlaraKlarnamen ausgeben.
# Hinweis: Schau dir dazu auf jeden Fall nochmal die .split() - Methode an. 
# Damit kannst du z. B. eine E-Mail-Adresse am @ - Symbol zersägen / zerlegen.


mail = "willy.wizard@zauberschule.de"

print(mail.split("@")[0]

# Korrekte Ausgabe:
# willy.wizard



# b.) Ziehe einen Namen aus einer Mailadresse der Form info@name.com
# Manchmal stehen die Namen bei einer Mailadresse auch erst hinter dem @-Zeichen. Gebe auch für solche Fälle die Namen aus; 
# entferne dabei die Endung .com bzw. .de. Du darfst dazu voraussetzen, dass innerhalb des Namens kein Punkt vorkommt. 
# Wenn die Mailadresse also info@Max-Mustermann.com lautet, sollst du Max-Mustermann ausgeben.
# Hinweis: Es ist okay, wenn du fÃ¼r die Berechnung mehere .split() - Befehle benötigst, oder ein Ergebnis zwischenspeichern mÃ¶chtest. 
# Gerne kannst du auch den Code aus der Teilaufgabe a) hier mitverwenden.

# Korrekte Ausgabe:
# helena-hexe

mail = "info@helena-hexe.com"

print(mail.split("@")[1].split(".")[0])
# c.) Berechne: Wie viele Kunden gibt es im Online-Shop?
# Aktuell legen alle Kunden (mail1, mail2, mail3) als separate Variable vor. Wir möchten daraus jetzt eine Liste bauen, sodass wir die Möglichkeit hätten, 
# später noch weitere Kunden in diese Liste hinzuzufÃ¼gen.
# überführe deswegen die Kunden mail1, mail2 und mail3 in die Liste clients und 
# lasse dir anschliessend die Anzahl der Elemente der Liste clients mit Hilfe von Python ausgeben.
# mail1 = "zarah.zauber@zauberberg.de"
# mail2 = "info@trixie-trickser.com"
# mail3 = "uwe_unhold@dunkelnetz.de" 

mail1 = "zarah.zauber@zauberberg.de"
mail2 = "info@trixie-trickser.com"
mail3 = "uwe_unhold@dunkelnetz.de" 

clients = []

clients.append(mail1)
clients.append(mail2)
clients.append(mail3)

print(clients)

# ['zarah.zauber@zauberberg.de', 'info@trixie-trickser.com', 'uwe_unhold@dunkelnetz.de']
# Gebe hier die Anzahl der Elemente der Liste clients aus
print(len(clients))
# Gewünschte Ausgabe:
# 3

# d.) Eine Mailadresse aus Strings zusammenbauen
# Plötzlich fällt der Mathemagierin ein, dass in der Liste clients noch ihr wichtigster Onlineshop-Kunde fehlt. 
# Die Infos zu ihm wurden bei einem misslungenen Trick in zwei Teile zersägt und liegen seitdem in der Liste ["Buehnenzauberer", "magic.com"] herum.
# Rekonstruiere mit Hilfe von Python die Mailadresse des Kunden (da fehlt ein @ zwischen "Buehnenzauberer" und "magic.com") und gebe sie aus, 
# damit sich der Onlineshop-Kundendienst nach seinem Wohlbefinden erkundigen kann.

zauberer = ["Buehnenzauberer", "magic.com"]

print("@".join(zauberer))
