# UA AIAA Payload 2026

This repository includes the payload codes for the [UA AIAA](https://uaaiaa.org/) Rocket Competition Team.

## Software

**VS Code Extension:** [PlatformIO IDE](https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide)

**Framework:** Arduino

### Libraries

| Libraries             | Installation                  |
| -                     | -                             |
| DFRobot_OzoneSensor   | [DFRobot Website](https://wiki.dfrobot.com/Gravity_IIC_Ozone_Sensor_(0-10ppm)%20SKU_SEN0321) |
| ICM_20948             | PlatformIO &rarr; Libraries   |
| Adafruit_BME280       | PlatformIO &rarr; Libraries   |
| SD                    | PlatformIO &rarr; Libraries   |
| Adafruit_SGP40        | PlatformIO &rarr; Libraries   |
| WatchDog              | [Arduino Built-In Library](https://docs.arduino.cc/libraries/watchdog/) |

## Hardware

### Pin Configuration

**Pin Configuration for I²C and SPI**

| Pin Name | Pin No.| Protocol |
| - | - | - |
| SDA | A4 | I²C |
| SCL | A5 | I²C |
| CLK / SCK | D13 | SPI |
| DO / MISO | D12 | SPI |
| DI / MOSI | D11 | SPI |
| CS for the SD Card Reader | D10 (or any) | SPI |

**Pin Configuration for Ultrasonic Sensor**

| Sensor | Trigger Pin | Echo Pin |
| - | - | - |
| Ultrasonic Sensor 1 | D2 | D3 |
| Ultrasonic Sensor 2 | D4 | D5 |
| Ultrasonic Sensor 3 | D6 | D7 |

**Other Pin Configuration**

| Sensor | Signal Pin |
| - | - |
| SW-18010P | A6 |

Reference: [Arduino Nano Every Full Pinout Diagram (Official)](https://content.arduino.cc/assets/Pinout-NANOevery_latest.pdf)

### Electronics

| Electronics | Description | Voltage | Protocol | On PCB |
| - | - | - | - | - |
| Microcontroller | [Arduino Nano Every](https://store-usa.arduino.cc/products/nano-every) | 5V | - | Y |
| SD Card Reader | [Adafruit MicroSD Card Breakout ADA254](https://www.amazon.com/Adafruit-MicroSD-Breakout-Board-ADA254/dp/B00NAY2NAI/) | 5V | SPI | Y |
| Ozone Sensor | [DFRobot Gravity: IIC Ozone Sensor V1.0](https://wiki.dfrobot.com/Gravity_IIC_Ozone_Sensor_(0-10ppm)%20SKU_SEN0321) | 3.3V - 5.5V | I²C | N |
| VOC Sensor | [Waveshare SGP40 VOC Sensor](https://www.waveshare.com/wiki/SGP40_VOC_Sensor#Test_the_codes) | 3.3V or 5V | I²C | N |
| IMU Sensor | [SparkFun 9DoF IMU Breakout - ICM 20948](https://www.amazon.com/SparkFun-Breakout-ICM-20948-connection-Accelerometer-Magnetometer/dp/B07VNV3WKL/) | 1.95 V - 3.6 V | I²C | Y |
| BME280 Sensor | [Starry GY-BME280 5V](https://www.amazon.com/Starry-Atmospheric-Pressure-Temperature-GY-BME280/dp/B0DRCNNBF3/) | 5V | I²C | Y |
| Ultrasonic Sensor | HC-SR04 | 5V | N/A | N |
| Vibration Sensor | [SW-18020P](https://www.adafruit.com/product/2384) | &le; 12V | N/A | N |

## PCB

### PCB resources

Arduino footprints and symbols: [Alarm-Siren/arduino-kicad-library](https://github.com/Alarm-Siren/arduino-kicad-library)

PCB manufacturer: [JLCPCB](https://jlcpcb.com/)

### How to generate Gerber and Drill files in KiCAD 9

See https://jlcpcb.com/help/article/how-to-generate-gerber-and-drill-files-in-kicad-9

## TODO:

- [ ] Vibration sensor test using `attachInterrupt()` (see [Teensy-Independent](https://github.com/buttonbugs/Teensy-Independent/blob/main/src/receiver.h#L62-L65))
- [ ] Add watchdog
    - [ ] GitHub Repo: https://docs.arduino.cc/libraries/watchdog/
