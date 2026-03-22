#ifndef READ_VIBRATION
#define READ_VIBRATION

extern int vibration_period_1_ms;
extern int vibration_period_2_ms;

void init_vibration_sensor();
void check_vibration_timeout();

#endif