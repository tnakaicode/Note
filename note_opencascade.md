# OpenCASCADE

## Build

* .hxx - this is the user header file to be included by your C++ code
* .cxx - this is the actual C++ implementation code compiled into the OpenCASCADE library
* .lxx - these are inline methods included by the .hxx file. This keeps the implementation of inline methods out of the user header file.
* .gxx - this is the actual C++ implementation code for generic classes.The same class will never have both a .cxx and .gxx.
* .ixx - user head file for an entire package included by the package level .cxx file
* .jxx - user header file for secondary classes of a package included by the package level .cxx file.

## Python Wrap

* [OCC](https://salsa.debian.org/kkremitzki-guest/opencascade.git)
  * OpenCASCADE 7.0
* [OCE](https://github.com/tpaviot/oce.git)
  * OpenCASCADE 6.9
* [SMESH](https://github.com/tpaviot/smesh.git)
* [PythonOCC](https://github.com/tpaviot/pythonocc-core.git)
* [PythonOCC-Utils](https://github.com/tpaviot/pythonocc-utils.git)
* [PythonOCC-DEMO](https://github.com/tpaviot/pythonocc-demos.git)

### Build Error

``` Error
TKMeshVS
```
