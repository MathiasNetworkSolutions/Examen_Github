import re

regex = r'^[1-9][0-9]{2}$'
#uitleg:
# zien als geheel dus terug ^$ gebruiken
# eerste getal is 1 dus filteren tussen 1-9
# tweede en derde getal mag wel 0 zijn (we aanvaarden dus alles) end it doen we 2 keer (vandaar de {2})


test_zinnen = [
    "123",  # K
    "456",  # K
    "99",   # NOK
    "1000", # NOK
    "005",  # NOK
    "987",  # K
]

data = []
for string in test_zinnen:
    if re.match(regex, string):
        data.append(string)
print(data)
