#include "ICM_20948.h"

#define AD0_VAL 1      // The value of the last bit of the I2C address (1 for 0x69, 0 for 0x68)
ICM_20948_I2C myICM;   // Create an I2C object

float imu_accX = 1;
float imu_accY = 1;
float imu_accZ = 1;
float imu_gyrX = 1;
float imu_gyrY = 1;
float imu_gyrZ = 1;
float imu_magX = 1;
float imu_magY = 1;
float imu_magZ = 1;
float imu_temp = 1;

void init_imu() {
    myICM.enableDebugging();
    myICM.begin(Wire, AD0_VAL);
    if (myICM.status != ICM_20948_Stat_Ok) {
        Serial.println("IMU Sensor not found!");
    }
    while (!myICM.dataReady()) {
        /* code */
    }
    
}

bool imu_ready() {
    return myICM.dataReady();
}

void read_imu() {
    myICM.getAGMT();
    imu_accX = myICM.accX();    // Accelerometer (accX, accY, accZ): Measured in milli-g's (mg)
    imu_accY = myICM.accY();
    imu_accZ = myICM.accZ();
    imu_gyrX = myICM.gyrX();    // Gyroscope (gyrX, gyrY, gyrZ): Measured in Degrees Per Second (DPS)
    imu_gyrY = myICM.gyrY();
    imu_gyrZ = myICM.gyrZ();
    imu_magX = myICM.magX();    // Magnetometer (magX, magY, magZ): Measured in Microtesla (uT)
    imu_magY = myICM.magY();
    imu_magZ = myICM.magZ();
    imu_temp = myICM.temp();    // Temperature (temp): Measured in Degrees Celsius (°C)
}