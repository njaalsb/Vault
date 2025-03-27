# Testscript for publish og subscribe i mqtt

import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
lst = []

# Hostname: Min laptop
hostname = "127.0.0.1"

# Callback for å koble til broker
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe("testTopic")

# Callback ved mottatt melding, dekodes og printes
def on_message(client, userdata, msg):
    lst.append(msg.payload.decode('UTF-8'))
    print(lst[0])
    print(msg.topic+" "+str(msg.payload))

# Eksempel payload
payload1 = u"Hei verden"

# publiseringsfunksjon: 
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
