import numpy as np

def markov_chain(trans_matrix, state, steps):
    states = [state]
    for _ in range(steps):
        state = np.random.choice(len(trans_matrix), p=trans_matrix[state])
        states.append(state)
    return states

# Transition matrix
trans_matrix = np.array([
    [0.9, 0.1],
    [0.5, 0.5]
])

# Initial state
initial_state = 0

# Number of steps
steps = 100

# Simulate the Markov chain
states = markov_chain(trans_matrix, initial_state, steps)

# Plot the transition states
plt.figure(figsize=(10, 5))
plt.plot(states, marker='o', markersize=3, linestyle='-', linewidth=1)
plt.title('Markov Chain Transition')
plt.xlabel('Steps')
plt.ylabel('State')
plt.grid(True)
plt.show()
