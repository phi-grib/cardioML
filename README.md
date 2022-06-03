# Use of Machine Learning algorithms to speed up electrophysiological simulations

In cardiotoxicity studies it is common to pre-compute the values of different biomarkers (![my equation](https://latex.codecogs.com/svg.image?APD_{90}) or TX) for a range of ion channel blockades. Since every simulation requires costly computations, to complete the matrix of simulations for several ion channels can be cumbersome. Some examples of how these simulations are run and used are included in the references.

Machine Learning can be used to obtain a good approximation of the relationship between the pharmacological input values and the arrhythmogenic biomarkers. The resulting function can be generated using only an small fraction of the computations required to generate the whole matrix. Therefore, the computational time required for the simulation can be significantly reduced. This function can then be used to predict the biomarker value for any combination of the covered range, with an excellent accuracy.

In this repository we have included a jupyter notebook and some simulation results that demonstrate this idea. 

Regarding the data matrices, they correspond to simulations using a modified version of the ventricular action potential model by O'Hara et al., which have been performed by Jordi Llopis, Beatriz Trenor and Javier Saiz at the Centro de Investigación e Innovación en Bioingeniería (Ci2B), Universitat Politècnica de València, Valencia, Spain.

- KrKsCaL.xlsx: This is the data matrix needed to build the ML models.
- APD90_12CiPA_drugs_IKrIKsICaL.xlsx: This excel file contains the input and output values for CiPA compounds.
- EFTPC_IC50_28_CiPADrugs.xlsx: This file contains D, ![my equation](https://latex.codecogs.com/svg.image?I&space;C_{50}) and hill coefficient to calculate the input values for CiPA compounds of the previous excel file.
- Folder "Matrix Building": This folder contains MATLAB functions for generating the KrKsCaL matrix. The script "buildMatrixKrKsNaL.m" is the main script which run the electrophysioloigcal simulations and generates the matrix

The equation to calculate input values is:

![my equation](https://latex.codecogs.com/svg.image?\text&space;{&space;Input&space;value&space;}=\log&space;_{10}\left(\left[\frac{D}{I&space;C_{50}}\right]^{h}\right))

# References

* Llopis J, Cano J, Gomis-Tena J, Romero L, Sanz F, Pastor M, Trenor B, Saiz J. In silico assay for preclinical assessment of drug proarrhythmicity. J Pharmacol Toxicol Methods 2019 99: 106595. PMID: 31962986 DOI: 10.1016/j.vascn.2019.05.106.

* O’Hara, T., Virág, L., Varró, A. & Rudy, Y. Simulation of the Undiseased Human Cardiac Ventricular Action Potential: Model Formulation and Experimental Validation. PLOS Comput. Biol. 7, e1002061 (2011).

## Licensing

CardioML was produced at the PharmacoInformatics lab (http://phi.upf.edu), in the framework of the eTRANSAFE project (http://etransafe.eu). eTRANSAFE has received support from IMI2 Joint Undertaking under Grant Agreement No. 777365. This Joint Undertaking receives support from the European Union’s Horizon 2020 research and innovation programme and the European Federation of Pharmaceutical Industries and Associations (EFPIA). 

![Alt text](images/eTRANSAFE-logo-git.png?raw=true "eTRANSAFE-logo") ![Alt text](images/imi-logo.png?raw=true "IMI logo")

Copyright 2022 Manuel Pastor (manuel.pastor@upf.edu)

CardioML is free software: you can redistribute it and/or modify it under the terms of the **GNU General Public License as published by the Free Software Foundation version 3**.

CardioML is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with CardioML source code. If not, see <http://www.gnu.org/licenses/>.

