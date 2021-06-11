#include <WiFi.h>
#include <HTTPClient.h>
#include <iostream>
#include <cstring>
#include <sstream>

// Configuration
const char ssid[] = "WARPSTAR-A358DF"; // SSID
const char pass[] = "9F60114A033FA";   // Password
const char serverName[] = "http://192.168.0.132:2001/";
static const int room_number = 205;

unsigned long lastTime = 0;
unsigned long timerDelay = 0;
const IPAddress ip_client(192, 168, 0, room_number); // Your IP address
const IPAddress gateway(192, 168, 0, 1);
const IPAddress dns(192, 168, 0, 1);
const IPAddress subnet(255, 255, 255, 0);
static WiFiClient client;

const int key_switch = 5;
const int photo_tr = 12;

const int red_led = 2;
const int yellow_led = 4;
const int white_led = 0;
const int blue_led = 15;

const int RED = 1;
const int YELLOW = 2;
const int led_level_bit = 8;
const int led_freq = 1000;

void error(int code);

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
}

void loop()
{
  //Check Key status and Light status
  std::string key_stat;
  if (digitalRead(key_switch) == 1)
  {
    key_stat = "1";
  }
  else
  {
    key_stat = "0";
  }

  std::string light_stat;
  if (digitalRead(photo_tr) == 1)
  {
    light_stat = "1";
  }
  else
  {
    light_stat = "0";
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
      if (response == "200")
      {
        digitalWrite(blue_led, HIGH);
        delay(200);
        digitalWrite(blue_led, LOW);
      }
      else
      {
        ledcWrite(YELLOW, 255);
        delay(200);
        ledcWrite(YELLOW, 0);
      }
    }
    else
    {
      Serial.print("Error on sending POST: ");
      Serial.println(httpResponseCode);
      error(2);
    }

    http.end(); //Free resources
  }
  else
  {
    Serial.println("Error in WiFi connection");
    error(1);
  }

  delay(10000); //Send a request every 10 seconds
}

void error(int code)
{
  digitalWrite(white_led, LOW);
  int level = 0;
  while (1)
  {
    while (1)
    {
      if (level > 255)
      {
        break;
      }
      ledcWrite(code, level);
      level++;
      delay(3);
    }
    while (1)
    {
      if (level < 0)
      {
        break;
      }
      ledcWrite(code, level);
      level--;
      delay(3);
    }
  }
}