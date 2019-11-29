# RF

Frequency
|    Freq |        t [sec] |      t [ms] |   t [us] |  t [ns] |
| ------: | -------------: | ----------: | -------: | ------: |
|    1 Hz |        1.0 sec |
|    2 Hz |        0.5 sec |
|   1 kHz |   1 / 1000 sec |      1.0 ms |
|   5 kHz |   1 / 5000 sec |      0.2 ms |   200 us |
|  10 kHz | 1 / 10,000 sec |      0.1 ms |   100 us |
|  30 kHz | 1 / 30,000 sec |     0.03 ms |    33 us |
|   1 MHz |   1 / 10^6 sec | 1 / 1000 ms |     1 us |
|   1 GHz |   1 / 10^9 sec | 1 / 10^6 ms | 0.001 us |    1 ns |
| 100 GHz |  1 / 10^11 sec | 1 / 10^8 ms |          | 0.01 ns |

Frequency Wavelength Time
|    Freq |         Wave |     Time |
| ------: | -----------: | -------: |
|    1 Hz | 299,792.5 km |  1.0 sec |
|    2 Hz | 149,896.2 km |  0.5 sec |
|   1 kHz |   299.792 km |   1.0 ms |
|   5 kHz |    59.958 km |   0.2 ms |
|  10 kHz |    29.979 km |   0.1 ms |
|  30 kHz |     9.993 km |    33 us |
|   1 MHz |    299.792 m |     1 us |
|   1 GHz |   299.792 mm | 0.001 us |
| 100 GHz |     2.998 mm |  0.01 ns |
| 200 GHz |     1.499 mm | 0.005 ns |

Conductivity
|      Material       | class          | $\sigma$ [S/m] |
| :-----------------: | :------------- | -------------: |
|    Fused Quartz     | Insulator      |      ~ 1.0E-17 |
|     Ceresin Wax     | Insulator      |      ~ 1.0E-17 |
|   Distilled Water   | Insulator      |       ~ 1.0E-4 |
|        GaAs         | Semi-Conductor |      ~ 2.38E-7 |
|      Sapphire       | Semi-Conductor |       ~ 5.5E-4 |
|     Micro-Fiber     | Semi-Conductor |       ~ 7.8E-4 |
|     Fresh Water     | Semi-Conductor |       ~ 1.0E-2 |
| Human Animal Tissue | Semi-Conductor |    ~ 0.2 - 0.7 |
| Intrinsic Germanium | Semi-Conductor |        ~ 2.227 |
|      Sea Water      | Semi-Conductor |          ~ 4.0 |
|    Silicon Steel    | Conductor      |         2.0E+6 |
|        Gold         | Conductor      |         4.1E+7 |
|       Copper        | Conductor      |        5.76E+7 |
|       Silver        | Conductor      |         6.1E+7 |

Dierectric
|     Material     | $\epsilon'_r$ | $\tan(\delta)$ |
| :--------------: | ------------: | -------------: |
|       Air        |        1.0006 |
|      Nylon       |           3.5 |         2.0E-2 |
|      Rubber      |        2.5E-3 |         2.0E-3 |
|   Fused Silica   |           3.8 |         7.5E-4 |
|     Sillicon     |          11.8 |
|      Teflon      |           2.1 |         3.0E-4 |
| Distrilled Water |            80 |         4.0E-2 |
|    Sea Water     |            81 |           4.62 |
| Dehydrated Water |             1 |              0 |

## Waveguide

### Rectanguler Waveguide

<https://www.everythingrf.com/tech-resources/waveguides-sizes>
![waveguide](./waveguide.jpg)

| EIA | Band [GHz] | Cutoff Low | Cutoff Next |      A x B [mm] |
| --- | ---------: | ---------: | ----------: | --------------: |
| WR5 |  140 ~ 220 |    115.714 |     231.429 | 1.2954 x 0.6477 |
| WR6 |  110 ~ 170 |     90.791 |     181.583 |  1.651 x 0.8255 |
| WR7 |  110 ~ 170 |     90.791 |     181.583 |  1.651 x 0.8255 |
| WR8 |   90 ~ 140 |     73.768 |     147.536 |  2.032 x 1.0160 |

- Waveguide Standard
  - MIL-Spec - United States Military Standard
  - IEC - International Electrotechnical Commission
  - EIA - Electronic Industries Alliance
  - RCSC - Radio Components Standardization Committee

### Circuler Waveguide

- [waveguide](https://www.qwed.eu/CircularWaveguides.pdf)
- Cutoff
  - $$ f_{c, m, n} = \frac{\nu}{2 \pi} \beta_{c, m, n} $$
- TE (H) - mode
  - $$ \beta_{c, m, n} = \frac{\chi^{'}_{m, n}}{a} $$
- TM (E) - mode
  - $$ \beta_{c, m, n} = \frac{\chi_{m, n}}{a} $$
- $TE_{11}$ mode
  - $$ f_{c, TE_{1, 1}} = \frac{c}{2 \pi} \beta_{c, TE_{1, 1}} = \frac{c}{2 \pi} \frac{\chi^{'}_{m, n}}{a} $$
- $TM_{01}$ mode
  - $$ f_{c, TM_{0, 1}} = \frac{c}{2 \pi} \beta_{c, TM_{0, 1}} = \frac{c}{2 \pi} \frac{\chi_{m, n}}{a}$$

### Corrugated Circuler Waveguide

### Coaxial Waveguide

- [ref1]

## Optics

- Field Expressions for the Electric and Magnetic short dipoles
- well known (e.g. [Stratton, 1941] or [Hansen, 1988].
- Here we will only give the expression for the Huygens source at large distances r,
- $$ E (r, \theta, \phi) = E_0 \frac{\exp(-jkr)}{r} (1 + \cos\theta) (\cos\phi\hat{\Theta} - \sin\phi\hat{\Phi} ) $$
- complex position $(x, y, z) = (0, 0, 0 - jb)$
  - $$ R = \sqrt{x^2 + y^2 + z^2 -b^2 + 2jbz} $$
- In Case,
  - $$ \rho^2 = \sqrt{x^2+y^2} $$
  - $$ z = r\cos \theta $$
  - $$ b \ll r = \sqrt{x^2 + y^2 + z^2} $$
  - Find
  - $$ R \cong \sqrt{ r^2 + j2br\cos\theta} \cong r + jb\cos\theta $$
  - Re-Define
  - $$ u = \exp(kb\cos\theta) \frac{\exp(-jkr)}{r} $$
  - $$ E (r, \theta, \phi) = N_f \exp(kb\cos\theta) \frac{\exp(-jkr)}{kr} (1 + \cos\theta) (\cos\phi\hat{\Theta} - \sin\phi\hat{\Phi} ) $$
  - Beam width is controlled by the parameter $b$
  - set $AdB (A < 0)$ at angle $\theta$
  - $$ b = \frac{20 \log_{10}((1+\cos\theta)/2) - A}{20k(1-\sin\theta)\log_{10}e} $$
  - $$ A = 20 \log_{10}((1+\cos\theta)/2) - 20bk(1-\sin\theta)\log_{10}e$$

### Gaussian Optics

## MoM

- The integral equation used for PEC objects is known
  - as the Mixed-Potential Electric Field Integral Equation (EFIE) formulation.
  - $$ \hat{n} \times E^{i} = \hat{n} \times L_{0} J_{s} $$
  - $$ L_{0}J_{S} = j\omega\mu_0 (\int_{S} J_{S}(r')G_{0}(r, r') dS' + \frac{1}{k_0^2}\int_{S} \nabla_{S}^{'}\cdot J_{S}(r') \nabla G_{0}(r, r') dS') $$
- Galerkin Finite Element Method

### Circularly polarized antenna

TE Mode: The electric field is perpendicular to the propagation direction, and there is no electric field component in the propagation direction.
In the xz-plane, the composition of $H_x$ and $H_y$ is oblique with respect to the z-axis, so the Poynting Vector is oblique with respect to the z-axis. The propagating wave travels while repeating reflection on the wall surface of the waveguide.
Due to this property, the waveguide has an in-tube wavelength in the z-axis direction.
The cutoff frequency determined by the boundary condition of the waveguide outer wall is determined by the cross-sectional length of the waveguide and the relative dielectric constant inside the waveguide.
A rectangular waveguide has the same cutoff frequency in TE Mode and TM Mode, but this state is called degeneracy.

$$ \frac{E_x^2}{|E_x|^2} - 2 \frac{E_x E_y}{|E_x||E_y|} \cos(\delta) + \frac{E_y^2}{|E_y|^2} = \sin^2(\delta) $$
$$ E_x = |E_x| \cos(\omega t) \cos(\delta_x) - |E_x| \sin(\omega t) \sin(\delta_x)$$
$$ E_y = |E_y| \cos(\omega t) \cos(\delta_y) - |E_y| \sin(\omega t) \sin(\delta_y)$$

Phaser
$$ \bm{E}(z) = \left[ \begin{array}{c}
  E_x \\
  E_y
\end{array} \right] = \left[ \begin{array}{c}
  |E_x| \exp^{j \delta_x} \\
  |E_y| \exp^{j \delta_y}
\end{array} \right] \exp^{-jkz} = \left[ \begin{array}{c}
  |E_x| \\
  |E_y| \exp^{j\delta}  
\end{array} \right] \exp^{-jkz} $$

LHCP: Left Hand Circuler Pol
$$ \bm{E_L}(z) = \frac{1}{\sqrt{2}} \left[ \begin{array}{c}
  1 \\
  j
\end{array} \right] $$

RHCP: Right Hand Circuler Pol
$$ \bm{E_R}(z) = \frac{1}{\sqrt{2}} \left[ \begin{array}{c}
  1 \\
  -j
\end{array} \right] $$

Jones Vectro
$$ \left[ \begin{array}{c}
  E_L \\
  E_R
\end{array} \right] = \frac{1}{\sqrt{2}} \left[ \begin{array}{cc}
  1 & j \\
  1 & -j
\end{array} \right] \left[ \begin{array}{c}
  E_x \\
  E_y
\end{array} \right] $$

Stokes Parameter
$$ \bm{S} = \left[ \begin{array}{l}
  S_0 = |E_x|^2 + |E_y|^2 = A^2 \\
  S_1 = |E_x|^2 - |E_y|^2 = A^2 \cos(2\tau) \cos(2\epsilon) \\
  S_2 = 2|E_x||E_y|^2 \cos(\delta) = A^2 \sin(2\tau) \cos(2\epsilon) \\
  S_3 = 2|E_x||E_y|^2 \sin(\delta) = A^2 \sin(2\epsilon)
\end{array} \right] $$

AR: Axis Ratio
$$ AR = \sqrt{\frac{|E_x|^2 \cos^2(\tau) + |E_x||E_y| \sin(2\tau)\cos(\delta) + |E_y|^2 \sin^2(\tau)}{|E_x|^2 \sin^2(\tau) - |E_x||E_y| \sin(2\tau)\cos(\delta) + |E_y|^2 \cos^2(\tau)}} $$

AR may be displayed in db. $AR<3Db$ is often circularly polarized, but AR is closely related to the cross-polarization discrimination XPD, which indicates the magnitude of the difference between the main polarization and cross-polarization.
The evaluation value of AR should be determined taking into account the effect of polarization loss between the transmitting and receiving antennas.

## Irregular Waveguide

Gyro-K, Opti-K, Gyro-KL

Consider the problem of excitation of uniformly filled irregular waveguide, the side surface of which $S_b$ differentfrom regular cylidical surface.

$$ \mathrm{rot}{\bm H} = \epsilon_0 \frac{\partial \bm E}{\partial t} + \bm J $$
$$ \mathrm{rot}{\bm E} = - \mu_0 \frac{\partial \bm H}{\partial t}$$
$$ \left.\left[\bm n, \bm E \right] \right|_{S_b} = \sqrt{\frac{\mu_{\sigma}}{\pi\sigma} } \int_0^t \frac{\partial \left. \left[\bm n, \left[ \bm H, \bm n \right] \right] \right|_{S_b}}{\partial\tau} \frac{d\tau}{\sqrt{t-\tau}} $$

- $\sigma$ - Waveguide Conductivity
- $\mu_{\sigma}$ - Waveguide Magnetic permeability

The Diensity of electric currents $J$ is determined by electron flux.

Introduce a curvilinear coordinate system $\left(r,\phi,s\right)$, connected with waveguide geometry.

- $r,\phi$ - polar coordinate in plane of cross section of waveguide
- $s$ - the arc length of the axis of waveguide

We Call

- $\bm t = \bm r' / |\bm r'|$ - unit vector tangent to waveguide axis
- $\bm n = \bm r'' / |\bm r''| = 1 / k \cdot r''$ - unit normal to waveguide axis
- $\bm b = \bm t \times \bm n$ - binormal to waveguide axis

By Frennes-Serre,

- $\bm t = k \cdot \bm n$
- $\bm n' = -k \cdot t + \tau \cdot \bm b$
- $\bm b' = -\tau \cdot \bm n$
- where
  - $k = 1 / \rho_k = |\bm r''|$ - angular velocity of rotation of the tangent around the binormal
  - $\rho_k$ - radius of curvature
  - $\tau = 1 / \rho_\tau = 1 / k[\bm r'\cdot\bm r''\cdot\bm r''']$ - rotational velocity of binormal round tangent
  - $\rho_\tau$ - torison radius

Certsian rectangular coordinate $(x, y, z)$ inside waveuide are assosiated with entered coordiate $(r, \phi, s)$ using following relation:

$$ \rm r(\rho, \phi, s) = \bm R(s) + \rho r_b(\phi, s) \{ \bm n(s)\cos(\phi) + \bm b(s) \sin(\phi) \} $$

- $\bm r$ - radius-vector of arbitrary point inside waveguide
- $\bm R(s)$ - equation of waveguide axis in Certesian coordinate
- $n(s), b(s)$ - unit vectors of main normal and binormal axis of waveguide
