---
title: Phase Re-Construction
---

- [1. 3D FFT Filtering](#1-3d-fft-filtering)
- [2. Phase recovery method](#2-phase-recovery-method)

## 1. 3D FFT Filtering

1. some focus image
2. Each Fourier Spectrum
   1. by 2D-FFT
3. Fourier Transform to Focus axis
4. 3D inv-FFT

## 2. Phase recovery method

- Fienup iteration
  - コヒーレント結像系の回折面と像面の振幅分布から位相分布を反復的に求める方法
  - Iteratively obtain the phase distribution from the diffraction distribution of the coherent imaging system and the amplitude distribution of the image plane
  - Gerchberg-Saxton
  - Method of phase recovery using only the amplitude distribution of the diffractive surface and the known condition of the object
  - The complex amplitude function of the diffractive surface obtained from the random phase and the observed amplitude distribution is used as the initial value,
  - and the object function obtained by inverse Fourier transform is shaped by giving known conditions
    - such as range of spread and non-negativeness.
  - Then, the phase of the complex amplitude function obtained by Fourier transform of the resulting object function is left unchanged and only the amplitude is replaced with the observed value,
  - and the object obtained by inverse Fourier transform of the modified complex amplitude function is further shaped under known conditions Cycle
- X-ray typography
  - A narrowed illumination beam narrower than the spread of the object is moved vertically and horizontally with some overlap in the illumination area,
  - and multiple diffraction intensity distributions are measured. How to calculate an iterative algorithm while sharing
- Method by strength transport equation
- x-ray diffraction microscopy <http://xrm.phys.northwestern.edu/research/pdf_papers/2007/rodenburg_prl_2007.pdf>
- <https://www.mpl.mpg.de/divisions/guck/software/>
  - Atomic force microscopy <https://nanite.readthedocs.io/en/stable/>
  - Optical diffraction tomography (ODT)
