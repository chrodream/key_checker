EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:LED D1
U 1 1 60D30F49
P 6350 4100
F 0 "D1" H 6343 4317 50  0000 C CNN
F 1 "White LED" H 6343 4226 50  0000 C CNN
F 2 "LED_THT:LED_D3.0mm" H 6350 4100 50  0001 C CNN
F 3 "~" H 6350 4100 50  0001 C CNN
	1    6350 4100
	-1   0    0    1   
$EndComp
$Comp
L Device:R R1
U 1 1 60D351D4
P 6900 4100
F 0 "R1" H 6970 4146 50  0000 L CNN
F 1 "R" H 6970 4055 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 6830 4100 50  0001 C CNN
F 3 "~" H 6900 4100 50  0001 C CNN
	1    6900 4100
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R2
U 1 1 60D3B902
P 6400 4550
F 0 "R2" H 6470 4596 50  0000 L CNN
F 1 "R" H 6470 4505 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 6330 4550 50  0001 C CNN
F 3 "~" H 6400 4550 50  0001 C CNN
	1    6400 4550
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R3
U 1 1 60D3BA89
P 6400 5050
F 0 "R3" H 6470 5096 50  0000 L CNN
F 1 "R" H 6470 5005 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 6330 5050 50  0001 C CNN
F 3 "~" H 6400 5050 50  0001 C CNN
	1    6400 5050
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R4
U 1 1 60D3BACF
P 6400 4800
F 0 "R4" H 6470 4846 50  0000 L CNN
F 1 "R" H 6470 4755 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 6330 4800 50  0001 C CNN
F 3 "~" H 6400 4800 50  0001 C CNN
	1    6400 4800
	0    -1   -1   0   
$EndComp
Wire Wire Line
	6050 4100 6200 4100
Wire Wire Line
	6500 4100 6750 4100
$Comp
L Device:R R5
U 1 1 60D7AB9A
P 4000 3350
F 0 "R5" H 4070 3396 50  0000 L CNN
F 1 "R" H 4070 3305 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 3930 3350 50  0001 C CNN
F 3 "~" H 4000 3350 50  0001 C CNN
	1    4000 3350
	-1   0    0    1   
$EndComp
Wire Wire Line
	4900 3650 4000 3650
Wire Wire Line
	4000 3500 4000 3650
Wire Wire Line
	3100 4450 3700 4450
Wire Wire Line
	4900 4350 3800 4350
Wire Wire Line
	4000 3200 4500 3200
Wire Wire Line
	4500 3200 4500 4950
Wire Wire Line
	4500 4950 4900 4950
Connection ~ 4000 3200
$Comp
L power:GND #PWR0101
U 1 1 60D85F84
P 3100 4450
F 0 "#PWR0101" H 3100 4200 50  0001 C CNN
F 1 "GND" H 3105 4277 50  0000 C CNN
F 2 "" H 3100 4450 50  0001 C CNN
F 3 "" H 3100 4450 50  0001 C CNN
	1    3100 4450
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 60D87381
P 6350 3150
F 0 "#PWR0102" H 6350 2900 50  0001 C CNN
F 1 "GND" H 6355 2977 50  0000 C CNN
F 2 "" H 6350 3150 50  0001 C CNN
F 3 "" H 6350 3150 50  0001 C CNN
	1    6350 3150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0103
U 1 1 60D879D0
P 6350 3750
F 0 "#PWR0103" H 6350 3500 50  0001 C CNN
F 1 "GND" H 6355 3577 50  0000 C CNN
F 2 "" H 6350 3750 50  0001 C CNN
F 3 "" H 6350 3750 50  0001 C CNN
	1    6350 3750
	1    0    0    -1  
$EndComp
Wire Wire Line
	6350 3150 5900 3150
Wire Wire Line
	5900 3750 6350 3750
Wire Wire Line
	6050 4450 5900 4450
Wire Wire Line
	6050 4100 6050 4450
$Comp
L Device:LED_BRCG D2
U 1 1 60D90AA2
P 6900 4800
F 0 "D2" H 6900 4333 50  0000 C CNN
F 1 "LED_BRCG" H 6900 4424 50  0000 C CNN
F 2 "LED_THT:LED_D5.0mm-4_RGB" H 6900 4750 50  0001 C CNN
F 3 "~" H 6900 4750 50  0001 C CNN
	1    6900 4800
	-1   0    0    1   
$EndComp
Wire Wire Line
	6700 4600 6700 4550
Wire Wire Line
	6700 4550 6550 4550
Wire Wire Line
	6700 4800 6550 4800
Wire Wire Line
	6550 5050 6700 5050
Wire Wire Line
	6700 5050 6700 5000
Wire Wire Line
	6250 4550 6250 4350
Wire Wire Line
	6250 4350 5900 4350
Wire Wire Line
	6250 4800 6150 4800
Wire Wire Line
	6150 4800 6150 4550
Wire Wire Line
	6150 4550 5900 4550
Wire Wire Line
	5900 4650 6050 4650
Wire Wire Line
	6050 4650 6050 5050
Wire Wire Line
	6050 5050 6250 5050
$Comp
L power:GND #PWR0104
U 1 1 60DA0216
P 7300 4900
F 0 "#PWR0104" H 7300 4650 50  0001 C CNN
F 1 "GND" H 7305 4727 50  0000 C CNN
F 2 "" H 7300 4900 50  0001 C CNN
F 3 "" H 7300 4900 50  0001 C CNN
	1    7300 4900
	1    0    0    -1  
$EndComp
Wire Wire Line
	7300 4900 7300 4800
Wire Wire Line
	7300 4100 7050 4100
Wire Wire Line
	7100 4800 7300 4800
Connection ~ 7300 4800
Wire Wire Line
	7300 4800 7300 4100
$Comp
L Device:R_POT RV1
U 1 1 60DA33FC
P 2750 3450
F 0 "RV1" H 2681 3496 50  0000 R CNN
F 1 "R_POT" H 2681 3405 50  0000 R CNN
F 2 "Potentiometer_THT:Potentiometer_ACP_CA6-H2,5_Horizontal" H 2750 3450 50  0001 C CNN
F 3 "~" H 2750 3450 50  0001 C CNN
	1    2750 3450
	1    0    0    -1  
$EndComp
Wire Wire Line
	2750 3300 2750 3200
Wire Wire Line
	2750 3200 4000 3200
NoConn ~ 2750 3600
$Comp
L adafruit:SSD1306 U2
U 1 1 60DCFADD
P 4050 2300
F 0 "U2" H 4278 2313 50  0000 L CNN
F 1 "SSD1306" H 4278 2222 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 4050 2550 50  0001 C CNN
F 3 "" H 4050 2550 50  0001 C CNN
	1    4050 2300
	1    0    0    -1  
$EndComp
Wire Wire Line
	4100 2500 4100 3150
Wire Wire Line
	4100 3150 4300 3150
Wire Wire Line
	4200 2500 4200 2900
Wire Wire Line
	4200 2900 3700 2900
Wire Wire Line
	3700 2900 3700 4450
Connection ~ 3700 4450
Wire Wire Line
	4000 2500 4000 2700
Wire Wire Line
	4700 2700 4700 4150
Wire Wire Line
	4700 4150 4900 4150
Wire Wire Line
	4900 4050 4800 4050
Wire Wire Line
	4800 4050 4800 2800
Wire Wire Line
	3900 2800 3900 2500
$Comp
L Device:R R6
U 1 1 60DD395E
P 4300 3000
F 0 "R6" H 4370 3046 50  0000 L CNN
F 1 "R" H 4370 2955 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 4230 3000 50  0001 C CNN
F 3 "~" H 4300 3000 50  0001 C CNN
	1    4300 3000
	-1   0    0    1   
$EndComp
$Comp
L Device:R R7
U 1 1 60DD4749
P 4600 3000
F 0 "R7" H 4670 3046 50  0000 L CNN
F 1 "R" H 4670 2955 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 4530 3000 50  0001 C CNN
F 3 "~" H 4600 3000 50  0001 C CNN
	1    4600 3000
	-1   0    0    1   
$EndComp
Connection ~ 4300 3150
Wire Wire Line
	4300 2850 4300 2800
Wire Wire Line
	4300 2800 3900 2800
Wire Wire Line
	4000 2700 4600 2700
Wire Wire Line
	4300 3150 4600 3150
Wire Wire Line
	4800 2800 4300 2800
Connection ~ 4300 2800
Connection ~ 4600 3150
Wire Wire Line
	4600 3150 4900 3150
Wire Wire Line
	4600 2850 4600 2700
Connection ~ 4600 2700
Wire Wire Line
	4600 2700 4700 2700
$Comp
L Key_checker-rescue:ESP32-Dev-Module-ESP32-footprints-Shem-Lib U1
U 1 1 60DE68AD
P 5400 3050
F 0 "U1" H 5400 3215 50  0000 C CNN
F 1 "ESP32" H 5400 3124 50  0000 C CNN
F 2 "ESP32:DIP-38_1000_ELL" H 5400 3100 50  0001 C CNN
F 3 "" H 5400 3100 50  0001 C CNN
	1    5400 3050
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_DIP_x01 SW1
U 1 1 60D33FE5
P 1050 5100
F 0 "SW1" H 1050 5367 50  0000 C CNN
F 1 "SW_DIP_x01" H 1050 5276 50  0000 C CNN
F 2 "switch_micro:SS-10GL" H 1050 5100 50  0001 C CNN
F 3 "~" H 1050 5100 50  0001 C CNN
	1    1050 5100
	0    -1   -1   0   
$EndComp
Connection ~ 4000 3650
$Comp
L Device:Q_Photo_NPN Q1
U 1 1 60D33560
P 950 4100
F 0 "Q1" H 1140 4146 50  0000 L CNN
F 1 "Q_Photo_NPN" H 1140 4055 50  0000 L CNN
F 2 "LED_THT:LED_D5.0mm" H 1150 4200 50  0001 C CNN
F 3 "~" H 950 4100 50  0001 C CNN
	1    950  4100
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x03_Male J1
U 1 1 60E05A12
P 3800 5150
F 0 "J1" V 3954 4962 50  0000 R CNN
F 1 "Conn_01x03_Male" V 3863 4962 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Horizontal" H 3800 5150 50  0001 C CNN
F 3 "~" H 3800 5150 50  0001 C CNN
	1    3800 5150
	0    -1   -1   0   
$EndComp
$Comp
L Connector:Conn_01x03_Male J2
U 1 1 60E08B69
P 1700 5650
F 0 "J2" V 1854 5462 50  0000 R CNN
F 1 "Conn_01x03_Male" V 1763 5462 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Horizontal" H 1700 5650 50  0001 C CNN
F 3 "~" H 1700 5650 50  0001 C CNN
	1    1700 5650
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3700 4950 3700 4450
Wire Wire Line
	3700 4450 4900 4450
Wire Wire Line
	3800 4950 3800 4350
Connection ~ 3800 4350
Wire Wire Line
	3900 3650 4000 3650
Wire Wire Line
	3800 3450 3800 4350
Wire Wire Line
	2900 3450 3800 3450
Wire Wire Line
	3900 3650 3900 4950
Wire Wire Line
	1600 5450 1600 5400
Wire Wire Line
	1600 5400 1050 5400
Wire Wire Line
	1600 5400 1600 4300
Wire Wire Line
	1600 4300 1050 4300
Connection ~ 1600 5400
Wire Wire Line
	1050 4800 1800 4800
Wire Wire Line
	1800 4800 1800 5450
Wire Wire Line
	1700 5450 1700 3900
Wire Wire Line
	1700 3900 1050 3900
$Comp
L power:+5V #PWR0105
U 1 1 60E1FADC
P 2750 3200
F 0 "#PWR0105" H 2750 3050 50  0001 C CNN
F 1 "+5V" H 2765 3373 50  0000 C CNN
F 2 "" H 2750 3200 50  0001 C CNN
F 3 "" H 2750 3200 50  0001 C CNN
	1    2750 3200
	1    0    0    -1  
$EndComp
Connection ~ 2750 3200
$Comp
L power:+3V3 #PWR0106
U 1 1 60E20281
P 3300 3150
F 0 "#PWR0106" H 3300 3000 50  0001 C CNN
F 1 "+3V3" H 3315 3323 50  0000 C CNN
F 2 "" H 3300 3150 50  0001 C CNN
F 3 "" H 3300 3150 50  0001 C CNN
	1    3300 3150
	1    0    0    -1  
$EndComp
Wire Wire Line
	3300 3150 4100 3150
Connection ~ 4100 3150
$EndSCHEMATC
