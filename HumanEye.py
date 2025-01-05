import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict

class HumanEye:
    def __init__(self):
        # All measurements in millimeters unless specified
        self.cornea_radius = 7.8
        self.eye_length = 24.0
        self.pupil_diameter = 3.0  # Variable depending on light
        self.lens_thickness = 3.6  # Variable during accommodation
        self.retina_radius = 12.0
        
        # Refractive indices
        self.n_cornea = 1.376
        self.n_aqueous = 1.336
        self.n_lens = 1.413
        self.n_vitreous = 1.336
        self.n_air = 1.0
        
        # Distances
        self.cornea_to_lens = 3.6
        self.lens_to_retina = self.eye_length - (self.cornea_to_lens + self.lens_thickness)
        
        # Initialize accommodation state (diopters)
        self.accommodation = 0  # Relaxed state

    def calculate_focal_length(self, object_distance: float) -> float:
        """Calculate the total focal length of the eye system."""
        # Convert object distance to meters for diopter calculations
        d = object_distance / 1000
        
        # Calculate required power in diopters
        power_needed = 1/d
        
        # Base power of the eye (approximately 60 diopters)
        base_power = 60
        
        # Add accommodation (up to 20 diopters depending on age)
        total_power = base_power + self.accommodation
        
        # Convert back to focal length in mm
        return 1000 / total_power

    def accommodate(self, object_distance: float) -> float:
        """Adjust lens power for clear vision at given distance."""
        # Maximum accommodation (age-dependent, using young adult)
        max_accommodation = 20  # diopters
        
        # Calculate required accommodation
        required_power = 1000/object_distance  # Convert mm to diopters
        base_power = 60
        needed_accommodation = required_power - base_power
        
        # Limit accommodation to physiological range
        self.accommodation = min(max_accommodation, max(0, needed_accommodation))
        
        # Update lens thickness (increases with accommodation)
        self.lens_thickness = 3.6 + (self.accommodation * 0.05)
        
        return self.accommodation

    def calculate_image_position(self, object_distance: float) -> float:
        """Calculate image position relative to retina."""
        self.accommodate(object_distance)
        f = self.calculate_focal_length(object_distance)
        
        # Using thin lens equation: 1/f = 1/u + 1/v
        # where u is object distance, v is image distance
        image_distance = 1 / (1/f - 1/object_distance)
        
        # Return difference from retina position (0 means perfect focus)
        return image_distance - self.eye_length

    def trace_rays(self, object_height: float, object_distance: float, num_rays: int = 5) -> List[List[Tuple[float, float]]]:
        """Trace multiple rays through the eye system."""
        rays = []
        angles = np.linspace(-np.pi/6, np.pi/6, num_rays)
        
        for theta in angles:
            ray = []
            # Starting point
            x = -object_distance
            y = object_height
            ray.append((x, y))
            
            # Ray to cornea
            x_cornea = 0
            y_cornea = y + (x_cornea - x) * np.tan(theta)
            ray.append((x_cornea, y_cornea))
            
            # Refraction at cornea
            theta_1 = np.arcsin(self.n_air * np.sin(theta) / self.n_cornea)
            
            # Ray to lens
            x_lens = self.cornea_to_lens
            y_lens = y_cornea + (x_lens - x_cornea) * np.tan(theta_1)
            ray.append((x_lens, y_lens))
            
            # Refraction at lens (simplified)
            f = self.calculate_focal_length(object_distance)
            theta_2 = np.arctan(y_lens/f)
            
            # Ray to retina
            x_retina = self.eye_length
            y_retina = y_lens + (x_retina - x_lens) * np.tan(theta_2)
            ray.append((x_retina, y_retina))
            
            rays.append(ray)
        
        return rays

    def plot_eye(self, object_height: float, object_distance: float):
        """Create a visualization of the eye and ray tracing."""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Plot eye structure
        # Cornea
        cornea_x = np.linspace(-2, 2, 100)
        cornea_y = np.sqrt(self.cornea_radius**2 - cornea_x**2)
        ax.plot(cornea_x, cornea_y, 'b-', label='Cornea')
        ax.plot(cornea_x, -cornea_y, 'b-')
        
        # Eye outline
        eye_x = np.linspace(0, self.eye_length, 100)
        eye_y_top = np.ones_like(eye_x) * self.retina_radius
        eye_y_bottom = -eye_y_top
        ax.plot(eye_x, eye_y_top, 'k-')
        ax.plot(eye_x, eye_y_bottom, 'k-')
        
        # Lens (simplified as line)
        ax.plot([self.cornea_to_lens, self.cornea_to_lens],
                [-self.retina_radius/2, self.retina_radius/2], 'g-', label='Lens')
        
        # Retina
        ax.plot([self.eye_length], [0], 'ro', label='Retina')
        
        # Trace rays
        rays = self.trace_rays(object_height, object_distance)
        for ray in rays:
            ray_x, ray_y = zip(*ray)
            ax.plot(ray_x, ray_y, 'r-', alpha=0.3)
        
        # Plot object
        ax.plot([-object_distance], [object_height], 'bo', label='Object')
        
        # Set plot properties
        ax.set_xlim(-object_distance*1.1, self.eye_length*1.1)
        max_height = max(object_height, self.retina_radius) * 1.2
        ax.set_ylim(-max_height, max_height)
        ax.set_aspect('equal')
        ax.grid(True)
        ax.set_xlabel('Distance (mm)')
        ax.set_ylabel('Height (mm)')
        ax.set_title('Human Eye Ray Tracing')
        ax.legend()
        
        # Add accommodation information
        info_text = f'Accommodation: {self.accommodation:.1f} D\n'
        info_text += f'Lens Thickness: {self.lens_thickness:.1f} mm'
        ax.text(0.02, 0.98, info_text, transform=ax.transAxes,
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        plt.savefig('eye_diagram.png')
        plt.close()

def main():
    eye = HumanEye()
    
    # Get input from user
    object_distance = float(input("Enter object distance (mm, e.g., 250 for 25cm): "))
    object_height = float(input("Enter object height (mm, e.g., 10): "))
    
    # Calculate accommodation needed
    accommodation = eye.accommodate(object_distance)
    print(f"\nAccommodation needed: {accommodation:.2f} diopters")
    
    # Calculate image position relative to retina
    image_error = eye.calculate_image_position(object_distance)
    print(f"Image position error: {image_error:.2f} mm from retina")
    
    # Create visualization
    eye.plot_eye(object_height, object_distance)
    print("\nEye diagram saved as 'eye_diagram.png'")
    
    # Calculate and display additional information
    focal_length = eye.calculate_focal_length(object_distance)
    print(f"\nEffective focal length: {focal_length:.2f} mm")
    print(f"Total eye power: {1000/focal_length:.2f} diopters")

if __name__ == "__main__":
    main()
