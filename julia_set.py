import numpy as np
import matplotlib.pyplot as plt

# This function checks if z is in the Julia set
def julia(z, c, max_iter):
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iter

# Create a grid of complex numbers
def julia_set(xmin, xmax, ymin, ymax, width, height, c, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    # Iterate over the grid checking if each point is in the Julia set
    for i in range(width):
        for j in range(height):
            n3[i, j] = julia(r1[i] + 1j * r2[j], c, max_iter)
    return n3

# Using pyplot from matplotlib to visualize the results
def display_julia(xmin, xmax, ymin, ymax, width, height, c, max_iter):
    n3 = julia_set(xmin, xmax, ymin, ymax, width, height, c, max_iter)
    
    plt.imshow(n3.T, extent=[xmin, xmax, ymin, ymax], cmap='inferno', interpolation='bicubic')
    plt.colorbar()
    plt.title(f"Julia Set for c = {c}")
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")
    plt.show()

# Example usage
c = complex(0.285, 0.01)
display_julia(-1.5, 1.5, -1.5, 1.5, 1000, 1000, c, 300)
