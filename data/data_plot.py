from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

from data_read import PayloadData
from data_calculation import calculate_speed_of_sound, calculate_density

# Key name used to save the calculation results
speed_of_sound = "Speed of Sound (m/s)"
air_density = "Density of Air (kg/m^3)"

# Global configuation
distance = 0.235        # The distance the sound travels in meters

def draw_acceleration(data, start=None, end=None, interval=None, output_file=None):

    trim_range = slice(start, end)

    X = data["Accelerometer X (milli-g)"][trim_range] / 1000
    Y = data["Accelerometer Y (milli-g)"][trim_range] / 1000
    Z = data["Accelerometer Z (milli-g)"][trim_range] / 1000
    magnitude = np.linalg.norm([X, Y, Z], axis=0)
    data_time = data["datetime"][trim_range]

    plt.plot(data_time, X, label="X")
    plt.plot(data_time, Y, label="Y")
    plt.plot(data_time, Z, label="Z")
    plt.plot(data_time, magnitude, label="Magnitude", color="black")

    if interval:
        plt.gca().xaxis.set_major_locator(mdates.SecondLocator(interval=interval))

    plt.xticks(rotation=45)     # Rotate labels for better readability
    plt.xlabel("Timestamp")
    plt.ylabel("Acceleration (g)")
    plt.tight_layout()
    plt.legend()
    plt.grid(alpha=0.2)
    if output_file:
        plt.savefig(output_file, dpi=300, transparent=False, bbox_inches='tight')
    plt.show()

def draw_pressure(data, start=None, end=None, interval=None, output_file=None):

    trim_range = slice(start, end)

    pressure = data["Pressure (Pa)"][trim_range]
    data_time = data["datetime"][trim_range]

    plt.plot(data_time, pressure)

    if interval:
        plt.gca().xaxis.set_major_locator(mdates.SecondLocator(interval=interval))

    plt.xticks(rotation=45)     # Rotate labels for better readability
    plt.xlabel("Timestamp")
    plt.ylabel("Pressure (Pa)")
    plt.tight_layout()
    plt.grid(alpha=0.2)
    if output_file:
        plt.savefig(output_file, dpi=300, transparent=False, bbox_inches='tight')
    plt.show()

def draw_temperature(data, start=None, end=None, interval=None, output_file=None):

    trim_range = slice(start, end)

    temperature_bme280 = data["BME280 Temperature (C)"][trim_range]
    temperature_imu = data["IMU Temperature (C)"][trim_range]
    data_time = data["datetime"][trim_range]

    plt.plot(data_time, temperature_bme280, label="BME280 (Environment Temperature, Accurate)")
    plt.plot(data_time, temperature_imu, label="IMU (Internal Chip Temperature, Inaccurate)")

    if interval:
        plt.gca().xaxis.set_major_locator(mdates.SecondLocator(interval=interval))

    plt.xticks(rotation=45)     # Rotate labels for better readability
    plt.xlabel("Timestamp")
    plt.ylabel("Temperature (C)")
    plt.tight_layout()
    plt.legend()
    plt.grid(alpha=0.2)
    if output_file:
        plt.savefig(output_file, dpi=300, transparent=False, bbox_inches='tight')
    plt.show()

def draw_pressure_temp(data, start=None, end=None, interval=None, output_file=None):

    trim_range = slice(start, end)

    # Sample monthly data
    temperature = data["BME280 Temperature (C)"][trim_range]
    pressure = data["Pressure (Pa)"][trim_range]
    data_time = data["datetime"][trim_range]

    # Create the main figure and the first axis (ax1)
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot Pressure on the primary left y-axis (Dashed Line)
    ax1.set_xlabel('Timestamp')
    ax1.set_ylabel('Pressure (Pa)')
    line1 = ax1.plot(data_time, pressure, color="#1F77B4", linewidth=2, label='Pressure')
    ax1.tick_params(axis='y')

    # Create the twin axis sharing the same x-axis
    ax2 = ax1.twinx()

    # Plot Temperature on the secondary right y-axis (Solid Line)
    ax2.set_ylabel('Temperature (°C)')
    line2 = ax2.plot(data_time, temperature, color="#FF7F0F", linewidth=2, label='Temperature')
    ax2.tick_params(axis='y')

    # Combine legends from both axes into a single box
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels)

    # Add grid lines
    ax1.grid(alpha=0.2)

    # Title and layout adjustments
    fig.tight_layout()

    # Display the plot
    if output_file:
        plt.savefig(output_file, dpi=300, transparent=False, bbox_inches='tight')
    plt.show()

def draw_ultrasonic(data, start=None, end=None, interval=None, output_file=None):

    trim_range = slice(start, end)

    T_1 = data["Ultrasonic 1 (ms)"][trim_range]
    T_2 = data["Ultrasonic 2 (ms)"][trim_range]
    T_3 = data["Ultrasonic 3 (ms)"][trim_range]
    average = np.mean([T_1, T_2, T_3], axis=0)
    data_time = data["datetime"][trim_range]

    plt.plot(data_time, T_1, label="Ultrasonic 1")
    plt.plot(data_time, T_2, label="Ultrasonic 2")
    plt.plot(data_time, T_3, label="Ultrasonic 3")
    plt.plot(data_time, average, label="Average", color="black")

    if interval:
        plt.gca().xaxis.set_major_locator(mdates.SecondLocator(interval=interval))

    plt.xticks(rotation=45)     # Rotate labels for better readability
    plt.xlabel("Timestamp")
    plt.ylabel("Ultrasonic (ms)")
    plt.tight_layout()
    plt.legend()
    plt.grid(alpha=0.2)
    if output_file:
        plt.savefig(output_file, dpi=300, transparent=False, bbox_inches='tight')
    plt.show()

def draw_density(data, start=None, end=None, interval=None, output_file=None):

    trim_range = slice(start, end)

    density = data[air_density][trim_range]
    data_time = data["datetime"][trim_range]

    plt.plot(data_time, density)
    plt.xticks(rotation=45)     # Rotate labels for better readability
    plt.xlabel("Timestamp")
    plt.ylabel("Density of Air (kg/m$^3$)")
    plt.tight_layout()
    plt.legend()
    plt.grid(alpha=0.2)
    if output_file:
        plt.savefig(output_file, dpi=300, transparent=False, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":

    # Read payload data
    payload_data = PayloadData("testing_20260617142200CDT")

    # Calculate the density of air
    payload_data.data[speed_of_sound] = calculate_speed_of_sound(payload_data.data, distance)
    payload_data.data[air_density] = calculate_density(payload_data.data, speed_of_sound_key=speed_of_sound)

    # Draw graphs
    # draw_acceleration(payload_data.data, 500, 1000, output_file=(payload_data.data_dir / "graph_acceleration.png"))
    # draw_pressure(payload_data.data, output_file=(payload_data.data_dir / "graph_pressure.png"))
    # draw_temperature(payload_data.data, output_file=(payload_data.data_dir / "graph_temperature.png"))
    # draw_pressure_temp(payload_data.data, output_file=(payload_data.data_dir / "graph_pressure_temp.png"))
    # draw_ultrasonic(payload_data.data, output_file=(payload_data.data_dir / "graph_ultrasonic.png"))
    draw_density(payload_data.data, output_file=(payload_data.data_dir / "graph_density.png"))