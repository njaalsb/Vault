import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

# MQTT Broker adresse
hostname = "127.0.0.1"
topic = "Topic"

# Callback ved vellykket tilkobling
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe(topic)

# Callback for mottatte meldinger
def on_message(client, userdata, msg):
    print(f"Mottatt melding: {msg.topic} -> {msg.payload.decode('utf-8')}")

# Opprett MQTT-klient
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

# Koble til broker
mqttc.connect(hostname, 1883, 60)

# Start en tråd for meldingshåndtering
mqttc.loop_start()

# Publiser meldinger hvert 2. sekund
counter = 0
while True:
    message = f"Melding nr: {counter}"
    publish.single(topic, message, hostname=hostname)
    print(f"Publisert: {message}")
    counter += 1
    time.sleep(2)
