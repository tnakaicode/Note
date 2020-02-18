# OpenCASCADE

## Build

- .hxx - this is the user header file to be included by your C++ code
- .cxx - this is the actual C++ implementation code compiled into the OpenCASCADE library
- .lxx - these are inline methods included by the .hxx file. This keeps the implementation of inline methods out of the user header file.
- .gxx - this is the actual C++ implementation code for generic classes.The same class will never have both a .cxx and .gxx.
- .ixx - user head file for an entire package included by the package level .cxx file
- .jxx - user header file for secondary classes of a package included by the package level .cxx file.

## Python Wrap

- [OCC](https://salsa.debian.org/kkremitzki-guest/opencascade.git)
  - OpenCASCADE 7.0
- [OCE](https://github.com/tpaviot/oce.git)
  - OpenCASCADE 6.9
- [SMESH](https://github.com/tpaviot/smesh.git)
- [PythonOCC](https://github.com/tpaviot/pythonocc-core.git)
- [PythonOCC-Utils](https://github.com/tpaviot/pythonocc-utils.git)
- [PythonOCC-DEMO](https://github.com/tpaviot/pythonocc-demos.git)
- OpenGL
  - freeglut3-dev
  - liboce-visualization11
  - opengl-4-man-doc
- conda install -c conda-forge -c dlr-sc -c pythonocc -c oce pythonocc-core smesh

```Markdown
conda install -c conda-forge pyopengl tk freetype vtk freeglut tbb mayavi sdl2
conda install -c dlr-sc freeimage freeimageplus gl2ps
conda install -c intel libpng tcl
```

### Build Error

### Explain

- Geom_BoundedSurface
  - <https://www.opencascade.com/doc/occt-7.4.0/refman/html/class_geom___bounded_surface.html>
  - The root class for bounded surfaces in 3D space.
  - A bounded surface is defined by a rectangle in its 2D parametric space
