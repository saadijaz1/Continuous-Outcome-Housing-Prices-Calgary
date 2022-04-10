## Calgary Housing Prices Model - Overview
This peoject was done by scraping the data from Zillow for city of Calgary, AB
Created a model that predicts the price of the property type based of number of bedrooms, bathrooms, square footage, postal code, and property type
Scrapped close to 900 listings on Zillow for the city of Calgary, AB
Extracted details from the listing to quantify the values of bedrooms, bathrooms, square footage, postal code, and property type
Tried Linear, Lasso, and Random Forest Regressors to find the best model
## Code and Resources Used
Python Version: 3.7 <br />
Packages: pandas, numpy, sklearn, matplotlib, seaborn, statsmodel, selenium, BeautifulSoup, regex, lxml, pickle <br />
Scraper Github: https://github.com/cargicar/housing_price_phoenix/blob/main/Zillow_scraping.ipynb
## Project Methodology
There are two Jupyter Notebooks:
1. Zillow_scrapper
	- This scrapper is based on the work of https://github.com/cargicar/housing_price_phoenix/blob/main/Zillow_scraping.ipynb
	- The scrapper was modified so that it would scrape all the details listed on the Zillow website for a particular listing
	- Next the data was cleaned by spliting the data into different columns and then trimming the postal codes so that it would retain the main area and drop the sub-areas
	- The data was then exported as a CSV file
	- Some minor cleaning was done in excel
2. Calgary_Housing_Analysis
      - After importing all the relevant libraries, the CSV file was imported to the Jupyter Notebook
      - Basic exploration and visualization of the data was done
      - Zipcode and Type of housing was replaced by dummy variables
      - Since data was skewed, it was tranformed using logarithmic transformation
      - The outliers from sqft column were removed
      - The data was split into train and test data with a split ratio of 70/30
      - Linear, Random Forest, and Lasso regression were performed and their errors were compared
      - Random Forest model performed best as the R2 value was highest for this model
