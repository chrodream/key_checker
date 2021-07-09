# Key Checker

## 概要

・親機(Raspberry Pi)と子機(ESP32)でHTTP通信を行い、各部屋の施錠状況を知ることができます。	
・いつ施錠/解錠されたかがログでわかります。



## 動作環境

・Raspberry Pi
・ESP32 DevkitC 32D/E



## 必要な部品

### 親機 (Raspberry Pi側)

| 品名                                | 個数 |
| ----------------------------------- | ---- |
| Raspberry Pi                        | 1    |
| micro SDカード(32bit版なら32GBまで) | 1    |

### 子機 (ESP32側)

| 品名                                                         | 配置場所       | 個数 (子機1つにつき) |
| ------------------------------------------------------------ | -------------- | -------------------- |
| [ESP32-DevkitC-32](https://akizukidenshi.com/catalog/g/gM-15673/) | U1             | 1                    |
| [0.96inch OLED](https://akizukidenshi.com/catalog/g/gP-12031/) | U2             | 1                    |
| 3mm 電源用 LED (指定なし)                                    | D1             | 1                    |
| [5mm RGB LED](https://www.marutsu.co.jp/pc/i/1356696/)       | D2             | 1                    |
| [30kΩ 半固定抵抗](https://akizukidenshi.com/catalog/g/gP-14907/) | RV1            | 1                    |
| 470Ω チップ抵抗                                              | R1, R2, R3, R4 | 4                    |
| 10kΩ チップ抵抗                                              | R5, R6, R7     | 3                    |
| [マイクロスイッチ](https://akizukidenshi.com/catalog/g/gP-14659/) | SW1            | 1                    |
| [照度センサ](https://akizukidenshi.com/catalog/g/gI-02325/)  | Q1             | 1                    |
| 3ピンピンソケット                                            | J1, J2         | 2                    |
| 3線ジャンパ                                                  |                | 1                    |



## 使用方法

1. Raspberry Piでkey_server.pyをPython3で起動させます。
   例: `python3 ~/key_checker/key_server.py`
2. client_esp.inoをESP32に書き込んでください。
   **注意: このときWi-FiのSSID, パスワード, 部屋番号を書き換えてください。**
3. ESP32を電源に接続すれば自動的に接続され、10秒ごとに状態が更新されます。



## トラブルシューティング

| エラーコード | 対応方法                                                     |
| ------------ | ------------------------------------------------------------ |
| -1           | Raspberry Pi側のIPアドレスが正しくない可能性があります。IPアドレス, サブネットマスク, DNS, HGWのアドレスが正しいか確認してください。 |
| -11          | SSH上で利用せずに直接起動させてください。                    |
| 3桁の番号    | HTTPのレスポンスコードです。                                 |
