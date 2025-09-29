import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import socket


hostname = socket.gethostname()

topic = "Topic"

# Callback funksjoner

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Vi koblet oss til med kode: {reason_code}")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"Mottat melding på {msg.topic} innhold: {msg.payload.decode('UTF-8')}")

# Oppretter MQTT-klient:

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

# kobler oss til broker
mqttc.connect(hostname, 1883, 60)

# starter loop
mqttc.loop_start()

counter = 0

while 1:
    message = f"Melding nr: {counter}"
    publish.single(topic, message, hostname = hostname)
    print(f"Publiserte folgende melding: {message}")
    counter += 1
    time.sleep(2)