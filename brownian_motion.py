import numpy as np
import matplotlib.pyplot as plt

def brownian_motion(n_steps=1000, delta_t=1):
    # Generate random steps
    steps = np.random.randn(n_steps, 2) * np.sqrt(delta_t)
    
    # Compute the position of the particle at each step
    position = np.cumsum(steps, axis=0)
    
    return position

# Simulate Brownian motion
n_steps = 1000
position = brownian_motion(n_steps)

# Plot the Brownian motion
plt.figure(figsize=(10, 10))
plt.plot(position[:, 0], position[:, 1], marker='o', markersize=1, linestyle='-', linewidth=0.5)
plt.title('2D Brownian Motion')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.grid(True)
plt.show()
