import re

regex = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
#uitleg
# we selecteren terug een geheel dus ^$
# we moeten met groepen () werken om de delen van de datum te onderscheiden
# 0[1-9]  zorgt ervoor dat we dag 0-9 kunnen filtern
# |       betekend of (either)
# [12][0-9]|3[01])    idem filter voor deze (filtern van 10-29 en 30 en 31)
# /       notatie van de slash
# (0[1-9]|1[0-2])  Zelfde systeem voor dit (filteren in groep op getallen van 1-12)
# /       terug een slash voor de data
# \d{4}   definieren van het haartal (4 cijfers)


test_zinnen = [
    "12/08/2023",  # K
    "31/12/2022",  # K
    "32/01/2022",  # NOK
    "01/13/2023",  # NOK
    "05/09/2021",  # K
    "15-08-2020",  # NOK
]

data = []
for string in test_zinnen:
    if re.match(regex, string):
        data.append(string)

print(data)
