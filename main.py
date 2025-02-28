import pyperclip
counter = 1

TimesPrint = int(input("Wie oft möchtest du den Text schreiben lassen: "))
Text = str(input("Was möchtest du schreiben: "))
TimesPrint = int(input("How many times would you like to write the text: "))
Text = str(input("What would you like to write: "))

# Hier wird der gesamte Text gespeichert, um ihn später in die Zwischenablage zu kopieren
gesamter_text = ""
# Here, the entire text is stored to be copied to the clipboard later
entire_text = ""

while counter < TimesPrint:
    gesamter_text += Text + "\n"  # Fügt den Text zu gesamter_text hinzu
    entire_text += Text + "\n"  # Adds the text to entire_text
    counter += 1

print(gesamter_text)
print(entire_text)

# Kopiert den gesamten Text in die Zwischenablage
pyperclip.copy(gesamter_text)
# Copies the entire text to the clipboard
pyperclip.copy(entire_text)