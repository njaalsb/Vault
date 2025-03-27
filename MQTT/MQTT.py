import paho.mqtt.client as mqtt
import time
import socket


# Hostname: MQTT-brokerens IP

hostname = "IP-addressen til brokeren"
topic = "testTopic"

client = socket.gethostbyname()

# Teller:
i = 0

# Callback for tilkobling

def on_connect(client, userdata, flags, reason_code):
    print(f"Koblet seg til broker {hostname} med kode: {reason_code}")
    client.subscribe(topic)

# Callback ved mottatt melding
def on_message(client, userdata, msg):
    decoded_msg = msg.payload.decode('UTF-8')
    print(f"Mottatt melding: {decoded_msg} paa topic {msg.topic}")

# Opprett MQTT-klient

mqttc = mqtt.Client(client_id="Brukernavn", clean_session=True, userdata=None)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

# Publiseringsfunksjon

def publisher(payload, topic):
    mqttc.publish(topic, payload)

# Koble til broker

mqttc.connect(hostname, 1883, 60)

publisher(topic,"test_payload")

# Starter en bakgrunnslokke for aa haandtere meldinger

mqttc.loop_forever()

# Send flere meldinger (blir blokkert av loop_forever())

for i in range(100000):
    i += 1
    publisher(f"Melding nr: {i}")
    time.sleep(1)


 