import time
import requests
import socket

# Koden henter informasjon om bussposisjoner fra EnTurs API
# Bussposisjoner og annen informasjon kan printes i terminalen
# For Python versjon 3.10.12, men burde fungere for nyere versjoner

# flag brukes her for å velge mellom "moduser"
flag = True

Outbound = []
Inbound = []

# API endpoint
GRAPHQL_ENDPOINT = "https://api.entur.io/realtime/v2/vehicles/graphql"

# Query, informasjonen vi ønsker å hente fra API'et (json format)
query = '''{
  vehicles(codespaceId: "ATB", lineRef: "ATB:Line:2_3") {
    line {
      lineRef
      lineName
    }
    lastUpdated
    location {
      latitude
      longitude
    }
    direction
    originName
    vehicleId
  }
}'''

# Identifikasjon
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'User-Agent': 'Njaal_NTNU' + socket.gethostname(),
    'ET-Client-Name': 'Njaal_NTNU' + socket.gethostname(),
    'ET-Client-ID': socket.gethostname()
}

# Funksjonen som sender query, lagrer resultatet i variabelen response
def sendGraphqlQuery(query):
    data = {'query': query}
    response = requests.post(GRAPHQL_ENDPOINT, json=data, headers=HEADERS)
    return response.json()

# Viss du skal mot moholt må bussen ha origin Hallset
# VIss du skal mot sentrum må bussen ha origin Lovohe

while flag == False:
    vehicleResponse = sendGraphqlQuery(query)
    lengde = len(vehicleResponse['data']['vehicles'])
    for i in range(lengde):
        tempDir = vehicleResponse['data']['vehicles'][i]['direction']
        if tempDir == "Outbound":
            directionId = vehicleResponse['data']['vehicles'][i]
            Outbound.append(directionId['vehicleId'])
        else:
            directionId = vehicleResponse['data']['vehicles'][i]
            Inbound.append(directionId['vehicleId'])
    # Henter input for å avgjøre reting
    # Printer deretter ID'en til bussene på linje 3
    # som går den retningen du skal
    svar = input("Skal du mot moholt?")
    if svar == "ja":
        dir = "Inbound"
        print(f'Du kan velge mellom disse bussene {Inbound}')
    else:
        dir = "Outbound"
        print(f'Du kan velge mellom disse bussene {Outbound}')
    Outbound.clear()
    Inbound.clear()


# Dersom du ønsker å printe responsene fra API'et kan flag setter til True
while flag == True:
    vehicleResponse = sendGraphqlQuery(query)
    # Printer hele responsen:
    print(vehicleResponse['data'])
    time.sleep(1)
    # Printer litt mer spesifikk data
    print(vehicleResponse['data']['vehicles'][0]['originName'])
    print(vehicleResponse['data']['vehicles'][0]['direction'])
    time.sleep(2)  # 2 sek pause
