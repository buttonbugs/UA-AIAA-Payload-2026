#ifndef READ_IMU
#define READ_IMU

void init_imu();
bool imu_ready();
void read_imu();

extern float imu_accX;
extern float imu_accY;
extern float imu_accZ;
extern float imu_gyrX;
extern float imu_gyrY;
extern float imu_gyrZ;
extern float imu_magX;
extern float imu_magY;
extern float imu_magZ;
extern float imu_temp;

#endif