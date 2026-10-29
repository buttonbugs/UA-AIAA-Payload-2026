'''
This code renders graph as a layer on top of the existing rocket camera recording and generate a new video.

Installation Requirements

pip install matplotlib
pip install moviepy
'''

import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import VideoClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

import numpy as np
import pandas as pd
from datetime import datetime

gps_data_path = "data/rocket_gps/66UofA_G_06-18-2026_17_05_35.csv"
gcsv_data_path = "data/rocket_camera/100RUNCAM/Split4g_0029.csv"
gcsv_header_path = "data/rocket_camera/100RUNCAM/Split4g_0029.gcsv"
input_video_path = "data/rocket_camera/Trim/Rocket Camera Recording.mp4"
output_video_path = "data/rocket_camera/Trim/Rocket Camera Graph.mp4"

liftoff_time_in_video = 5.15        # seconds
liftoff_time_in_gcsv = 432984       # ms
liftoff_time_in_gps = "2026-06-18 17:28:17"
liftoff_dt_in_gps = datetime.strptime(f"{liftoff_time_in_gps}", "%Y-%m-%d %H:%M:%S")

# 0. Read csv data
gps_data_frame = pd.read_csv(gps_data_path, keep_default_na=False)      # keep_default_na = True: return NaN if empty; keep_default_na = False: return '' if empty
gps_data = gps_data_frame.to_dict(orient='list')
gps_alt = np.array(gps_data["TRACKER Alt asl"], dtype=float)
gps_rel_time = np.array([(datetime.strptime(f"{d} {t}", "%Y-%m-%d %H:%M:%S.%f") - liftoff_dt_in_gps).total_seconds() for d, t in zip(gps_data["DATE"], gps_data["TIME"])], dtype=float)
gps_data_index_start = np.searchsorted(gps_rel_time, -liftoff_time_in_video, side='left') - 1

with open(gcsv_header_path, "r") as gcsv_file:

    gcsv_header = gcsv_file.read().split("\nt,rx,ry,rz,ax,ay,az\n")[0]
    ascale = float(gcsv_header.split("\n")[-1].split(",")[-1])

gcsv_data_frame = pd.read_csv(gcsv_data_path, keep_default_na=False)      # keep_default_na = True: return NaN if empty; keep_default_na = False: return '' if empty
gcsv_data = gcsv_data_frame.to_dict(orient='list')
gcsv_accel_x = np.array(gcsv_data["ax"], dtype=float) * ascale          # Convert unit to g
gcsv_accel_y = np.array(gcsv_data["ay"], dtype=float) * ascale          # Convert unit to g
gcsv_accel_z = np.array(gcsv_data["az"], dtype=float) * ascale          # Convert unit to g
gcsv_accel = np.hypot(np.hypot(gcsv_accel_x, gcsv_accel_y), gcsv_accel_z)       # Calculate magnitude (np.hypot() is faster than np.linalg.norm())
gcsv_rel_time = (np.array(gcsv_data["t"], dtype=float) - liftoff_time_in_gcsv) / 1000   # Convert ms to s
gcsv_data_index_start = np.searchsorted(gcsv_rel_time, -liftoff_time_in_video, side='left') - 1

# 1. Load the original background video
bg_clip = VideoFileClip(input_video_path)
duration = bg_clip.duration
fps = bg_clip.fps

# 2. Setup Matplotlib Figure with a transparent background
plt.style.use('dark_background')                # White font
fig, ax = plt.subplots(figsize=(10.2, 5.6))  # 720p: (6.2, 3.6), 1080p: (10.6, 5.6)
ax2 = ax.twinx()
fig.patch.set_alpha(0.0)  # Transparent figure background
ax.patch.set_alpha(0.0)   # Transparent axes background

ax.set_title("T-00:00:00.00")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Altitude above sea level (ft)")
ax2.set_ylabel("Acceleration (G)")
ax.ticklabel_format(style='plain', axis='both', useOffset=False)     # Prevent axes from showing scientific notation
ax.yaxis.set_major_formatter(StrMethodFormatter('{x:.0f}'))
ax2.yaxis.set_major_formatter(StrMethodFormatter('{x:.1f}'))

gps_line, = ax.plot([], [], lw=1.5, color="red", label="Altitude")
accel_ax_line_placeholder = ax.plot([], [], lw=1.5, color="orange", label="Acceleration")
accel_line, = ax2.plot([], [], lw=1, color="orange", label="Acceleration")
ax.legend(frameon=False)

def format_launch_timer(total_seconds):
    # Determine the countdown or countup sign
    sign = "+" if total_seconds >= 0 else "-"
    
    # Work with absolute time to calculate components
    abs_seconds = abs(total_seconds)
    
    hours = int(abs_seconds // 3600)
    minutes = int((abs_seconds % 3600) // 60)
    seconds = abs_seconds % 60
    
    # :05.2f ensures the seconds field is zero-padded to 5 characters total (e.g., 05.20)
    return f"T{sign}{hours:02d}:{minutes:02d}:{seconds:05.2f}"

def update(frame):
    t = frame / fps - liftoff_time_in_video
    ax.set_title(format_launch_timer(t))

    # 0. Extract GPS data
    gps_data_index = np.searchsorted(gps_rel_time, t, side='left') - 1
    gcsv_data_index = np.searchsorted(gcsv_rel_time, t, side='left') - 1

    # 1. Generate dynamic data points
    gps_graph_t         = gps_rel_time  [gps_data_index_start: gps_data_index]
    gps_graph_alt       = gps_alt       [gps_data_index_start: gps_data_index]

    gcsv_graph_t        = gcsv_rel_time [gcsv_data_index_start: gcsv_data_index]
    gcsv_graph_accel    = gcsv_accel    [gcsv_data_index_start: gcsv_data_index]

    # 2. Update the line data
    gps_line.set_data(gps_graph_t, gps_graph_alt)
    accel_line.set_data(gcsv_graph_t, gcsv_graph_accel)

    # 3. DYNAMICALLY RESIZE AXES HERE:
    ax.relim()             # Recalculate data limits based on line.get_data()
    ax.autoscale_view()    # Rescale the view limits to fit those data limits
    ax2.relim()
    ax2.autoscale_view()

    return gps_line, accel_line

# 4. Create the animation frame-generator function for MoviePy
# We convert each matplotlib frame into an RGB image array
def make_frame(t):
    # t is the current time in seconds. Map it to animation frames.
    frame_number = int(t * fps)
    update(frame_number)
    
    # Draw and extract raw RGBA buffer
    fig.canvas.draw()
    rgba_image = np.asarray(fig.canvas.buffer_rgba())
    
    # MoviePy expects RGB (3 channels), separate the Alpha if needed
    # (Alternatively, keep alpha if using an explicit masking layer)
    rgb_image = rgba_image[:, :, :3]
    return rgb_image

# Generate a clip from the matplotlib figures
# Use the figure's alpha channel as a mask for perfect transparency transparency
def make_mask(t):
    frame_number = int(t * fps)
    update(frame_number)
    fig.canvas.draw()
    rgba_image = np.asarray(fig.canvas.buffer_rgba())
    # Scale alpha channel from 0-255 to 0.0-1.0
    return rgba_image[:, :, 3] / 255.0

# 5. Build the overlay clip
graph_clip = VideoClip(make_frame, duration=duration)
graph_mask = VideoClip(make_mask, is_mask=True, duration=duration)

graph_clip = graph_clip.with_mask(graph_mask)
graph_clip = graph_clip.with_position(('center', 'center'))

# 6. Composite the clips together and save
final_clip = CompositeVideoClip([bg_clip, graph_clip])
final_clip.write_videofile(output_video_path, fps=fps, codec="libx264", audio_codec="aac")

# Clean up memory
plt.close(fig)
bg_clip.close()
final_clip.close()