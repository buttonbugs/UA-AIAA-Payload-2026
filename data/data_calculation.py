import numpy as np

from data_read import PayloadData

speed_of_sound = "Speed of Sound (m/s)"
air_density = "Density of Air (kg/m^3)"

def calculate_speed_of_sound(data: object, distance: float):
    '''
    distance in meters
    -> return speed in meters per second
    '''
    
    # Get data
    T_1 = data["Ultrasonic 1 (ms)"]/1000
    T_2 = data["Ultrasonic 2 (ms)"]/1000
    T_3 = data["Ultrasonic 3 (ms)"]/1000

    # Calculate average time
    T = np.mean([T_1, T_2, T_3], axis=0)

    # Calculate the speed of sound
    c = distance / T

    return c

def calculate_density(data: object, speed_of_sound_key: str = speed_of_sound):
    
    # Get data
    T_C = data["BME280 Temperature (C)"]
    RH = data["Humidity (%RH)"]
    pressure = data["Pressure (Pa)"]
    c = data[speed_of_sound_key]

    # ------ Calculation ------
    # 1. Calculate the saturation vapor pressure of water using Buck equation
    p_sat = 611.21 * np.exp(
        (18.678 - T_C / 234.5) * T_C / (257.14 + T_C)
    )

    # 2. Calcualte the partial pressure of water vapor
    p_v = (RH / 100) * p_sat

    # 3. Calculate the mole fraction of water vapor
    x_v = p_v / pressure

    # 5. Adjust the Isentropic Exponent
    gamma_d = 1.4       # The ratio of specific heats for dry air
    gamma_v = 1.33      # The ratio of specific heats for water vapor
    gamma_mix = (1 - x_v) * gamma_d + x_v * gamma_v

    # 6. Calculate the air density
    density = gamma_mix * pressure / c**2

    return density


if __name__ == "__main__":

    # Read payload data
    payload_data = PayloadData("testing_20260617142200CDT")

    # Calculation
    payload_data.data[speed_of_sound] = calculate_speed_of_sound(payload_data.data, 0.235)
    payload_data.data[air_density] = calculate_density(payload_data.data)
    print(payload_data.data[air_density])