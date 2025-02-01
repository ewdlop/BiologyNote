import numpy as np
import matplotlib.pyplot as plt

def calculate_wetness(d, v, v_r, r, A_t, A_f, theta):
    """
    Calculate the wetness of a person moving through the rain.
    :param d: Distance to shelter (m)
    :param v: Speed of person (m/s)
    :param v_r: Speed of rain (m/s)
    :param r: Rain density (raindrops per m³)
    :param A_t: Top-down cross-sectional area (m²)
    :param A_f: Front-facing cross-sectional area (m²)
    :param theta: Angle of rain from vertical (radians)
    :return: Wetness amount
    """
    T = d / v  # Time to reach shelter
    
    # Wetness from vertical rain
    W_t = r * A_t * v_r * T
    
    # Wetness from frontal rain
    relative_velocity = abs(v * np.cos(theta) + v_r * np.sin(theta))
    W_f = r * A_f * relative_velocity * T
    
    return W_t + W_f

# Parameters
d = 10  # meters to shelter
v_values = np.linspace(0.5, 10, 100)  # Speeds from 0.5 to 10 m/s
v_r = 5  # Rain falling speed (m/s)
r = 100  # Rain density (drops per m³)
A_t = 0.5  # Top-down area (m²)
A_f = 0.8  # Front-facing area (m²)
theta = np.radians(30)  # Rain at 30-degree angle

# Compute wetness for different speeds
wetness_values = [calculate_wetness(d, v, v_r, r, A_t, A_f, theta) for v in v_values]

# Ultra Instinct Simulation
def ultra_instinct_reaction(speed, difficulty):
    """Simulate Ultra Instinct reaction time and evasion ability."""
    base_reaction_time = 0.2  # seconds (average human reaction)
    enhanced_reaction_time = base_reaction_time / (1 + speed / 10)  # Faster reaction with speed
    evasion_success = np.exp(-difficulty / (speed + 1))  # Probability of successful evasion
    return enhanced_reaction_time, evasion_success

ui_speeds = np.linspace(0.5, 10, 100)
reaction_times, evasion_probs = zip(*[ultra_instinct_reaction(v, 5) for v in ui_speeds])

# Plot results
fig, ax1 = plt.subplots(figsize=(8, 5))
ax1.plot(v_values, wetness_values, label="Total Wetness", color="b")
ax1.set_xlabel("Speed of Person (m/s)")
ax1.set_ylabel("Wetness (arbitrary units)", color="b")
ax1.tick_params(axis='y', labelcolor="b")
ax1.legend(loc="upper left")
ax1.grid()

ax2 = ax1.twinx()
ax2.plot(ui_speeds, reaction_times, label="Reaction Time (s)", color="r")
ax2.plot(ui_speeds, evasion_probs, label="Evasion Probability", color="g")
ax2.set_ylabel("Reaction Time & Evasion Probability", color="r")
ax2.tick_params(axis='y', labelcolor="r")
ax2.legend(loc="upper right")

plt.title("Effect of Running Speed on Wetness & Ultra Instinct Abilities")
plt.show()
