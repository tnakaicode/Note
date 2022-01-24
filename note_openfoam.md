# 1. OpenFOAM

- reactingParcelFilmFoam
- MHD
- MincraftでモデリングOpenFoamで風を吹かせて解析
- 熱平衡・高温高圧では、中性子・陽子は古典的粒子として扱える
  - Maxwell Boltzmann

## 1.1. Build

```bash
# OpenFOAM-Plus
git clone https://develop.openfoam.com/Development/OpenFOAM-plus.git
cd OpenFOAM-plus
git submodule add https://develop.openfoam.com/Development/ThirdParty-plus.git ThirdParty
git submodule update -i

# OpenFOAM
git clone https://develop.openfoam.com/Development/openfoam.git
```

Thirdparty

```bash
wget https://gforge.inria.fr/frs/download.php/file/37622/scotch_6.0.6.tar.gz
wget http://algo2.iti.kit.edu/schulz/software_releases/KaHIP_2.00.tar.gz
wget http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/metis-5.1.0.tar.gz
wget https://dl.bintray.com/boostorg/release/1.64.0/source/boost_1_64_0.tar.gz
wget ftp://ftp.fftw.org/pub/fftw/fftw-3.3.7.tar.gz
wget https://github.com/CGAL/cgal/archive/releases/CGAL-4.9.1.tar.gz
git clone https://github.com/ornladios/ADIOS2.git ADIOS2-git
```

```markdown
source etc/bashrc
./Allwmake
```

## 1.2. MHD (EHD)

## 1.3. Flow Electrificationin

- Flow Electrificationin
- 流動帯電
- 油を流動させることにより油及び絶縁物が帯電　流動帯電
- 外部から電圧を与えなくても局部的な高電界部位を生じる
- 油中放電を起こすことがある
- 油中の正・負イオンの固体への吸着エネルギーの差により負イオンが固体絶縁物により多く吸着される
  - 結果として油中に残留正イオンが分布する
  - 油中正電荷密度の分布は,油が静止しているときには,導電電流と拡散電流との平衡の結果決定される
- 基礎的な事項
  - 流れの状態と電荷発生量の関係
  - 漏れ電流　/　レイノルズ数
  - デバイ長 $\delta$ 電場を遮断するのに必要な長さ
  - 油の誘電率 $\epsilon$
  - 油の導電率 $\kappa$
  - 油中油中電荷密度分布
    - $q = \sigma_0 / \delta \exp( -(x-s)/\delta )$
  - 十分長いパイプ中で油が流動した際の帯電量
    - 電荷密度分布と速度分布の積
- 油中放電
  - 油にかかる電界が油の絶縁破壊強度を超えたときに発生する
- <https://github.com/fppimenta/rheoTool.git>
  - governing isothermal 等温
  - single-phase 単相交流
  - transient flows 一時的な流れ
  - under laminar conditions 層流条件
  - for incompressible fluids 非圧縮性流れ
  - in static grids
  - weak electrolyte
    - 弱電解質
    - 弱酸・弱塩基
    - 一部の分子だけが分離
    - 中性分子とイオンの間に化学平衡が成立
  - Mass Conservation
    - 質量保存
    - $$ \nabla \cdot u = 0 $$
  - Momentum balance
    - $$ \rho ( \frac{\partial u}{\partial t} + u \cdot \nabla u) = - \nabla p + \nabla \dot{\tau} + f$$
    - $$ f = f_E = \nabla [ \epsilon (EE - \frac{E^2}{2}I )] = \rho_E E - \frac{E^2}{2} \nabla \epsilon $$
  - PNP Model
    - Poisson-Nernst-Planck model
    - Absence of Magnetic effect
    - The standard law governing
      - the transport of charged species in aweak electrolyte,
      - under the action of an electric field
      - neglecting any reaction

## 1.4. PETSc/Tao

- Portable, Extensible Toolkit for Scientific Computation
- <https://www.mcs.anl.gov/petsc/index.html>
  - MLSVM Multilevel Support Vector Machines with PETSc.
  - PermonSVM support vector machines and PermonQP quadratic programming
  - MOOSE - Multiphysics Object-Oriented Simulation Environment FEM
    - built on top of libMesh and PETSc
  - SLEPc - Scalable Library for Eigenvalue Problems
  - COOLFluiD - CFD, plasma and multi-physics simulation package
  - Fluidity - a finite element/volume fluids code
  - OpenFVM - finite volume based CFD solver
  - OOFEM - object oriented finite element library
  - libMesh - adaptive finite element library
  - FEniCS - sophisticated Python based finite element simulation package
  - Firedrake - sophisticated Python based finite element simulation package
  - DEAL.II - sophisticated C++ based finite element simulation package
  - PHAML - The Parallel Hierarchical Adaptive MultiLevel Project
  - Chaste - Cancer, Heart and Soft Tissue Environment
  - PyClaw - A massively parallel, high order accurate, hyperbolic PDE solver
  - PetIGA - A framework for high performance Isogeometric Analysis
  - MFEM - lightweight, scalable C++ library for finite element methods
  - FreeFEM - finite element PDE solver with embedded domain specific language
  - Python Bindings
    - petsc4py (documentation) from Lisandro Dalcin at KAUST
