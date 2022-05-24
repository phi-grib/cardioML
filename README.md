# Use of Machine Learning algorithms to speed up electrophysiological simulations

In cardiotoxicity studies it is common to pre-compute the values of different biomarkers (APD90 or TX) for a range of ion channel blockades. Since every simulation requires costly computations, to complete the matrix of simulations for several ion channels can be cumbersome. Some examples of how these simulations are run and used are included in the references

The relationship between the input values and the biomarker is not too complex and Machine Learning can be used to obtain a good approximation. The resulting function can be generated using only an small fraction of the computations required to generate the whole matrix. This function can then be used to predict the biomarker value for any combination of the covered range, with an excellent accuracy

In this repository we have included a jupyter notebook and example simulation results that demonstrate this idea. 

Regarding to data matrices correspond to simulations using modified O'Hara** version which have been produced by Jordi Llopis, Beatriz Trenor and Javier Saiz.

- KrKsCaL.xlsx: This is data matrix for build the ML models.
- APD90_12CiPA_drugs_IKrIKsICaL.xlsx: This excel contains the input and output values for CiPA compounds.
- EFTPC_IC50_28_CiPADrugs.xlsx: This file contains D, <img src="https://render.githubusercontent.com/render/math?math={IC}_50"> and hill coefficient for calculate the input values for CiPA compounds of the previous excel file.

The equation for calculate input values consists of:

![my equation](https://latex.codecogs.com/svg.image?\text&space;{&space;Input&space;value&space;}=\log&space;_{10}\left(\left[\frac{D}{I&space;C_{50}}\right]^{h}\right))

# References

* Llopis J, Cano J, Gomis-Tena J, Romero L, Sanz F, Pastor M, Trenor B, Saiz J. In silico assay for preclinical assessment of drug proarrhythmicity. J Pharmacol Toxicol Methods 2019 99: 106595. PMID: 31962986 DOI: 10.1016/j.vascn.2019.05.106.
** O’Hara, T., Virág, L., Varró, A. & Rudy, Y. Simulation of the Undiseased Human Cardiac Ventricular Action Potential: Model Formulation and Experimental Validation. PLOS Comput. Biol. 7, e1002061 (2011).
