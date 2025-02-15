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
plt.figure(figsize=(12, 8))

# Use fewer points but still enough for smooth curves
x = np.linspace(-np.sqrt(3.3), np.sqrt(3.3), 1000)

# Just plot two alpha values to compare
alpha1, alpha2 = 1, 20

# Create two subplots
plt.subplot(121)
y1 = heart_function(x, alpha1)
plt.plot(x, y1, 'r-', linewidth=2)
plt.title(f'α = {alpha1}')
plt.grid(True)
plt.axis('equal')

plt.subplot(122)
y2 = heart_function(x, alpha2)
plt.plot(x, y2, 'r-', linewidth=2)
plt.title(f'α = {alpha2}')
plt.grid(True)
plt.axis('equal')

plt.tight_layout()
plt.show()