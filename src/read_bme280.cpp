#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

Adafruit_BME280 bme; // I2C by default

float bme_temp = 0;
float bme_pressure = 0;
float bme_humidity = 0;

void init_bme280() {
    Serial.println(F("BME280 test"));

    // Check your sensor's I2C address, could also be 0x77
    if (!bme.begin(0x76)) {
        Serial.println("Could not find a valid BME280 sensor, check wiring!");
    }
    Serial.println("BME280 sensor connected!");
}

void read_bme280() {
    bme_temp = bme.readTemperature();
    bme_pressure = bme.readPressure();
    bme_humidity = bme.readHumidity();
}
