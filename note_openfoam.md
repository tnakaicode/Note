# OpenFOAM

## Build

``` git
git clone https://develop.openfoam.com/Development/OpenFOAM-plus.git
cd OpenFOAM-plus
git submodule add https://develop.openfoam.com/Development/ThirdParty-plus.git ThirdParty
git submodule update -i
```

``` build
source etc/bashrc
./Allwmake
```

## MHD (EHD)
