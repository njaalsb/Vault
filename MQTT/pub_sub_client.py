# Testscript for publish og subscribe i mqtt

import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
lst = []

# Hostname: Min laptop
hostname = "172.22.224.1"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("testTopic")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    lst.append(msg.payload.decode('UTF-8'))
    print(lst[0])
    print(msg.topic+" "+str(msg.payload))

# Funksjon for bulisering:
payload1 = u"Hei verden"

def publisher(payload1):
    publish.single("testTopic", payload1, hostname = hostname)
    
    
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

topic = u"testTopic"
payload = u'Hei verden, funker dette?'

# publisher
for i in range(5):
    publisher(payload)
