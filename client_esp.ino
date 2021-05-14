#include "./src/WiFi.h"
#include "./src/WiFiUdp.h"
const char ssid[] = "WARPSTAR-A358DF"; // SSID
const char pass[] = "9F60114A033FA";   // password
static WiFiUDP wifiUdp;
static const char *raspberryIP = "192.168.0.100";
static const int raspberryPort = 2001; //送信先のポート

static const int seconds = 1000;
static const int minutes = 1000 * 60;

IPAddress remoteIP; // 相手のIPアドレス
int port;

static void WiFi_setup()
{
  static const int kLocalPort = 2000; //自身のポート
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
  }
  wifiUdp.begin(kLocalPort);
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
  char i[64];

  while (1)
  {
    count++;

    //パケットの送信
    wifiUdp.beginPacket(raspberryIP, raspberryPort);
    wifiUdp.printf("ESP32Dev Borad: %d", count);
    wifiUdp.endPacket();

    //パケットの受信
    if (wifiUdp.parsePacket())
    {
      wifiUdp.read(i, 64);
      remoteIP = wifiUdp.remoteIP();
      port = wifiUdp.remotePort();
      Serial.print(remoteIP);
      Serial.print(" / ");
      Serial.print(port);
      Serial.print(" / ");
      Serial.println(i); // UDP通信で来た値を表示
    }

    delay(1 * minutes);
  }
}