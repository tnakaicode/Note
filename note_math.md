# Math

$$ \int_0 ^\infty \frac{1}{1 + x^2} \frac{1}{1 + x^N} dx $$

$$\begin{aligned}
  I &=& \int_0^\infty \frac{u^N}{(1+u^2)(1+u^N)} du \\
  &=& \int_0^\infty \frac{1 - 1 +u^N}{(1+u^2)(1+u^N)} du \\
  &=& - I + \int_0^\infty \frac{1}{(1+u^2)} du \\
  &=& - I + \frac{\pi}{2}
\end{aligned}$$

- $$ \nabla \cdot u = 0 $$
- $$ \mathrm{rot} \vec{E}  = - \frac{1}{c} \frac{\partial \vec{B}}{\partial t} $$
- $$ \mathrm{div} \vec{B}  = 0 $$
- $$ \mathrm{rot} \vec{B}  = \frac{1}{c} \frac{\partial \vec{E}}{\partial t} + \frac{4\pi}{c} \vec{j} $$
- $$ \mathrm{div} \vec{E}  = 4 \pi \rho_{\varepsilon } $$

## Symbol Perturbation method

It is determined how many points are required to define a single curve. The case where more points than the number are on the curve is called degeneration.  
It is natural to think that the input includes degeneration. In particular, if all the input points are grid points, many points will be on a straight line.  
Basically, the algorithm is designed in consideration of the degeneration, but when the degeneration is considered, the division is complicated, and it becomes more difficult to verify the validity of the algorithm. There is a perturbation method as a method for solving this.  
It is good to move all the points to eliminate the shrinkage in order to eliminate the shrinkage. However, if the points are moved too much, the set of points has a different topology from the original set of points.  
In addition, even if the user can move without changing the topology, another degeneration may occur.  
Further, it is important to make the moving distance minute, but if it is made too small, another problem is caused due to calculation errors.  
If a calculation time overhead is allowed, there is a calculation method having the same effect as effectively moving by a minute distance. (Symbol perturbation method)  
  
Consider a symbol perturbation method to avoid the degeneracy that three points are arranged on the same straight line.  
Given n points $p_1(x_1,y_1),p_2(x_2,y_2),...,p_n(x_n,y_n)$, each point $p_i(x_i,y_i)$ is converted to Move to $p_i^*$.  
  
$$ p_i^* (x_i + \epsilon^{M^i}, y_i + \epsilon^{M^i}) $$
  
Here, $M$ is a sufficiently large positive integer.  

## Generalized error analysis of regenerating kernel Hilbert space Gaussian process regression

Let the topological space $\Chi = \mathbb{R}^d$ be the input space. The normal distribution with mean $\mu\in\mathbb{R}$ and variance $\sigma^2\ge0$ on R is given by the density function $p(x)$.
$$ p (x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp(-\frac{(x-\mu)^2}{2\sigma^2}) $$
When $\sigma = 0$, it is a Dirac measure on the order of $\mu$.
