#include <Arduino.h>
#include "config.h"
#include "Wire.h"

#include "read_ozone.h"
#include "read_sgp40.h"
#include "read_imu.h"
#include "read_bme280.h"

uint8_t voc = 0;

void setup() {
    Wire.begin();       // Important! Initialize the I2C (Inter-Integrated Circuit) communication protocol
    delay(2000);
    Serial.begin(9600);
    init_bme280();
}

void loop() {
    Serial.print("IMU:");
    Serial.print(" Check");
    read_bme280();
    Serial.println(bme_temp, 15);
    delay(500);
}