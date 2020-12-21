# King County Housing predictions
![Seattle_pic](/notebooks/report/figures/readme.png)

# Table of Contents

<!--ts-->
 * [General Setup Instructions](https://github.com/howen7/KingHousing#general-setup-instructions)
 * [Context of Project](https://github.com/howen7/KingHousings#Context)
 * [Data](https://github.com/howen7/KingHousing#Data)
 * [Process](https://github.com/howen7/KingHousing#models-used--methodology)
 * [Results & Next Steps](https://github.com/howen7/KingHousing#Results)
<!--te-->

```
.
├── readme.md     
├── environment.yml
├── notebooks
│   ├── exploratory
│   │   ├── DataFilering.ipynb
│   │   ├── Hot_Encoder_Dummy_Data.ipynb
│   │   ├── Hunter_FM.ipynb
│   │   ├── Jons_DataExploration.ipynb
│   │   ├── Paul_first_model.ipynb
│   │   ├── presentation_hunter.ipynb
│   └── report
│       ├── figures
│       │   ├── Porch.png
│       │   ├── basementdist.png
│       │   ├── basementdistribution.png
│       │   ├── basementgrade.png
│       │   ├── waterlocation.png
│       └── FinalNotebook.ipynb
├── references
│   ├──Lookup.doc
│   ├──Parcel.doc
│   ├──README.md
│   ├──REAL Property Sales.doc
│   └──Residential Building.doc
└── src
    ├── my_mods.py
    ├── best_weights_mod1.hdf5   
    ├── history_mod1.json
    └── data
        ├──combined.json
        ├──combined_onbehot.json
        ├──combined_with_dummies.json
        ├──presentation.json
        └──zipcodes.json

```
# General Setup Instructions 

Ensure that you have installed [Anaconda](https://docs.anaconda.com/anaconda/install/).

### `linreg2-env` conda Environment

This project relies on you using the [`environment.yml`](environment.yml) file to recreate the `linreg2-env` conda environment. To do so, please run the following commands *in your terminal*:
```bash
# create the linreg2-env conda environment
conda env create -f environment.yml
# activate the conda environment
conda activate linreg2-env
# if needed, make linreg2-env available to you as a kernel in jupyter
python -m ipykernel install --user --name linreg2-env --display-name "Python 3 (linreg2-env)"
```
# Context:

The focus of this project was to look at King County Washington Housing selling data and provide inferential conlusions on what factors affect housing prices and also to build a linear regression model that would accurately predicate the sale price of the home by finding the features of the home that had the most influence on housing price.


# Aims:
The initial scope of our data analysis sought to answer three primary questions: 
1.)Does higher square footage increases home sale price? 
2.)Does having a porch increases home sale price? 
3.)Does Having a beachfront or lakefront increases home sale price?
   

# Data:

The Data used was from www5.kingcounty.gov/sdc/Metadata.aspx?Layer=parcel#AttributeInfo


# Models used + Methodology:

Our initial data cleaning we selected for single family homes sold within the most recent year at the time of this writing, 2019. There was thought to expand the scope of our study to the past 5 years, but we suspected doing this would overcomplicate our findings, and possibly affect our final linear model. For the sake of simplicity we decided to focus our attention on single family homes, and then also later framed our findings to address people who may be looking to sell their homes or increase their home sale values by focusing on improving specific features of their homes.

Our first simple model attempted to answer the more obvious positively coorelated feature, Total Square footage of Living Space to the Sale Price, with Sale Price being our independent variable. We obtained an R-Squared value of 0.188, and found that Total Square footage of the house increased the value of the house $368 per sq. foot. We went on to build from this low R-Squared value.

We then looked to our next feature of having a porch versus not having a porch and how this affected sale price of the home. Porch Data was in our original dataframe. To be able to adequately see if there was a difference between the two groups we defined houses with porches, as house with sq. foot of open porch > 0. After running an independent t-test between the two groups we found that there was a significant difference in sale price between the two. We kept open porch sq. footage as a continuous variable in our final analysis.

From here we took our categorical variables, beach front and lakefront locations, created dummy variables for each and then appended them to our original dataframe that contained our continuous variables. We then removed our independent variable, SalePrice. Next we created a correlation matrix and ran a correlation test that compared colinearity between variables and removed variables that had high collinearity between eachother from our dataframe. We defined high collinearity between (0.75 and 1.00). This process helped prevent us from violating multicolinearity within the model.


# Results:
Our final model predicted that SquareFootage, Having a porch, and having beach front property increases the sale price. 

For every 1 square footage increase Sale Price of a house increases by 319.
For every 1 square footage of porch the Sale Price of a house increases by 125.
Depending on which lake the house is on it can increase the sale price by 92,000 and 1,238,000


### Future Investigations and Recommendations:

It would be interesting to see how well this lines up with actual data. Using zillow you could see how close our model comes to predicting selling prices of houses bases on square footage, porch and area where its located. 

## Citations

<sup>1</sup>County, King. Parcel, 2008, www5.kingcounty.gov/sdc/Metadata.aspx?Layer=parcel#AttributeInfo. 

<sup>2</sup> King County. “King County Department of Assessments.” King County Department of Assessments: Assessments Data Download, 2013, info.kingcounty.gov/assessor/DataDownload/default.aspx. 






