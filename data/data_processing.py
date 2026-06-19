from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

from data_read import PayloadData

def draw_accel(data, start=None, end=None, interval=None):

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
    plt.grid(linewidth = 0.2)
    plt.show()

def draw_pressure(data, start=None, end=None, interval=None):

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
    plt.grid(linewidth = 0.2)
    plt.show()

def draw_ultrasonic(data, start=None, end=None, interval=None):

    trim_range = slice(start, end)

    X = data["Ultrasonic 1 (ms)"][trim_range]
    Y = data["Ultrasonic 2 (ms)"][trim_range]
    Z = data["Ultrasonic 3 (ms)"][trim_range]
    average = np.mean([X, Y, Z], axis=0)
    data_time = data["datetime"][trim_range]

    plt.plot(data_time, X, label="Ultrasonic 1")
    plt.plot(data_time, Y, label="Ultrasonic 2")
    plt.plot(data_time, Z, label="Ultrasonic 3")
    plt.plot(data_time, average, label="Average", color="black")

    if interval:
        plt.gca().xaxis.set_major_locator(mdates.SecondLocator(interval=interval))

    plt.xticks(rotation=45)     # Rotate labels for better readability
    plt.xlabel("Timestamp")
    plt.ylabel("Ultrasonic (ms)")
    plt.tight_layout()
    plt.legend()
    plt.grid(linewidth = 0.2)
    plt.show()

if __name__ == "__main__":
    payload_data = PayloadData("testing_20260617142200CDT")
    draw_accel(payload_data.data, 500, 1000)
    draw_pressure(payload_data.data)
    draw_ultrasonic(payload_data.data)