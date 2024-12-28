import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 10.0       # Length of the rod
T = 1.0        # Total time
Nx = 100       # Number of spatial points
Nt = 500       # Number of time points
alpha = 0.01   # Thermal diffusivity (diffusion coefficient)

# Discretization
dx = L / (Nx - 1)
dt = T / Nt
x = np.linspace(0, L, Nx)
u = np.zeros(Nx)
u_new = np.zeros(Nx)

# Initial condition: a Gaussian pulse in the center
u = np.exp(-((x - L/2)**2) / (0.1))

# Boundary conditions: u(0, t) = 0, u(L, t) = 0
u[0] = 0
u[-1] = 0

# Stability condition for the explicit method
r = alpha * dt / dx**2
if r > 0.5:
    raise ValueError("Stability condition violated: r must be <= 0.5")

# Time-stepping loop
for n in range(1, Nt):
    for i in range(1, Nx-1):
        u_new[i] = u[i] + r * (u[i+1] - 2*u[i] + u[i-1])
    
    # Update u
    u = u_new.copy()

# Plot the final temperature distribution
plt.plot(x, u, label='t={:.2f}'.format(T))
plt.xlabel('Position')
plt.ylabel('Temperature')
plt.title('1D Diffusion Equation')
plt.legend()
plt.grid(True)
plt.show()
