# Vault
Repository med fleksibel kode og funksjoner som er skrevet for å være enkle og lett anvennelige til andre prosjekter. 

### Nyttige MQTT-kommandoer:
Systemcontrol for MQTT:
    * systemctl status mosquitto.service
    * systemctl start mosquitto.service
    * systemctl stop mosquitto.service
    * systemctl restart mosquitto.service
    
Subscribe: 
    * mosquitto_sub -d -t testTopic

Publish:
    * mosquitto_pub -d -t testTopic -m "*Insert payload here*"
