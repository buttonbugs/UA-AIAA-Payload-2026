#include <Arduino.h>
#include "config.h"

void init_ultrasonic(int trigPin, int echoPin) {
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
}

float read_ultrasonic(int trigPin, int echoPin) {
    // 1. Clear the trigPin by setting it LOW
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);

    // 2. Trigger the sensor by setting trigPin HIGH for 10 microseconds
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    // 3. Read the echoPin; pulseIn returns the travel time in microseconds
    return pulseIn(echoPin, HIGH, ULTRASONIC_TIMEOUT) / 1000000.0F;
}