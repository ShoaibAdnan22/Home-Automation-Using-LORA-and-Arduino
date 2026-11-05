#include <SPI.h> #include <LoRa.h> #define LIGHT_PIN 7
#define FAN_PIN 8 void setup() {
Serial.begin(9600); while (!Serial);
LoRa.begin(433E6); // Use correct frequency pinMode(LIGHT_PIN, OUTPUT);
pinMode(FAN_PIN, OUTPUT);
}
void loop() {
int packetSize = LoRa.parsePacket(); if ( packetSize) {
String command = ""; while (LoRa.available()) {
command += (char)LoRa.read();
}
if (command == "LIGHT_ON") { digitalWrite(LIGHT_PIN, HIGH);
} else if (command == "LIGHT_OFF") { digitalWrite(LIGHT_PIN, LOW);
} else if (command == "FAN_ON") { digitalWrite(FAN_PIN, HIGH);
} else if (command == "FAN_OFF") { digitalWrite(FAN_PIN, LOW);
}
}
}
