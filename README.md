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
After OpenFOAM is installed, you need to install **ITHACA-FV**, a library for reduced-order modeling in fluid dynamics. ITHACA-FV is required to run this project. You can find more information about the ITHACA-FV repository and its installation details, please refer [here](https://github.com/giovastabile/ITHACA-FV).





## Project Structure

The repository is divided into three main folders to organize the different scripts, results, and changes for running the simulation with different Radial Basis Functions (RBFs) incorporated into data assimilation.

### 1. `Changed codes`
This folder contains some modified files that need to be replaced in the ITHACA-FV. These files have been altered to incorporate the changes necessary for running the data assimilation with the selected RBF methods.


#### Instructions for Replacing Files:

1. After cloning the ITHACA-FV repository, navigate to the following directory inside the cloned ITHACA-FV repo:

    ```bash
    cd ITHACA-FV/src/
    ```

2. Replace the following files with the corresponding files in the `Changed codes` folder:
    - Replace `ensembleClass.C` with the modified `ensembleClass.C` from the `Changed codes` folder.
    - Replace `ensembleClass.H` with the modified `ensembleClass.H` from the `Changed codes` folder.

    Use the following commands to copy and replace the files:

    ```bash
    cp /path/to/your/repo/Changed\ codes/ensembleClass.C ITHACA-FV/src/
    cp /path/to/your/repo/Changed\ codes/ensembleClass.H ITHACA-FV/src/
    ```

    **Explanation**:
    - Replace `/path/to/your/repo/` with the actual path where you have cloned your repository containing the `Changed codes` folder.
    - The `cp` command copies the modified `ensembleClass.C` and `ensembleClass.H` files from the `Changed codes` folder to the `ITHACA-FV/src/` directory, replacing the original files.

3. Once the files are replaced, recompile the ITHACA-FV library to ensure the changes take effect:


### 2. `Data Assimilation _Multiquadric-RBF`
This folder contains:
- **Main Scripts**: The scripts required to run the data assimilation simulation using **Multiquadric Radial Basis Functions (RBFs)**.
- **Results**: The results from running the simulations, including relevant figures and plots.
- **Figures**: Figures and visualizations included in the paper.

To run the simulation with the **Multiquadric RBF**, navigate to the `Data Assimilation _Multiquadric-RBF` folder and execute the following script:

```bash
cd Data\ Assimilation\ _Multiquadric-RBF
python main.py


### 3. `Data Assimilation _Gaussian-RBF`
This folder contains:
- **Main Scripts**: The scripts required to run the data assimilation simulation using Gaussian Radial Basis Functions (RBFs).
- **Results**: The results from running the simulations, including relevant figures and plots.
- **Figures**: Figures and visualizations included in the paper.

To run the simulation with the **Gaussian RBF**, navigate to the `Data Assimilation _Gaussian-RBF` folder and execute the following script:

```bash
cd Data\ Assimilation\ _Gaussian-RBF
python main.py
