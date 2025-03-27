# Vault
Repository med fleksibel kode og funksjoner som er skrevet for å være enkle og lett anvennelige til andre prosjekter. Inneholder også en rekke nyttige og ganske "basic" kommandoer til Raspberry Pi.

# Raspberry pi:
## SSH:
Kjør kommando følgende kommando dersom du er på samme nettverk som Raspberry pi:
  * hostname -I

For å koble deg til med SSH skriv følgende kommando i CMD, powershell, terminal eller lignende:
  * ssh brukernavn@hostname

Dersom Raspberry Pi er på et annet nettverk (og du har gjort port-forwarding på det nettverket), bruk følgende kommando for å koble deg til med SSH:
  *  ssh brukernavn@hostname -p portnummer

Her er brukernavnet det samme som sist, men hostname vil være IP-addressen til ruteren din.

Når du har logget deg på Raspberry pi, kjør alltid føldene kommando:
  * sudo apt update && sudo apt upgrade

## Nyttige MQTT-kommandoer:
### Systemcontrol for MQTT:
Disse kommandoene kan kjøres i Linux CLI for å starte/stoppe/sjekke statusen til MQTT-broker.
  * systemctl status mosquitto.service
  * systemctl start mosquitto.service
  * systemctl stop mosquitto.service
  * systemctl restart mosquitto.service
    
### Subscribe: 
Med denne kommandoen kan du abonnere på en topic (her kalt "testTopic") direkte gjennom terminalen.
  * mosquitto_sub -d -t testTopic

### Publish:
Med denne komandoen kan du sende en payload i form av en string på topic "testTopic" direkte gjennom terminalen. 
  * mosquitto_pub -d -t testTopic -m "*Insert payload here*"
