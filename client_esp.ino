#include <WiFi.h>
#include <WiFiUdp.h>

// Config
const char ssid[] = "WARPSTAR-A358DF"; // SSID
const char pass[] = "9F60114A033FA";   // password
static const int room_number = 205;32


static WiFiUDP wifiUdp;
//ESP32 -> RPi(192.168.0.100 :2001)
static const char *raspberryIP = "192.168.0.100"; // Raspberry Pi's IP
static const int raspberryPort = 2001;            // Raspberry Pi's port

static const int seconds = 1000;
static const int minutes = 1000 * 60;

IPAddress remoteIP; // 相手のIPアドレス
int port;

static void WiFi_setup()
{
  //RPi -> ESP32(DHCP:2002)
  static const int esp32_port = 2002; //ESP's port
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
  }
  wifiUdp.begin(esp32_port);
}

static void Serial_setup()
{
  Serial.begin(115200);
  Serial.println(""); // to separate line
}

void setup()
{
  Serial_setup();
  WiFi_setup();
}

void loop()
{
  int count = 0;
  char rpi_input[32];
  char key_stat[32];

  while (1)
  {
    count++;

    //send packets
    wifiUdp.beginPacket(raspberryIP, raspberryPort);
    wifiUdp.printf("ESP32Dev Borad: %d", count); // send string
    wifiUdp.endPacket();

    //recieve packets
    if (wifiUdp.parsePacket())
    {
      wifiUdp.read(rpi_input, 32);
      remoteIP = wifiUdp.remoteIP();
      port = wifiUdp.remotePort();
      Serial.print(remoteIP);
      Serial.print(" / ");
      Serial.print(port);
      Serial.print(" / ");
      Serial.println(rpi_input); // UDP通信で来た値を表示
    }
    delay(1 * seconds);
  }
}