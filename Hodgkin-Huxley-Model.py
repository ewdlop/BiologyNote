# In biophysics, the neuron gateway, often referred to as the neuron ion channel or sodium channel, plays a crucial role in the transmission of electrical signals in the nervous system. Sodium (Na⁺) ion channels are essential for the initiation and propagation of action potentials in neurons.

# Here's a brief overview of how sodium channels work and a simple simulation of the Hodgkin-Huxley model, which describes how action potentials in neurons are initiated and propagated.

# Overview of Sodium Channels
# Resting State: In the resting state, the inside of the neuron is negatively charged relative to the outside. The sodium channels are typically closed.
# Depolarization: When a neuron is stimulated, sodium channels open, allowing Na⁺ ions to flow into the cell. This causes the inside of the cell to become more positive, leading to depolarization.
# Repolarization: After a brief period, the sodium channels close, and potassium (K⁺) channels open, allowing K⁺ ions to flow out of the cell, restoring the negative charge inside the neuron.
# Hyperpolarization: The potassium channels slowly close, often causing a slight overshoot in the negative charge, known as hyperpolarization.
# Restoration: The neuron returns to its resting state, ready for the next action potential.
# Hodgkin-Huxley Model
# The Hodgkin-Huxley model is a mathematical model that describes how action potentials in neurons are initiated and propagated. It uses a set of nonlinear differential equations to model the ionic currents through the membrane of the squid giant axon.

import numpy as np
import matplotlib.pyplot as plt

# Constants
C_m = 1.0  # membrane capacitance, in uF/cm^2
g_Na = 120.0  # maximum conducances, in mS/cm^2
g_K = 36.0
g_L = 0.3
E_Na = 50.0  # Nernst reversal potentials, in mV
E_K = -77.0
E_L = -54.387

# Time parameters
T = 50.0  # ms
dt = 0.01  # ms
time = np.arange(0, T+dt, dt)

# Stimulation parameters
I = np.zeros_like(time)
I[1000:4000] = 10.0  # stimulus current, in uA/cm^2

# Functions to calculate alpha and beta values
def alpha_n(V): return 0.01 * (V + 55) / (1 - np.exp(-(V + 55) / 10))
def beta_n(V): return 0.125 * np.exp(-(V + 65) / 80)
def alpha_m(V): return 0.1 * (V + 40) / (1 - np.exp(-(V + 40) / 10))
def beta_m(V): return 4.0 * np.exp(-(V + 65) / 18)
def alpha_h(V): return 0.07 * np.exp(-(V + 65) / 20)
def beta_h(V): return 1 / (1 + np.exp(-(V + 35) / 10))

# Initialize variables
V = np.zeros_like(time)
n = np.zeros_like(time)
m = np.zeros_like(time)
h = np.zeros_like(time)
V[0] = -65.0  # initial membrane potential
n[0] = alpha_n(V[0]) / (alpha_n(V[0]) + beta_n(V[0]))
m[0] = alpha_m(V[0]) / (alpha_m(V[0]) + beta_m(V[0]))
h[0] = alpha_h(V[0]) / (alpha_h(V[0]) + beta_h(V[0]))

# Simulation
for t in range(1, len(time)):
    V[t] = V[t-1] + dt * (I[t-1] - g_Na * (m[t-1]**3) * h[t-1] * (V[t-1] - E_Na) - g_K * (n[t-1]**4) * (V[t-1] - E_K) - g_L * (V[t-1] - E_L)) / C_m
    n[t] = n[t-1] + dt * (alpha_n(V[t-1]) * (1 - n[t-1]) - beta_n(V[t-1]) * n[t-1])
    m[t] = m[t-1] + dt * (alpha_m(V[t-1]) * (1 - m[t-1]) - beta_m(V[t-1]) * m[t-1])
    h[t] = h[t-1] + dt * (alpha_h(V[t-1]) * (1 - h[t-1]) - beta_h(V[t-1]) * h[t-1])

# Plot the results
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time, V, label='Membrane Potential (mV)')
plt.title('Hodgkin-Huxley Neuron Model')
plt.ylabel('Membrane Potential (mV)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, I, label='Stimulus Current (uA/cm^2)')
plt.xlabel('Time (ms)')
plt.ylabel('Current (uA/cm^2)')
plt.legend()

plt.tight_layout()
plt.show()
