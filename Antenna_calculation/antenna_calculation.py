import numpy as np
import skrf as rf
import matplotlib.pyplot as plt

# Formula to convert normalized impedance to reflection coefficient
def z_to_gamma(z):
    return (z - 1) / (z + 1)

# A. Curve 1+bj (Constant Resistance = 1)
b_values = np.linspace(-100, 100, 1000) # Range of reactance
z_r1 = 1 + 1j * b_values
gamma_r1 = z_to_gamma(z_r1)

# B. Curve a+0.5j (Constant Reactance = 0.5)
a_values = np.linspace(0, 100, 1000)  # Range of resistance (0 to infinity)
z_x05 = a_values + 0.5j
gamma_x05 = z_to_gamma(z_x05)

# Plotting
plt.figure(figsize=(16, 10))
rf.plotting.smith(chart_type='zy', draw_labels=True) # Draws the background circles
rf.plotting.plot_smith(gamma_r1, color='red', lw=2, label='z = 1 + bj')
rf.plotting.plot_smith(gamma_x05, color='blue', lw=2, label='z = a + 0.5j')

plt.legend()

plt.show()
