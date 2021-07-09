# Key Checker

## Overview

​	・Know the lock status of each room by HTTP communication between the primary device(Raspberry Pi) and the secondary device(ESP32).
​	・See in the log when the door was locked or unlocked.



## Environment

​	・Raspberry Pi
​	・ESP32 Devkit-C 32D/E



## Parts list

### Primary (Raspberry Pi)

| Products                                         | Quantity |
| ------------------------------------------------ | -------- |
| Raspberry Pi                                     | 1        |
| micro SD Card(Limit to 32GB if you use 32bit OS) | 1        |

### Secondary (ESP32)

| Products                                                     | KiCAD assign   | Quantity (per each) |
| ------------------------------------------------------------ | -------------- | ------------------- |
| [ESP32-DevkitC-32](https://akizukidenshi.com/catalog/g/gM-15673/) | U1             | 1                   |
| [0.96inch OLED](https://akizukidenshi.com/catalog/g/gP-12031/) | U2             | 1                   |
| 3mm Power LED (No specification)                             | D1             | 1                   |
| [5mm RGB LED](https://www.marutsu.co.jp/pc/i/1356696/)       | D2             | 1                   |
| [30kΩ Semi-fixed resistance](https://akizukidenshi.com/catalog/g/gP-14907/) | RV1            | 1                   |
| 470Ω Chip-resistor                                           | R1, R2, R3, R4 | 4                   |
| 10kΩ Chip-resistor                                           | R5, R6, R7     | 3                   |
| [Micro switch](https://akizukidenshi.com/catalog/g/gP-14659/) | SW1            | 1                   |
| [Illumination sensor ](https://akizukidenshi.com/catalog/g/gI-02325/) | Q1             | 1                   |
| 3-Pin socket                                                 | J1, J2         | 2                   |
| 3-line wire                                                  |                | 1                   |



## Usage

1. Launch key_server.py on Raspberry Pi 
   e.g. `python3 ~/key_checker/key_server.py`
2. upload client_esp.ino to ESP32.
   **Notice: Please change Wi-Fi's SSID, Password and Room number.**
3. Sends a HTTP data per 10 seconds when ESP is connected to Power supply.



## Trouble-shooting

| Error Code      | Response method                                              |
| --------------- | ------------------------------------------------------------ |
| -1              | Maybe Network configuration is wrong. Please check IP-address, Subnet mask, DNS and Home Gate Way's address are correct. |
| -11             | Please do not launch on SSH.                                 |
| 3-digits number | It's HTTP response code.                                     |