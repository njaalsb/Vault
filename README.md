# Vault
Repository med fleksibel kode og funksjoner som er skrevet for å være enkle og lett anvennelige til andre prosjekter. 

## Nyttige MQTT-kommandoer:
# Systemcontrol for MQTT:
Disse kommandoene kan kjøres i Linux CLI for å starte/stoppe/sjekke statusen til MQTT-broker.
  * systemctl status mosquitto.service
  * systemctl start mosquitto.service
  * systemctl stop mosquitto.service
  * systemctl restart mosquitto.service
    
# Subscribe: 
Med denne kommandoen kan du abonnere på en topic (her kalt "testTopic") direkte gjennom terminalen.
  * mosquitto_sub -d -t testTopic

# Publish:
Med denne komandoen kan du sende en payload i form av en string på topic "testTopic" direkte gjennom terminalen. 
  * mosquitto_pub -d -t testTopic -m "*Insert payload here*"
