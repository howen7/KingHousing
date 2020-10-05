The focus of this project was to look at King County Washington Housing selling data and provide inferential conlusions on what factors affect housing prices and also to build a linear regression model that would accurately predicate the sale price of the home by finding the features of the home that had the most influence on housing price. The initial scope of our data analysis sought to answer three primary questions: 1.)Does higher square footage increases home sale price? 2.)Does having a porch increases home sale price? 3.)Does Having a beachfront or lakefront increases home sale price?

In our initial data cleaning we selected for single family homes sold within the most recent year at the time of this writing, 2019. There was thought to expand the scope of our study to the past 5 years, but we suspected doing this would overcomplicate our findings, and possibly affect our final linear model. For the sake of simplicity we decided to focus our attention on single family homes, and then also later framed our findings to address people who may be looking to sell their homes or increase their home sale values by focusing on improving specific features of their homes.

Our first simple model attempted to answer the more obvious positively coorelated feature, Total Square footage of Living Space to the Sale Price, with Sale Price being our independent variable. We obtained an R-Squared value of 0.188, and found that Total Square footage of the house increased the value of the house $368 per sq. foot. We went on to build from this low R-Squared value.

We then looked to our next feature of having a porch versus not having a porch and how this affected sale price of the home. Porch Data was in our original dataframe. To be able to adequately see if there was a difference between the two groups we defined houses with porches, as house with sq. foot of open porch > 0. After running an independent ttest between the two groups we found that there was a significant difference in sale price between the two. We kept open porch sq. footage as a continuous variable in our final analysis.

From here we took our categorical variables, beach front and lakefront locations, created dummy variables for each and then appended them to our original dataframe that contained our continuous variables. We then removed our independent variable, SalePrice. Next we created a correlation matrix and ran a correlation test that compared colinearity between variables and removed variables that had high collinearity between eachother from our dataframe. We defined high collinearity between (0.75 and 1.00). This process helped prevent us from violating multicolinearity within the model.


### Conclusions
Our final model predicted that SquareFootage, Having a porch, and having beach front property increases the sale price. 

For every 1 square footage increase Sale Price of a house increases by 319.
For every 1 square footage of porch the Sale Price of a house increases by 125.
Depending on which lake the house is on it can increase the sale price by 92,000 and 1,238,000


## Citations

<sup>1</sup>County, King. Parcel, 2008, www5.kingcounty.gov/sdc/Metadata.aspx?Layer=parcel#AttributeInfo. 

<sup>2</sup> King County. “King County Department of Assessments.” King County Department of Assessments: Assessments Data Download, 2013, info.kingcounty.gov/assessor/DataDownload/default.aspx. 




