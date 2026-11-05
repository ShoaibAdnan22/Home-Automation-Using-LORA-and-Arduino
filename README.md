# Home-Automation-Using-LORA-and-Arduino

An off-grid, low-power telemetry and home automation system built using Arduino Uno microcontrollers and Semtech SX1278 LoRa transceivers operating in the sub-GHz 433 MHz band[cite: 8, 13, 14, 19]. The project demonstrates long-range, decentralized device control and real-time environmental monitoring independent of continuous internet or cellular infrastructure[cite: 8, 9, 26].

---

## Overview

Conventional smart-home architectures rely heavily on local Wi-Fi, Bluetooth, or cellular networks, creating single points of failure in remote, rural, or grid-disconnected environments[cite: 8, 10]. This project implements a dedicated peer-to-peer RF link using LoRa (Long Range) chirp spread spectrum technology to provide resilient transmission over long distances while maintaining low energy consumption[cite: 8, 10, 14].

The system collects environmental sensor telemetry and executes voice-directed or script-driven actuation commands to switch high-voltage AC loads safely via electromechanical relays[cite: 8, 17, 21, 22, 25].

---

Flow Chart:
<img width="850" height="793" alt="image" src="https://github.com/user-attachments/assets/894ad969-dfec-4e32-a4be-3ff4f3de10e8" />

---
## Features

- **Long-Range Sub-GHz Wireless Link:** Utilizes Semtech SX1278 (Ra-02) transceivers operating at 433 MHz via SPI for noise-tolerant packet transmission[cite: 8, 14, 19].
- **Real-Time Environmental Monitoring:** Continuous data acquisition from DHT11 (temperature and humidity) and MQ-135 (air quality/gas index) sensors[cite: 14, 15, 25].
- **Mains AC Load Control:** Actuation of 230V AC home appliances (bulbs, fans) through optoisolated SPDT relay modules[cite: 8, 16, 17].
- **Voice-to-Serial Command Bridge:** Python integration converting speech commands to ASCII packet strings via serial communication at 9600 baud[cite: 21, 22].
- **Zero-Cloud Dependency:** Operates fully off-grid without requiring external cloud gateways, routers, or persistent internet connectivity[cite: 8, 9, 26].

---

## Hardware Components

| Component | Function / Interface |
| :--- | :--- |
| **Arduino Uno R3 (ATmega328P)**[cite: 8, 13] | Primary controller for data acquisition and relay logic[cite: 13, 26] |
| **Semtech SX1278 / Ra-02 LoRa Module**[cite: 8, 14] | 433 MHz wireless transceiver (SPI interface)[cite: 8, 14, 19] |
| **DHT11 Sensor**[cite: 14] | Temperature (0–50°C) and relative humidity (20–90% RH) sensing[cite: 14] |
| **MQ-135 Gas Sensor**[cite: 15] | Air quality and hazardous gas monitoring (Analog voltage)[cite: 15] |
| **5V SPDT Relay Module**[cite: 8, 17] | Optoisolated switching interface for 230V AC electrical loads[cite: 8, 17] |
| **5V / 230V Power Supply**[cite: 8] | System and load excitation[cite: 8] |

---

## Software & Dependencies

- **Arduino IDE:** Embedded C/C++ development with `LoRa.h` and `SPI.h` libraries[cite: 18, 19]
- **Python 3.x:** Control script for host serial interface[cite: 21, 24]
  - `pyserial`[cite: 21]
  - `SpeechRecognition`[cite: 21]
  - `pyttsx3`[cite: 21]

---

## Experimental Results

During validation testing, telemetry data was parsed and logged over the Arduino Serial Monitor at 9600 baud[cite: 25]:
- Ambient temperature consistently stabilized at **~34.10°C**[cite: 25]
- Relative humidity maintained baseline levels at **~50.00% RH**[cite: 25]
- Gas sensor analog indices showed stable baseline ambient readings (**~209** ADC value)[cite: 25]
- Bidirectional command execution for load switching (`LIGHT_ON`, `LIGHT_OFF`, `FAN_ON`, `FAN_OFF`) verified deterministic trigger responses over the wireless link[cite: 20, 22].

<img width="1280" height="588" alt="image" src="https://github.com/user-attachments/assets/5b9d57ce-b3da-4451-93a6-6f4d0a19594c" />
