import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 10.0       # Length of the domain
T = 1.0        # Total time
Nx = 100       # Number of spatial points
Nt = 500       # Number of time points
D = 0.01       # Diffusion coefficient
v = 1.0        # Convection velocity

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
r = D * dt / dx**2
s = v * dt / dx
if r > 0.5 or s > 1:
    raise ValueError("Stability condition violated: r must be <= 0.5 and s must be <= 1")

# Time-stepping loop
for n in range(1, Nt):
    for i in range(1, Nx-1):
        u_new[i] = u[i] + r * (u[i+1] - 2*u[i] + u[i-1]) - s * (u[i] - u[i-1])
    
    # Update u
    u = u_new.copy()

# Plot the initial and final distribution
plt.plot(x, np.exp(-((x - L/2)**2) / (0.1)), label='Initial Condition')
plt.plot(x, u, label=f'Final Condition at t={T}')
plt.xlabel('Position')
plt.ylabel('Concentration')
plt.title('1D Convection-Diffusion Equation')
plt.legend()
plt.grid(True)
plt.show()
