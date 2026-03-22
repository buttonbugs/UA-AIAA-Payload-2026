#include <Arduino.h>
#include "config.h"

int last_millis_1 = 0;
int vibration_period_1_ms = 0;

int last_millis_2 = 0;
int vibration_period_2_ms = 0;

void onchange_1() {
    if (!digitalRead(VIBRATION_SENSOR_1)) {
        vibration_period_1_ms = millis() - last_millis_1;
        last_millis_1 = vibration_period_1_ms;
    }
}

void onchange_2() {
    if (!digitalRead(VIBRATION_SENSOR_1)) {
        vibration_period_2_ms = millis() - last_millis_2;
        last_millis_2 = vibration_period_2_ms;
    }
}

void init_vibration_sensor() {
    // Pin mode
    pinMode(VIBRATION_SENSOR_1, INPUT_PULLUP);
    pinMode(VIBRATION_SENSOR_2, INPUT_PULLUP);

    // Init the millis() last time
    last_millis_1 = millis();
    last_millis_2 = millis();

    // Attach events
    attachInterrupt(VIBRATION_SENSOR_1, onchange_1, CHANGE);
    attachInterrupt(VIBRATION_SENSOR_2, onchange_2, CHANGE);
}