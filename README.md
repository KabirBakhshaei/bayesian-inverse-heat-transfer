# bayesian-inverse-heat-transfer
Optimized Bayesian framework for real-time inverse heat transfer problem estimation using reduced order methods and data assimilation.

# Bayesian-Inverse-Heat-Transfer

## Overview
This repository contains the code and data for the paper **"Optimized Bayesian Framework for Inverse Heat Transfer Problems Using Reduced Order Methods."** This framework aims to provide accurate, real-time estimation of the heat flux in Continuous Casting machinery using Bayesian methods combined with Reduced Order Models (ROMs) and Data Assimilation techniques.

## Abstract
Accurate real-time prediction of the heat flux is imperative for the smooth operation of Continuous Casting machinery at the boundary region where the mold and molten steel meet, which is not physically measurable. A stochastic inverse heat transfer problem is formulated to infer the transient heat flux treated as an unknown Neumann boundary condition. Our research represents a significant contribution to achieving probabilistic boundary condition estimation in real-time, handling noisy measurements, and dealing with errors in the model.

## Installation
To run the code, follow these steps:

### 1. Install OpenFOAM
First, ensure that **OpenFOAM** is installed on your system. You can follow the official installation guide for your operating system from the [OpenFOAM website](https://www.openfoam.com/download).

Supported versions:
- [OpenFOAM 2106](https://www.openfoam.com/news/main-news/openfoam-v2106)
- [OpenFOAM 2212](https://www.openfoam.com/news/main-news/openfoam-v2212)
- [OpenFOAM 2306](https://www.openfoam.com/news/main-news/openfoam-v2306)
- [OpenFOAM 2312](https://www.openfoam.com/news/main-news/openfoam-v2312)


### 2. Install ITHACA-FV
After OpenFOAM is installed, you need to install **ITHACA-FV**, a library for reduced-order modeling in fluid dynamics. ITHACA-FV is required to run this project. You can find the ITHACA-FV repository [here](https://github.com/giovastabile/ITHACA-FV).


To install ITHACA-FV:
```bash
# Clone the repository
git clone https://github.com/giovastabile/ITHACA-FV.git
cd ITHACA-FV

# Initialize submodules and source the bashrc
git submodule update --init
source etc/bashrc

# Compile the library
./Allwmake

# Follow the installation instructions in the ITHACA-FV repository
