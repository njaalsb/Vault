#include <WiFi.h>
#include <PubSubClient.h>


/*
 * Kode for ESP32 som MQTT klient, kun for publisering. Koden er blokkerende, ikke optimalisert, men lesbar og fungerende.
 */

// Wi-Fi detaljer
const char* ssid = "**********";
const char* password = "******";

// MQTT Broker detaljer
const char* mqtt_broker = "127.0.0.1";
const int mqtt_port = 1883; 
const char* mqtt_topic = "test/topic";

// WiFi og MQTT klient
WiFiClient espClient;
PubSubClient client(espClient);

void setupWiFi() {
  delay(10);
  Serial.println("Kobler til WiFi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }

  Serial.println("\nWiFi tilkoblet!");
  Serial.print("IP-adresse: ");
  Serial.println(WiFi.localIP());
}

void reconnectMQTT() {
  while (!client.connected()) {
    Serial.println("Kobler til MQTT-broker...");
    if (client.connect("ESP32Client")) {
      Serial.println("Tilkoblet!");
    } else {
      Serial.print("Feil: ");
      Serial.println(client.state());
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  setupWiFi();

  client.setServer(mqtt_broker, mqtt_port);
}

void loop() {
  if (!client.connected()) {
    reconnectMQTT();
  }
  client.loop();

  static unsigned long lastPublishTime = 0;
  unsigned long currentTime = millis();

  if (currentTime - lastPublishTime >= 5000) { // Hver 5. sekund
    const char* message = "Hei fra ESP32!";
    client.publish(mqtt_topic, message);
    Serial.println("Publisert melding: ");
    Serial.println(message);
    lastPublishTime = currentTime;
  }
}
