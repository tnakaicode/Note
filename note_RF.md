# RF

Frequency
| Freq    | second [sec]   | second [ms] | second [us] | second [ns] |
| ------- | -------------- | ----------- | ----------- | ----------- |
| 1 Hz    | 1.0 sec        | -           | -           |
| 2 Hz    | 0.5 sec        | -           | -           |
| 1 kHz   | 1 / 1000 sec   | -           | -           |
| 5 kHz   | 1 / 5000 sec   | 0.2 ms      | 200 us      |
| 10 kHz  | 1 / 10,000 sec | 0.1 ms      | 100 us      |
| 30 kHz  | 1 / 30,000 sec | 0.03 ms     | 33 us       |
| 1 MHz   | 1 / 10^6 sec   | 1 / 1000 ms | 1 us        |
| 1 GHz   | 1 / 10^9 sec   | 1 / 10^6 ms | 0.001 us    | 1 ns        |
| 100 GHz | 1 / 10^11 sec  | 1 / 10^8 ms | -           | 0.01 ns     |

Frequency Wavelength Time
| Freq    | Wave         | Time     |
| ------- | ------------ | -------- |
| 1 Hz    | 299,792.5 km | 1.0 sec  |
| 2 Hz    | 149,896.2 km | 0.5 sec  |
| 1 kHz   | 299.792 km   | 0.1 sec  |
| 5 kHz   | 59.958 km    | 0.2 ms   |
| 10 kHz  | 29.979 km    | 0.1 ms   |
| 30 kHz  | 9.993 km     | 33 us    |
| 1 MHz   | 299.792 m    | 1 us     |
| 1 GHz   | 299.792 mm   | 0.001 us |
| 100 GHz | 2.998 mm     | 0.01 ns  |
| 200 GHz | 1.499 mm     | 0.005 ns |

## Waveguide

### Rectanguler Waveguide

<https://www.everythingrf.com/tech-resources/waveguides-sizes>
![waveguide](./waveguide.jpg)

| EIA | Band [GHz] | Cutoff Low | Cutoff Next | A x B [mm]      |
| --- | ---------- | ---------- | ----------- | --------------- |
| WR5 | 140 ~ 220  | 115.714    | 231.429     | 1.2954 x 0.6477 |
| WR6 | 110 ~ 170  | 90.791     | 181.583     | 1.651 x 0.8255  |
| WR7 | 110 ~ 170  | 90.791     | 181.583     | 1.651 x 0.8255  |
| WR8 | 90 ~ 140   | 73.768     | 147.536     | 2.032 x 1.016   |

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
