## THe Longevity Benefits of Homeownership

This repository contains code and materials to replicate ["The Longevity Benefits of Longevity."](https://osf.io/preprints/socarxiv/7ya3f/)

### Replication Package

This repository includes code to replicate all figures and tables in the paper. Please note that to run the replication code, you will have to downloading the publicly-available CenSoc-DMF file AND having access to a repository of complete count Census data from IPUMS for the years 1870-1940.  

1. Clone this repository
2. Download CenSoc-DMF V2.1 and update scripts to point towards your data files  
3. Run the `00_run_all.Rmd` script, which will run all code (or run scripts `01` to `05` individually)

#### Computing 

All computing was carried out on a server with approximately 200GB of available RAM. This analysis requires reading in datasets that are approximately 100GB in size.  

#### Data 

Please download the CenSoc-DMF file from [CenSoc.berkeley.edu](https://censoc.berkeley.edu/data/). In addition, you will need access to a complete count census repository. Alternatively, you can download files from [IPUMS USA](https://usa.ipums.org/usa/). 

#### Code 

After downloading the required data, researchers can run the following script to replicate all figures and tables: 

- `00_run_all.Rmd` - this file runs all scripts. 

Alternatively, researchers can run the following files individually in order: 

- `01_identify_sibs.Rmd` - This file identifies sibs in the 1920 Census and links them onto the 1940 Census and DMF mortality records 
- `02_homeownership_decade.Rmd` - Calculate homeownership rates using complete count census data from 1900, 1910, 1920, 1930, and 1940.   
- `03_representativity_table.Rmd` - Compare the representativeness of our samples to the general population 
- `04_lexis_diagram.Rmd` - Create a lexis diagram that 
- `05_pooled_analysis.Rmd` - Estimate the unadjusted difference in life expectancy between homeowners and renters.  
- `06_sibling_analysis.Rmd` - Estimate the causal effect of homeownership on longevity 
- `07_homeownership_homevalue.Rmd` - Estimate effect heterogeity with respect to homeownership 
- `08_homeownership_homevalue.Rmd` - Estimate unadjusted difference in life expectancy at age 65 between homeowners and renters 

### Authors

- [Casey Breen](caseybreen.com)

