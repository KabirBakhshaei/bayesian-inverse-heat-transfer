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

1. **Replace files in the ITHACA-FV repository**:

    a. Inside `ITHACA-FV/src/`, replace `ensembleClass.C`, `ensembleClass.H`, `muq2ithaca.C`, and `muq2ithaca.H` with the corresponding files from the `Changed codes` folder:

    ```bash
    cp /path/to/your/repo/Changed\ codes/ensembleClass.C ITHACA-FV/src/
    cp /path/to/your/repo/Changed\ codes/ensembleClass.H ITHACA-FV/src/
    cp /path/to/your/repo/Changed\ codes/muq2ithaca.C ITHACA-FV/src/
    cp /path/to/your/repo/Changed\ codes/muq2ithaca.H ITHACA-FV/src/
    ```

    b. Inside `ITHACA-FV/src/Fang2017filter_wDF`, replace `Fang2017filter_wDF.C` and `Fang2017filter_wDF.H` with the corresponding files from the `Changed codes` folder:

    ```bash
    cp /path/to/your/repo/Changed\ codes/Fang2017filter_wDF.C ITHACA-FV/src/Fang2017filter_wDF/
    cp /path/to/your/repo/Changed\ codes/Fang2017filter_wDF.H ITHACA-FV/src/Fang2017filter_wDF/
    ```
    c. Inside `ITHACA-FV-KF/src/ITHACA_FOMPROBLEMS/sequentialIHTP`, replace `sequentialIHTP.C`, `sequentialIHTP.H`, and `createThermocouples.H` with the corresponding files from the `Changed codes` folder:

    ```bash
    cp /path/to/your/repo/Changed\ codes/sequentialIHTP.C ITHACA-FV-KF/src/ITHACA_FOMPROBLEMS/sequentialIHTP/
    cp /path/to/your/repo/Changed\ codes/sequentialIHTP.H ITHACA-FV-KF/src/ITHACA_FOMPROBLEMS/sequentialIHTP/
    cp /path/to/your/repo/Changed\ codes/createThermocouples.H ITHACA-FV-KF/src/ITHACA_FOMPROBLEMS/sequentialIHTP/
    ```

    **Explanation**:
    - Replace `/path/to/your/repo/` with the actual path where you have cloned your repository containing the `Changed codes` folder.
    - The `cp` command copies the modified files from the `Changed codes` folder to the appropriate directories in the ITHACA-FV and ITHACA-FV-KF repositories, replacing the original files.

3. **Recompile the ITHACA-FV and ITHACA-FV-KF libraries**:

    After replacing the files, recompile the libraries to ensure the changes take effect.


### 2. `Data Assimilation _Multiquadric-RBF`
This folder contains:
- **Main Scripts**: The scripts required to run the data assimilation simulation using **Multiquadric Radial Basis Functions (RBFs)**.
- **Results**: The results from running the simulations, including relevant figures and plots.
- **Figures**: Figures and visualizations included in the paper.

To run the simulation with the **Multiquadric RBF**, navigate to the `Data Assimilation _Multiquadric-RBF` folder and execute the following script:

```bash
cd Data\ Assimilation\ _Multiquadric-RBF
python main.py
```

### 3. `Data Assimilation _Gaussian-RBF`
This folder contains:
- **Main Scripts**: The scripts required to run the data assimilation simulation using Gaussian Radial Basis Functions (RBFs).
- **Results**: The results from running the simulations, including relevant figures and plots.
- **Figures**: Figures and visualizations included in the paper.

To run the simulation with the **Gaussian RBF**, navigate to the `Data Assimilation _Gaussian-RBF` folder and execute the following script:

```bash
cd Data\ Assimilation\ _Gaussian-RBF
python main.py
```
