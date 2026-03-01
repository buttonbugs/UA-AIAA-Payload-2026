#include <Arduino.h>
#include "config.h"
#include "Wire.h"

#include "write_sd.h"

uint8_t voc = 0;

void setup() {
    Wire.begin();       // Important! Initialize the I2C (Inter-Integrated Circuit) communication protocol
    Serial.begin(9600);
    delay(100);
    init_sd();
}

void loop() {
    write_sd();
    delay(1000);
}