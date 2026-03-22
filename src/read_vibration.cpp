#include <Arduino.h>
#include "config.h"

int last_timeout_millis = 0;

int last_millis_1 = 0;
int vibration_period_1_ms = 0;

int last_millis_2 = 0;
int vibration_period_2_ms = 0;

void onchange_1() {
    if (!digitalRead(VIBRATION_SENSOR_1)) {
        vibration_period_1_ms = millis() - last_millis_1;
        last_millis_1 = millis();
    }
}

void onchange_2() {
    if (!digitalRead(VIBRATION_SENSOR_2)) {
        vibration_period_2_ms = millis() - last_millis_2;
        last_millis_2 = millis();
    }
}

void init_vibration_sensor() {
    // Pin mode
    pinMode(VIBRATION_SENSOR_1, INPUT_PULLUP);
    pinMode(VIBRATION_SENSOR_2, INPUT_PULLUP);

    // Init timeout
    last_timeout_millis = millis();
    
    // Attach events
    last_millis_1 = millis();
    attachInterrupt(VIBRATION_SENSOR_1, onchange_1, CHANGE);
    last_millis_2 = millis();
    attachInterrupt(VIBRATION_SENSOR_2, onchange_2, CHANGE);
}

void check_vibration_timeout() {
    if (millis() - last_timeout_millis > VIBRATION_TIMEOUT_MS) {
        if (vibration_period_1_ms <= last_timeout_millis) {
            vibration_period_1_ms = 0;
            last_millis_1 = millis();
        }
        if (vibration_period_2_ms <= last_timeout_millis) {
            vibration_period_2_ms = 0;
            last_millis_2 = millis();
        }
        last_timeout_millis = millis();
    }
}