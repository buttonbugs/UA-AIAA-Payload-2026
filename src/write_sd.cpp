#include <SPI.h>
#include <SD.h>
#include "config.h"

int file_id = 0;
char file_name[13] = "data_000.csv";

void init_sd() {
    Serial.print("Initializing SD card...");
    if (!SD.begin(SD_CARD_CS)) {
        Serial.println("initialization failed!");
        return;
    }
    Serial.println("initialization done.");
    file_size_test(true);
}

void file_size_test(bool file_change = false) {
    File dataFile = SD.open(file_name);
    uint32_t file_size = dataFile.size();
    dataFile.close();                   // Crucial: Always close to save data
    while (file_size >= FILE_SIZE_LIMIT) {      // create another data file when the current file size exceeds FILE_SIZE_LIMIT
        file_change = true;
        file_id++;
        sprintf(file_name, "data_%03d.csv", file_id);

        // Get file size
        File dataFile = SD.open(file_name);
        file_size = dataFile.size();
        dataFile.close();               // Crucial: Always close to save data
    }
    if (file_change) {
        write_column_headers();
    }
    
}

void write_column_headers (){
    File dataFile = SD.open(file_name, FILE_WRITE);
    dataFile.print('"Timestamp (ms)",');
    dataFile.print('"Ozone (PPB)",');
    dataFile.print('"VOC",');
    dataFile.print('"Accelerometer X (milli-g)",');
    dataFile.print('"Accelerometer Y (milli-g)",');
    dataFile.print('"Accelerometer Z (milli-g)",');
    dataFile.print('"Gyroscope X (deg/s)",');
    dataFile.print('"Gyroscope Y (deg/s)",');
    dataFile.print('"Gyroscope Z (deg/s)",');
    dataFile.print('"Magnetometer X (uT)",');
    dataFile.print('"Magnetometer Y (uT)",');
    dataFile.print('"Magnetometer Z (uT)",');
    dataFile.print('"IMU Temperature (C)",');
    dataFile.print('"BME280 Temperature (C)",');
    dataFile.print('"Pressure (Pa)",');
    dataFile.print('"Humidity (%RH)",');
    dataFile.print('"Ultrasonic 1 (us)",');
    dataFile.print('"Ultrasonic 2 (us)",');
    dataFile.print('"Ultrasonic 3 (us)",');
    dataFile.print('\n');
    dataFile.close();               // Crucial: Always close to save data
}

void write_sd() {
    //
}