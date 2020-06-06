# OpenFOAM

## Build

```markdown
git clone https://develop.openfoam.com/Development/OpenFOAM-plus.git
cd OpenFOAM-plus
git submodule add https://develop.openfoam.com/Development/ThirdParty-plus.git ThirdParty
git submodule update -i
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

## MHD (EHD)
