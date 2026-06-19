from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

from data_read import PayloadData

filtered_data_file = "filtered.csv"


# Works with explicit offsets (+HH:MM)
dt_offset = datetime.fromisoformat("2026-06-15T10:30:00+05:30")
print(dt_offset)  # 2026-06-15 10:30:00+05:30

def draw_accel(data):
    X = np.array(data["Accelerometer X (milli-g)"]) / 1000
    Y = np.array(data["Accelerometer Y (milli-g)"]) / 1000
    Z = np.array(data["Accelerometer Z (milli-g)"]) / 1000
    plt.plot(data["datetime"], X, label="X (g)")
    plt.plot(data["datetime"], Y, label="Y (g)")
    plt.plot(data["datetime"], Z, label="Z (g)")
    plt.plot(data["datetime"], (X**2 + Y**2 + Z**3)**.5, label="Magnitude (g)", color="black")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    payload_data = PayloadData("testing_20260617142200CDT")
    draw_accel(payload_data.data)