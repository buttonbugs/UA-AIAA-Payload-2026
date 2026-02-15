#include <Arduino.h>
#include "config.h"

#include "read_ozone.h"
#include "read_sgp40.h"

uint8_t voc = 0;

void setup() {
    Serial.begin(9600);
    init_sgp40();
}

void loop() {
    /*   Smooth data collection
        COLLECT_NUMBER                    // The collection range is 1-100
    */
    voc = read_sgp40();
    Serial.println(int(voc));
    delay(500);
}