import numpy as np
import skrf as rf
import matplotlib.pyplot as plt

# Formula to convert normalized impedance to reflection coefficient
def z_to_gamma(z):
    return (z - 1) / (z + 1)

# Formula to convert normalized admittance to reflection coefficient
def y_to_gamma(y):
    return (1 - y) / (1 + y)

# A. Curve 1+bj (Constant Resistance = 1)
b_values = np.linspace(-100, 100, 1000) # Range of reactance
z_r1 = 1 + 1j * b_values
gamma_r1 = z_to_gamma(z_r1)

# B. Curve a+0.5j (Constant Reactance = 0.5)
a_values = np.linspace(0, 100, 1000)  # Range of resistance (0 to infinity)
z_x05 = a_values + 0.5j
gamma_x05 = z_to_gamma(z_x05)

# C. Curve with Constant Conductance (g = 0.5)
susceptance_values = np.linspace(-100, 100, 1000)
y_g05 = 0.5 + 1j * susceptance_values
gamma_g05 = y_to_gamma(y_g05)

# D. Curve with Constant Susceptance (b = -1)
conductance_values = np.linspace(0, 100, 1000)
y_b1 = conductance_values - 1j
gamma_b1 = y_to_gamma(y_b1)

z_point1 = 1 + 0.5j
gamma_point1 = z_to_gamma(z_point1)

""" ------ Plotting ------ """
plt.figure(figsize=(16, 10))
rf.plotting.smith(chart_type='zy', draw_labels=True) # Draws the background circles
# Plot Impedance
rf.plotting.plot_smith(gamma_r1, color='red', lw=2, label='z = 1 + bj')
rf.plotting.plot_smith(gamma_x05, color='blue', lw=2, label='z = a + 0.5j')
# Plot Admittance
rf.plotting.plot_smith(gamma_g05, color='purple', lw=2, ls='--', label='y = 0.5 + jb')
rf.plotting.plot_smith(gamma_b1, color='orange', lw=2, ls='--', label='y = g - 1j')

# Points
rf.plotting.plot_smith(np.array([gamma_point1]), color='black', marker='o', markersize=10, label='z = 1 + 0.5j')

plt.legend()

plt.show()
