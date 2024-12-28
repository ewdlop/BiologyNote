import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

# Parameters
size = 100  # Size of the grid
T = 100     # Number of time steps
r = 10      # Radius of the kernel
dt = 0.1    # Time step size

# Kernel: Gaussian kernel
def gaussian_kernel(radius, sigma=1.0):
    ax = np.arange(-radius, radius + 1)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-0.5 * (np.square(xx) + np.square(yy)) / np.square(sigma))
    return kernel / np.sum(kernel)

# Growth function
def growth_function(x, mu=0.1, sigma=0.03):
    return 2 * np.exp(-np.square((x - mu) / sigma)) - 1

# Initialize the grid with random values
grid = np.random.rand(size, size)

# Create the kernel
kernel = gaussian_kernel(r)

# Simulation
for t in range(T):
    # Convolution with the kernel
    convolved = convolve(grid, kernel, mode='wrap')
    
    # Apply the growth function
    growth = growth_function(convolved)
    
    # Update the grid
    grid += dt * growth
    
    # Ensure grid values are within [0, 1]
    grid = np.clip(grid, 0, 1)
    
    # Display the grid
    if t % 10 == 0:
        plt.imshow(grid, cmap='viridis')
        plt.title(f'Time step: {t}')
        plt.colorbar()
        plt.show()
