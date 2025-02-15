import numpy as np
import matplotlib.pyplot as plt

def heart_function(x, alpha=1.0):
    """
    Computes the heart function f(x) = x^(2/3) + 0.9*sqrt(3.3 - x^2)*sin(alpha*pi*x)
    """
    mask = 3.3 - x**2 >= 0
    result = np.zeros_like(x)
    valid_x = x[mask]
    
    result[mask] = (np.sign(valid_x) * np.abs(valid_x)**(2/3) + 
                   0.9 * np.sqrt(3.3 - valid_x**2) * np.sin(alpha * np.pi * valid_x))
    return result

# Create figure
fig, axes = plt.subplots(2, 2, figsize=(15, 8))
axes = axes.ravel()

# Use fewer points for faster plotting
x = np.linspace(-2, 2, 500)

# Test alpha values
alpha_values = [0.5, 0.8, 1.0, 1.2]

for i, alpha in enumerate(alpha_values):
    y = heart_function(x, alpha)
    axes[i].plot(x, y, 'r-', linewidth=2)
    axes[i].set_title(f'α = {alpha}')
    axes[i].grid(True)
    axes[i].set_xlabel('x')
    axes[i].set_ylabel('y')
    
    # Set aspect ratio to squish vertically
    axes[i].set_aspect(0.5)  # This makes it more squished vertically
    
    # Set consistent axis limits
    axes[i].set_xlim(-2.5, 2.5)
    axes[i].set_ylim(-2.5, 2.5)

plt.tight_layout()
plt.show()