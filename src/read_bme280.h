#ifndef BME280
#define BME280

extern float bme_temp;
extern float bme_pressure;
extern float bme_humidity;

void init_bme280();
void read_bme280();

#endif