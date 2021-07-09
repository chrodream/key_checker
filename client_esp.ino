#include <WiFi.h>
#include <HTTPClient.h>
#include <iostream>
#include <cstring>
#include <sstream>
#include <Wire.h>
#include "SSD1306.h"

// Configuration
const char ssid[] = "Your SSID"; // SSID
const char pass[] = "Your Password";   // Password
const char serverName[] = "http://192.168.0.100:2001/";
static const int room_number = 123;

unsigned long lastTime = 0;
unsigned long timerDelay = 0;
const IPAddress ip_client(192, 168, 0, room_number); // Your IP address
const IPAddress gateway(192, 168, 0, 1);
const IPAddress dns(192, 168, 0, 1);
const IPAddress subnet(255, 255, 255, 0);
static WiFiClient client;

const int key_switch = 35;
const int photo_tr = 12;

const int red_led = 2;    // WiFi cannot connect
const int yellow_led = 4; // Posting error
const int white_led = 0;  // Power LED
const int blue_led = 15;  // Posting data successfully

const int RED = 1;
const int YELLOW = 2;
const int led_level_bit = 8;
const int led_freq = 1000;

SSD1306 display(0x3c, 26, 27);

void error(int code); // When ESP occurred errors

void setup()
{
  // Setting input pin
  pinMode(key_switch, INPUT);
  pinMode(photo_tr, INPUT);
  pinMode(red_led, OUTPUT);
  pinMode(yellow_led, OUTPUT);
  pinMode(white_led, OUTPUT);
  digitalWrite(white_led, HIGH);
  digitalWrite(blue_led, LOW);
  ledcSetup(RED, led_freq, led_level_bit);
  ledcSetup(YELLOW, led_freq, led_level_bit);
  ledcAttachPin(red_led, RED);
  ledcAttachPin(yellow_led, YELLOW);

  // Starting Wi-Fi
  Serial.begin(115200);
  WiFi.config(ip_client, gateway, subnet, dns); // Set static IP
  WiFi.begin(ssid, pass);                       // Connect to server
  Serial.print("Connecting");
  int count = 0;
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(500);
    count++;
    if (count >= 20) // if ESP cannot connect for 10 sec.
    {
      error(1);
    }
  }
  Serial.print("\n");
  Serial.println("WiFi Connected");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  display.init();
  display.setFont(ArialMT_Plain_10);
  display.drawString(0, 0, "Connected");
  display.drawString(0, 10, WiFi.localIP().toString());
  display.setFont(ArialMT_Plain_24);
  display.drawString(0, 20, "Room");
  display.drawString(70, 20, (String)room_number);
  display.display();
}

void loop()
{
  std::string key_stat;
  std::string light_stat;
  //Check Key status and Light status
  for (int loop_count = 0; loop_count < 100; loop_count++)
  {
    display.clear();
    display.setFont(ArialMT_Plain_16);
    if (digitalRead(key_switch) == HIGH && digitalRead(photo_tr) == HIGH)
    {
      key_stat = "0";
      light_stat = "1";
      display.drawString(0, 45, "Key");
      display.drawString(64, 45, "Light");
    }
    else if (digitalRead(key_switch) == HIGH && digitalRead(photo_tr) == LOW)
    {
      key_stat = "0";
      light_stat = "0";
      display.drawString(0, 45, "Key");
    }
    else if (digitalRead(key_switch) == LOW && digitalRead(photo_tr) == HIGH)
    {
      key_stat = "1";
      light_stat = "1";
      display.drawString(64, 45, "Light");
    }
    else
    {
      key_stat = "1";
      light_stat = "0";
    }

    display.setFont(ArialMT_Plain_10);
    display.drawString(0, 0, "Connected");
    display.drawString(0, 10, WiFi.localIP().toString());
    display.setFont(ArialMT_Plain_24);
    display.drawString(0, 20, "Room");
    display.drawString(70, 20, (String)room_number);
    display.display();
    delay(100);
  }
  // make send text
  std::ostringstream room_number_ostring;
  room_number_ostring << room_number;
  std::string send_std_string = "room_num=";
  send_std_string.append(room_number_ostring.str());
  send_std_string.append("&key_stat=");
  send_std_string.append(key_stat);
  send_std_string.append("&light_stat=");
  send_std_string.append(light_stat);
  // convert from std::string to char arry
  int send_std_string_count = send_std_string.length();
  char sendtext[send_std_string_count + 1];
  strcpy(sendtext, send_std_string.c_str());
  Serial.println(sendtext);

  // Send data to Server over Wi-Fi
  if (WiFi.status() == WL_CONNECTED) // Check WiFi connection status
  {
    HTTPClient http;

    http.begin(serverName);                                              //Specify destination for HTTP request
    http.addHeader("Content-Type", "application/x-www-form-urlencoded"); //Specify content-type header

    int httpResponseCode = http.POST(sendtext); //Send the actual POST request

    if (httpResponseCode > 0)
    {
      String response = http.getString(); //Get the response to the request
      Serial.println(httpResponseCode);   //Print return code
      Serial.println(response);           //Print request answer
      if (httpResponseCode >= 100 && httpResponseCode <= 299)
      {
        digitalWrite(blue_led, HIGH);
        delay(200);
        digitalWrite(blue_led, LOW);
      }
      else
      {
        error(httpResponseCode);
      }
    }
    else
    {
      Serial.print("Error on sending POST: ");
      Serial.println(httpResponseCode);
      error(httpResponseCode);
    }
    http.end(); //Free resources
  }
  else
  {
    Serial.println("Error in WiFi connection");
    error(1);
  }
}

void error(int code)
{
  digitalWrite(white_led, LOW);
  display.clear();
  display.setFont(ArialMT_Plain_16);
  int rep, lap = 0;
  if (code >= 100)
  {
    rep = code;
    code = 2;
  }
  int level = 0;
  while (1)
  {
    lap++;
    while (1)
    {
      if (level > 250)
      {
        level = 250;
        break;
      }
      ledcWrite(code, level);
      level++;
      display.drawString(0, 0, "Error code");
      display.drawString(80, 0, (String)code);
      if (code == 1)
      {
        display.drawString(0, 20, "No Wi-Fi");
        display.drawString(0, 40, "connection");
      }
      else if (code == 2)
      {
        display.drawString(0, 20, "Reqest Error");
        display.drawString(0, 40, "Code: ");
        display.drawString(50, 40, (String)rep);
      }
      else if (code == -1)
      {
        display.drawString(0, 20, "No Reply");
        display.drawString(0, 40, "from server");
      }
      else
      {
        display.drawString(0, 20, "Unknown Error");
      }
      display.display();
      delay(3);
    }

    display.clear();
    while (1)
    {
      if (level < 0)
      {
        level = 0;
        break;
      }
      ledcWrite(code, level);
      level--;
      display.drawString(0, 0, "Error code");
      display.drawString(80, 0, (String)code);
      display.display();
      delay(3);
    }
    display.clear();

    if (lap >= 5)
    {
      display.setFont(ArialMT_Plain_16);
      display.drawString(0, 0, "Retrying");
      display.display();
      for (int i = 60; i <= 90; i = i + 5)
      {
        display.drawString(i, 0, ".");
        display.display();
        delay(500);
      }
      ESP.restart(); // Reboot ESP32
    }
  }
}