#include <Arduino.h>
#include "config.h"
#include "Wire.h"

#include "write_sd.h"
#include "read_vibration.h"

uint8_t voc = 0;

void setup() {
    Wire.begin();       // Important! Initialize the I2C (Inter-Integrated Circuit) communication protocol
    Serial.begin(9600);
    delay(100);
    // init_sd();
    init_vibration_sensor();
}

void loop() {
    // write_sd();
    delay(SAMPLE_ECHOTERVAL);
    check_vibration_timeout();
    Serial.print(vibration_period_1_ms);
    Serial.println(vibration_period_2_ms);
}