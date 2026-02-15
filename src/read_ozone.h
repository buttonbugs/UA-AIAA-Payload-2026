#ifndef READ_OZONE
#define READ_OZONE
#include "DFRobot_OzoneSensor.h"
#include "config.h"

DFRobot_OzoneSensor Ozone;
void init_ozone() {
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

int16_t read_ozone() {
    return Ozone.readOzoneData(COLLECT_NUMBER);     // Unit: PPB
}

#endif