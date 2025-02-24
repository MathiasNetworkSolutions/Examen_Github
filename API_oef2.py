import requests

# Vraag land
land = input("Voer een land in: ").strip().lower()
api_url = f"https://restcountries.com/v3.1/name/{land}"
response = requests.get(api_url)

# Check
if response.status_code == 200:
    data = response.json()
    hoofdstad = data[0]["capital"][0]
    bevolking = data[0]["population"]
    
    print("\nLandinformatie:")
    print(f"Land: {land}")
    print(f"Hoofdstad: {hoofdstad}")
    print(f"Bevolking: {bevolking}")  
    print(f"Officiële taal/talen:")
    talen = data[0]["languages"].values()
    for taal in talen:
        print(f"- {taal}")

else:
    print("FOUT!")
    print(f"Statuscode: {response.status_code}")
