import requests

#Data uit api halen
api_url = "https://randomuser.me/api/"
# Haal gegevens op
response = requests.get(api_url)


#checken of alles goed is toe gekomen
if response.status_code == 200:
    # JSON-response omzetten naar een Python-woordenboek
    data = response.json()
    # Extract voornaam en achternaam
    # omdat het in "levelzs werkt moeten we dus level per level definieren"
    first_name = data["results"][0]["name"]["first"]
    last_name = data["results"][0]["name"]["last"]
    # Toon de naam
    print(f"Gebruiker: {first_name} {last_name}")
else:
    print("back to work my man, job not done :(")
    print(f"statuscode: {response.status_code}")