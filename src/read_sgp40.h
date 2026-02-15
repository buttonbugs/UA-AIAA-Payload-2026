#ifndef READ_SGP40
#define READ_SGP40

#include "config.h"
#include "SGP40.h"
#include "Arduino.h"


void init_sgp40() {
    if(SGP40_Init() != 0){
        Serial.println("6");
    }
}

uint8_t read_sgp40() {
    return SGP40_MeasureVOC(25, 50);
}

#endif