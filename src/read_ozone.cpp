#include "DFRobot_OzoneSensor.h"

#define OZONE_COLLECT_NUMBER   20                // collect number, the collection range is 1-100
#define Ozone_IICAddress OZONE_ADDRESS_3
/*   iic slave Address, The default is ADDRESS_3
       ADDRESS_0               0x70              // iic device address
       ADDRESS_1               0x71
       ADDRESS_2               0x72
       ADDRESS_3               0x73
*/

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
    return Ozone.readOzoneData(OZONE_COLLECT_NUMBER);     // Unit: PPB
}
