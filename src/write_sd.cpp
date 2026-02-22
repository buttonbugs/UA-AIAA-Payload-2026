#include <SPI.h>
#include <SD.h>
#include "config.h"

void init_sd() {
    Serial.print("Initializing SD card...");
    if (!SD.begin(SD_CARD_CS)) {
        Serial.println("initialization failed!");
        return;
    }
    Serial.println("initialization done.");

    // Open the file. FILE_WRITE appends data if the file already exists.
    File dataFile = SD.open("data.txt", FILE_WRITE);

    if (dataFile) {
        Serial.println("Writing to data.txt...");
        dataFile.println("Hello from Nano Every!");
        dataFile.close(); // Crucial: Always close to save data
        Serial.println("Done.");
    } else {
        Serial.println("Error opening data.txt");
    }
}
