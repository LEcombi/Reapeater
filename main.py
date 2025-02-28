import pyperclip
counter = 1

TimesPrint = int(input("Wie oft möchtest du den Text schreiben lassen: "))
Text = str(input("Was möchtest du schreiben: "))

# Hier wird der gesamte Text gespeichert, um ihn später in die Zwischenablage zu kopieren
gesamter_text = ""

while counter < TimesPrint:
    gesamter_text += Text + "\n"  # Fügt den Text zu gesamter_text hinzu
    counter += 1

print(gesamter_text)

# Kopiert den gesamten Text in die Zwischenablage
pyperclip.copy(gesamter_text)
