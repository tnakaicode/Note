---
title: Dealii
---

- [1. Build](#1-build)
- [2. Step-61 Weak Galerkin scheme](#2-step-61-weak-galerkin-scheme)
- [3. with OpenFOAM](#3-with-openfoam)

## 1. Build

- [deal.ii](https://github.com/dealii/dealii.git)
- [pymor](https://github.com/pymor/pymor.git)
- [pymor-dealii](https://github.com/pymor/pymor-deal.II.git)
- [meep](https://github.com/NanoComp/meep)

```bash
sudo apt install libpetsc-complex-dev petsc-dev
cmake -DDEAL_II_WITH_PETSC=OFF -DDEAL_II_PETSC_WITH_COMPLEX=OFF -DDEAL_II_WITH_P4EST=OFF -DDEAL_II_WITH_TRILINOS=OFF ..
```

## 2. Step-61 Weak Galerkin scheme

## 3. with OpenFOAM

- <https://medium.com/@mustafaabbs2/setting-up-a-fluid-structure-interaction-workflow-with-openfoam-and-deal-ii-80718f2e2e0e>
