#include <WiFi.h>

// Config
const char ssid[] = "WARPSTAR-A358DF"; // SSID
const char pass[] = "9F60114A033FA";   // Password
static const int room_number = 205;

const IPAddress ip_client(192, 168, 0, room_number); // Your IP address
const IPAddress ip_server(192, 168, 0, 132);         // Server's address
const IPAddress gateway(192, 168, 0, 1);
const IPAddress dns(192, 168, 0, 1);
const IPAddress subnet(255, 255, 255, 0);
static WiFiClient client;

static const int seconds = 1000;
static const int minutes = 1000 * 60;

void setup()
{
  Serial.begin(115200);
  WiFi.config(ip_client, gateway, subnet, dns); // Set static IP
  WiFi.begin(ssid, pass);                       // Connect to server
  Serial.printf("\n");
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(500);
  }
  Serial.printf("\n");
  Serial.println("WiFi Connected");

  client.connect(ip_server, 10205); // Select and connect Server's IP and port number
}

void loop()
{
  // Check Status
  int key_stat, light_stat, check_digit;
  if (1)
  {
    key_stat = 1;
  }
  else
  {
    key_stat = 0;
  }
  if (2)
  {
    light_stat = 1;
  }
  else
  {
    light_stat = 0;
  }
  check_digit = (room_number * 1000 + key_stat * 100 + light_stat * 10) % 10;
  int value = room_number * 1000 + key_stat * 100 + light_stat * 10 + check_digit;
  Serial.println(value);
  if (client.connected() == true)
  {
    client.write("1234123412341234");
  }

  delay(1 * seconds);
}