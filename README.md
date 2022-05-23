# Use of Machine Learning algorithms to speed up electrophisiological simulations

In cardiotoxicity studies it is common to pre-compute the values of different biomarkers (APD90 or TX) for a range of ion channel blockades. Since every simulation requires costly computations, to complete the matrix of simulations for several ion channels can be cumbersome. Some examples of how these simulations are run and used are included in the references

The relationship between the input values and the biomarker is not too complex and Machine Learning can be used to obtain a good aproximation. The resulting function can be generated using only an small fraction of the computations required to generate the whole matrix. This function can then be used to predict the biomarker value for any combination of the covered range, with an excelent accuracy

In this repository we have included a jupyter notebook and example simulation results that demonstrate this idea. 

# References

* Llopis J, Cano J, Gomis-Tena J, Romero L, Sanz F, Pastor M, Trenor B, Saiz J. In silico assay for preclinical assessment of drug proarrhythmicity. J Pharmacol Toxicol Methods 2019 99: 106595. PMID: 31962986 DOI: 10.1016/j.vascn.2019.05.106

