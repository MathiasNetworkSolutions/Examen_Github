import re
regex = r'^[A-Z].+\.$'
tekst = [
    "Dit is een correcte test zin.", # K
    "Dit is geen correcte zin",      # NOK
    "dit helaas ook niet.",          # NOK
    "Ooh dit wel."                   # K
]

# Lijst om de matches in op te slaan aangezien ik meerdere zinnen heb
data = []


for string in tekst:
    if re.match(regex, string):
        data.append(string)

print(data)
