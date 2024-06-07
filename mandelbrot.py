import numpy as np
import matplotlib.pyplot as plt

#This function checks if c is in the mandelbrot set
def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iter

#create a grid of complex numbers
def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    #Iterate over the grid checking if each point is in the mandelbrot set
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j * r2[j], max_iter)
    return n3

#Using pyplot from matplotlib to visualize the results
def display_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    n3 = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    plt.imshow(n3.T, extent=[xmin, xmax, ymin, ymax], cmap='Blues_r', interpolation='bilinear')
    plt.colorbar()
    plt.title("Mandelbrot Set")
    plt.xlabel("Re(c)")
    plt.ylabel("Im(c)")
    plt.show()

# The mote iterations the code goes over, the more defined the fractal will be
display_mandelbrot(-2.0, 1.0, -1.5, 1.5, 1000, 1000, 50)
