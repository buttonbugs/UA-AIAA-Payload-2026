#ifndef READ_ULTRASONIC
#define READ_ULTRASONIC

void init_ultrasonic(int trigPin, int echoPin);
float read_ultrasonic(int trigPin, int echoPin);

#endif