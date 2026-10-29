'''
This code renders graph as a layer on top of the existing rocket camera recording and generate a new video.

Installation Requirements

pip install matplotlib
pip install moviepy
'''

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import VideoClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

import numpy as np
import pandas as pd
from datetime import datetime

gps_data_path = 'data/rocket_gps/66UofA_G_06-18-2026_17_05_35.csv'
input_video_path = "data/rocket_camera/Trim/Rocket Camera Recording.mp4"
output_video_path = "data/rocket_camera/Trim/Rocket Camera Graph.mp4"

liftoff_time_in_video = 5.15        # seconds
liftoff_time_in_gps = "2026-06-18 17:28:17"
liftoff_dt_in_gps = datetime.strptime(f"{liftoff_time_in_gps}", "%Y-%m-%d %H:%M:%S")

# 0. Read gps data
gps_data_frame = pd.read_csv(gps_data_path, keep_default_na=False)      # keep_default_na = True: return NaN if empty; keep_default_na = False: return '' if empty
gps_data = gps_data_frame.to_dict(orient='list')
gps_alt = np.array(gps_data["TRACKER Alt asl"])

# Time relative to T
gps_rel_time = np.array([(datetime.strptime(f"{d} {t}", "%Y-%m-%d %H:%M:%S.%f") - liftoff_dt_in_gps).total_seconds() for d, t in zip(gps_data["DATE"], gps_data["TIME"])])
gps_data_index_start = np.searchsorted(gps_rel_time, -liftoff_time_in_video, side='left') - 1

print(gps_rel_time[-100:])

# 1. Load the original background video
bg_clip = VideoFileClip(input_video_path)
duration = bg_clip.duration
fps = bg_clip.fps

# 2. Setup Matplotlib Figure with a transparent background
fig, ax = plt.subplots(figsize=(10.6, 5.6))
fig.patch.set_alpha(0.0)  # Transparent figure background
ax.patch.set_alpha(0.0)   # Transparent axes background
ax.set_title("T", color='white')
ax.set_xlabel("Time (s)", color='white')
ax.set_ylabel("Altitude above sea level (ft)", color='white')

# Style the plot lines/labels so they are visible over the video
# ax.set_xlim(0, 2 * np.pi)
# ax.set_ylim(-1.5, 1.5)
ax.tick_params(colors='white')  # White text for dark videos
for spine in ax.spines.values():
    spine.set_color('white')

line, = ax.plot([], [], lw=2)

# 3. Animation functions
def init():
    line.set_data([], [])
    return line,

def update(frame):
    t = frame / fps - liftoff_time_in_video
    ax.set_title(f"T{t:+.2f}", color='white')

    # 0. Extract GPS data
    gps_data_index = np.searchsorted(gps_rel_time, t, side='left') - 1

    # 1. Generate your dynamic data points
    gps_graph_t = gps_rel_time[gps_data_index_start: gps_data_index]
    gps_graph_alt = gps_alt[gps_data_index_start: gps_data_index]

    # 2. Update the line data
    line.set_data(gps_graph_t, gps_graph_alt)

    # 3. DYNAMICALLY RESIZE AXES HERE:
    ax.relim()             # Recalculate data limits based on line.get_data()
    ax.autoscale_view()    # Rescale the view limits to fit those data limits

    return line,

# 4. Create the animation frame-generator function for MoviePy
# We convert each matplotlib frame into an RGB image array
def make_frame(t):
    # t is the current time in seconds. Map it to your animation frames.
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
final_clip.write_videofile(output_video_path, fps=fps, codec="libx264")

# Clean up memory
plt.close(fig)
bg_clip.close()
final_clip.close()