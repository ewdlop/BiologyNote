import numpy as np
import matplotlib.pyplot as plt

def random_walk(steps):
    # Generate random steps in 2D
    x = np.cumsum(np.random.choice([-1, 1], steps))
    y = np.cumsum(np.random.choice([-1, 1], steps))
    return x, y

# Parameters
steps = 1000

# Perform the random walk
x, y = random_walk(steps)

# Plot the random walk
plt.figure(figsize=(10, 10))
plt.plot(x, y, marker='o', markersize=1, linestyle='-', linewidth=0.5)
plt.title('Random Walk')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
