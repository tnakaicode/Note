# OpenCASCADE

## Build

* .hxx - this is the user header file to be included by your C++ code
* .cxx - this is the actual C++ implementation code compiled into the OpenCASCADE library
* .lxx - these are inline methods included by the .hxx file. This keeps the implementation of inline methods out of the user header file.
* .gxx - this is the actual C++ implementation code for generic classes.The same class will never have both a .cxx and .gxx.
* .ixx - user head file for an entire package included by the package level .cxx file
* .jxx - user header file for secondary classes of a package included by the package level .cxx file.

## Pyhto Wrap

* [OCC](https://salsa.debian.org/kkremitzki-guest/opencascade.git)
* [OCE](https://github.com/tpaviot/oce.git)
* [SMESH](https://github.com/tpaviot/smesh.git)
* [OCC](https://github.com/tpaviot/pythonocc-core.git)
* [utils](https://github.com/tpaviot/pythonocc-utils.git)
* [DEME](https://github.com/tpaviot/pythonocc-demos.git)
