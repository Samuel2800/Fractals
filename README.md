# Fractals
## Mandelbrot
The Mandelbrot set is a set of complex numbers for which a particular sequence does not diverge to infinity.<br>
To understand the Mandelbrot fractal, we have to understand the different parts that compose it.

### Complex Numbers
A complex number is a number of the form *z = a + bi*, where:
- *a* is the real part
- *b* is the imaginary part
- *i* is the imaginary unit, staisfying *i<sup> 2</sup> = - 1*

### Mandelbrot Set
The Mandelbrot set is defined by iterating the function:<br>
*f<sub>c </sub>(z) = z<sup> 2 </sup> + c* <br>
where *c* is a complex number. Starting with *z<sub>0 </sub> = 0*, the sequence is: <br>
*z<sub> n + 1 </sub> = z<sub>n</sub><sup>2</sup> + c*

### COnvergence and Divergence
For each complex number *c*:
- If the sequence *{z<sub>n</sub>}* remains bounded (does not tend to infinity) as *n* goes to infinity, then *c* is in the Mendelbrot set.
- If the sequence *{z<sub>n</sub>}* tends to infinity, then *c* is not in the mendelbrot set.

### Practical Computation
In practive we cannot iterate the sequence infinitely, so we use a maximum number of iterators *N<sub>max</sub> to check if the sequence diverges. <br>We also use a bailout value *B* (often set to 2) because if *|z<sub>n</sub>|* ever excedes *B*, the sequence will diverge.

The steps to determine if a complex number *c* is in the Mandelbrot set are:
1. Set *z<sub>0</sub> = 0*.
2. Iterate *z<sub>n+1</sub> = z<sub>n</sub><sup>2</sup> + c* for *n = 0, 1, 2,..., N<sub>max</sub>.
3. If *|z<sub>n</sub>|* exceeds *B* at any point, *c* is not in the Mandelbrot set.
4. If after *N<sub>max</sub>* iterations *|z<sub>n</sub>|* has not exceeded *B*, *c* is considered to be in the mandelbrot set.

### Visualization
1. Map each pixel of an image to a complex number *c*.
2. Apply the iteration steps for each *c*.
3. Color the pixel based on whether *c* is in the Mandelbrot set and how quickly the sequence diverges.

## Julia Set
The Julia set is a fractal that is closely related to the Mandelbrot set. Both sets are defined in the context of complex dynamics, which studies the behavior of complex functions under iteration. It is defined for a given complex number *c* and consists of the set of complex numbers *z* that do not escape to infinity under the iteration *f(z) = z<sup> 2</sup> + c*.

### Math Details
1. Iteration Function<br>
*f(x) = z<sup> 2</sup> + c*<br>
Here, *z* is a complex number and *c* is a constant complex number.

2. Escaping to Infinity<br>
    - The point *z* is considered to have escaped to infinity if the magnutude of *z* exceeds a certain threshold (usually 2).
    - The number of iterations it takes for *z* to escape gives information about the structure of the Julia set.

3. Bounded and Unbounded Points<br>
    - Points *z* that remain bounded under iteration belon to the bounded Julia set.
    - The Julia set itself is the boundary of the filled Julia set.

### Visualizing the Julia Set
To visualize the Julia set, you iterate the function *f(z)* for each point in a grid of complex numbers, similar to the Mandelbrot set. The color of each point on the grid is determined by how quickly it scapes to infinity.

### COmparison with Mendelbrot Set
- The Mendelbrot set considers a grid of complex numbers *c* and checks the behavior of the function *f(z) = z<sup> 2</sup> + c* starting from *z = 0*.
- The Julia set fixes *c* and considers a grid of complex numbers *z*, iterating *f(z) = z <sup>2</sup> + c* for each *z*.

### Other Nice Values for *c*
- *c = 0.285 + 0.01i*
- *c = -0.4 + 0.6i*
- *c = 0.355 + 0.355i*
- *c = -1476*
- *c = 0.285*