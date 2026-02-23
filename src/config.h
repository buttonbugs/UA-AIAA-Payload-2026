#ifndef CONFIG
#define CONFIG

#define FILE_NAME "payload_data_.csv"        // the file that

#define FILE_SIZE_LIMIT 5E4         // bytes, create another data file when the current file size exceeds the this number; 4GB = 4,294,967,296 bytes > 4E9 bytes

#define SAMPLE_ECHOTERVAL 10        // milliseconds per data sample

#define ULTRASONIC_TIMEOUT 30000    // microseconds, prevent the code from freezing when unable to get data from the ultrasonic sensor

#define E_DECIMAL_PLACE 7           // Scientific notation decimal places, Arduino float data types typically provide 6 to 7 decimal digits of precision

/* Pin Configuration */
// Ultrasonic Sensor
#define ULTRASONIC_1_TRIG 2
#define ULTRASONIC_1_ECHO 3
#define ULTRASONIC_2_TRIG 4
#define ULTRASONIC_2_ECHO 5
#define ULTRASONIC_3_TRIG 6
#define ULTRASONIC_3_ECHO 7

// SD Card Reader
#define SD_CARD_CS 10               // SD card Chip Select (set to 10 by default)

#endif