# Dealii

## Build

- [deal.ii](https://github.com/dealii/dealii.git)
- [pymor](https://github.com/pymor/pymor.git)
- [pymor-dealii](https://github.com/pymor/pymor-deal.II.git)
- [meep](https://github.com/NanoComp/meep)

```bash
sudo apt install libpetsc-complex-dev petsc-dev
cmake -DDEAL_II_WITH_PETSC=OFF -DDEAL_II_PETSC_WITH_COMPLEX=OFF -DDEAL_II_WITH_P4EST=OFF -DDEAL_II_WITH_TRILINOS=OFF ..
```

## Step-61 Weak Galerkin scheme
