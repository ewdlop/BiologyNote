import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict
from enum import Enum

class VisionType(Enum):
    NORMAL = "normal"
    MYOPIA = "myopia"
    HYPEROPIA = "hyperopia"
    ASTIGMATISM = "astigmatism"

class GradientIndexLens:
    def __init__(self, center_index: float = 1.41, edge_index: float = 1.37):
        self.center_index = center_index
        self.edge_index = edge_index
        self.radius = 5.0  # mm
        
    def get_index(self, r: float) -> float:
        """Calculate refractive index at radius r using gradient profile."""
        # Gradient index formula: n(r) = n0 * (1 - (r/a)²/2)
        normalized_r = min(1.0, r/self.radius)
        return self.center_index * (1 - (normalized_r**2)/2)
    
    def calculate_power(self, curvature: float) -> float:
        """Calculate lens power considering GRIN effect."""
        # Simplified GRIN lens power calculation
        avg_index = (self.center_index + self.edge_index) / 2
        return (avg_index - 1) * curvature

class AsphericSurface:
    def __init__(self, r0: float, q: float):
        self.r0 = r0  # Vertex radius of curvature
        self.q = q    # Conic constant (q < 0 for prolate, q > 0 for oblate)
        
    def get_height(self, r: float) -> float:
        """Calculate surface height at radius r."""
        return (r**2/self.r0) / (1 + np.sqrt(1 - (1+self.q)*(r/self.r0)**2))

class EnhancedHumanEye:
    def __init__(self, vision_type: VisionType = VisionType.NORMAL):
        # Basic parameters
        self.eye_length = 24.0  # mm
        self.vision_type = vision_type
        
        # Vision defect parameters
        if vision_type == VisionType.MYOPIA:
            self.eye_length += 2.0  # Longer eye
        elif vision_type == VisionType.HYPEROPIA:
            self.eye_length -= 1.5  # Shorter eye
        
        # Cornea (aspheric)
        self.cornea = AsphericSurface(7.8, -0.26)  # Typical prolate cornea
        
        # Gradient index lens
        self.lens = GradientIndexLens()
        self.lens_thickness = 3.6
        
        # Astigmatism parameters (if needed)
        self.astigmatism_axis = 0
        self.astigmatism_power = 0
        if vision_type == VisionType.ASTIGMATISM:
            self.astigmatism_axis = 45  # degrees
            self.astigmatism_power = 2  # diopters
        
        # Accommodation
        self.accommodation = 0
        self.max_accommodation = 20  # diopters, age-dependent
        
        # Chromatic aberration parameters
        self.chromatic_dispersion = {
            'red': {'λ': 700, 'Δn': -0.001},
            'green': {'λ': 550, 'Δn': 0},
            'blue': {'λ': 400, 'Δn': 0.001}
        }

    def calculate_chromatic_aberration(self, wavelength: float) -> float:
        """Calculate chromatic focal shift for given wavelength."""
        # Linear approximation of chromatic dispersion
        reference_λ = 550  # nm (green light)
        dispersion_coefficient = 0.0001  # mm/nm
        return dispersion_coefficient * (wavelength - reference_λ)

    def ray_trace_chromatic(self, object_distance: float, ray_height: float, 
                           wavelength: float) -> List[Tuple[float, float]]:
        """Trace a ray considering chromatic aberration."""
        ray = []
        x = -object_distance
        y = ray_height
        ray.append((x, y))
        
        # Adjust refractive indices for wavelength
        λ_factor = (wavelength - 550) / 150  # Normalized to green light
        n_adjustment = self.chromatic_dispersion['blue']['Δn'] * λ_factor
        
        # Modified ray tracing with chromatic effects
        # Start at cornea
        x_cornea = 0
        ray.append((x_cornea, y))
        
        # Through lens
        x_lens = self.lens_thickness
        n_effective = self.lens.center_index + n_adjustment
        θ_lens = np.arctan(y / object_distance)
        y_lens = y - x_lens * np.tan(θ_lens * (1 - 1/n_effective))
        ray.append((x_lens, y_lens))
        
        # To retina
        x_retina = self.eye_length
        ray.append((x_retina, 0))  # Assuming perfect focus for simplicity
        
        return ray

    def plot_enhanced_eye(self, object_distance: float, object_height: float):
        """Create detailed visualization including chromatic aberration."""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # Plot 1: Geometric ray tracing
        self._plot_eye_structure(ax1)
        
        # Ray tracing for different colors
        colors = ['red', 'green', 'blue']
        wavelengths = [700, 550, 400]
        
        for color, λ in zip(colors, wavelengths):
            rays = [self.ray_trace_chromatic(object_distance, h, λ) 
                   for h in np.linspace(0, object_height, 5)]
            for ray in rays:
                x, y = zip(*ray)
                ax1.plot(x, y, color=color, alpha=0.3)
        
        ax1.set_title('Ray Tracing with Chromatic Aberration')
        
        # Plot 2: Focal plane analysis
        self._plot_focal_analysis(ax2, object_distance)
        
        plt.tight_layout()
        plt.savefig('enhanced_eye_diagram.png')
        plt.close()

    def _plot_eye_structure(self, ax):
        """Plot detailed eye structure."""
        # Corneal surface
        r = np.linspace(-5, 5, 100)
        z = np.array([self.cornea.get_height(ri) for ri in r])
        ax.plot(z, r, 'b-', label='Cornea')
        ax.plot(z, -r, 'b-')
        
        # Eye outline
        t = np.linspace(0, self.eye_length, 100)
        ax.plot(t, np.ones_like(t) * 12, 'k-')
        ax.plot(t, -np.ones_like(t) * 12, 'k-')
        
        # Lens gradient index visualization
        x_lens = np.linspace(3, 7, 20)
        y_lens = np.linspace(-6, 6, 20)
        X, Y = np.meshgrid(x_lens, y_lens)
        R = np.sqrt(X**2 + Y**2)
        N = np.array([[self.lens.get_index(r) for r in row] for row in R])
        ax.contour(X, Y, N, levels=10, cmap='viridis', alpha=0.3)
        
        ax.set_aspect('equal')
        ax.grid(True)
        ax.set_xlabel('Axial Distance (mm)')
        ax.set_ylabel('Height (mm)')

    def _plot_focal_analysis(self, ax, object_distance: float):
        """Plot focal plane analysis."""
        z = np.linspace(15, 30, 100)
        
        # Calculate spot size for different wavelengths
        colors = ['red', 'green', 'blue']
        wavelengths = [700, 550, 400]
        
        for color, λ in zip(colors, wavelengths):
            focal_shift = self.calculate_chromatic_aberration(λ)
            spot_size = np.abs(z - (self.eye_length + focal_shift))
            ax.plot(z, spot_size, color=color, label=f'{λ}nm')
        
        ax.axvline(x=self.eye_length, color='k', linestyle='--', label='Retina')
        ax.set_xlabel('Axial Distance (mm)')
        ax.set_ylabel('Spot Size (mm)')
        ax.set_title('Focal Analysis')
        ax.legend()
        ax.grid(True)

def main():
    # Test different vision conditions
    vision_types = [VisionType.NORMAL, VisionType.MYOPIA, 
                   VisionType.HYPEROPIA, VisionType.ASTIGMATISM]
    
    for vision_type in vision_types:
        print(f"\nAnalyzing {vision_type.value} vision...")
        eye = EnhancedHumanEye(vision_type)
        
        # Test object at 6m (far point)
        far_distance = 6000  # mm
        eye.plot_enhanced_eye(far_distance, 10)
        print(f"Eye length: {eye.eye_length:.1f} mm")
        
        if vision_type == VisionType.ASTIGMATISM:
            print(f"Astigmatism power: {eye.astigmatism_power:.1f} D at {eye.astigmatism_axis}°")
        
        # Calculate and display chromatic aberration
        ca_range = eye.calculate_chromatic_aberration(700) - eye.calculate_chromatic_aberration(400)
        print(f"Chromatic aberration range: {ca_range:.3f} mm")

if __name__ == "__main__":
    main()
