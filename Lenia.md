Lenia is a cellular automaton that generalizes Conway's Game of Life to a continuous domain. It is an example of a continuous cellular automaton with smooth dynamics and complex behavior. Here, I'll provide an introduction to Lenia along with a Python implementation.

### Introduction to Lenia

Lenia is defined on a continuous, two-dimensional grid where each cell has a real-valued state that evolves over time according to a set of rules. The evolution rules involve convolution operations with a kernel and a growth function that determines how the state of each cell changes.

### Python Implementation

Below is a basic implementation of Lenia in Python using NumPy for efficient numerical operations. This implementation includes:
- Initialization of the grid.
- Convolution with a kernel.
- Update rules based on the growth function.

```python
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
```

### Explanation

1. **Kernel**: A Gaussian kernel is used for convolution. The `gaussian_kernel` function generates a 2D Gaussian kernel with a specified radius and standard deviation.
2. **Growth Function**: The `growth_function` is a Gaussian-like function that determines how the state of each cell changes based on the convolved values.
3. **Initialization**: The grid is initialized with random values between 0 and 1.
4. **Simulation Loop**: The main loop performs the following steps at each time step:
   - Convolve the grid with the kernel.
   - Apply the growth function to the convolved values.
   - Update the grid based on the growth values.
   - Ensure the grid values remain within the range [0, 1].
   - Display the grid every 10 time steps using `matplotlib`.

### Running the Simulation

To see the evolution of the Lenia automaton, you can run the provided script. The `matplotlib` library will display the grid at specified intervals, allowing you to observe the complex patterns that emerge over time.

Feel free to experiment with different parameters (e.g., grid size, kernel radius, growth function parameters) to see how they affect the behavior of the Lenia automaton.
