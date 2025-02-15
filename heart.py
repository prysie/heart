import numpy as np
import matplotlib.pyplot as plt

def heart_function(x, alpha=1.0):
    """
    Computes the heart function f(x) = x^(2/3) + 0.9*sqrt(3.3 - x^2)*sin(alpha*pi*x)
    with y-values flipped for negative x
    """
    mask = 3.3 - x**2 >= 0
    result = np.zeros_like(x)
    valid_x = x[mask]
    
    # Calculate the basic function
    result[mask] = (np.sign(valid_x) * np.abs(valid_x)**(2/3) + 
                   0.9 * np.sqrt(3.3 - valid_x**2) * np.sin(alpha * np.pi * valid_x))
    
    # Flip y-values for negative x
    result[x < 0] = -result[x < 0]
    
    return result

# Create figure
plt.figure(figsize=(15, 6))

# Use enough points for smooth curves
x = np.linspace(-np.sqrt(3.3), np.sqrt(3.3), 1000)

# Try some different alpha values
alpha_values = [5, 7, 10, 15]

# Create subplots
for i, alpha in enumerate(alpha_values, 1):
    plt.subplot(2, 2, i)
    y = heart_function(x, alpha)
    plt.plot(x, y, 'r-', linewidth=2)
    plt.title(f'α = {alpha}')
    plt.grid(True)
    plt.axis('equal')

plt.tight_layout()
plt.show()

# Also show the best one separately
plt.figure(figsize=(8, 8))
best_alpha = 10  # We can adjust this after seeing the results
y = heart_function(x, best_alpha)
plt.plot(x, y, 'r-', linewidth=2)
plt.title(f'Heart Shape (α = {best_alpha})')
plt.grid(True)
plt.axis('equal')
plt.show()