"""
===================================================================================
                    Cuckoo Search Algorithm Implementation
===================================================================================
Created by: Claude (Anthropic AI Assistant)
Model: Claude 3.5 Sonnet
Version: 1.0
Created: 2024

A comprehensive implementation of the Cuckoo Search optimization algorithm,
inspired by the brood parasitism of cuckoo birds.
===================================================================================
"""

import numpy as np
from typing import Callable, List, Tuple, Optional
import matplotlib.pyplot as plt

class CuckooSearch:
    """Implementation of Cuckoo Search Algorithm."""
    
    def __init__(self, 
                 n_nests: int = 25,
                 dimension: int = 2,
                 lb: float = -10.0,
                 ub: float = 10.0,
                 pa: float = 0.25,
                 alpha: float = 1.0,
                 beta: float = 1.5):
        """
        Initialize Cuckoo Search Algorithm.
        
        Args:
            n_nests: Number of nests (population size)
            dimension: Problem dimension
            lb: Lower bound of search space
            ub: Upper bound of search space
            pa: Probability of nest abandonment
            alpha: Step size scaling factor
            beta: Lévy flight parameter
        """
        self.n_nests = n_nests
        self.dimension = dimension
        self.lb = lb
        self.ub = ub
        self.pa = pa
        self.alpha = alpha
        self.beta = beta
        
        # Initialize nests randomly
        self.nests = self._init_nests()
        self.best_nest = None
        self.best_fitness = float('inf')
        self.fitness_history = []
        
    def _init_nests(self) -> np.ndarray:
        """Initialize nest positions randomly within bounds."""
        return np.random.uniform(
            self.lb,
            self.ub,
            size=(self.n_nests, self.dimension)
        )
    
    def _levy_flight(self) -> np.ndarray:
        """Generate Lévy flight step."""
        sigma1 = np.power(
            (gamma(1 + self.beta) * np.sin(np.pi * self.beta / 2)) /
            (gamma((1 + self.beta) / 2) * self.beta * np.power(2, (self.beta - 1) / 2)),
            1 / self.beta
        )
        sigma2 = 1
        
        u = np.random.normal(0, sigma1, size=self.dimension)
        v = np.random.normal(0, sigma2, size=self.dimension)
        step = u / np.power(np.abs(v), 1 / self.beta)
        
        return step
    
    def _get_cuckoo(self, nest: np.ndarray) -> np.ndarray:
        """Generate new solution via Lévy flight."""
        step_size = self.alpha * self._levy_flight()
        new_nest = nest + step_size
        
        # Ensure bounds
        new_nest = np.clip(new_nest, self.lb, self.ub)
        return new_nest
    
    def _abandon_nests(self) -> None:
        """Abandon worst nests based on probability pa."""
        for i in range(self.n_nests):
            if np.random.random() < self.pa:
                self.nests[i] = self._init_nests()[0]
    
    def optimize(self, 
                objective_func: Callable,
                n_iterations: int = 1000,
                verbose: bool = False) -> Tuple[np.ndarray, float, List[float]]:
        """
        Run the Cuckoo Search optimization.
        
        Args:
            objective_func: Function to minimize
            n_iterations: Number of iterations
            verbose: Whether to print progress
            
        Returns:
            best_solution: Best solution found
            best_fitness: Best fitness value
            fitness_history: History of best fitness values
        """
        # Evaluate initial population
        fitness = np.array([objective_func(nest) for nest in self.nests])
        best_idx = np.argmin(fitness)
        self.best_nest = self.nests[best_idx].copy()
        self.best_fitness = fitness[best_idx]
        
        for iteration in range(n_iterations):
            # Get cuckoo
            cuckoo_idx = np.random.randint(self.n_nests)
            new_nest = self._get_cuckoo(self.nests[cuckoo_idx])
            
            # Evaluate new solution
            new_fitness = objective_func(new_nest)
            
            # Replace if better
            if new_fitness < fitness[cuckoo_idx]:
                self.nests[cuckoo_idx] = new_nest
                fitness[cuckoo_idx] = new_fitness
                
                # Update best solution
                if new_fitness < self.best_fitness:
                    self.best_nest = new_nest.copy()
                    self.best_fitness = new_fitness
            
            # Abandon worst nests
            self._abandon_nests()
            
            # Re-evaluate all nests
            fitness = np.array([objective_func(nest) for nest in self.nests])
            
            # Track progress
            self.fitness_history.append(self.best_fitness)
            
            if verbose and (iteration + 1) % 100 == 0:
                print(f"Iteration {iteration + 1}/{n_iterations}, Best Fitness: {self.best_fitness:.6f}")
        
        return self.best_nest, self.best_fitness, self.fitness_history
    
    def plot_convergence(self) -> None:
        """Plot convergence history."""
        plt.figure(figsize=(10, 6))
        plt.plot(self.fitness_history)
        plt.title('Convergence History')
        plt.xlabel('Iteration')
        plt.ylabel('Best Fitness')
        plt.yscale('log')
        plt.grid(True)
        plt.show()

def test_functions():
    """Collection of test functions for optimization."""
    
    def sphere(x: np.ndarray) -> float:
        """Sphere function."""
        return np.sum(x**2)
    
    def rosenbrock(x: np.ndarray) -> float:
        """Rosenbrock function."""
        return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)
    
    def rastrigin(x: np.ndarray) -> float:
        """Rastrigin function."""
        return 10 * len(x) + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))
    
    return {
        'sphere': sphere,
        'rosenbrock': rosenbrock,
        'rastrigin': rastrigin
    }

def main():
    """Example usage of Cuckoo Search Algorithm."""
    
    # Test functions
    functions = test_functions()
    
    # Problem settings
    n_nests = 25
    dimension = 30
    lb = -5.0
    ub = 5.0
    n_iterations = 1000
    
    # Initialize optimizer
    cs = CuckooSearch(
        n_nests=n_nests,
        dimension=dimension,
        lb=lb,
        ub=ub
    )
    
    # Run optimization
    print("\nOptimizing Sphere Function:")
    best_solution, best_fitness, _ = cs.optimize(
        functions['sphere'],
        n_iterations=n_iterations,
        verbose=True
    )
    
    print(f"\nBest Solution: {best_solution}")
    print(f"Best Fitness: {best_fitness:.6f}")
    
    # Plot convergence
    cs.plot_convergence()

if __name__ == "__main__":
    main()
