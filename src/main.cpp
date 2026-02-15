#include <Arduino.h>
#include "DFRobot_OzoneSensor.h"
#include "config.h"



DFRobot_OzoneSensor Ozone;
void setup() {
    Serial.begin(9600);
    while(!Ozone.begin(Ozone_IICAddress)) {
        Serial.println("I2c device number error !");
        delay(1000);
    }
    Serial.println("I2c connect success !");
    /*   Set iic mode, active mode or passive mode
        MEASURE_MODE_AUTOMATIC            // active  mode
        MEASURE_MODE_PASSIVE              // passive mode
    */
    Ozone.setModes(MEASURE_MODE_PASSIVE);
}

void loop() {
    /*   Smooth data collection
        COLLECT_NUMBER                    // The collection range is 1-100
    */
    int16_t ozoneConcentration = Ozone.readOzoneData(COLLECT_NUMBER);
    Serial.print("Ozone concentration is ");
    Serial.print(ozoneConcentration);
    Serial.println(" PPB.");
    delay(1000);
}