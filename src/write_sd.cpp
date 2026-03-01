#include <SPI.h>
#include <SD.h>
#include "config.h"

#include "read_ozone.h"
#include "read_sgp40.h"
#include "read_imu.h"
#include "read_bme280.h"
#include "read_ultrasonic.h"

File dataFile;

int file_id = 0;
char file_name[13] = "data_000.csv";

void init_sensors() {
    Serial.print("Initializing Sensors...");
    init_ozone();
    init_sgp40();
    init_imu();
    init_bme280();
    init_ultrasonic(ULTRASONIC_1_TRIG, ULTRASONIC_1_ECHO);
    init_ultrasonic(ULTRASONIC_2_TRIG, ULTRASONIC_2_ECHO);
    init_ultrasonic(ULTRASONIC_3_TRIG, ULTRASONIC_3_ECHO);
}

void write_column_headers(){
    dataFile = SD.open(file_name, FILE_WRITE);
    if (dataFile) {
        dataFile.print("\"Timestamp (ms)\",");
        dataFile.print("\"Ozone (PPB)\",");
        dataFile.print("\"Air quality (VOC)\",");
        dataFile.print("\"Accelerometer X (milli-g)\",");
        dataFile.print("\"Accelerometer Y (milli-g)\",");
        dataFile.print("\"Accelerometer Z (milli-g)\",");
        dataFile.print("\"Gyroscope X (deg/s)\",");
        dataFile.print("\"Gyroscope Y (deg/s)\",");
        dataFile.print("\"Gyroscope Z (deg/s)\",");
        dataFile.print("\"Magnetometer X (uT)\",");
        dataFile.print("\"Magnetometer Y (uT)\",");
        dataFile.print("\"Magnetometer Z (uT)\",");
        dataFile.print("\"IMU Temperature (C)\",");
        dataFile.print("\"BME280 Temperature (C)\",");
        dataFile.print("\"Pressure (Pa)\",");
        dataFile.print("\"Humidity (%RH)\",");
        dataFile.print("\"Ultrasonic 1 (us)\",");
        dataFile.print("\"Ultrasonic 2 (us)\",");
        dataFile.print("\"Ultrasonic 3 (us)\",");
        dataFile.print("\n");
        dataFile.close();               // Crucial: Always close to save data
        Serial.println("CSV File Column Headers Added");
    } else {
        Serial.println("Unable to add column headers");
    }
}

void file_size_test(bool add_column_headers) {
    uint32_t file_size = 0;
    dataFile = SD.open(file_name, FILE_WRITE);
    if (dataFile) {
        file_size = dataFile.size();
        dataFile.close();                   // Crucial: Always close to save data
    } else {
        Serial.print("file_size_test() failed.");
        return;
    }
    while (file_size >= FILE_SIZE_LIMIT) {      // create another data file when the current file size exceeds FILE_SIZE_LIMIT
        add_column_headers = true;
        file_id++;
        sprintf(file_name, "data_%03d.csv", file_id);

        // Get file size
        dataFile = SD.open(file_name, FILE_WRITE);
        if (dataFile) {
            file_size = dataFile.size();
            dataFile.close();               // Crucial: Always close to save data
        }
    }
    if (add_column_headers) {
        write_column_headers();
    }
    
}

void init_sd() {
    init_sensors();
    Serial.print("Initializing SD card...");
    if (!SD.begin(SD_CARD_CS)) {
        Serial.println("initialization failed!");
        return;
    }
    file_size_test(true);
    Serial.println("initialization done.");
}

void write_sd_E(float data) {
    char sciBuffer[E_DECIMAL_PLACE + 6];                    // Buffer to hold the converted scientific notation text
    dtostre(data, sciBuffer, E_DECIMAL_PLACE, 'E');         // Convert data to scientific notation with 6 decimal places
    dataFile.print(sciBuffer);          // Writes "1.23E+02" to the file
    dataFile.print(",");
}

void write_sd() {
    file_size_test(false);
    dataFile = SD.open(file_name, FILE_WRITE);
    if (dataFile) {
        Serial.println("Start writing file");
        
        // Timestamps
        dataFile.print(millis());
        dataFile.print(",");
        
        // Ozone
        dataFile.print(read_ozone());
        dataFile.print(",");
        
        // Air quality (VOC)
        dataFile.print(read_sgp40());
        dataFile.print(",");
        
        // IMU
        read_imu();
        write_sd_E(imu_accX);
        write_sd_E(imu_accY);
        write_sd_E(imu_accZ);
        write_sd_E(imu_gyrX);
        write_sd_E(imu_gyrY);
        write_sd_E(imu_gyrZ);
        write_sd_E(imu_magX);
        write_sd_E(imu_magY);
        write_sd_E(imu_magZ);
        write_sd_E(imu_temp);
        
        // BME280
        read_bme280();
        write_sd_E(bme_temp);
        write_sd_E(bme_pressure);
        write_sd_E(bme_humidity);
        
        // Ultrasonic Sensor
        /* 
        write_sd_E(read_ultrasonic(ULTRASONIC_1_TRIG, ULTRASONIC_1_ECHO));
        write_sd_E(read_ultrasonic(ULTRASONIC_2_TRIG, ULTRASONIC_2_ECHO));
        write_sd_E(read_ultrasonic(ULTRASONIC_3_TRIG, ULTRASONIC_3_ECHO));
        */

        // New line
        dataFile.print("\n");
        dataFile.close();               // Crucial: Always close to save data
        Serial.println("Finish writing file");
    } else {
        Serial.println("Unable to open the file");
    }
}