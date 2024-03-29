---
title: OpenCASCADE
---

- [1. Install](#1-install)
- [2. Build](#2-build)
- [3. Python Wrap](#3-python-wrap)
  - [3.1. Build Error](#31-build-error)
  - [3.2. Explain](#32-explain)
- [4. DICE](#4-dice)

## 1. Install

```bash
# python=3.7
conda install -c dlr-sc pythonocc-core=7.4.0

# python=3.8
conda install -c conda-forge pythonocc-core=7.4.0
```

## 2. Build

- .hxx - this is the user header file to be included by your C++ code
- .cxx - this is the actual C++ implementation code compiled into the OpenCASCADE library
- .lxx - these are inline methods included by the .hxx file. This keeps the implementation of inline methods out of the user header file.
- .gxx - this is the actual C++ implementation code for generic classes.The same class will never have both a .cxx and .gxx.
- .ixx - user head file for an entire package included by the package level .cxx file
- .jxx - user header file for secondary classes of a package included by the package level .cxx file.

## 3. Python Wrap

- [OCC](https://salsa.debian.org/kkremitzki-guest/opencascade.git)
  - OpenCASCADE 7.0
- [OCE](https://github.com/tpaviot/oce.git)
  - OpenCASCADE 6.9
- [SMESH](https://github.com/tpaviot/smesh.git)
- [PythonOCC](https://github.com/tpaviot/pythonocc-core.git)
- [PythonOCC-Utils](https://github.com/tpaviot/pythonocc-utils.git)
- [PythonOCC-DEMO](https://github.com/tpaviot/pythonocc-demos.git)
- [OCCT](https://github.com/LaughlinResearch/pyOCCT.git)
  - <https://github.com/tnakaicode/pythonocct.git>
  - <https://pyocct.readthedocs.io/en/latest/index.html>
- [AFEM](https://github.com/LaughlinResearch/AFEM.git)
  - <https://github.com/tnakaicode/pythonocct-afem.git>
  - <https://github.com/tnakaicode/pythonocct.git>
  - <https://github.com/tnakaicode/AFEM-OCC.git>
- [Netgen](https://ngsolve.org/docu/latest/i-tutorials/index.html)
  - conda install -c conda-forge -c ngsolve ngsolve
- [Nastran]
- OpenGL
  - freeglut3-dev
  - liboce-visualization11
  - opengl-4-man-doc
- conda install -c conda-forge -c dlr-sc pythonocc-core
  - python=3.7.6
  - python=3.8
- conda install -c laughlinresearch pyocct
  - python=3.6.7

```bash
conda install -c conda-forge pyopengl tk freetype vtk freeglut tbb mayavi sdl2
conda install -c dlr-sc freeimage freeimageplus gl2ps
conda install -c intel libpng tcl
```

### 3.1. Build Error

### 3.2. Explain

- Geom_BoundedSurface
  - <https://www.opencascade.com/doc/occt-7.4.0/refman/html/class_geom___bounded_surface.html>
  - The root class for bounded surfaces in 3D space.
  - A bounded surface is defined by a rectangle in its 2D parametric space

## 4. DICE
