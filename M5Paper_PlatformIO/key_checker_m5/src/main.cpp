#include <M5EPD.h>
#include <WiFi.h>

M5EPD_Canvas canvas(&M5.EPD);
// uint32_t getPercent(void);

void setup()
{
    // M5 startup
    M5.begin();
    M5.BatteryADCBegin();
    M5.EPD.SetRotation(90);
    M5.EPD.Clear(true);
    WiFi.begin("Sguest-2g", "Senkou107");

    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }
    Serial.print("Connected!");
    canvas.createCanvas(540, 960);
    canvas.setTextSize(3);
    canvas.drawJpgUrl("https://shinycolors.idolmaster.jp/pc/static/img/download/wallpaper/wp_hokagoclimaxgirls_750x1334.jpg");
    // canvas.drawJpgFile(SD, "/img.jpg"); // read image in SD card
    canvas.pushCanvas(0, 0, UPDATE_MODE_GC16);
    delay(3000);

    // サーバの設定
}

void loop()
{
    // サーバーにデータの要求
    // データを格納
    // EPDで表示
    canvas.drawString("Hello World", 185, 48);
    canvas.drawNumber(M5.getBatteryVoltage(), 200, 100);
    delay(300 * 1000); // wait 5 minutes
}