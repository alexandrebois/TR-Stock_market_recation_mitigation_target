# Estimating stock market reaction to firms' GhG emission mitigation

This repository contains the code and data used for the research trimester, and has the following organisation :

* One **data** folder, to store the raw data that will be used.
* One **result** folder, to save the results. This folder already contains an 'AR.csv' file that is calculated in notebook 2, as it takes 15min to run the code. 
* 3 Notebooks and one python script, used to process and analyse the data/results.

### Role of the noteboooks 

The first notebook is used to visualize the data from the Science Based Target initiative (SBTi), in order to visualize selection bias in the data that we will process later. 

The second notebook calculates the anormal returns using Mc'Kinlay's market model, for all the firms available, and results in the creation of a 'AR.csv' dataframe that contains the raw result data.

The last notebook focuses on the result we got in notebook 2, and contains validity tests of the results and also heterogeneity studies of the results.

The python script contains three useful function that are often used, in order to make the notebook clearer and shorter. 

### Raw data contents and origin

* companies-taking-action.xlsx : an excel file dowloaded from the SBTi, that lists all the companies whose GhG emission mitigation plan has been approved by the SBTi. This excel contains data about the sector, the geographical origin, and the date of the GhG emission mitigation annoucement. The main problem of this file is that the dates availables only have a one-month precision, while we need the precise date to calculate the anormal return.
* date.csv : contains the precise date where companies revealed that their Ghg emission mitigation plan was validated by the SBTi, the data is also from the SBTi. This file contains fewer companies that the companies-taking-action.xlsx, but can be used to calculate anormals returns
* info.csv : an other dataframe from the SBTi, that contains informations about the companies we studied (sector, type, geographical origin ...)
  
To link these three dataframe, we will use the ISIN number of the companies as an index.
  
We also have two files from datastream that contains informations about the stock market:

* equities.csv : contains the value of the main equity of the studied firms
* indices.csv : contains the market index used in the market model