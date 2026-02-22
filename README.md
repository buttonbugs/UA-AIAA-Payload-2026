# UA AIAA Payload 2026

This repository includes the payload codes for the [UA AIAA](https://uaaiaa.org/) Rocket Compotition Team.

## Software

**VS Code Extension:** [PlatformIO IDE](https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide)

**Framework:** Arduino

## Hardware

### Pin Configuration

| Protocol | Pin Name | Pin No.|
| - | - | - |
| I²C | SDA | A4 |
| I²C | SCL | A5 |
| SPI | SCK | D13 |
| SPI | MISO | D12 |
| SPI | MOSI | D11 |
| SPI | CS for the SD Card Reader | D10 (or any) |


Reference: [Arduino Nano Every Full Pinout Diagram (Official)](https://content.arduino.cc/assets/Pinout-NANOevery_latest.pdf)

### Electronics

| Electronics | Description | Voltage | Protocol |
| - | - | - | - |
| Microcontroller | [Arduino Nano Every](https://store-usa.arduino.cc/products/nano-every) | 5V | I²C and SPI |
| SD Card Reader | [Adafruit MicroSD Card Breakout ADA254](https://www.amazon.com/Adafruit-MicroSD-Breakout-Board-ADA254/dp/B00NAY2NAI/) | 5V | SPI |
| Ozone Sensor | [DFRobot Gravity: IIC Ozone Sensor V1.0](https://wiki.dfrobot.com/Gravity_IIC_Ozone_Sensor_(0-10ppm)%20SKU_SEN0321) | 3.3V - 5.5V | I²C |
| VOC Sensor | [Waveshare SGP40 VOC Sensor](https://www.waveshare.com/wiki/SGP40_VOC_Sensor#Test_the_codes) | 3.3V or 5V | I²C |
| IMU Sensor | [SparkFun 9DoF IMU Breakout - ICM 20948](https://www.amazon.com/SparkFun-Breakout-ICM-20948-connection-Accelerometer-Magnetometer/dp/B07VNV3WKL/) | 1.95 V - 3.6 V | I²C |
| Pressure/Temp/Humidity Sensor | [Starry GY-BME280 5V](https://www.amazon.com/Starry-Atmospheric-Pressure-Temperature-GY-BME280/dp/B0DRCNNBF3/) | 5V | I²C |