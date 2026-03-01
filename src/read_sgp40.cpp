#include <Wire.h>
#include <Adafruit_SGP40.h>
#include "Arduino.h"

Adafruit_SGP40 sgp;

void init_sgp40() {
    if (! sgp.begin()){
        Serial.println("SGP40 Sensor not found");
    }
    
    Serial.println("SGP40 Sensor connected.");
}

int32_t read_sgp40() {
    return sgp.measureVocIndex();
}
